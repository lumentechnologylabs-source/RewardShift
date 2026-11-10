"""Learn the simple coin-and-return task using Q-learning."""

import random
from world import World
import json
from pathlib import Path

ACTIONS = ("left", "right", "collect", "return")
TRAINING_EPISODES = 10_000
MAX_STEPS = 40


def observe(world):
    """The information available to the agent."""
    return (
        world.position,
        world.carrying,
        world.coin_position,
    )


def choose_action(q_table, state, rng, exploration):
    values = q_table.setdefault(state, [0.0] * len(ACTIONS))

    # During training, sometimes try an exploratory action.
    if rng.random() < exploration:
        return rng.randrange(len(ACTIONS))

    # Otherwise choose a learned best action.
    # Resolve equal values randomly, without favoring a direction.
    best_value = max(values)
    best_actions = [
        i for i, value in enumerate(values)
        if value == best_value
    ]
    return rng.choice(best_actions)


def train(seed=42):
    rng = random.Random(seed)
    q_table = {}
    world = World()
    recent_successes = 0

    for episode in range(TRAINING_EPISODES):
        world.reset()
        exploration = max(0.05, 1.0 - episode / 8_000)

        for _ in range(MAX_STEPS):
            state = observe(world)
            action = choose_action(
                q_table, state, rng, exploration
            )
            world.step(ACTIONS[action])

            reward = 20.0 if world.delivered else -1.0
            next_state = observe(world)

            if world.done:
                future_value = 0.0
            else:
                next_values = q_table.setdefault(
                    next_state, [0.0] * len(ACTIONS)
                )
                future_value = max(next_values)

            # Update only the value of the action just tried.
            old_value = q_table[state][action]
            target = reward + 0.95 * future_value
            q_table[state][action] += 0.2 * (
                target - old_value
            )

            if world.done:
                recent_successes += 1
                break

        # The step cap stops this attempt; it is not a
        # terminal state of the underlying task.
        if (episode + 1) % 1_000 == 0:
            print(
                f"Episode {episode + 1:5}: "
                f"{recent_successes}/1000 deliveries "
                f"during training"
            )
            recent_successes = 0

    return q_table


def evaluate(q_table):
    """Test learned choices without further learning."""
    rng = random.Random(12345)
    successes = 0
    delivery_steps = []

    for _ in range(100):
        world = World()

        for step in range(1, MAX_STEPS + 1):
            action = choose_action(
                q_table, observe(world), rng, 0.0
            )
            world.step(ACTIONS[action])

            if world.done:
                successes += 1
                delivery_steps.append(step)
                break

    print(f"\nEvaluation: {successes}/100 deliveries")
    if delivery_steps:
        average = sum(delivery_steps) / len(delivery_steps)
        print(f"Average steps per delivery: {average:.1f}")


def demonstrate(q_table):
    rng = random.Random(99)
    world = World()
    print("\nOne attempt using learned values:")

    for _ in range(MAX_STEPS):
        action = choose_action(
            q_table, observe(world), rng, 0.0
        )
        name = ACTIONS[action]
        print(f"{name:8} -> {world.step(name)}")
        if world.done:
            return

    print("Stopped at the step limit without delivery.")
MEMORY_FILE = Path(__file__).resolve().with_name("learned_values.json")


def save_agent(q_table, path=MEMORY_FILE):
    """Save learned values and the action order they belong to."""
    records = [
        {"state": list(state), "values": values}
        for state, values in q_table.items()
    ]

    data = {
        "format_version": 1,
        "world_version": "coin_return_v1",
        "actions": list(ACTIONS),
        "training_seed": 42,
        "training_episodes": TRAINING_EPISODES,
        "records": records,
    }

    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(data, indent=2, allow_nan=False),
        encoding="utf-8",
    )
    temporary.replace(path)
    print(f"Saved learned values to: {path}")


def load_agent(path=MEMORY_FILE):
    """Load values saved for this version of the task."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))

    if (
        data.get("format_version") != 1
        or data.get("world_version") != "coin_return_v1"
        or data.get("actions") != list(ACTIONS)
    ):
        raise ValueError("Saved agent does not match this task.")

    q_table = {}
    for record in data["records"]:
        state = tuple(record["state"])
        values = record["values"]

        if len(state) != 3 or len(values) != len(ACTIONS):
            raise ValueError("Saved agent contains an invalid record.")

        q_table[state] = [float(value) for value in values]

    return q_table

if __name__ == "__main__":
    print("Training locally...\n")
    learned_values = train(seed=42)
    save_agent(learned_values)

    restored_values = load_agent()
    assert restored_values == learned_values
    print("Save/load check passed.")

    evaluate(restored_values)
    demonstrate(restored_values)