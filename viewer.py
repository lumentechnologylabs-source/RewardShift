"""Watch untrained and trained RewardShift agents."""

import random
import tkinter as tk
from tkinter import ttk

from world import World
from agent import load_agent, observe, choose_action, ACTIONS, MAX_STEPS

BG = "#101c24"
PANEL = "#192b36"
MINT = "#76dfc5"
GOLD = "#ffd16b"
WHITE = "#e7eef2"


class Viewer:
    def __init__(self, root, learned):
        self.root = root
        self.learned = learned
        self.timer = None
        self.running = False

        root.title("RewardShift — Watch them learn")
        root.configure(bg=BG)
        root.geometry("980x430")

        tk.Label(
            root, text="RewardShift",
            font=("Segoe UI", 24, "bold"),
            fg=MINT, bg=BG
        ).pack(pady=(16, 0))

        tk.Label(
            root,
            text="Same task. Different experience. No learning during playback.",
            font=("Segoe UI", 11), fg=WHITE, bg=BG
        ).pack(pady=(0, 12))

        self.canvas = tk.Canvas(
            root, width=940, height=235,
            bg=BG, highlightthickness=0
        )
        self.canvas.pack()

        buttons = tk.Frame(root, bg=BG)
        buttons.pack(pady=8)

        for label, command in [
            ("Play", self.play),
            ("Pause", self.pause),
            ("One step", self.single_step),
            ("Replay", self.reset),
        ]:
            ttk.Button(
                buttons, text=label, command=command
            ).pack(side="left", padx=5)

        tk.Label(
            root,
            text="Mint face = agent   |   Gold circle = coin   |   Blue square = base",
            font=("Segoe UI", 10), fg=WHITE, bg=BG
        ).pack(pady=5)

        self.reset()

    def pause(self):
        self.running = False
        if self.timer is not None:
            self.root.after_cancel(self.timer)
            self.timer = None

    def reset(self):
        self.pause()
        self.lanes = []
        for title, table in [
            ("Untrained — random choices", {}),
            ("Trained — learned action values", self.learned),
        ]:
            self.lanes.append({
                "title": title,
                "world": World(),
                "table": table,
                "rng": random.Random(12345),
                "steps": 0,
                "message": "Ready at base.",
            })
        self.draw()

    def advance(self):
        for lane in self.lanes:
            world = lane["world"]
            if world.done or lane["steps"] >= MAX_STEPS:
                continue

            action = choose_action(
                lane["table"], observe(world),
                lane["rng"], 0.0
            )
            name = ACTIONS[action]
            message = world.step(name)
            lane["steps"] += 1
            lane["message"] = f"{name}: {message}"

            if lane["steps"] == MAX_STEPS and not world.done:
                lane["message"] = "Step limit reached. No delivery."

        self.draw()

    def single_step(self):
        self.pause()
        self.advance()

    def play(self):
        if not self.running:
            self.running = True
            self.tick()

    def tick(self):
        self.timer = None
        if not self.running:
            return
        self.advance()

        active = any(
            not lane["world"].done
            and lane["steps"] < MAX_STEPS
            for lane in self.lanes
        )
        if active:
            self.timer = self.root.after(550, self.tick)
        else:
            self.running = False

    def draw(self):
        c = self.canvas
        c.delete("all")

        for index, lane in enumerate(self.lanes):
            x = 15 + index * 470
            world = lane["world"]

            c.create_rectangle(
                x, 0, x + 455, 230,
                fill=PANEL, outline="#34505e"
            )
            c.create_text(
                x + 18, 24, anchor="w",
                text=lane["title"], fill=WHITE,
                font=("Segoe UI", 13, "bold")
            )

            for square in range(4):
                left = x + 38 + square * 96
                c.create_rectangle(
                    left, 60, left + 82, 142,
                    fill="#11212b", outline="#45616e"
                )
                c.create_text(
                    left + 41, 154, text=str(square),
                    fill="#a3b8c4"
                )

                if square == world.base:
                    c.create_rectangle(
                        left + 8, 68, left + 74, 134,
                        outline="#75acff", width=3
                    )

                if square == world.coin_position:
                    c.create_oval(
                        left + 26, 85, left + 56, 115,
                        fill=GOLD, outline=""
                    )

                if square == world.position:
                    c.create_oval(
                        left + 21, 80, left + 61, 120,
                        fill=MINT, outline=""
                    )
                    for eye in (33, 49):
                        c.create_oval(
                            left + eye, 91,
                            left + eye + 4, 96,
                            fill=BG, outline=""
                        )
                    if world.carrying:
                        c.create_oval(
                            left + 54, 107, left + 70, 123,
                            fill=GOLD, outline=""
                        )

            status = "DELIVERED!" if world.done else (
                "Carrying coin" if world.carrying else "Not carrying"
            )
            c.create_text(
                x + 18, 180, anchor="w",
                text=f"Actions: {lane['steps']}/40   |   {status}",
                fill=MINT if world.done else WHITE,
                font=("Segoe UI", 11)
            )
            c.create_text(
                x + 18, 208, anchor="w",
                text=lane["message"], width=420,
                fill=WHITE, font=("Segoe UI", 10)
            )


if __name__ == "__main__":
    print("Loading saved agent...")
    learned = load_agent()
    print("Loaded. No retraining needed.")

    root = tk.Tk()
    app = Viewer(root, learned)
    root.mainloop()