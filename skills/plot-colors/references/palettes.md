# Academic Plot Color Schemes

Use these palettes as named defaults. Keep category-to-color mappings stable across all related figures in a paper, deck, dashboard, or appendix.

## Academic Scheme Library

### Academic Categorical

Use for unordered categories in papers, slides, and reports. This is the safest general-purpose academic palette.

```text
blue        #0072B2
orange      #E69F00
green       #009E73
purple      #CC79A7
sky         #56B4E9
vermillion  #D55E00
yellow      #F0E442
black       #000000
```

Default order: blue, orange, green, purple, vermillion, sky. Use yellow only for large filled marks or annotations with dark outlines.

### Restrained Academic

Use when the figure should look serious, quiet, and durable in a paper, brown-bag seminar, dissertation defense, or academic slide deck.

```text
ink         #243447
blue        #2F6B9A
teal        #2A9D8F
ochre       #B0892F
brick       #B75D45
plum        #7C5A82
slate       #6B7280
mist        #D8DEE9
```

Good pairings:

- control versus treatment: slate `#6B7280`, blue `#2F6B9A`
- two treatments: blue `#2F6B9A`, brick `#B75D45`
- mechanism groups: teal `#2A9D8F`, ochre `#B0892F`, plum `#7C5A82`
- text and axes: ink `#243447`, slate `#6B7280`, mist `#D8DEE9`

### Journal Minimal

Use for print-forward economics, political science, sociology, public policy, and statistics papers where colors should not dominate the figure.

```text
main        #2F5597
secondary   #A65E2E
tertiary    #5B7F5B
quaternary  #6F5B7F
neutral     #6B7280
light       #D1D5DB
dark        #1F2937
```

Use only two or three colors in a single figure. Prefer neutral gray plus one accent when the result is simple.

### Editorial Modern

Use for polished policy charts, working-paper summaries, lab websites, and public-facing research notes.

```text
navy        #1B365D
cyan        #0086A8
coral       #D95F59
gold        #D4A72C
mint        #4C956C
violet      #6D5BD0
warm gray   #7A7A73
```

Use navy or warm gray for context, then one bright accent for the main point. Avoid using all seven colors at once.

### Highlight

Use when most series are context and one or two series carry the message.

```text
context     #CBD5E1
context dk  #94A3B8
primary     #005AB5
secondary   #D55E00
positive    #009E73
negative    #B2182B
text        #1F2933
```

Default: all non-focal series in context gray, focal series in primary blue. Use secondary orange only for a true comparison or benchmark.

### Treatment And Control

Use for randomized experiments, quasi-experiments, treatment/control plots, and policy comparisons.

```text
control     #6B7280
treatment   #0072B2
treat alt   #D55E00
placebo     #009E73
excluded    #CBD5E1
event       #111827
```

Use treatment blue for treated units, gray for controls, orange only for a second active treatment, and black for event timing or reference lines.

### Event Study

Use for event-study coefficients, dynamic treatment effects, impulse responses, or time relative to treatment.

```text
estimate    #0072B2
ci fill     #0072B2
pre trend   #6B7280
event line  #D55E00
zero line   #111827
excluded    #CBD5E1
```

Use estimate blue for the coefficient path, the same blue at alpha `0.15` to `0.25` for confidence intervals, orange for the event line, and black or dark gray for the zero line.

### Coefficient Plot

Use for regression coefficient plots, forest plots, meta-analysis summaries, and specification curves.

```text
estimate    #2F6B9A
ci          #8FB7D4
baseline    #111827
positive    #009E73
negative    #B75D45
omitted     #D1D5DB
```

Use one estimate color unless signs are the substantive message. If color encodes sign, still include a zero line and order coefficients logically.

### Multi-Arm Experiment

Use when there is one control and several active arms.

```text
control     #6B7280
arm 1       #0072B2
arm 2       #D55E00
arm 3       #009E73
arm 4       #7C5A82
arm 5       #B0892F
pooled      #111827
```

Keep control gray. If a pooled treatment estimate appears, make it dark and visually distinct from individual arms.

### Mechanism

Use for mechanism channels, mediation, decomposition, contribution plots, or theory components.

```text
information #2F6B9A
incentives  #B0892F
constraints #B75D45
selection   #7C5A82
spillover   #2A9D8F
residual    #6B7280
```

Use stable semantic names across the paper or deck. Do not reuse the same color for different mechanisms in neighboring figures.

### Subgroups

Use for heterogeneity by demographic, geography, baseline status, or market segment.

```text
overall     #111827
group 1     #2F6B9A
group 2     #B75D45
group 3     #2A9D8F
group 4     #7C5A82
group 5     #B0892F
other       #9CA3AF
```

Plot the overall estimate in black or dark gray when shown with subgroups. Use direct labels if the legend gets long.

### Ordered Academic

Use for terciles, quartiles, quintiles, income bins, exposure bins, risk levels, or ordinal survey categories.

```text
lowest      #E8EEF4
low         #C7D7E8
middle      #8FB1D1
high        #4F82B5
highest     #1F4E79
```

Use light to dark to encode order. Do not assign arbitrary categorical colors to ordered bins.

### Likert And Survey

Use for agreement, satisfaction, ideology scales, and other balanced ordinal survey responses.

```text
strong neg  #B2182B
neg         #EF8A62
neutral     #F7F7F7
pos         #67A9CF
strong pos  #2166AC
missing     #D1D5DB
```

Center neutral responses. Use a diverging stacked bar only when the question has a natural negative-to-positive structure.

### Model Comparison

Use for comparing estimators, models, algorithms, or specifications.

```text
baseline    #6B7280
preferred   #0072B2
alternative #D55E00
robust      #009E73
oracle      #111827
invalid     #B91C1C
```

Make the preferred model visually prominent only after the caption or text makes the criterion clear.

### Print And Grayscale

Use when the figure must survive black-and-white printing, photocopying, or journal workflows that downgrade color.

```text
black       #111111
dark gray   #444444
medium      #777777
light       #AAAAAA
very light  #DDDDDD
white       #FFFFFF
accent      #0072B2
```

Use line types, marker shapes, and direct labels. The accent color is optional and should not be required to read the figure.

## Sequential Schemes

Sequential schemes encode magnitude from low to high. Use the darkest values for the highest magnitude and keep legends ordered.

### Sequential Blue

Use for rates, counts, probabilities, and general intensity.

```text
#F7FBFF
#DEEBF7
#C6DBEF
#9ECAE1
#6BAED6
#3182BD
#08519C
```

### Sequential Teal

Use when blue is already reserved for a categorical concept, or for density and model-score surfaces.

```text
#F3FBF8
#D7F0EA
#A8DBD3
#66BFB6
#2C9990
#0B625F
```

### Sequential Purple

Use for secondary outcomes, uncertainty surfaces, or ordered categorical heatmaps where blue would imply the main result.

```text
#FCFBFD
#EFEDF5
#DADAEB
#BCBDDC
#9E9AC8
#756BB1
#54278F
```

### Sequential Green

Use for cumulative adoption, coverage, completion, compliance, or positive accumulation. Do not use it as the opposite of red unless labels also carry the meaning.

```text
#F7FCF5
#E5F5E0
#C7E9C0
#A1D99B
#74C476
#31A354
#006D2C
```

### Sequential Gray

Use for secondary magnitude encoding or when hue would overstate importance.

```text
#F8F9FA
#E9ECEF
#DEE2E6
#ADB5BD
#6C757D
#343A40
```

Pair with one accent color for annotations or highlighted cells.

## Diverging Schemes

Diverging schemes must be centered at a substantive reference point, usually zero, parity, a policy threshold, or the sample mean. Do not let auto-scaling move the neutral midpoint.

### Diverging Blue Rust

Use for treatment effects, residuals, differences, and below or above benchmark.

```text
low         #2166AC
low mid     #67A9CF
low light   #D1E5F0
neutral     #F7F7F7
high light  #FDDBC7
high mid    #EF8A62
high        #B2182B
```

### Diverging Purple Green

Use when red would imply danger or political meaning and the contrast is simply low versus high.

```text
low         #762A83
low mid     #9970AB
low light   #E7D4E8
neutral     #F7F7F7
high light  #D9F0D3
high mid    #5AAE61
high        #1B7837
```

### Diverging Navy Gold

Use for slide decks or policy graphics where a warmer high side is desired without using alarm red.

```text
low         #1B365D
low mid     #5D7FA3
low light   #D9E3EF
neutral     #F8F7F2
high light  #F1DBA5
high mid    #D4A72C
high        #8A5A00
```

### Diverging Red Gray Blue

Use when negative and positive are central, but the plot should remain understated.

```text
negative    #B75D45
neg light   #E6C4B8
neutral     #F2F2F2
pos light   #BFD3E6
positive    #2F6B9A
```

## Status Colors

Use sparingly for diagnostics, QA dashboards, and validation reports.

```text
success     #15803D
warning     #C2410C
danger      #B91C1C
info        #2563EB
neutral     #64748B
missing     #9CA3AF
```

Pair status color with labels or icons. Never encode pass/fail with color alone.
