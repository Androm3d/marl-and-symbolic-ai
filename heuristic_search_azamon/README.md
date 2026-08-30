# 📦 Azamon: Combinatorial Logistics Optimization & Local Search (Java / AIMA)

A high-performance combinatorial local search optimization framework built in **Java (AIMA Framework)** to solve large-scale **Package-to-Transport Allocation and Routing** problems under non-linear capacity constraints, shipping deadlines, and vehicle tariffs. Developed for the *Artificial Intelligence (IA)* curriculum at **UPC-FIB**.

[![Java 17+](https://img.shields.io/badge/Language-Java%2017%2B-red.svg)](https://www.oracle.com/java/)
[![AIMA](https://img.shields.io/badge/Framework-AIMA%20Java-blue.svg)](https://github.com/aimacode/aima-java)
[![Optimization](https://img.shields.io/badge/Domain-Local%20Search-green.svg)](https://en.wikipedia.org/wiki/Simulated_annealing)

---

## 🏛️ System Architecture & AIMA Design Pattern

The codebase adheres strictly to the **AIMA (Artificial Intelligence: A Modern Approach)** search interface:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            AZAMON LOCAL SEARCH CORE                         │
├───────────────────┬─────────────────────────────────────────────────────────┤
│ 📦 AzaState       │ Package-to-carrier assignment & weight vector state     │
│ 🎯 HeuristicFn 1  │ Total transportation cost minimization                  │
│ 🌟 HeuristicFn 2  │ Multi-objective cost + client unhappiness penalty       │
│ 🔄 Successors     │ Move, Swap, and Combined Move-Swap state generation     │
│ ⚡ Algorithms     │ Hill-Climbing (Steepest Ascent) & Simulated Annealing   │
└───────────────────┴─────────────────────────────────────────────────────────┘
```

---

## 🔬 Operators & Heuristic Formulations

### 1. Neighborhood Operators:
* **Move Operator (`AzaMoveSuccessorHC` / `SA`)**: Reallocates a single package from transport $T_i$ to transport $T_j$.
* **Swap Operator (`AzaSwapSuccessorHC` / `SA`)**: Interchanges assignments of two packages across different carriers.
* **Combined Operator (`AzaMoveSwapSuccessorHC` / `SA`)**: Evaluates unified move and swap transitions to avoid premature local extrema.

### 2. Heuristic Functions:
* **$h_1$ (Economic Cost Minimization)**:
  $$h_1(s) = \sum_{t \in T} \text{VehicleFee}(t) + \sum_{p \in \text{Pkg}(t)} \text{Weight}(p) \cdot \text{Rate}(t)$$
* **$h_2$ (Cost + Service Level Penalties)**:
  $$h_2(s) = h_1(s) + \lambda \sum_{p \in P} \max\left(0, \text{DeliveryDate}(p) - \text{Deadline}(p)\right)^2$$

---

## ⚙️ Compilation & Execution

```bash
# Compile with AIMA and Azamon dependencies
javac -cp "lib/AIMA.jar:lib/Azamon.jar:src" src/main.java src/IA/Azamon/*.java -d bin

# Execute benchmark search experiments
java -cp "lib/AIMA.jar:lib/Azamon.jar:bin" main
```

---

## 👥 Authors & Collaborators

* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d))
* **Víctor Ramírez Arimaha** ([@Edexel2vic](https://github.com/Edexel2vic))
* **Adrià Cebrián Ruiz** ([@pacopua](https://github.com/pacopua))

---

## 📂 Repository Contents

```
heuristic_search_azamon/
├── src/                          # Complete Java source code
│   ├── main.java                 # Benchmark driver & experiment runner
│   └── IA/Azamon/                # AzaState, Heuristics, and Successor generators
├── lib/                          # AIMA.jar & Azamon.jar problem dependencies
└── Local_Search.pdf              # Comprehensive academic research report & plots
```
