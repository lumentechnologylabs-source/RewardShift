# RewardShift

An independent, open experimental archive investigating how reward structures influence agent behavior.

## Mission

RewardShift aims to contribute transparent, reproducible experimental evidence that researchers, developers, and educators can examine, challenge, visualize, and build upon.

**The archive is the contribution. The experiments are how we build it.**

## Research Principles

- Evidence over expectations
- Reproducible experiments
- Preservation of experimental data
- Transparent methods and limitations
- Open scientific discussion
- Independence from commercial influence

## Level 1: Learning to Complete a Task

The initial experiment uses a Python Q-learning agent in a simple coin-collection environment.

Recorded results from one experimental run:

| Metric | Untrained | Trained |
|---|---|---|
| Successful deliveries | 34/100 | 100/100 |
| Average evaluation steps | 28.1 | 6.0 |

Training used 10,000 episodes with seed 42.

These results describe a controlled experimental environment and do not establish generalization to other environments or AI systems.

## Project Files

- `agent.py` - Learning agent
- `world.py` - Experimental environment
- `viewer.py` - Visualization
- `check_learning.py` - Training and evaluation
- `learned_values.json` - Saved learned values
- `learning_check.txt` - Recorded experimental results

## Research Direction

Future experiments will investigate how agents respond to restricted objectives, reporting opportunities, and changing reward structures.

The long-term goal is a freely accessible, well-documented archive of experimental observations and results.
