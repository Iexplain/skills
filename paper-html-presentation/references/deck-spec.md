# Journal-Club Deck Specification

This specification defines a strong default for a one-paper HTML presentation. Adapt the order and emphasis to the study; do not force irrelevant sections into the deck.

## Narrative arc

A useful journal-club deck answers five questions:

1. What did the authors try to learn?
2. What evidence could answer that question?
3. What did they find?
4. How believable and generalizable is the finding?
5. What should the audience take away or investigate next?

## Default slide set

Use 10–14 slides for an 8–15 minute presentation.

| Slide | Purpose | Required content |
|---|---|---|
| 1 | Cover | Title, authors, journal/year, presenter, DOI/PMID |
| 2 | One-minute takeaway | Question, design, main result, bottom line |
| 3 | Background and gap | Only facts needed to understand why the study matters |
| 4 | Research question | Exact question, hypothesis, prespecified outcome when available |
| 5 | Study design | Design diagram or concise flow; discovery/validation structure |
| 6 | Population or data | Inclusion criteria, sample size, groups, missingness, key baseline facts |
| 7 | Methods | Measurement, reference standard, model, validation, statistics |
| 8 | Main result | Primary outcome with effect size, uncertainty, denominator, and test |
| 9 | Secondary or mechanism | One coherent supporting result; avoid slide dumping |
| 10 | Figure deep dive | Original or faithfully reconstructed key figure with interpretation |
| 11 | Critical appraisal | Bias, confounding, leakage, calibration, multiplicity, missing data |
| 12 | Generalizability | Population, specimen, setting, assay, and transportability limits |
| 13 | Implications | What changes in the field or project; what does not follow |
| 14 | Discussion | Two to four focused questions |
| 15 | References and credits | Full citation, DOI/PMID, figure sources, data/code links |

For short papers, combine slides 3–4 and 11–12. For complex ML or omics studies, split model development and validation into separate slides. For diagnostic studies, always show the reference standard and a 2×2 table or equivalent when reported.

## Study-specific priorities

### Diagnostic accuracy

- Show intended-use population, index test threshold, reference standard, and verification process.
- Report sensitivity, specificity, predictive values with prevalence, likelihood ratios, or AUC with confidence intervals as available.
- Distinguish analytical validity, clinical validity, and clinical utility.
- Explain discordant-result adjudication and whether the threshold was selected and tested in the same data.

### Omics and machine learning

- Show feature selection, preprocessing, hyperparameter tuning, and test-set isolation.
- State sample size relative to feature dimension.
- Show calibration and clinically meaningful baselines, not only accuracy or AUC.
- Treat site, batch, specimen type, and repeated measurements as potential leakage or confounding sources.

### Intervention or randomized trial

- Show allocation, masking, follow-up, intention-to-treat population, absolute effects, and harms.
- Distinguish statistical significance from clinical importance.
- Identify prespecified versus post hoc outcomes.

### Mechanistic or preclinical study

- Separate observation from causal evidence.
- State model organism, perturbation, sample size, replication, and effect size.
- Mark the human-relevance gap explicitly.

### Review or meta-analysis

- Show search scope, inclusion criteria, heterogeneity, risk-of-bias assessment, and publication-bias checks.
- Avoid treating pooled precision as certainty when studies are heterogeneous.

## Evidence labels

Use consistent labels or badges:

- `论文结果`: a direct report from the paper.
- `作者解释`: the paper's proposed mechanism or conclusion.
- `汇报人点评`: presenter analysis, criticism, or connection to PMHostX.
- `图中估算`: visually estimated values.
- `重绘`: chart reconstructed from reported values.

## Figure policy

- A figure must remain interpretable at presentation scale.
- Do not show a manuscript page as a substitute for explaining a result.
- Keep original figure numbers in the caption so the audience can return to the paper.
- If a figure cannot be embedded, provide a clear text-based placeholder and the exact source location; do not use an unrelated illustration.
- For reconstructed charts, retain the original units and disclose transformation or normalization.

## Visual system

- 16:9 canvas, minimum body text around 24 px, minimum captions around 16 px.
- Maximum 6–8 short bullet lines on a standard slide.
- High-contrast neutral background with one accent color; use a second accent sparingly.
- Use horizontal flow for time or workflow, grouped bars for comparisons, and dot plots for distributions when the source data support them.
- Avoid 3-D charts, truncated axes, dual axes without explicit justification, and decorative graphics that compete with evidence.
- Every chart needs title, units, denominator or `n`, uncertainty definition, and source.

## HTML delivery

- Use semantic `<section class="slide">` elements.
- Keep all CSS, JavaScript, fonts, and images in the single HTML file.
- Support keyboard navigation with left/right arrows and space, plus clickable controls.
- Add a progress indicator and slide counter.
- Include `@media print` rules so each slide starts on a new printed page.
- Use `lang` and viewport metadata, descriptive image alt text, and accessible contrast.
- Avoid external scripts, tracking, remote fonts, and network-dependent assets.
