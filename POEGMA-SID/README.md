# Multi-Agent RL on POEGMA: Joint Action Learning (JAL-GT)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=flat-square&logo=pytorch)](https://pytorch.org/)
[![MARL](https://img.shields.io/badge/MARL-POEGMA-brightgreen?style=flat-square)]()

A multi-agent reinforcement learning benchmark evaluating **Joint Action Learning (JAL-GT)** and **Independent Q-Learning (IQL)** in Partially Observable Environment Games for Multi-Agents (**POEGMA**).

---

## 📊 Experimental Results & Hyperparameter Optimization

![Optuna Parameter Importances](figures/optuna_param_importance-1.png)
*Figure 1: Optuna Hyperparameter Importance Scores for MARL JAL-GT Policy Convergence. Demonstrates the impact of learning rate $\alpha$, discount factor $\gamma$, and exploration schedules.*

![Optuna Parallel Coordinates](figures/optuna_parallel_coordinates-1.png)
*Figure 2: Parallel Coordinates Sweep across hyperparameter trials, tracking cumulative joint agent reward trajectories.*

![Nash Equilibrium Convergence History](figures/nash_optuna_history-1.png)
*Figure 3: Optimization history of Nash Equilibrium solution concept convergence over 1,000 training episodes.*

---

## 📌 Game-Theoretic Solution Concepts Evaluated

The framework computes dynamic joint-action equilibria across four distinct solution concepts:

| Solution Concept | Mathematical Criterion | Key Optimization Goal |
| :--- | :--- | :--- |
| ⚖️ **Nash Equilibrium** | $R_i(a_i^*, a_{-i}^*) \ge R_i(a_i, a_{-i}^*), \quad \forall a_i \in A_i$ | No agent has unilateral incentive to deviate |
| 📈 **Pareto Efficiency** | $\nexists a \in A \text{ s.t. } R_i(a) \ge R_i(a^*) \, \forall i \land R_j(a) > R_j(a^*) \, \exists j$ | Maximizes collective efficiency without harming any agent |
| 🛡️ **Minimax / MaxiMin** | $\max_{a_i} \min_{a_{-i}} R_i(a_i, a_{-i})$ | Worst-case payoff maximization under adversarial uncertainty |
| 🤝 **Social Welfare** | $\arg\max_{a \in A} \sum_{i=1}^N R_i(a)$ | Maximizes total cumulative joint payoff across all agents |

---

## 📁 Project Structure

```
POEGMA-SID/
├── main.py                                    # Execution & CLI driver script
├── baseline.ipynb                             # Baseline performance evaluation notebook
├── requirements.txt                           # PyTorch and Gym dependencies
├── figures/                                   # Embedded benchmark PNG figures
└── src/
    └── plots/                                 # Raw Optuna evaluation output PDFs
```

---

## 🛠️ Setup & Execution

### 1. Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Running Training & Evaluation
```bash
python main.py
```

---

## 👤 Author
* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d)) – *UPC-FIB*
