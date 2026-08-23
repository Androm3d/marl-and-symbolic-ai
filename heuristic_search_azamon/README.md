# Heuristic Search & Local Optimization: Azamon Logistics

[![Java](https://img.shields.io/badge/Java-11%2B-orange?style=flat-square&logo=java)](https://www.oracle.com/java/)
[![AIMA](https://img.shields.io/badge/AIMA-Heuristic_Search-blue?style=flat-square)]()

A Java implementation of heuristic search and local optimization algorithms (Hill-Climbing and Simulated Annealing) utilizing the AIMA core framework for package logistics optimization (`Azamon`). Developed for *Artificial Intelligence (IA)* at **UPC -- FIB**.

---

## ⚡ Algorithmic Search Heuristics

1. **State Representation**: Package assignments across distribution centers, transport offer choices, and delivery deadline constraints.
2. **Successor Functions & Operators**: Swap operators, center re-assignments, and transportation mode shifts.
3. **Local Search Solvers**:
   * **Hill-Climbing**: Greedy steepest-descent cost minimization.
   * **Simulated Annealing**: Stochastic exponential temperature cooling schedule $T_{k+1} = \alpha T_k$ avoiding local optima.

---

## 👤 Author
* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d)) – *UPC-FIB*
