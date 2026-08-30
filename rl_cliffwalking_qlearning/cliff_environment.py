"""
CliffWalking Environment Implementation
"""
import numpy as np

class CliffWalkingEnv:
    def __init__(self, rows=4, cols=12):
        self.rows = rows
        self.cols = cols
        self.start = (3, 0)
        self.goal = (3, 11)
        self.cliff = [(3, i) for i in range(1, 11)]
        self.actions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # Left, Right, Up, Down
        self.reset()

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, action):
        if self.state == self.goal:
            return self.state, 0, True
        r, c = self.state
        dr, dc = self.actions[action]
        nr, nc = max(0, min(self.rows - 1, r + dr)), max(0, min(self.cols - 1, c + dc))
        next_state = (nr, nc)
        if next_state in self.cliff:
            self.state = self.start
            return self.start, -100, False
        elif next_state == self.goal:
            self.state = self.goal
            return self.goal, -1, True
        else:
            self.state = next_state
            return next_state, -1, False
