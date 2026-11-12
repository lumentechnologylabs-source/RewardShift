# RewardShift — Research Roadmap

**Version:** 0.1 — Draft  
**Status:** Working roadmap, subject to revision  
**Project:** RewardShift — Open AI Agent Behavior Research

> **The archive is the contribution. The experiments are how we build it.**

## 1. Mission

RewardShift is an independent, open research project investigating how reward structures, environmental constraints, and learning algorithms influence the behavior of artificial intelligence agents.

Our objective is to create a growing collection of reproducible experiments, transparent observations, and accessible visualizations that other researchers, developers, educators, and interested members of the public can inspect, reproduce, critique, and extend.

RewardShift combines rigorous experimental methods with approachable storytelling and interactive demonstrations.

**Our guiding philosophy: Playful on the surface. Rigorous at the core.**

## 2. Research Principles

RewardShift operates according to the following commitments:

1. **Reproducibility:** Publish the code, configurations, random seeds, and instructions necessary to reproduce experiments.
2. **Transparency:** Distinguish hypotheses, observations, interpretations, and limitations.
3. **Experimental integrity:** Preserve controls, original results, unexpected findings, and unsuccessful experiments.
4. **Traceability:** Connect published conclusions to identifiable experiment versions and supporting data.
5. **Comparability:** Change experimental variables deliberately and document differences between conditions.
6. **Open criticism:** Encourage independent replication, methodological criticism, and alternative explanations.
7. **Methodological improvement:** Document corrections and protocol amendments without silently rewriting the historical record.

Unexpected results are not automatically experimental failures. They are observations requiring investigation.

Similarly, results that support a hypothesis do not automatically establish that the experimental methodology was valid.

## 3. Completed Research

### Level 1 — Coin Collection and Return

**Status:** Initial implementation completed and published.

Level 1 establishes a simple reinforcement-learning environment using tabular Q-learning.

The agent must navigate a four-position environment, collect a coin, and return it to its starting position.

The environment supports four actions:

- Left
- Right
- Collect
- Return

The implementation includes:

- A deterministic environment
- A tabular Q-learning agent
- Exploration and exploitation during training
- Saved and restored learned Q-values
- A visual demonstration
- Baseline and post-training evaluation

**Initial observed results:**

| Measurement | Result |
|---|---|
| Pre-training evaluation | 34 successful deliveries / 100 attempts |
| Post-training evaluation | 100 successful deliveries / 100 attempts |
| Average post-training delivery length | 6.0 steps |
| Training duration | 10,000 episodes |
| Training seed | 42 |

These results demonstrate successful learning of the initial task under the evaluated conditions.

They do not establish generalization to unfamiliar environments or provide evidence of broader AI alignment.

The original implementation is preserved as a reference baseline.

## 4. Active Research

### Level 2 — The Cost of Honesty

**Status:** Experimental design and development.

**Primary research question:**

How does changing the incentive for honest reporting affect an agent's behavior when it encounters an explicitly inaccessible objective?

The environment will introduce restricted coin collection and a mechanism for reporting the restriction.

An agent attempting to collect a restricted coin will receive explicit information that collection is prohibited or impossible under the environment's rules.

**Proposed experimental conditions:**

| Condition | Reporting incentive |
|---|---|
| A — Control | Reporting receives an appropriate reward |
| B — Reduced | Reporting receives a smaller reward |
| C — Penalized | Reporting incurs a penalty |

The intent is to hold the learning algorithm and relevant environmental conditions constant while varying the incentive for reporting.

**Planned observations include:**

- Successful task completion
- Reporting frequency
- Continued attempts to collect restricted coins
- Actions taken after explicit restriction notification
- Episode termination behavior
- Differences across training runs and evaluation seeds

The exact reward values, environment specification, observation representation, termination conditions, and evaluation procedures will be defined in `experiments/level_02_protocol.md` before experimental data collection.

The Level 2 experiment will not be considered preregistered or finalized until those decisions are documented and frozen.

## 5. Planned Research

### 5.1 Holdout Evaluation — Generalization

Investigate whether an agent trained under one environmental configuration can respond appropriately to a different configuration without retraining.

Potential changes include relocating accessible and restricted coins.

Holdout configurations will be reserved for evaluation and excluded from training and model selection.

**Research question:** Has the agent learned behavior that transfers to new configurations, or has it primarily learned responses specific to the training environment?

### 5.2 Inferred Restrictions — Coin Detector

Introduce an environment in which an agent can detect a coin but is not explicitly informed that collection is restricted.

The agent must interpret repeated unsuccessful collection attempts.

Potential behaviors include:

- Continuing collection attempts
- Abandoning the objective
- Investigating alternative approaches
- Reporting uncertainty or inability to complete the task

**Research question:** Can an agent learn to recognize and respond appropriately to an inaccessible objective without receiving an explicit restriction notification?

This experiment is separate from Level 2 because discovering a constraint and responding to a known constraint are different research problems.

### 5.3 Three-Agent Comparative Framework

Develop a controlled framework featuring three agent categories.

**Untrained Agent**

Uses the standard agent architecture without learning. Establishes a pre-training behavioral baseline.

**Standard Agent**

Uses the unchanged reference Q-learning implementation. Serves as the trained control.

**Tinkered Agent**

Uses a deliberately modified learning algorithm or architecture. Serves as the experimental agent.

The Untrained and Standard agents share the same underlying architecture. Only the Tinkered Agent's learning implementation is subject to experimental modification.

Every modification to the Tinkered Agent must be documented with:

- A unique experiment or version identifier
- The motivation and hypothesis
- The precise implementation changes
- Relevant parameters
- Training and evaluation conditions
- Results and supporting data
- Known limitations and alternative explanations

Previous implementations and results must remain recoverable.

### 5.4 Experimental Learning Algorithms

Investigate how deliberate modifications to the learning process affect agent behavior.

Potential research areas include exploration strategies, learning-rate schedules, future-reward estimation, and responses to uncertainty.

Comparisons will use an unchanged Standard Agent as a reference wherever appropriate.

Modifications to the learning algorithm must be distinguished from modifications to the reward function or environment.

### 5.5 Adversarial and Cooperative Environments

Explore environments containing multiple agents with different learning histories, objectives, or incentives.

Possible comparisons include:

- Standard versus Tinkered
- Standard versus multiple Standard agents
- Competitive and cooperative task structures

These experiments remain exploratory and require individual protocols before implementation.

### 5.6 Incentive Laboratory

Develop configurable experiments in which reward parameters can be varied while other relevant conditions remain controlled.

Potential applications include testing sensitivity to reporting rewards, penalties, task-completion incentives, and competing objectives.

User-configurable demonstrations must be distinguished from controlled research runs.

## 6. Research Infrastructure

RewardShift will maintain a modular architecture that supports reuse of validated experimental components.

The intended infrastructure includes:

- A Python experiment engine
- Versioned environments and agent implementations
- Reusable experiment runners
- Explicit configuration files
- Automated validation tests
- Reproducible training and evaluation
- Structured result storage
- Documented compatibility between experiment versions
- Public access to code and supporting research artifacts

Where browser-based and Python implementations share an experimental specification, their behavior should be checked for consistency.

Any differences between implementations must be documented.

### Documentation

The research repository will maintain:

- `RESEARCH_ROADMAP.md` — Current research direction and planned investigations
- `RESEARCH_PROTOCOLS.md` — Standing methodological standards
- `PROTOCOL_CHANGELOG.md` — Changes to research methods and their rationale
- `experiments/level_02_protocol.md` — Level 2 experimental design

Additional experiment-specific protocols and result reports will be created as necessary.

Experimental protocols should be committed before their corresponding experimental runs. Later changes must be recorded as amendments.

Git history provides a useful chronological record but does not independently guarantee research integrity.

## 7. Public Interfaces and Education

### Browser-Based Playground

Develop an accessible interface for exploring agent behavior.

Potential features include:

- Animated gridworld environments
- Untrained, Standard, and Tinkered agent demonstrations
- Visible actions and decisions
- Experiment comparisons
- Q-value and reward visualizations
- Configurable incentive parameters
- Links to underlying research data

Interactive demonstrations will be clearly distinguished from formal research evidence.

### Q-Learning Microscope

Create an educational visualization showing how Q-values change during training.

The tool may illustrate action selection, exploration, reward signals, learning updates, and learned policies.

### Research Newsletter

Explore a long-form publication on Substack documenting experimental questions, methods, results, unexpected observations, and lessons learned.

GitHub remains the authoritative technical research archive.

LinkedIn may serve as a public record of proposed hypotheses, project milestones, and invitations for discussion.

### RewardShift Cartoon Laboratory

Develop a recurring three- or four-panel cartoon strip to make reinforcement-learning concepts approachable.

Proposed recurring characters include:

- **Untrained Agent:** Curious, chaotic, and inclined to consume stationery
- **Standard Agent:** The dependable worker who wants to collect its coins and go home
- **Tinkered Agent:** The experimental inventor whose behavior raises new questions
- **Mark from Corporate:** The demanding but necessary guardian of documentation and data integrity
- **LiDAR O'Reilly:** The research associate responsible for observations and laboratory notes
- **Clippy:** An enthusiastically helpful and frequently unsolicited assistant

Cartoons illustrate research questions; they do not constitute experimental evidence.

The comic strip's title and publication format remain undecided.

## 8. Community and Collaboration

RewardShift aims to encourage meaningful participation rather than prioritize audience size.

Potential community activities include:

- Independent reproduction of experiments
- Suggestions for new research questions
- Methodological criticism
- Contributions to documentation and testing
- Educational use of experimental materials
- Public discussion of results and limitations

GitHub Discussions is a proposed central location for community feedback and research suggestions.

Contributions and external suggestions should be acknowledged appropriately.

## 9. Publication and Research Integrity

The intended publication sequence is:

1. Formulate a research question.
2. Document hypotheses and experimental design.
3. Define controls, metrics, and limitations.
4. Commit the experimental protocol.
5. Implement and validate the experiment.
6. Conduct experimental runs.
7. Preserve raw results and relevant metadata.
8. Analyze outcomes, including unexpected findings.
9. Publish results with supporting evidence.
10. Document corrections, limitations, and follow-up questions.

Exploratory investigations may lead to new hypotheses, but those hypotheses must be identified as arising after the relevant observations.

No result should be presented as confirmatory evidence for a hypothesis formulated after seeing that result.

## 10. Long-Term Objective

RewardShift's long-term objective is to create a growing, transparent, reproducible archive of experiments investigating how learning systems behave under competing incentives, environmental constraints, uncertainty, and changes to their learning algorithms.

The project does not assume that findings from simple tabular Q-learning environments automatically generalize to large language models or more complex AI systems.

Any broader implications must be supported by appropriate evidence and stated with corresponding limitations.

The project's success will be evaluated not only by the behaviors its agents demonstrate, but also by the usefulness, reproducibility, and intellectual honesty of the resulting research archive.

---

**Guiding statement**

*The archive is the contribution. The experiments are how we build it.*

**Research philosophy**

*Playful on the surface. Rigorous at the core.*