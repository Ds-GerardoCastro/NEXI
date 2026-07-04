#!/usr/bin/env python3
"""
Render an open-letter markdown file to a 2-page PDF.

Designed for the simple markdown subset used in NEXI outreach letters:
  - # / ## / ### headings
  - --- horizontal rule
  - paragraphs (blank-line separated)
  - bullet lists (lines starting with `- `)
  - inline **bold** and [text](url) links

Usage:
  python generate_pdf.py [input.md] [output.pdf]

Defaults:
  input.md  = ./<this-script-dir>/turner-et-al-open-letter.md
  output.pdf = ./<this-script-dir>/turner-et-al-open-letter.pdf

Dependencies:
  reportlab>=4.0
"""

import argparse
import re
import sys
from html import escape
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    KeepTogether,
)


# Inline markdown → reportlab markup
# - escape HTML special chars first
# - then convert **bold** and [text](url)
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BACKTICK_RE = re.compile(r"`([^`]+)`")


def _inline(text: str) -> str:
    """Convert markdown inline formatting to reportlab Paragraph markup."""
    text = escape(text, quote=False)
    text = _BOLD_RE.sub(r"<b>\1</b>", text)
    text = _BACKTICK_RE.sub(r'<font face="Courier">\1</font>', text)
    text = _LINK_RE.sub(r'<a href="\2" color="#0a4f8a"><u>\1</u></a>', text)
    return text


def _build_styles():
    base = getSampleStyleSheet()["Normal"]
    body = ParagraphStyle(
        "Body",
        parent=base,
        fontName="Times-Roman",
        fontSize=10.5,
        leading=13.0,
        spaceAfter=5,
        alignment=TA_JUSTIFY,
        textColor=black,
    )
    title = ParagraphStyle(
        "Title",
        parent=body,
        fontName="Times-Bold",
        fontSize=13,
        leading=16,
        spaceAfter=8,
        alignment=TA_LEFT,
    )
    subhead = ParagraphStyle(
        "Subhead",
        parent=body,
        fontName="Times-Italic",
        fontSize=10,
        leading=12,
        spaceAfter=2,
        alignment=TA_LEFT,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=body,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
    )
    closing = ParagraphStyle(
        "Closing",
        parent=body,
        spaceAfter=2,
        alignment=TA_LEFT,
    )
    return {
        "body": body,
        "title": title,
        "subhead": subhead,
        "bullet": bullet,
        "closing": closing,
    }


def _parse_blocks(md: str):
    """Yield (kind, content) tuples from a markdown source.

    Kinds: 'h1', 'h2', 'h3', 'hr', 'p', 'ul' (with items list), 'meta'.
    'meta' is reserved for the leading **Key:** value lines.
    """
    lines = md.splitlines()
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.rstrip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("# "):
            yield ("h1", stripped[2:].strip())
            i += 1
        elif stripped.startswith("## "):
            yield ("h2", stripped[3:].strip())
            i += 1
        elif stripped.startswith("### "):
            yield ("h3", stripped[4:].strip())
            i += 1
        elif stripped == "---":
            yield ("hr", None)
            i += 1
        elif stripped.startswith("- "):
            items = []
            while i < n and lines[i].rstrip().startswith("- "):
                items.append(lines[i].rstrip()[2:].strip())
                i += 1
            yield ("ul", items)
        else:
            # paragraph: collect until blank line
            buf = [stripped]
            i += 1
            while i < n and lines[i].strip():
                buf.append(lines[i].rstrip())
                i += 1
            text = " ".join(buf)
            # Heuristic: if paragraph is just `**Key:** value`, treat as meta
            if re.match(r"^\*\*[^*]+:\*\*\s+\S", text) and len(text) < 220:
                yield ("meta", text)
            else:
                yield ("p", text)


def _doc_title(md: str) -> str:
    m = re.search(r"^# (.+)$", md, re.MULTILINE)
    head = re.sub(r"[*_`]", "", m.group(1)).strip() if m else "Open letter"
    return head + " - Nature Intelligence Project"


def _default_md(here: Path) -> Path:
    cands = sorted(here.glob("*-open-letter.md"))
    return cands[0] if cands else here / "open-letter.md"


def render(md_path: Path, pdf_path: Path) -> dict:
    md = md_path.read_text(encoding="utf-8")
    styles = _build_styles()
    story = []

    for kind, content in _parse_blocks(md):
        if kind == "h1":
            story.append(Paragraph(_inline(content), styles["title"]))
            story.append(Spacer(1, 4))
        elif kind == "h2":
            story.append(Paragraph(_inline(content), styles["title"]))
        elif kind == "h3":
            story.append(Paragraph(_inline(content), styles["subhead"]))
        elif kind == "hr":
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#888888")))
            story.append(Spacer(1, 6))
        elif kind == "meta":
            story.append(Paragraph(_inline(content), styles["closing"]))
        elif kind == "ul":
            for item in content:
                story.append(Paragraph("• " + _inline(item), styles["bullet"]))
            story.append(Spacer(1, 2))
        elif kind == "p":
            story.append(Paragraph(_inline(content), styles["body"]))

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=LETTER,
        leftMargin=0.9 * inch,
        rightMargin=0.9 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.85 * inch,
        title=_doc_title(md),
        author="Juan Gerardo Castro Sánchez",
        subject="Open letter - Nature Intelligence Project",
    )

    page_count = {"n": 0}
    def _on_page(canvas, doc):
        page_count["n"] = doc.page

    doc.build(story, onFirstPage=_on_page, onLaterPages=_on_page)
    return {"pages": page_count["n"], "out": str(pdf_path)}


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="?",
        default=str(_default_md(here)),
        help="Input markdown file (default: ./turner-et-al-open-letter.md)",
    )
    parser.add_argument(
        "output",
        nargs="?",
        default=str(_default_md(here).with_suffix(".pdf")),
        help="Output PDF path (default: ./turner-et-al-open-letter.pdf)",
    )
    args = parser.parse_args()

    md_path = Path(args.input)
    pdf_path = Path(args.output)

    if not md_path.exists():
        print(f"Input markdown not found: {md_path}", file=sys.stderr)
        return 2

    result = render(md_path, pdf_path)
    print(f"Rendered: {result['out']}")
    print(f"Pages:    {result['pages']}")
    if result["pages"] > 2:
        print(
            f"WARNING: letter rendered to {result['pages']} pages; target is <= 2.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
