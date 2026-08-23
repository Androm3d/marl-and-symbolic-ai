# Multi-Agent Reinforcement Learning & Symbolic AI Architecture

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=flat-square&logo=pytorch)](https://pytorch.org/)
[![AgentSpeak / Jason](https://img.shields.io/badge/AgentSpeak-Jason-orange?style=flat-square)]()
[![Honors](https://img.shields.io/badge/Honors-Matr%C3%ADcula%20de%20Honor-gold?style=flat-square)]()

A comprehensive suite exploring autonomous agent coordination, combining **Multi-Agent Reinforcement Learning (MARL)** under partial observability, **AgentSpeak / BDI Symbolic Agent Architectures**, and **PDDL Automated Planning**.

---

## 📌 Repository Exploration Guide

This repository is organized into five standalone, fully documented computational subprojects:

| Subproject Directory | Focus & Algorithmic Domain | Key Technologies | Detailed Subproject Guide |
| :--- | :--- | :--- | :---: |
| 🤖 **[`POEGMA-SID/`](./POEGMA-SID/)** | Multi-Agent RL on POEGMA (JAL-GT with Nash, Pareto, Minimax & Welfare equilibria) | PyTorch, MARL, Game Theory | [📖 View POEGMA MARL Guide](./POEGMA-SID/README.md) |
| 🎯 **[`agentspeak_symbolic_ctf/`](./agentspeak_symbolic_ctf/)** | Symbolic AgentSpeak BDI Capture-The-Flag team architecture (*Matrícula de Honor*) | AgentSpeak, Jason, Pygomas | [📖 View Symbolic BDI Guide](./agentspeak_symbolic_ctf/README.md) |
| 🎲 **[`rl_cliffwalking_qlearning/`](./rl_cliffwalking_qlearning/)** | Gridworld RL algorithm benchmarks (Q-Learning, REINFORCE, DP & Model-Based) | Python, Gym, Q-Learning | [📖 View RL Benchmarks Guide](./rl_cliffwalking_qlearning/README.md) |
| 🚀 **[`pddl_automated_planning/`](./pddl_automated_planning/)** | Automated planning domain & problem specifications | PDDL, Metric-FF Solver | [📖 View PDDL Guide](./pddl_automated_planning/README.md) |
| 📦 **[`heuristic_search_azamon/`](./heuristic_search_azamon/)** | Local search heuristics & Simulated Annealing package logistics | Java, AIMA, Hill-Climbing | [📖 View Azamon Guide](./heuristic_search_azamon/README.md) |

---

## 🖼️ Experimental Visualizations & Visual Proof

### 1. Optuna Hyperparameter Importance for MARL POEGMA Policy Convergence
![Optuna Parameter Importances](POEGMA-SID/figures/optuna_param_importance-1.png)
*Demonstrates feature importance scores for learning rate $\alpha$, discount factor $\gamma$, and exploration schedules in multi-agent joint action learning.*

### 2. Cliff Walking Gridworld State Value Heatmap & Optimal Path
![Cliff Walking Policy Heatmap](rl_cliffwalking_qlearning/figures/q_learning_policy_heatmap.png)
*Cliff Walking Gridworld State Value Heatmap $V(s)$ and optimal path learned via Q-Learning, avoiding the high-penalty cliff region ($R = -100$).*

---

## 👥 Contributors & Credits
* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d))
* **Víctor Ramírez Arimaha** ([@Edexel2vic](https://github.com/Edexel2vic))
* **Adrià Cebrián Ruiz** ([@pacopua](https://github.com/pacopua))
