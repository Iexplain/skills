---
name: paper-html-presentation
description: "Turn one research paper—provided as PDF, text, citation, DOI/PMID, or notes—into a polished standalone HTML journal-club presentation with traceable claims and optional embedded figures. Use for one-paper group-meeting slide decks; do not use for generic websites, multi-paper reviews, or redesigning an existing deck unless requested."
---

# Paper HTML Presentation

Create a presentation-ready HTML deck for sharing and discussing one research paper. Follow the user's language and requested emphasis; when unspecified, produce a concise Chinese journal-club deck.

## Required outcome

- Deliver one self-contained `.html` file that opens directly in a browser without a server.
- Make the scientific story easy to present in 8–15 minutes, not merely a formatted paper summary.
- Keep every quantitative claim traceable to the paper. Distinguish reported results, authors' interpretation, and the presenter's critique.
- Preserve the user's supplied material and constraints. Do not invent missing methods, statistics, figures, or conclusions.

## Workflow

1. Inspect all available source material and identify the paper type, central question, design, cohort or dataset, reference standard, primary outcome, main result, and limitations.
2. Build a small claim–evidence ledger before writing slides. Record each important number or conclusion with its source location when available: page, section, figure, table, or supplementary item.
3. Read `references/deck-spec.md` and choose the slide structure that fits the study. Diagnostic, omics/ML, intervention, mechanism, and methods papers need different narratives.
4. Start from `assets/deck-template.html`. Keep its navigation, print behavior, and responsive styling unless the user requests a different visual system.
5. Add figures only when their source and use are clear. Embed user-provided or openly accessible images as base64 data URIs so the HTML remains standalone.
6. Run `python3 scripts/validate_deck.py <output.html>`, then manually inspect the browser layout, figure legibility, navigation, and print/PDF output.

## Evidence rules

- Never fabricate or silently round values. Use the precision reported by the paper.
- If a value is estimated from a figure, label it as visual estimation. If a chart is reconstructed, state that it is redrawn from reported values.
- Do not scrape or embed paywalled figures without permission. Use the user-provided PDF/figures, open-access material, or text-only placeholders that point to the original figure.
- Preserve figure panel labels and captions when they are necessary to interpret the evidence.
- Use cautious wording for post hoc analyses, exploratory findings, surrogate endpoints, retrospective designs, and unvalidated models.
- Keep the reference list complete enough for the audience to identify and retrieve the paper; add DOI/PMID when available.

## Presentation rules

- Lead with the question and the one-sentence answer. Put background only where it changes interpretation.
- Prefer one claim per slide and one primary visual per slide. Do not paste whole manuscript pages.
- Put detailed caveats beside the result they affect; collect only cross-cutting issues in the appraisal section.
- Use a visible distinction between `论文结果`, `作者解释`, and `汇报人点评` when those meanings coexist.
- Make slides readable from the back of a room: high contrast, large type, limited text, and no critical information encoded by color alone.
- Include 2–4 discussion questions that arise from the evidence, not generic questions such as “有什么问题？”

## Figures and data visualization

- Prefer original figures supplied by the user when exact visual fidelity matters.
- Crop only decorative whitespace; do not remove axes, legends, error bars, panel labels, or significance markers needed for interpretation.
- Recreate charts only from explicit numerical data in the paper or source files. Keep units, denominators, error definitions, and statistical tests visible.
- Do not combine independent cohorts or endpoints into one chart unless the paper does so and the visual clearly preserves their distinction.
- For machine-learning papers, show validation design and baseline alongside performance; avoid presenting pooled metrics without relevant subgroup or site controls.

## Completion checks

Confirm that the final deck contains:

- paper title, authors, journal/year, DOI or PMID when available;
- question, design, population/data, methods, main result, limitations, and implications;
- sample sizes and denominators wherever they affect interpretation;
- source labels for figures and reconstructed charts;
- at least two evidence-based discussion questions;
- a final reference/credits section;
- no unresolved placeholders, broken local assets, or unsupported external dependencies.
