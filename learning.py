
"""Reusable tabular Q-learning functions for RewardShift."""


def choose_action(q_table, state, rng, exploration, actions):
    """Choose an action index using epsilon-greedy selection."""
    values = q_table.setdefault(state, [0.0] * len(actions))

    if rng.random() < exploration:
        return rng.randrange(len(actions))

    best_value = max(values)
    best_actions = [
        i for i, value in enumerate(values)
        if value == best_value
    ]
    return rng.choice(best_actions)


def update_q_value(
    q_table, state, action, reward,
    next_state, done, actions,
    learning_rate=0.2, discount=0.95
):
    """Update the value of one state-action pair."""
    if done:
        future_value = 0.0
    else:
        next_values = q_table.setdefault(
            next_state, [0.0] * len(actions)
        )
        future_value = max(next_values)

    old_value = q_table[state][action]
    target = reward + discount * future_value

    q_table[state][action] += learning_rate * (
        target - old_value
    )
