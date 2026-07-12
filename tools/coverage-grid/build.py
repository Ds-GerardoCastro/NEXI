#!/usr/bin/env python3
"""
Coverage design-space grid — builder (two spaces + bridge).

Builds:
  - AI grid      : cognitive-function x AI-architecture   (from AI RESEARCH vault)
  - Nature grid  : cognitive-function x biological-clade   (from NIP vault)
  - Bridge view  : per function, AI coverage vs Nature coverage (Nature-hot/AI-cold = target)

Cell states: 1 covered / 2 field-known / 3 frontier (see taxonomy.yaml).
Emits coverage-matrix.json and a self-contained coverage-heatmap.html.
Run from tools/coverage-grid/.  Requires: pyyaml.
"""
import json, os, re, glob, collections, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

HERE = os.path.dirname(os.path.abspath(__file__))
# The tool may live inside the private Hyperion repo OR inside the public NEXI
# repo (which sits alongside Hyperion). Resolve the vault root from either.
# NOTE: regeneration requires the maintainer's private Hyperion vaults; the
# committed coverage-matrix.json / coverage-heatmap.html are the published snapshot.
_CANDS = [os.path.normpath(os.path.join(HERE, "..", "..")),                   # tool inside Hyperion/
          os.path.normpath(os.path.join(HERE, "..", "..", "..", "Hyperion"))]  # tool inside NEXI/ (Hyperion sibling)
HYP = next((c for c in _CANDS if os.path.isdir(os.path.join(c, "AI RESEARCH"))), _CANDS[-1])
VAULT_AI = os.path.join(HYP, "AI RESEARCH", "principles")
VAULT_NAT = os.path.join(HYP, "NATURE INTELLIGENCE PROJECT", "principles")


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def load_yaml(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return yaml.safe_load(f)


def principle_source_counts(pdir):
    counts = collections.Counter()
    for f in glob.glob(os.path.join(pdir, "*.md")):
        txt = open(f, encoding="utf-8", errors="ignore").read()
        m = re.search(r"^source:\s*'?\[\[([^\]]+)\]\]", txt, re.M)
        if m:
            counts[norm(m.group(1).split("|")[0])] += 1
    return counts


def match_count(aliases, counts):
    total, matched = 0, []
    al = [norm(a) for a in aliases]
    for link, n in counts.items():
        for a in al:
            if link == a or link.startswith(a[:24]) or a.startswith(link[:24]):
                total += n; matched.append(link); break
    return total, set(matched)


def build_grid(functions, cols, col_field, field_known, sources, counts):
    """Generic grid builder. col_field is 'arch' or 'clade'."""
    fk = {(c["fn"], c[col_field]) for c in field_known}
    cellmap = {}
    consumed = set()
    for src in sources:
        pc, links = match_count(src["aliases"], counts)
        consumed |= links
        for cell in src["cells"]:
            key = f'{cell["fn"]}|{cell[col_field]}'
            c = cellmap.setdefault(key, {"sources": [], "source_count": 0, "principle_count": 0})
            c["sources"].append(src["id"]); c["source_count"] += 1; c["principle_count"] += pc
    grid = []
    covered = fknown = frontier = 0
    for fn in functions:
        for col in cols:
            key = f'{fn["id"]}|{col["id"]}'
            if key in cellmap:
                c = cellmap[key]; state = 1; covered += 1
            elif (fn["id"], col["id"]) in fk:
                c = {"sources": [], "source_count": 0, "principle_count": 0}; state = 2; fknown += 1
            else:
                c = {"sources": [], "source_count": 0, "principle_count": 0}; state = 3; frontier += 1
            grid.append({"fn": fn["id"], "col": col["id"], "state": state,
                         "source_count": c["source_count"], "principle_count": c["principle_count"],
                         "sources": c["sources"]})
    totals = {"grid_cells": len(functions) * len(cols), "covered": covered,
              "field_known": fknown, "frontier": frontier,
              "sources_mapped": len(sources), "principles_counted": sum(counts.values())}
    return {"cells": grid, "totals": totals}, consumed


def build_bridge(functions, ai_grid, nat_grid):
    ai_by_fn = collections.defaultdict(lambda: [0, 0])   # [covered_cells, principles]
    nat_by_fn = collections.defaultdict(lambda: [0, 0])
    for c in ai_grid["cells"]:
        if c["state"] == 1:
            ai_by_fn[c["fn"]][0] += 1; ai_by_fn[c["fn"]][1] += c["principle_count"]
    for c in nat_grid["cells"]:
        if c["state"] == 1:
            nat_by_fn[c["fn"]][0] += 1; nat_by_fn[c["fn"]][1] += c["principle_count"]
    rows = []
    for fn in functions:
        ai_cov, ai_p = ai_by_fn[fn["id"]]
        nat_cov, nat_p = nat_by_fn[fn["id"]]
        if nat_cov > 0 and ai_cov == 0:
            flag = "nature-hot-ai-cold"      # mine nature -> AI
        elif ai_cov > 0 and nat_cov == 0:
            flag = "ai-hot-nature-cold"
        elif ai_cov == 0 and nat_cov == 0:
            flag = "both-empty"
        else:
            flag = "both"
        rows.append({"fn": fn["id"], "ai_cov": ai_cov, "ai_p": ai_p,
                     "nat_cov": nat_cov, "nat_p": nat_p, "flag": flag})
    return rows


def main():
    tax = load_yaml("taxonomy.yaml")
    smap = load_yaml("sources.yaml")
    functions = tax["functions"]
    ai_cols = tax["ai_architectures"]
    nat_cols = tax["nature_clades"]

    ai_counts = principle_source_counts(VAULT_AI)
    nat_counts = principle_source_counts(VAULT_NAT)

    ai_grid, ai_consumed = build_grid(functions, ai_cols, "arch",
                                      tax.get("field_known_ai", []),
                                      smap["ai_sources"], ai_counts)
    nat_grid, nat_consumed = build_grid(functions, nat_cols, "clade",
                                        tax.get("field_known_nature", []),
                                        smap["nature_sources"], nat_counts)
    bridge = build_bridge(functions, ai_grid, nat_grid)

    out = {"functions": functions,
           "ai": {"cols": ai_cols, **ai_grid},
           "nature": {"cols": nat_cols, **nat_grid},
           "bridge": bridge}
    with open(os.path.join(HERE, "coverage-matrix.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    write_html(out)

    # report
    def rep(name, grid, counts, consumed, sources):
        t = grid["totals"]
        print(f"[{name}] {len(functions)}fn x {len(grid['cells'])//len(functions)}cols = {t['grid_cells']} cells | "
              f"covered={t['covered']} field-known={t['field_known']} frontier={t['frontier']} | "
              f"{t['principles_counted']}p across {len(counts)} links")
        miss = sorted(set(counts) - consumed)
        if miss:
            print(f"   WARNING unmatched source links: {miss}")
    rep("AI", ai_grid, ai_counts, ai_consumed, smap["ai_sources"])
    rep("NATURE", nat_grid, nat_counts, nat_consumed, smap["nature_sources"])
    nh = [b["fn"] for b in bridge if b["flag"] == "nature-hot-ai-cold"]
    ah = [b["fn"] for b in bridge if b["flag"] == "ai-hot-nature-cold"]
    print(f"[BRIDGE] nature-hot/AI-cold (mine->AI): {nh or 'none'}")
    print(f"         AI-hot/nature-cold: {ah or 'none'}")
    print("wrote coverage-matrix.json + coverage-heatmap.html")


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Design-Space Coverage — AI &amp; Nature</title>
<style>
  :root{--bg:#0d1117;--panel:#131a22;--ink:#e6edf3;--fog:#8b98a5;--line:#243040;
    --bio:#5fe3a1;--amber:#f0b15a;--machine:#7aa2f7;--rose:#f7768e;}
  *{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--ink);
    font:14px/1.5 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;padding:26px}
  h1{font-size:20px;margin:0 0 4px} h2{font-size:16px;margin:30px 0 6px;color:var(--machine)}
  .sub{color:var(--fog);font-size:13px;max-width:940px;margin-bottom:8px}
  .tabs{display:flex;gap:8px;margin:16px 0}
  .tab{padding:7px 14px;border:1px solid var(--line);border-radius:8px;cursor:pointer;color:var(--fog);background:var(--panel);font-size:13px}
  .tab.on{color:var(--ink);border-color:var(--machine)}
  .totals{display:flex;gap:16px;flex-wrap:wrap;margin:10px 0 14px;font-size:12.5px}
  .totals b{font-size:17px} .chip{display:inline-flex;align-items:center;gap:6px;color:var(--fog)}
  .sw{width:12px;height:12px;border-radius:3px;display:inline-block}
  .sw.c{background:var(--bio)} .sw.f{background:transparent;border:1.5px dashed var(--amber)} .sw.fr{background:#1a2230;border:1px solid var(--line)}
  .wrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--panel);padding:14px}
  table{border-collapse:collapse}
  th.col{height:158px;white-space:nowrap;vertical-align:bottom;padding:0 2px;color:var(--fog);font-size:11px;font-weight:500}
  th.col div{transform:rotate(-60deg);transform-origin:left bottom;width:22px;translate:9px 0}
  th.row{text-align:right;padding:0 12px 0 4px;font-size:12px;font-weight:500;white-space:nowrap}
  td.cell{width:28px;height:28px;padding:0}
  td.cell .box{width:24px;height:24px;margin:2px;border-radius:5px}
  .st3 .box{background:#161d28;border:1px solid #1e2734}
  .st2 .box{background:transparent;border:1.5px dashed var(--amber)}
  .st1 .box{background:var(--bio)}
  .corner{color:var(--machine);font-size:11px;text-align:right;padding-right:12px;vertical-align:bottom}
  .foot{color:var(--fog);font-size:11.5px;margin-top:10px;max-width:940px}
  /* bridge */
  .br{border-collapse:collapse;margin-top:6px}
  .br th{color:var(--fog);font-size:12px;text-align:center;padding:4px 10px;font-weight:500}
  .br td{padding:3px 10px;font-size:12.5px;border-top:1px solid var(--line)}
  .br td.fn{text-align:right;color:var(--ink)}
  .br .bar{height:16px;border-radius:3px;display:inline-block;vertical-align:middle}
  .br .ai .bar{background:var(--machine)} .br .nat .bar{background:var(--bio)}
  .br td.mid{width:14px} .br .flag{font-size:10.5px;padding:2px 7px;border-radius:10px;white-space:nowrap}
  .flag.nh{color:var(--bio);border:1px solid rgba(95,227,161,.5)}
  .flag.ah{color:var(--machine);border:1px solid rgba(122,162,247,.5)}
  .flag.be{color:var(--fog);border:1px solid var(--line)}
  .flag.bo{color:var(--amber);border:1px solid rgba(240,177,90,.4)}
  .hidden{display:none}
</style></head><body>
<h1>Design-Space Coverage &mdash; AI &amp; Natural Intelligence</h1>
<div class="sub">Rows = cognitive functions (shared bridge axis). Each grid enumerates the <b>full reference design space</b> (external taxonomies), so un-ingested / unstudied cells are visible as gaps. <b>Covered</b> = a vault source maps here. <b>Field-known</b> = real research exists but is not yet ingested (search target). <b>Frontier</b> = no known research. Hover any cell for detail. Source-level binning &mdash; private.</div>
<div class="tabs">
  <div class="tab on" data-v="ai">AI SOTA</div>
  <div class="tab" data-v="nature">Natural Intelligence</div>
  <div class="tab" data-v="bridge">Bridge: Nature &harr; AI</div>
</div>
<div id="v-ai"></div>
<div id="v-nature" class="hidden"></div>
<div id="v-bridge" class="hidden"></div>
<script>
const DATA = __DATA__;
const fnLabel = Object.fromEntries(DATA.functions.map(f=>[f.id,f.label]));

function legend(t){return `<div class="totals">`+
  `<span class="chip"><span class="sw c"></span><b style="color:var(--bio)">${t.covered}</b>&nbsp;covered</span>`+
  `<span class="chip"><span class="sw f"></span><b style="color:var(--amber)">${t.field_known}</b>&nbsp;field-known</span>`+
  `<span class="chip"><span class="sw fr"></span><b>${t.frontier}</b>&nbsp;frontier</span>`+
  `<span class="chip">of <b>${t.grid_cells}</b> cells &middot; ${t.sources_mapped} sources, ${t.principles_counted} principles</span></div>`;}

function renderGrid(elId, space, colNoun){
  const cols=space.cols, cellmap={};
  space.cells.forEach(c=>cellmap[c.fn+"|"+c.col]=c);
  let h=legend(space.totals)+`<div class="wrap"><table><tr><td class="corner">function &darr; / ${colNoun} &rarr;</td>`;
  cols.forEach(a=>h+=`<th class="col"><div>${a.label}</div></th>`);
  h+="</tr>";
  DATA.functions.forEach(f=>{
    h+=`<tr><th class="row">${f.label}</th>`;
    cols.forEach(a=>{
      const c=cellmap[f.id+"|"+a.id], s=c?c.state:3;
      let op=s===1?Math.min(1,0.4+0.2*c.source_count):1;
      const tip=`${f.label}  ×  ${a.label}\n`+(s===1?`covered — ${c.source_count} source(s), ${c.principle_count} principles\n[${c.sources.join(", ")}]`:s===2?"field-known — research exists, not yet ingested (search target)":"frontier — no known research yet");
      h+=`<td class="cell st${s}"><div class="box" style="${s===1?'opacity:'+op:''}" title="${tip.replace(/"/g,'&quot;')}"></div></td>`;
    });
    h+="</tr>";
  });
  document.getElementById(elId).innerHTML=h+"</table></div>";
}
renderGrid("v-ai", DATA.ai, "architecture");
renderGrid("v-nature", DATA.nature, "clade");

// bridge
(function(){
  const b=DATA.bridge, maxAi=Math.max(1,...b.map(x=>x.ai_cov)), maxNat=Math.max(1,...b.map(x=>x.nat_cov));
  const fl={"nature-hot-ai-cold":["nh","nature-hot / AI-cold &rarr; mine to AI"],"ai-hot-nature-cold":["ah","AI-hot / nature-cold"],"both-empty":["be","both empty"],"both":["bo","both covered"]};
  let h=`<div class="sub" style="margin-top:6px">Per function: <span style="color:var(--machine)">AI</span> coverage vs <span style="color:var(--bio)">Nature</span> coverage (number of covered cells in that row). <b style="color:var(--bio)">Nature-hot / AI-cold</b> rows are where biology has explored a function AI has not &mdash; the highest-value mining targets.</div>`;
  h+=`<div class="wrap"><table class="br"><tr><th>function</th><th style="color:var(--machine)">AI</th><th></th><th style="color:var(--bio)">Nature</th><th></th></tr>`;
  b.forEach(r=>{
    const f=fl[r.flag];
    h+=`<tr><td class="fn">${fnLabel[r.fn]}</td>`+
       `<td class="ai" style="text-align:right"><span class="bar" style="width:${8+70*r.ai_cov/maxAi}px"></span> <span style="color:var(--fog)">${r.ai_cov}</span></td><td class="mid"></td>`+
       `<td class="nat"><span class="bar" style="width:${8+70*r.nat_cov/maxNat}px"></span> <span style="color:var(--fog)">${r.nat_cov}</span></td>`+
       `<td><span class="flag ${f[0]}">${f[1]}</span></td></tr>`;
  });
  document.getElementById("v-bridge").innerHTML=h+"</table></div>";
})();

document.querySelectorAll(".tab").forEach(t=>t.onclick=()=>{
  document.querySelectorAll(".tab").forEach(x=>x.classList.remove("on")); t.classList.add("on");
  ["ai","nature","bridge"].forEach(v=>document.getElementById("v-"+v).classList.toggle("hidden", v!==t.dataset.v));
});
</script></body></html>"""


def write_html(out):
    html = HTML_TEMPLATE.replace("__DATA__", json.dumps(out, ensure_ascii=False))
    with open(os.path.join(HERE, "coverage-heatmap.html"), "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
