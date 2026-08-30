# 🤖 Multi-Agent Reinforcement Learning & Symbolic AI Suite

A comprehensive repository showcasing research and implementations in **Multi-Agent Reinforcement Learning (MARL), Game-Theoretic Equilibria, Belief-Desire-Intention (BDI) Systems, and Automated Planning**, developed across courses at **UPC-FIB** (*Distributed Intelligent Systems - SID [Matrícula de Honor]* and *Artificial Intelligence - IA*).

[![Python 3.10+](https://img.shields.io/badge/Language-Python%203.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-red.svg?logo=pytorch)](https://pytorch.org/)
[![Highest Honors](https://img.shields.io/badge/Academic-Matr%C3%ADcula%20de%20Honor-gold.svg)](https://www.fib.upc.edu/)

---

## 🏛️ Repository Architecture

```
marl-and-symbolic-ai/
├── POEGMA-SID/                   # Multi-Agent Pathfinding (MAPF) & Game-Theoretic JAL [MH]
│   ├── src/                      # Joint Action Learning (Nash, Pareto, Minimax, Welfare)
│   ├── figures/                  # Optuna hyperparameter optimization contours & Pareto fronts
│   └── pogema_marl_hpo_v_simple.db # SQLite database of Bayesian HPO trials
├── agentspeak_symbolic_ctf/      # BDI Capture-the-Flag tactical multi-agent architecture
│   ├── agents/                   # AgentSpeak (.asl) plans (Coordinator, Attacker, Defender, Scout)
│   └── run_simulation.py         # Multi-agent battle runner in PyGomas
├── rl_cliffwalking_qlearning/    # Temporal Difference RL benchmark (Q-Learning vs. SARSA)
│   ├── figures/                  # Continuous State-Value potential heatmaps & learning curves
│   └── q_learning.py             # TD(0) Off-policy Q-Learning and SARSA implementations
├── pddl_automated_planning/      # PDDL 2.1 automated planning for planetary rover exploration
│   └── rovers_domain.pddl        # STRIPS action schemas, fluents & problem definitions
└── heuristic_search_azamon/      # Combinatorial package routing via Simulated Annealing
    └── azamon_search.py          # Local search engine with Boltzmann cooling schedules
```

---

## 📊 Visual Highlights & Analytics

### 1. Multi-Agent Game-Theoretic Hyperparameter Sweeps (`POEGMA-SID`)
<p align="center">
  <img src="POEGMA-SID/figures/optuna_parallel_coordinates-1.png" width="48%" alt="Optuna Parallel Coordinates" />
  <img src="POEGMA-SID/figures/nash_optuna_history-1.png" width="48%" alt="Nash Equilibrium Convergence History" />
</p>

### 2. Reinforcement Learning: State-Value Heatmap & Convergence (`rl_cliffwalking`)
<p align="center">
  <img src="rl_cliffwalking_qlearning/figures/q_learning_policy_heatmap.png" width="48%" alt="Q-Learning State-Value Function Heatmap" />
  <img src="rl_cliffwalking_qlearning/figures/rl_algorithm_convergence.png" width="48%" alt="Episodic Reward Convergence" />
</p>

---

## 🔬 Core Methodological Pillars

### 1. Game-Theoretic Multi-Agent Pathfinding (`POEGMA-SID`) — *Matrícula de Honor*
* **Joint Action Learners (JAL)**: Solves multi-agent coordination under partial observability across 4 game-theoretic solution concepts: **Nash Equilibrium, Pareto Optimality, Minimax Safety, and Social Welfare Maximization**.
* **Bayesian Hyperparameter Optimization (Optuna)**: Explores high-dimensional learning rates ($\alpha$), discount factors ($\gamma$), and exploration schedules ($\epsilon_{\text{max}} \to \epsilon_{\text{min}}$) to isolate optimal coordination regimes.

### 2. BDI Multi-Agent Coordination (`agentspeak_symbolic_ctf`)
* Modeled in **AgentSpeak(L)** for real-time tactical Capture-The-Flag simulations.
* Features specialized role allocation (Coordinator, Attacker, Defender, Scout) communicating via asynchronous message brokers.
* **Collaborators**: Edgar ([@Edexel2vic](https://github.com/Edexel2vic)) and Pau ([@pacopua](https://github.com/pacopua)).

### 3. Temporal Difference Learning (`rl_cliffwalking_qlearning`)
* Rigorously benchmarks Off-Policy Q-Learning against On-Policy SARSA on the CliffWalking gridworld.
* Highlights the empirical tension between optimal risky trajectories vs. safe risk-averse exploration.

### 4. Symbolic Planning & Heuristic Search (`pddl` & `azamon`)
* **PDDL 2.1**: Autonomous planetary rover exploration with STRIPS preconditions and effect schemas.
* **Azamon Local Search**: Non-linear package-to-transport combinatorial optimization solved via Simulated Annealing.

---

## 👥 Authors & Credits

* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d))
* **Edgar** ([@Edexel2vic](https://github.com/Edexel2vic)) — *CTF AgentSpeak Co-Author*
* **Pau** ([@pacopua](https://github.com/pacopua)) — *CTF AgentSpeak Co-Author*
