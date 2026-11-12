# RewardShift — Research Protocols

**Version:** 0.1 — Draft  
**Status:** Proposed standing research standards  
**Applies to:** All RewardShift experiments  
**Related documents:** `RESEARCH_ROADMAP.md`, `PROTOCOL_CHANGELOG.md`, and experiment-specific protocols

---

## 1. Purpose

This document establishes the standing scientific and methodological standards for RewardShift.

RewardShift is an independent research project investigating how reward structures, environmental constraints, and learning algorithms influence the behavior of artificial intelligence agents.

These protocols are intended to ensure that experiments are transparent, reproducible, traceable, and open to independent scrutiny.

**Guiding principle:**

*The archive is the contribution. The experiments are how we build it.*

**Research philosophy:**

*Playful on the surface. Rigorous at the core.*

## 2. Research Integrity

RewardShift commits to preserving an accurate historical record of its research activities.

All research must distinguish between:

- **Hypotheses:** Predictions made before examining relevant experimental outcomes.
- **Observations:** Behaviors or measurements recorded during experiments.
- **Interpretations:** Explanations proposed for observed results.
- **Conclusions:** Claims supported by the available evidence.
- **Limitations:** Conditions or uncertainties restricting the conclusions that may reasonably be drawn.

Unexpected results, unsuccessful experiments, and findings that contradict a hypothesis must be retained and reported.

Results must not be selectively omitted to create a misleading impression of success.

Exploratory findings must not be retrospectively presented as confirmation of previously established hypotheses.

Errors may be corrected, but the correction and its rationale must be documented.

## 3. Experimental Design

Every formal experiment must have a written, version-controlled protocol before its first designated research run.

The protocol must identify:

1. Research question
2. Hypothesis or hypotheses
3. Independent variables
4. Dependent variables and outcome metrics
5. Controlled variables
6. Experimental conditions
7. Agent and environment versions
8. Training and evaluation procedures
9. Random seeds and sampling strategy
10. Planned analysis methods
11. Success, failure, and termination criteria
12. Known limitations and potential confounding factors

Where relevant, the protocol should also specify the number of training runs, evaluation episodes, and the rationale for those quantities.

The protocol must distinguish exploratory analysis from analyses intended to test a prespecified hypothesis.

### 3.1 Experimental Controls

When comparing agents or reward structures, all variables not intentionally under investigation should be held constant wherever feasible.

Any unavoidable differences must be documented and considered when interpreting results.

A comparison must not be described as controlled if meaningful differences between conditions remain unaccounted for.

### 3.2 Baseline Preservation

RewardShift maintains reference implementations for comparison.

The Standard Agent is the unchanged reference learning implementation for experiments in which it serves as the control.

The Untrained Agent uses the corresponding standard architecture without training.

The Tinkered Agent may contain experimental modifications to the learning algorithm or architecture.

Changes to the Standard Agent must not be introduced silently during comparisons.

If a reference implementation must change, the revised version must be identified and comparisons must account for the change.

### 3.3 Separating Experimental Variables

Changes to the reward function, environment, observation representation, and learning algorithm must be distinguished from one another.

Where an experiment necessarily changes multiple factors, the protocol must identify them and explain how their effects will be interpreted.

No experiment should attribute an observed behavioral difference to a single factor without sufficient controls or supporting evidence.

## 4. Reproducibility Standards

Every formal experiment must preserve sufficient information for another researcher to reproduce the procedure.

Required information includes, where applicable:

- Source code revision or Git commit identifier
- Environment name and version
- Agent implementation and version
- Reward function and parameter values
- Training episode count
- Evaluation episode count
- Maximum steps per episode
- Learning rate and discount factor
- Exploration policy and schedule
- Random seeds and random-number generator details
- Relevant software and dependency versions
- Execution instructions
- Output file locations and formats

A fixed seed supports reproducibility but does not, by itself, demonstrate that findings are robust.

Experiments intended to support general behavioral conclusions should evaluate performance across multiple appropriate seeds or independent runs.

Where full reproducibility is not possible, the limitations must be stated.

### 4.1 Determinism

Deterministic environments should produce consistent outcomes when initialized with identical relevant configurations and random seeds.

Any sources of nondeterminism must be documented.

### 4.2 Training and Evaluation Separation

Evaluation must not silently update an agent's learned parameters.

Training and evaluation procedures must be explicitly separated unless online learning during evaluation is itself the subject of the experiment.

Evaluation configurations intended as holdouts must not be used for training or iterative model selection.

If holdout information is exposed during development, that exposure must be documented and a new holdout may be required.

## 5. Data Collection and Preservation

Raw experimental results are primary research artifacts.

Formal research runs should record, where applicable:

- Experiment identifier
- Protocol version
- Code revision
- Run identifier
- Date and time
- Agent and environment configuration
- Random seeds
- Episode-level outcomes
- Action counts or trajectories relevant to the hypothesis
- Reward totals
- Completion and reporting outcomes
- Errors and interruptions
- Relevant system or execution information

The required schema for each experiment must be specified in its experiment-specific protocol.

### 5.1 Raw Data Integrity

Original raw results must be preserved without silent alteration.

Data cleaning, aggregation, and transformation should produce derived datasets rather than overwrite original observations.

If data must be corrected, the original record, correction procedure, and reason must remain traceable.

### 5.2 Failed and Interrupted Runs

Failed, interrupted, or invalid runs must not simply disappear from the research record.

Each should be identified and classified.

Examples include:

- Software execution failure
- Environment implementation defect
- Invalid experimental configuration
- Interrupted execution
- Unexpected but valid agent behavior

The distinction between a methodological failure and an unfavorable result is essential.

A valid experiment that contradicts its hypothesis is not a failed experiment.

### 5.3 Exclusion Criteria

Rules for excluding runs or observations from the primary analysis should be specified before the relevant research runs.

Post hoc exclusions must be disclosed and justified.

Where practical, analyses should show whether conclusions change when excluded observations are included.

## 6. Analysis and Interpretation

Experimental analysis must distinguish measured results from proposed explanations.

Reports should include relevant descriptive statistics and appropriate comparisons across conditions.

Where useful, report variation across seeds, uncertainty estimates, and the distribution of outcomes rather than only averages.

Claims must not exceed the scope of the evidence.

In particular, behavior observed in a small tabular Q-learning environment must not automatically be generalized to large language models, autonomous production systems, or human cognition.

### 6.1 Unexpected Findings

Unexpected findings should be documented and investigated.

Potential follow-up experiments may be proposed, but those investigations require their own documented hypotheses and methods when used for confirmatory testing.

### 6.2 Negative Results

Results that fail to support a hypothesis are part of the research record.

They must not be concealed solely because they are disappointing or less interesting than anticipated.

### 6.3 Alternative Explanations

Reports should identify plausible alternative explanations for important observations.

Where possible, follow-up experiments should be designed to distinguish between competing explanations.

## 7. Protocol Versioning and Amendments

Standing research protocols and experiment-specific protocols must be version-controlled.

The repository maintains `PROTOCOL_CHANGELOG.md` to document substantive methodological changes.

Each amendment should record:

- Date
- Affected document or experiment
- Previous protocol version
- New protocol version
- Description of the change
- Reason for the change
- Whether experimental runs had already occurred
- Expected effect on comparability or interpretation

### 7.1 Before Experimental Runs

A protocol may be revised freely during design, provided revisions remain traceable.

The finalized protocol must be committed before the corresponding formal experimental runs begin.

### 7.2 After Experimental Runs Begin

Changes made after formal runs begin must be documented as amendments.

The original protocol version must remain recoverable.

Runs conducted under different protocol versions must be distinguishable.

Changes that materially affect experimental conditions, measurements, or analysis may require a new experiment identifier or a separate analysis.

### 7.3 Corrections

Corrections to code, data, or documentation must not erase the historical record of the original issue.

When a defect invalidates results, affected runs must be identified and their validity status updated.

Corrected runs must be recorded separately.

## 8. Code and Agent Version Control

All experiment implementations must be maintained under version control.

Research reports should identify the code revision used to produce their results.

Changes to agent algorithms, environment behavior, reward calculations, observation encoding, and termination conditions must be documented.

### 8.1 Standard Agent

The Standard Agent provides a reference implementation.

Any modification that changes its behavior must be versioned and documented.

Previous versions must remain recoverable.

### 8.2 Tinkered Agent

The Tinkered Agent is the designated experimental implementation.

Each substantive modification should receive a unique identifier, such as `TINK-001`.

Modification records should include:

- Hypothesis or motivation
- Implementation changes
- Relevant parameter differences
- Comparison conditions
- Results
- Limitations
- Follow-up questions

The Tinkered Agent's modifications must not silently alter the reference Standard Agent.

## 9. Validation and Quality Assurance

Before collecting formal research data, the relevant implementation should pass documented validation checks.

These may include:

- Environment reset behavior
- Valid and invalid actions
- Reward calculation
- State transitions
- Episode termination
- Observation accuracy
- Training and evaluation separation
- Save and load consistency
- Seed reproducibility
- Result logging

Validation should test whether the implementation matches the written experimental specification.

Passing tests does not guarantee scientific validity, but it reduces the risk of drawing conclusions from implementation defects.

## 10. Publication Standards

Formal research publications should provide or link to:

1. Research question and hypotheses
2. Applicable protocol and version
3. Code revision
4. Experimental conditions
5. Training and evaluation procedures
6. Raw or appropriately accessible supporting data
7. Analysis methods
8. Results
9. Limitations
10. Relevant amendments and corrections

Public summaries may simplify technical explanations, but they must not misrepresent the underlying findings.

### 10.1 Public Hypotheses

RewardShift may publish hypotheses through LinkedIn, GitHub, or other public channels before conducting experiments.

These publications provide useful context and chronological evidence.

However, a public timestamp alone does not establish that a complete experimental protocol was prespecified.

### 10.2 Educational Demonstrations

Interactive demonstrations, cartoons, and illustrative examples must be distinguishable from formal experimental results.

Fictional character behavior is not research evidence.

### 10.3 Independent Scrutiny

Research materials should be organized to facilitate independent inspection and replication.

Constructive criticism, replication attempts, and alternative interpretations are encouraged.

When external feedback results in a methodological change, that contribution should be acknowledged where appropriate.

## 11. Research Roles and Accountability

RewardShift currently operates as a small independent research project using human direction and AI-assisted development.

The human researcher retains responsibility for research decisions, publication, and the accuracy of the public record.

AI assistance may support:

- Experimental design discussions
- Code generation and review
- Documentation
- Test development
- Data analysis
- Identification of potential methodological weaknesses

AI-generated suggestions and outputs must be reviewed rather than assumed correct.

The use