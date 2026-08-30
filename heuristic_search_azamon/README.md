# 📦 Azamon: Combinatorial Logistics Optimization & Local Search

A high-performance local search optimization framework solving large-scale **Package-to-Transport Routing and Allocation** problems under non-linear capacity constraints and deadline penalties. Developed for the *Artificial Intelligence (IA)* curriculum at **UPC-FIB**.

[![Python 3.10+](https://img.shields.io/badge/Language-Python%203.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![Optimization](https://img.shields.io/badge/Domain-Heuristic%20Search-green.svg)](https://en.wikipedia.org/wiki/Simulated_annealing)

---

## 🏛️ Problem Formulation & Mathematical Model

The problem models an e-commerce logistics network allocating $N$ packages across $M$ transport vehicles with heterogeneous capacities $C_t$:
$$\min_{\mathbf{x}} \sum_{t=1}^M \left[ \text{BaseCost}(t) + \sum_{p \in \text{Pkg}(t)} w_p \cdot c_p + \lambda \cdot \max\left(0, \sum_{p \in \text{Pkg}(t)} w_p - C_t\right) \right]$$

### Local Search Operators:
1. **Move Operator**: Reassign package $p_i$ from transport $T_a$ to transport $T_b$.
2. **Swap Operator**: Exchange assignments of package $p_i \in T_a$ and $p_j \in T_b$.
3. **Transport Consolidator**: Shift all packages from under-utilized carrier $T_k$ and decommission vehicle.

---

## 🔬 Search Algorithms Implemented

* **Steepest-Descent Hill Climbing**: Greedily explores the complete 1-neighborhood $\mathcal{N}(s)$ and accepts strictly improving transitions ($\Delta E < 0$).
* **Simulated Annealing (SA)**: Escapes local minima via Boltzmann probabilistic acceptance of uphill moves:
  $$P(\text{accept}) = \exp\left(-\frac{\Delta E}{T_k}\right), \quad T_{k+1} = \alpha \cdot T_k \quad (\alpha = 0.995)$$

---

## 📂 Files

* `azamon_search.py`: Complete heuristic search solver with Hill Climbing and Simulated Annealing.
* `data/`: Problem instances and benchmark test suites.
