# Multi-Agent Reinforcement Learning & Symbolic AI Architecture

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=flat-square&logo=pytorch)](https://pytorch.org/)
[![AgentSpeak / Jason](https://img.shields.io/badge/AgentSpeak-Jason-orange?style=flat-square)]()
[![Honors](https://img.shields.io/badge/Honors-Matr%C3%ADcula%20de%20Honor-gold?style=flat-square)]()

A comprehensive suite exploring autonomous agent coordination, combining **Multi-Agent Reinforcement Learning (MARL)** under partial observability and **AgentSpeak / BDI (Belief-Desire-Intention) Symbolic Agent Architectures**.

---

## 📌 Repository Exploration Guide

This repository is organized into three standalone, fully documented computational subprojects:

| Subproject Directory | Focus & Algorithmic Domain | Key Technologies | Detailed Subproject Guide |
| :--- | :--- | :--- | :---: |
| 🤖 **[`POEGMA-SID/`](./POEGMA-SID/)** | Multi-Agent RL on POEGMA (JAL-GT with Nash, Pareto, Minimax & Welfare equilibria) | PyTorch, MARL, Game Theory | [📖 View POEGMA MARL Guide](./POEGMA-SID/README.md) |
| 🎯 **[`agentspeak_symbolic_ctf/`](./agentspeak_symbolic_ctf/)** | Symbolic AgentSpeak BDI Capture-The-Flag team architecture (*Matrícula de Honor*) | AgentSpeak, Jason, Pygomas | [📖 View Symbolic BDI Guide](./agentspeak_symbolic_ctf/README.md) |
| 🎲 **[`rl_cliffwalking_qlearning/`](./rl_cliffwalking_qlearning/)** | Gridworld RL algorithm benchmarks (Q-Learning, REINFORCE, DP & Model-Based) | Python, Gym, Q-Learning | [📖 View RL Benchmarks Guide](./rl_cliffwalking_qlearning/README.md) |

---

## 🖼️ Experimental Visualizations & Visual Proof

### 1. Optuna Hyperparameter Importance for MARL POEGMA Policy Convergence
![Optuna Parameter Importances](POEGMA-SID/figures/optuna_param_importance-1.png)
*Demonstrates feature importance scores for learning rate $\alpha$, discount factor $\gamma$, and exploration schedules in multi-agent joint action learning.*

### 2. Cliff Walking Gridworld State Value Heatmap & Optimal Path
![Cliff Walking Policy Heatmap](rl_cliffwalking_qlearning/figures/q_learning_policy_heatmap.png)
*Cliff Walking Gridworld State Value Heatmap $V(s)$ and optimal path learned via Q-Learning, avoiding the high-penalty cliff region ($R = -100$).*

---

## 📐 Algorithmic Overview & Mathematical Foundations

### 1. Multi-Agent RL & Solution Concepts (`POEGMA-SID/`)
In partially observable multi-agent environments, agents learn joint policies $a = (a_1, \dots, a_N) \in A$. Joint Action Learning updates $Q$-values over joint action space with specialized equilibrium selection:
- **Nash Equilibrium**: $R_i(a_i^*, a_{-i}^*) \ge R_i(a_i, a_{-i}^*)$
- **Pareto Efficiency**: No agent can be made better off without making another worse off.
- **Minimax**: Maximizes worst-case payoff under adversarial uncertainty: $\max_{a_i} \min_{a_{-i}} R_i(a_i, a_{-i})$.

### 2. Symbolic BDI Agent Architecture (`agentspeak_symbolic_ctf/`)
Implements dynamic belief updating, desire generation, and intention execution in **AgentSpeak (Jason)**. Agents dynamically assign roles (Flag Runner, Escort, Defender) and pass message primitives (`.send`) to maintain shared situational awareness.

---

## 🛠️ Quickstart Guide

### 1. Run MARL POEGMA Training
```bash
cd POEGMA-SID
pip install -r requirements.txt
python main.py
```

### 2. Explore Gridworld RL Benchmarks
```bash
cd rl_cliffwalking_qlearning
python3 generate_rl_plots.py
```

---

## 👤 Author
* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d)) – *Specialization in CS & AI, UPC-FIB*
