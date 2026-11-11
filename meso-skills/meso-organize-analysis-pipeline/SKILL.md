---
name: meso-organize-analysis-pipeline
description: "On explicit selection, organize research files for reruns."
metadata:
  level: task
  status: draft
  category: meso-empirical-analysis
---

# Organize research files for reruns

[Empirical code and data](../meso-empirical-analysis/SKILL.md) · [Related micro rule](../../micro-skills/organize-analysis-scripts/SKILL.md)

**Use when** — Working research scripts, data, or outputs need a layout another person can rerun.

**Correction behind the workflow** — The user should be able to find the script behind an exhibit and run the ordinary cleaning sequence in order. Extra folders and parallel versions can obscure both.

**Begin** — Run only after the person selects this task for the current request.

1. Start with the active exhibits and edits in progress. Trace their generating scripts, input files, and shared dependencies. Read the latest structural decisions in the conversation, including changes of mind, before choosing which paths to move.
2. Arrange preparation, estimation or training, and exhibit generation as recognizable stages. Keep substantial cleaning in preparation scripts and give each concrete exhibit an identifiable generating script. Use the established numbered root layout where it applies. In a Stata package, make the substantive do-files execute their own analysis and reserve calls between those files for the run-all entry point.
3. Classify the data before moving anything. Keep original source names under the raw-data convention. Preserve working references to externally stored datasets. Place newly created working data in the established processed-data location. Follow the user's stated exceptions for particular sources.
4. Connect each generated output to its producer. Where outputs use subfolders, name them after the script's descriptive stem with its numeric prefix and extension removed. Keep individual tables and figures available for later assembly. Update an existing file index with script, inputs, outputs, and specification so a collaborator can follow the same path.
5. Run the ordinary preparation steps in order using their defaults. Python cleaning steps should run directly without required command-line arguments. Download steps can retain their options. After a path or code change, regenerate an affected exhibit and compare its sample and substantive values with the previous output. Fix a broken dependency once and recheck.

**Deliver and stop** — Return the working layout or proposed layout, the ordinary run order, and the reproduction result for the tested path. Compare affected sample membership or values before concluding that restructuring had little impact. Allow at most one targeted correction and recheck. Another round or workflow requires a fresh human choice.

**Stay asleep for** — Design a new project scaffold, tidy a general app repository, or prepare a reader-facing replication release.
