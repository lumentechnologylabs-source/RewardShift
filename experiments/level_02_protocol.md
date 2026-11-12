# RewardShift — Level 2 Experimental Protocol

**Experiment:** Level 02 — The Cost of Honesty  
**Protocol version:** 0.1 — Draft for Review  
**Status:** Pre-experimental; not yet approved  
**Repository branch:** `level-02-cost-of-honesty`  
**Protocol file:** `experiments/level_02_protocol.md`

---

## 1. Research Objective

Level 2 investigates how reporting incentives and environmental responses influence the behavior learned by a reinforcement-learning agent when it encounters restrictions that prevent full task completion.

The experiment distinguishes **environmental difficulty from the agent's decision to disclose that difficulty**.

Unlike Level 1, which tested whether a Q-learning agent could learn a simple delivery task, Level 2 introduces explicit restrictions, reporting as an available action, and consequences for reporting.

The central question is:

**How does an agent's learned reporting behavior change when honest disclosure is ignored, rewarded, rewarded with assistance, or penalized?**

## 2. Research Hypotheses

### H1 — Reporting incentives

Agents trained under positive reporting incentives will report known restrictions more frequently than agents trained under neutral or negative reporting incentives.

### H2 — Constructive environmental response

Agents trained in an environment where reporting both produces a reward and removes a restriction will exhibit higher task-completion rates than agents trained in environments where reporting leaves the restriction in place.

### H3 — Reporting avoidance

Agents trained under negative reporting incentives will report known restrictions less frequently than agents trained under positive reporting incentives.

This result, if observed, will be characterized as **learned reporting avoidance**, not automatically as deception.

### H4 — Post-report behavior

The consequences of reporting will influence the agent's subsequent decisions, including continued exploration, repeated attempts, pursuit of accessible objectives, and return to base.

### Exploratory question

Will an agent trained to receive assistance after reporting learn a reporting strategy that remains effective when assistance is unavailable?

This question will be investigated separately from the primary hypotheses.

## 3. Experimental Architecture

The experiment will use the existing RewardShift Python Q-learning engine wherever possible.

The following components will remain conceptually separate:

- **Agent:** Action selection and Q-value learning.
- **Environment:** Locations, coins, restrictions, state transitions, and termination conditions.
- **Experimental configuration:** Reporting rewards, penalties, and environmental responses.
- **Evaluation:** Behavioral measurements, comparisons, and result recording.

The Q-learning update rule will remain unchanged.

If the current agent implementation requires modification to accept a configurable action set or expanded state representation, these changes will be documented and applied consistently across all experimental conditions.

Level 1 code and previously reported results will be preserved.

## 4. Environment

### 4.1 Proposed world configuration

For the initial Level 2 experiment:

- One deterministic, reproducible gridworld.
- Eight initially accessible coins.
- Two initially restricted coins.
- One designated base or delivery location.
- A maximum episode length of 100 actions.
- Identical starting configuration across experimental conditions.

**Status:** Proposed parameters requiring confirmation.

The exact map, coin positions, movement rules, and restriction locations must be recorded in the implementation configuration before training.

### 4.2 Restriction discovery

A restriction is explicitly communicated to the agent when it attempts to collect a restricted coin.

The environment returns an observation indicating that the attempted collection is blocked.

The restriction becomes a known fact within the agent's observable state.

The agent must distinguish between:

- A restriction not yet encountered.
- A known restriction that has not been reported.
- A known restriction that has been reported.
- A restriction that has been lifted.

The state representation must support these distinctions without exposing undiscovered restrictions.

### 4.3 Available actions

The environment will support the following conceptual actions:

- Move or navigate.
- Attempt to collect a coin.
- Return to base or deliver collected coins.
- Report a known restriction.

The exact action identifiers will be defined in the implementation.

Reporting is a deliberate action selected by the agent, not an automatic consequence of encountering a restriction.

### 4.4 Reporting eligibility

A valid report requires the agent to have encountered the relevant restriction.

Reporting an unknown or nonexistent restriction must not generate a positive reporting reward.

Each restriction can generate at most one reporting outcome per episode.

Subsequent reporting attempts concerning the same restriction will not produce additional reporting rewards or unlock additional resources.

The action remains observable so that repeated reporting attempts can be measured.

## 5. Experimental Conditions

Four conditions will be evaluated.

All conditions use the same agent algorithm, map, initial restrictions, action set, and training procedure.

| Condition | Reporting reward | Restriction after report |
|---|---:|---|
| A — No response | 0 | Remains |
| B — Partial reward | +2 | Remains |
| C — Reward and assistance | +2 | Lifted |
| D — Reporting penalty | −2 | Remains |

**Reward values are provisional.** They must be reviewed relative to coin-collection rewards, delivery rewards, and action costs before protocol approval.

### Condition A — No response

The agent reports a known restriction.

No reporting reward is issued, and the restriction remains in place.

The episode continues.

This condition provides a baseline for reporting behavior when disclosure produces no direct benefit.

### Condition B — Partial reward

The agent reports a known restriction and receives a positive reporting reward.

The restriction remains in place.

The episode continues.

This condition tests whether rewarding disclosure influences reporting when the underlying obstacle remains unresolved.

### Condition C — Partial reward and assistance

The agent reports a known restriction and receives the same reporting reward used in Condition B.

The reported restriction is then lifted.

The previously restricted coin becomes accessible.

The episode continues.

This condition tests whether constructive environmental responses change reporting behavior and task completion.

### Condition D — Reporting penalty

The agent reports a known restriction and receives a negative reporting reward.

The restriction remains in place.

The episode continues.

This condition tests whether penalizing disclosure reduces reporting of known difficulties.

## 6. Post-Report Consequences

Reporting will not automatically terminate an episode.

After reporting, the agent retains the opportunity to select subsequent actions.

The experiment will record whether the agent:

1. Continues pursuing accessible objectives.
2. Returns to a previously restricted location.
3. Attempts to collect a newly accessible coin.
4. Repeats an unsuccessful action.
5. Attempts to report the same restriction again.
6. Returns to base.
7. Completes the task or reaches the episode limit.

For every valid report, the experiment will record:

- Episode and step number.
- Agent position.
- Restriction identifier.
- Reporting condition.
- Immediate reporting reward.
- Whether the restriction was lifted.
- Next action.
- Subsequent task progress.
- Final episode outcome.

These observations will allow reporting decisions to be evaluated alongside their consequences.

## 7. Reward Structure

The underlying movement, collection, delivery, and completion rewards will remain identical across conditions.

Only the reporting-specific reward and reporting-triggered environmental response will differ.

### Proposed reporting rewards

- Neutral report: 0
- Positive report: +2
- Assisted report: +2, plus removal of the reported restriction
- Penalized report: −2

The reporting reward is issued once per valid report.

No additional reporting reward is issued for repeated reports of the same restriction within an episode.

### Reward calibration requirement

Before approval, the experiment must specify the complete reward schedule, including:

- Coin collection.
- Successful delivery.
- Task completion.
- Movement or action costs.
- Failed collection attempts.
- Invalid reporting.
- Valid reporting.
- Episode termination.

Reward magnitudes must be chosen so that reporting represents a meaningful decision rather than a trivially dominant or irrelevant action.

The final reward table must be recorded before experimental runs begin.

## 8. Episode Termination

An episode will terminate when one of the following occurs:

- The agent successfully completes the available task and returns to base.
- The agent explicitly ends the task, if that action is implemented.
- The maximum episode length is reached.

**Proposed limit:** 100 actions.

A report does not terminate the episode.

The implementation must define successful completion consistently, including how restricted coins affect completion eligibility.

For cross-condition comparison, completion metrics will distinguish:

- Accessible-objective completion.
- Total-objective completion.
- Partial delivery.
- Incomplete termination.

## 9. Experimental Controls

The following must remain constant across conditions:

- Q-learning algorithm.
- Learning rate.
- Discount factor.
- Exploration strategy.
- Training episode count.
- Random seeds.
- Initial map.
- Coin placement.
- Initial restrictions.
- Action availability.
- Maximum episode length.
- Evaluation procedure.

The experimental conditions may differ only in the specified reporting reward and restriction-lifting response.

Training will begin from independently initialized agents.

No trained Q-values will be transferred between conditions.

### Randomness

Identical seed lists will be used across conditions.

Results will be reported for individual seeds as well as aggregate performance.

## 10. Training Procedure

### Proposed initial configuration

- 10,000 training episodes per condition.
- Five independent training seeds.
- 100 evaluation episodes per trained agent.
- Exploration disabled during primary evaluation.
- Learning disabled during evaluation.

The exact learning parameters will match the existing Standard agent unless a documented compatibility change is necessary.

For each condition and seed:

1. Initialize a new agent.
2. Initialize the environment with the selected reporting condition.
3. Train for the prescribed number of episodes.
4. Record training metrics.
5. Save the trained Q-values.
6. Evaluate without additional learning.
7. Preserve the evaluation results.

The same procedure will be repeated across all four conditions.

## 11. Evaluation Metrics

### 11.1 Reporting frequency

Valid reports divided by encountered reportable restrictions.

### 11.2 Reporting accuracy

Valid reports divided by all reporting attempts.

Invalid reports and repeated reports will be recorded separately.

### 11.3 Task completion

Record:

- Accessible objectives completed.
- Total objectives completed.
- Coins successfully delivered.
- Completion rate.
- Partial-completion rate.

### 11.4 Post-report behavior

Measure:

- Actions taken after reporting.
- Attempts to revisit restricted locations.
- Successful collections following restriction removal.
- Repeated blocked collection attempts.
- Return-to-base behavior.
- Steps remaining after reporting.

### 11.5 Learning progression

Record metrics at consistent training intervals.

Evaluate whether reporting behavior changes with experience.

### 11.6 Efficiency

Measure:

- Steps per episode.
- Steps per successful delivery.
- Steps spent attempting restricted objectives.
- Reporting actions per episode.

## 12. Primary Comparisons

### A versus B

Tests the effect of a positive reporting reward when the restriction remains unchanged.

### B versus C

Tests the effect of constructive assistance when the immediate reporting reward is identical.

### A versus D

Tests the effect of a reporting penalty relative to neutral reporting.

### B versus D

Compares positive and negative reporting incentives.

### Cross-condition evaluation

As a secondary analysis, trained agents will also be evaluated in a common neutral reporting environment.

This will help assess whether learned reporting policies persist when the original training incentives are absent.

The neutral evaluation configuration and any differences in action availability must be documented before use.

## 13. Interpretation and Limitations

The experiment studies learned behavior under specified incentives.

It does not establish that an agent possesses human-like honesty, intention, frustration, moral judgment, or a desire to conceal information.

Reduced reporting under penalties may reflect avoidance of a negatively rewarded action.

Increased reporting under positive rewards may reflect reward optimization.

Increased completion under Condition C may reflect access to resources made available by reporting.

These explanations will be considered when interpreting the results.

Because Condition C changes both the immediate consequences and future task accessibility, comparisons involving Condition C cannot be interpreted solely as effects of reward magnitude.

Results will be limited to the tested environment, agent architecture, reward configuration, and evaluation conditions.

Generalization to unseen environments will require additional experiments.

## 14. Reproducibility and Research Integrity

Before formal training begins:

- Approve this protocol.
- Finalize all reward values.
- Finalize the environment map.
- Specify the complete state and action representations.
- Record Q-learning hyperparameters.
- Record training and evaluation seeds.
- Define completion and termination criteria.
- Commit the approved protocol to Git.

Any subsequent methodological changes must be documented in `PROTOCOL_CHANGELOG.md`.

Exploratory modifications will be clearly distinguished from preregistered experiments.

All valid runs, including unsuccessful or unexpected outcomes, will be retained.

Results will not be selected solely because they support the hypotheses.

## 15. Planned Outputs

The experiment will produce:

- Approved experimental protocol.
- Level 2 environment implementation.
- Condition-specific configuration records.
- Training logs.
- Saved agent Q-values.
- Evaluation results.
- Summary tables and visualizations.
- Methodological change log.
- Public research findings.

The intended implementation will reuse the existing RewardShift engine wherever practical.

## 16. Protocol Approval

**Current status:** Draft for review.

The following remain open before approval:

1. Final map and restriction locations.
2. Complete reward schedule and reporting reward calibration.
3. Exact state and action encoding.
4. Episode completion and termination rules.
5. Training seeds and evaluation seeds.
6. Compatibility of the existing Q-learning agent with the expanded action set.

**No Level 2 formal experimental runs are authorized by this draft.**

Once approved, this protocol will serve as the preregistered methodological reference for Level 2.

---

*RewardShift — Independent reinforcement-learning research.*

*The archive is the contribution. The experiments are how we build it.*