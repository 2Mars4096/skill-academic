# Meso-skills

A meso skill helps finish one recognizable piece of work. Each card gives the inputs to inspect, a short procedure, a test that can change the result, and a deliverable. The [micro-skill map](../micro-skills/README.md) supplies the corresponding task vocabulary and preferences.

| Category | Task and check |
| --- | --- |
| [Research discovery and design](meso-research-design/SKILL.md) | [Screen research questions](meso-screen-research-questions/SKILL.md) · creative comparison |
| [Empirical code and data](meso-empirical-analysis/SKILL.md) | [Clean records for an analysis sample](meso-clean-analysis-records/SKILL.md) · [Link data sources and audit coverage](meso-link-analysis-sources/SKILL.md) · [Construct a panel and its measures](meso-construct-analysis-panel/SKILL.md)<br>[Organize research files for reruns](meso-organize-analysis-pipeline/SKILL.md)<br>[Check a descriptive pattern](meso-describe-empirical-pattern/SKILL.md) · [Estimate and verify a baseline](meso-estimate-empirical-baseline/SKILL.md) · [Compare a regression variation with its baseline](meso-vary-regression/SKILL.md)<br>[Choose the next empirical test](meso-advance-empirical-analysis/SKILL.md) |
| [Academic manuscripts](meso-academic-writing/SKILL.md) | [Write a paper’s data section](meso-write-data-section/SKILL.md) · reconstruction check<br>[Write an empirical results section](meso-write-empirical-results/SKILL.md) · interpretation check |
| [Research exhibits and presentations](meso-research-exhibits/SKILL.md) | [Prepare a comparative figure](meso-draw-comparison-figure/SKILL.md) · final-size visual check |
| [Professional communication and follow-up](meso-professional-communication/SKILL.md) | [Report what changed after feedback](meso-report-on-feedback/SKILL.md) · coverage check |
| [Software implementation and maintenance](meso-software-maintenance/SKILL.md) | [Verify a reported bug fix](meso-verify-reported-bug/SKILL.md) · reproduction check |

## Human selection

Open [Meso-skills](meso-skills/SKILL.md) or invoke `$meso-skills`. Ask “Which workflow fits this task?” to receive one suggestion and its pass limit. To start immediately, say “Use the data-section workflow once on this draft.” Accepting a named suggestion also selects it for that request.

Category cards are menus. Every card has implicit invocation disabled. Each task ends after its initial check or, when there is a specific failure to correct, one revision and recheck. A missing input produces a specific open item. Further rounds and additional tasks require a new human choice. Reading a related micro rule supplies context and does not change its saved status.

## Selection of the first workflows

The priority was the cost of getting the task wrong a second time. The first cards cover recurring corrections that require several linked decisions and have an observable test. For example, the data-section check traces an observation from source to sample. The idea-screening check asks whether the surviving explanations predict anything different. A formatting preference with a direct check can stay at the micro level.

Each task should produce a recognizable deliverable through several dependent steps. A correction belongs at the step where it changes the decision or verification. When revising a workflow from feedback, read the preceding request, the response being corrected, and later qualifications wherever available. Establish the task and the scope of the rejection before generalizing it.

The correction on each card is a generalization of user feedback. The task boundaries, ordering, and one-revision limit are design choices for an explicit-only trial. All entries start as drafts.

## History reviewed

The review screened 3,144 local Codex transcript files across current and archived history, separated agent runs, and screened the local CLI prompt history as a supplementary source. It also consulted the previous micro-skill synthesis. Three listed Codex chats had no retrievable transcript. In this pass, 204 of the 386 listed ChatGPT chats were read through their available message pages. The history service rate-limited further reads. These sources overlap. The selection reflects recurring corrections and their consequences, without assigning frequency rankings or recording historical project details.

A follow-up review screened 3,147 local transcript files, checked the CLI prompt history, and consulted three relevant ChatGPT chats for data preparation, research file structure, and analytical sequencing. The added cards generalize corrections about sample loss, merge coverage, aggregation, reproducible exhibits, and the evidence needed before moving to a further test. The one-test limit is a workflow design choice.

The contextual review on 2026-11-11 read correction passages with surrounding assistant and user turns in two local conversation records, plus neighboring user turns from five older CLI histories. Those older histories preserve user prompts, while full assistant responses were unavailable for the selected corrections. This pass revised the affected multi-step workflows for sample audits, pipeline reorganization, measure construction, descriptive checks, regression comparisons, progressive analysis, and bug verification. Earlier file counts describe screening coverage. They do not represent complete conversational reading of every file.
