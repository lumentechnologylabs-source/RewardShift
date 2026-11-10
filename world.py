"""RewardShift: first environment check."""


class World:
    def __init__(self):
        self.reset()

    def reset(self):
        self.position = 0
        self.base = 0
        self.coin_position = 2
        self.carrying = False
        self.delivered = False
        self.done = False

    def step(self, action):
        if self.done:
            raise RuntimeError("This episode has ended. Call reset().")

        if action == "right":
            self.position = min(3, self.position + 1)
            message = f"Moved to square {self.position}."

        elif action == "left":
            self.position = max(0, self.position - 1)
            message = f"Moved to square {self.position}."

        elif action == "collect":
            if self.position == self.coin_position:
                self.carrying = True
                self.coin_position = None
                message = "Collected the coin."
            else:
                message = "No coin here."

        elif action == "return":
            if self.position == self.base and self.carrying:
                self.carrying = False
                self.delivered = True
                self.done = True
                message = "Delivered the coin. Task complete!"
            else:
                message = "Delivery requires a coin and being at base."

        else:
            raise ValueError(f"Unknown action: {action}")

        return message


if __name__ == "__main__":
    world = World()
    print("Environment check: scripted actions, no learning yet.\n")

    actions = ["right", "right", "collect", "left", "left", "return"]

    for action in actions:
        print(f"{action:8} -> {world.step(action)}")

    assert world.delivered
    print("\nEnvironment check passed.")
