# Gridworld Reinforcement Learning: Q-Learning & Policy Search

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Reinforcement Learning](https://img.shields.io/badge/RL-Q--Learning-brightgreen?style=flat-square)]()

A comparative suite of classic and policy-gradient **Reinforcement Learning** algorithms implemented on Gridworld / Cliff Walking environments.

---

## 📊 Performance & Policy Heatmaps

![Cliff Walking Policy Heatmap](figures/q_learning_policy_heatmap.png)
*Figure 1: CliffWalking Gridworld State Value Heatmap $V(s)$ and optimal path learned via Q-Learning, avoiding the high-penalty cliff region ($R = -100$).*

![RL Reward Convergence Comparison](figures/rl_algorithm_convergence.png)
*Figure 2: Sum of rewards per episode across Q-Learning (Off-Policy TD), SARSA (On-Policy TD), and REINFORCE (Monte Carlo Policy Gradient).*

---

## 📌 Implemented RL Algorithms

1. **Q-Learning (`Q-learning/`)**:
   * Off-policy Temporal Difference control algorithm with $\epsilon$-greedy exploration:
     $$Q(s, a) \leftarrow Q(s, a) + \alpha \Big[ R + \gamma \max_{a'} Q(s', a') - Q(s, a) \Big]$$
2. **Value Iteration & Policy Iteration (`Value_Iteration/`)**:
   * Dynamic programming Bellman optimality equation solvers:
     $$V_{k+1}(s) = \max_{a} \sum_{s', r} p(s', r | s, a) \Big[ r + \gamma V_k(s') \Big]$$
3. **Model-Based Reinforcement Learning (`ModelBased/`)**:
   * Learned transition model $P(s' | s, a)$ and reward model $R(s, a)$ with simulated planning updates.
4. **REINFORCE Policy Gradient (`Reinforce/`)**:
   * Monte Carlo policy gradient optimization on parameterized stochastic policies $\pi_\theta(a|s)$.

---

## 📁 Repository Directory Structure

```
rl_cliffwalking_qlearning/
├── Q-learning/                                # Tabular Q-Learning solver & visualizer
├── Value_Iteration/                           # DP Bellman optimality solver
├── ModelBased/                                # Learned transition & reward model RL
├── Reinforce/                                 # REINFORCE Monte Carlo policy gradient
└── figures/                                   # Embedded convergence & policy figures
```

---

## 👤 Author
* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d)) – *UPC-FIB*
