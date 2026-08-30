# 🚩 AgentSpeak / BDI Multi-Agent Capture-The-Flag (CTF)

A distributed **Belief-Desire-Intention (BDI)** Multi-Agent Architecture for adversarial **Capture-The-Flag (CTF)** tactical simulations in PyGomas, developed for the *Distributed Intelligent Systems (SID)* curriculum at **UPC-FIB** (*Awarded Highest Honors / Matrícula de Honor*).

[![AgentSpeak](https://img.shields.io/badge/Language-AgentSpeak%20(L)-orange.svg)](http://jason.sourceforge.net/)
[![Python 3.10+](https://img.shields.io/badge/Language-Python%203.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![Highest Honors](https://img.shields.io/badge/Academic-Matr%C3%ADcula%20de%20Honor-gold.svg)](https://www.fib.upc.edu/)

---

## 🏛️ Tactical Multi-Agent BDI Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DISTRIBUTED BDI CTF ARCHITECTURE                      │
├───────────────────┬─────────────────────────────────────────────────────────┤
│ 🎖️ Coordinator   │ Global belief aggregator, dynamic role & target assign  │
│ 🏹 Attacker       │ Flag extraction, defensive interception & escort routes │
│ 🛡️ Defender       │ Perimeter patrolling, base interception & zone defense  │
│ 🔭 Scout          │ Fog-of-war reconnaissance & enemy position broadcasting │
└───────────────────┴─────────────────────────────────────────────────────────┘
```

---

## 🔬 BDI Agent Reasoning Cycle

Each agent executes an asynchronous BDI deliberation cycle:
1. **Belief Revision**: Sensor inputs and incoming KQML/FIPA communication messages update the internal belief base $\mathcal{B}$.
2. **Option Generation (Desires $\mathcal{D}$)**: Triggered plans generate candidate intentions based on environmental context (e.g., enemy spotted, flag dropped, low health).
3. **Deliberation & Filter (Intentions $\mathcal{I}$)**: Active intentions are organized into execution stacks.
4. **Action Execution**: Atomic physical actions (move, shoot, grab flag) dispatched to the simulation engine.

---

## 👥 Authors & Collaborators

* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d))
* **Víctor Ramírez Arimaha** ([@Edexel2vic](https://github.com/Edexel2vic))
* **Adrià Cebrián Ruiz** ([@pacopua](https://github.com/pacopua))

---

## 📂 Subproject Contents

* `agents/`: AgentSpeak (`.asl`) agent decision plans:
  * `coordinator.asl`: Global situational awareness and target allocation.
  * `attacker.asl`: Fast pathfinding to enemy flag and dynamic retreat routes.
  * `defender.asl`: Base defense and intercept trajectories.
  * `scout.asl`: High-speed terrain scanning and hostile tracking.
* `run_simulation.py`: Entrypoint for launching multi-agent battles.
