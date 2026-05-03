# 5. The NEXI Framework

> **Status: stub.** Section to be developed in a subsequent revision.

## 5.1 The two-layer catalog

Planned coverage: distinction between **patterns** (architectural primitives, the engineering ingredient layer) and **clusters** (intelligence models, the architecture-and-theory layer). Why the cluster framing was adopted (the patterns in NEXI are co-dependent; flat catalogs invite the failure mode of "import one ingredient, expect a meal").

## 5.2 Schema and metadata

Planned coverage: the JSON Schemas for `nexi.yaml` and `cluster.yaml`. Required fields, the falsifiable-hypothesis enforcement, the status field as audit trail (template / draft / canonical / deprecated). How machine-validated metadata drives the catalog index.

## 5.3 Layered cards

Planned coverage: the layered-document format that addresses two audiences (engineers and reviewers) in the same file. Quick-start at the top; theoretical depth and falsifiable hypothesis below. Why layering is preferred over writing two separate documents.

## 5.4 Application formats

Planned coverage: the four formats an NEXI may populate (architecture, skill, communication, coordination). The framework-neutral skill specification and its translations to Claude skills, OpenAI function calling, MCP, LangChain / LlamaIndex, multi-agent RL, robotics. Why platform-neutrality is a contribution beyond mere convenience.

## 5.5 Cluster as intelligence model

Planned coverage: the cluster definition (≥ 2 member patterns, coherent problem class, system-level falsifiable hypothesis, complementarity notes). Why complementarity is the load-bearing claim — adopting one pattern in isolation is the cataloged failure mode.

## 5.6 Repository structure as artifact

Planned coverage: the public repository at <https://github.com/Ds-GerardoCastro/NEXI> as a contribution-friendly artifact. The methodology gate, the open invitation, the eventual community-contribution model.
