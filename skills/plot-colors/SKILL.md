---
name: plot-colors
description: Choose and enforce professional color schemes for statistical plots, charts, dashboards, academic figures, and publication graphics. Use when creating or revising visualizations in Python, R, LaTeX, ggplot2, matplotlib, seaborn, plotnine, Altair, or similar tools where palette choice, color semantics, accessibility, or visual polish matters.
---

# Plot Colors

## Overview

Use this skill to make plotting colors deliberate, consistent, accessible, and publication-ready. Pick colors by data role first, then by aesthetic preference.

The output should usually include:

- a named palette with hex values
- a variable-to-color mapping when categories are stable
- notes on accessibility, contrast, and export context
- code changes for the plotting library being used

## Start Here

1. Identify the color role:
   - `categorical`: unordered groups
   - `ordered categorical`: ranked bins
   - `sequential`: low to high magnitude
   - `diverging`: negative to positive or below to above reference
   - `highlight`: one or two focal series against context
   - `status`: success, warning, danger, neutral
2. Choose one palette family from `Scheme Selector`.
3. Assign stable colors to stable concepts. The same variable should keep the same color across figures.
4. Check the figure in grayscale and colorblind-safe terms. Do not rely on red versus green alone.
5. Keep non-data ink quiet: use muted axes, light grids, and dark text.

## Hard Rules

- Do not use rainbow, `jet`, or hue-only gradients for numeric data.
- Use at most 6 categorical colors in a normal academic plot. If there are more groups, combine, facet, or highlight.
- Do not let bright yellow carry thin lines or small text. Use it only for filled marks with a dark outline or as a secondary accent.
- Reserve red for negative, loss, warning, or treated-as-problem meanings unless the domain clearly says otherwise.
- Use saturation to focus attention. Context series should usually be gray or low-alpha.
- Use line style, marker shape, labels, or facetting in addition to color for important distinctions.
- Keep background and grids restrained:
  - background: `#FFFFFF` or `#FAFAF7`
  - text: `#1F2933`
  - axis: `#475569`
  - grid: `#D9DEE7`

## Scheme Selector

Choose the scheme by empirical job. Do not pick a palette only because it looks attractive.

| Case | Default scheme | Why |
| --- | --- | --- |
| Paper figure with unrelated groups | `Academic Categorical` | colorblind-safe and recognizable |
| Serious seminar or job-market slides | `Restrained Academic` | polished, muted, readable on projectors |
| One focal result among many context series | `Highlight` | makes the claim visually obvious |
| Experiment, treatment/control, DiD | `Treatment And Control` | stable causal-design semantics |
| Event study | `Event Study` | separates estimates, confidence, event, and zero line |
| Regression coefficient plot | `Coefficient Plot` | distinguishes estimates, uncertainty, and reference |
| Mechanism or decomposition plot | `Mechanism` | multiple related concepts without garish colors |
| Ordered bins or quantiles | `Ordered Academic` | keeps order visible through luminance |
| Heatmap, map, density, risk score | a `Sequential` scheme | one direction of magnitude |
| Difference, residual, effect around zero | a `Diverging` scheme | centered around a meaningful midpoint |
| Print-first journal output | `Print And Grayscale` | works in black and white |
| Validation or diagnostics | `Status` | conventional status semantics |

## Detailed Palette Reference

Read [references/palettes.md](references/palettes.md) whenever selecting or implementing a color scheme. It contains the full academic palette catalog, including categorical, treatment/control, event-study, coefficient-plot, mechanism, subgroup, ordered, Likert, model-comparison, print/grayscale, sequential, diverging, and status schemes.

## Chart Guidance

### Lines

- Use 2 to 4 colored lines at most.
- Put the focal line in the strongest color and context lines in gray.
- Use direct labels when possible. Legends are acceptable when labels would clutter.
- For confidence bands, use the same hue with low alpha, typically `0.12` to `0.20`.

### Bars

- Use one color for a single series.
- Use grouped colors only when groups are the point of the chart.
- Sort bars by value or a meaningful domain order. Color should not compensate for poor ordering.

### Scatter

- Use alpha before adding more colors when points overlap.
- Use color for group and marker shape for a second important categorical variable.
- Avoid tiny low-contrast points on white backgrounds.

### Heatmaps And Maps

- Sequential data gets sequential palettes.
- Difference data gets diverging palettes centered at zero or the benchmark.
- Missing values should be light neutral gray and explicitly labeled.

### Multi-Panel Figures

- Keep color mappings identical across panels.
- Share legends unless panels encode genuinely different variables.
- Use panel titles and direct labels to reduce legend decoding.

## Implementation Snippets

### Python: matplotlib and seaborn

```python
PLOT_COLORS = {
    "control": "#6B7280",
    "treatment": "#0072B2",
    "event": "#D55E00",
    "placebo": "#009E73",
    "text": "#1F2933",
    "axis": "#475569",
    "grid": "#D9DEE7",
}

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(
    style="whitegrid",
    rc={
        "axes.edgecolor": PLOT_COLORS["axis"],
        "axes.labelcolor": PLOT_COLORS["text"],
        "text.color": PLOT_COLORS["text"],
        "xtick.color": PLOT_COLORS["axis"],
        "ytick.color": PLOT_COLORS["axis"],
        "grid.color": PLOT_COLORS["grid"],
        "figure.facecolor": "#FFFFFF",
        "axes.facecolor": "#FFFFFF",
    },
)
```

### R: ggplot2

```r
plot_colors <- c(
  control = "#6B7280",
  treatment = "#0072B2",
  event = "#D55E00",
  placebo = "#009E73"
)

p +
  scale_color_manual(values = plot_colors) +
  scale_fill_manual(values = plot_colors) +
  theme_minimal(base_size = 11) +
  theme(
    text = element_text(color = "#1F2933"),
    axis.text = element_text(color = "#475569"),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "#D9DEE7", linewidth = 0.25)
  )
```

### Diverging Scale

```r
scale_fill_gradient2(
  low = "#2166AC",
  mid = "#F7F7F7",
  high = "#B2182B",
  midpoint = 0
)
```

```python
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm

cmap = LinearSegmentedColormap.from_list(
    "blue_rust",
    ["#2166AC", "#67A9CF", "#F7F7F7", "#EF8A62", "#B2182B"],
)
norm = TwoSlopeNorm(vmin=-max_abs, vcenter=0, vmax=max_abs)
```

## QA Checklist

Before finishing a plot color pass, check:

- The chosen palette matches the data role.
- Important categories have stable colors across all related plots.
- The plot is readable when printed in grayscale.
- Red and green are not the only distinction for a key comparison.
- Legends, direct labels, annotations, and captions use the same names as the data.
- Axis, grid, and background colors do not compete with the data.
- Exported PNG/PDF/SVG output matches the intended colors.
