# 🤖 Multi-Agent Pathfinding & Game-Theoretic Joint Action Learning (POEGMA)

A multi-agent reinforcement learning and game theory framework evaluating **Joint Action Learning (JAL-GT)** across game-theoretic solution concepts (**Nash Equilibrium, Pareto Optimality, Minimax Safety, and Social Welfare Maximization**) in partially observable grid environments. Developed for the *Distributed Intelligent Systems (SID)* curriculum at **UPC-FIB** (*Awarded Highest Honors / Matrícula de Honor*).

[![Python 3.10+](https://img.shields.io/badge/Language-Python%203.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-red.svg?logo=pytorch)](https://pytorch.org/)
[![Optuna](https://img.shields.io/badge/HPO-Optuna-blueviolet.svg)](https://optuna.org/)
[![Highest Honors](https://img.shields.io/badge/Academic-Matr%C3%ADcula%20de%20Honor-gold.svg)](https://www.fib.upc.edu/)

---

## 📊 Bayesian Hyperparameter Optimization & Empirical Sweeps

<p align="center">
  <img src="figures/optuna_parallel_coordinates-1.png" width="48%" alt="Optuna Parallel Coordinates" />
  <img src="figures/nash_optuna_history-1.png" width="48%" alt="Nash Equilibrium Optimization History" />
</p>

<p align="center">
  <img src="figures/optuna_param_importance-1.png" width="48%" alt="Optuna Parameter Importance" />
  <img src="src/plots/jalgt/paretosolutionconcept/jalgt_paretosolutionconcept_reward_distribution.png" width="48%" alt="Pareto Reward Distribution" />
</p>

---

## 🔬 Game-Theoretic Solution Concepts

The system implements four distinct game-theoretic equilibrium solution concepts:
1. **Nash Equilibrium**: Mutual best-response profile where no agent has an incentive to unilaterally deviate:
   $$\forall i, \quad u_i(a_i^*, \mathbf{a}_{-i}^*) \ge u_i(a_i, \mathbf{a}_{-i}^*)$$
2. **Pareto Optimality**: Joint action profile where no agent can increase utility without decreasing another agent's utility:
   $$\nexists \mathbf{a} \text{ s.t. } \forall i, u_i(\mathbf{a}) \ge u_i(\mathbf{a}^*) \wedge \exists j, u_j(\mathbf{a}) > u_j(\mathbf{a}^*)$$
3. **Minimax Safety**: Conservative risk-averse policy maximizing security values under adversarial assumptions:
   $$a_i^* = \arg\max_{a_i} \min_{\mathbf{a}_{-i}} u_i(a_i, \mathbf{a}_{-i})$$
4. **Social Welfare Maximization**: Cooperative optimization maximizing aggregate collective payoff:
   $$\mathbf{a}^* = \arg\max_{\mathbf{a}} \sum_{i=1}^N u_i(\mathbf{a})$$

---

## 👥 Authors & Collaborators

* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d))
* **Edgar** ([@Edexel2vic](https://github.com/Edexel2vic))
* **Pau** ([@pacopua](https://github.com/pacopua))

---

## 📂 Subproject Contents

* `src/`: Joint action learning core and solution concepts (`solution_concepts.py`, `trial.py`, `utils.py`).
* `figures/`: Empirical Optuna HPO sweeps, parameter importances, and convergence histories.
* `pogema_marl_hpo_v_simple.db`: Full SQLite database storing Bayesian HPO trials.
* `baseline.ipynb`: End-to-end evaluation notebook.
