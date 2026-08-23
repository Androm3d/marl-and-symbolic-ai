# AgentSpeak / BDI Symbolic Capture-The-Flag Team Architecture

[![AgentSpeak](https://img.shields.io/badge/AgentSpeak-Jason-orange?style=flat-square)]()
[![BDI Architecture](https://img.shields.io/badge/BDI-Belief--Desire--Intention-blue?style=flat-square)]()
[![Honors](https://img.shields.io/badge/Honors-Matr%C3%ADcula%20de%20Honor-gold?style=flat-square)]()

**Recipient of Matrícula de Honor (Highest Honors) in Distributed Intelligent Systems (SID) @ UPC-FIB.**

A multi-agent team coordination system implemented in **AgentSpeak (Jason)** using the **Belief-Desire-Intention (BDI)** paradigm in a simulated Capture-The-Flag (`Pygomas`) environment.

---

## 📌 Architecture & BDI Paradigm

```
                   ┌──────────────────────────────────────────────┐
                   │             ENVIRONMENT PERCEPTS             │
                   └──────────────────────┬───────────────────────┘
                                          │
                                          ▼
                               ┌─────────────────────┐
                               │    BELIEF BASE      │
                               └──────────┬──────────┘
                                          │ Trigger Events (+!flag_captured)
                                          ▼
                               ┌─────────────────────┐
                               │   DESIRE / GOALS    │
                               └──────────┬──────────┘
                                          │ Context Checks [holding_flag]
                                          ▼
                               ┌─────────────────────┐
                               │   INTENTION / PLANS │
                               └──────────┬──────────┘
                                          │
                                          ▼
                   ┌──────────────────────────────────────────────┐
                   │          ACTIONS & TEAM COMMUNICATION        │
                   └──────────────────────────────────────────────┘
```

---

## 🎯 Key Capabilities & Agent Roles

1. **Dynamic Role Allocation**: Agents autonomously partition into **Offensive Flag Runners**, **Escorts**, and **Base Defenders** based on live spatial distance and health metrics.
2. **Inter-Agent Communication Protocol**: Uses agent-to-agent message passing (`.send`) to alert teammates when the flag is spotted, under attack, or being returned to base.
3. **Symbolic Reactive & Proactive Planning**: AgentSpeak plan triggers respond instantly to enemy encounters while pursuing long-term strategic capture goals.

---

## 📁 Project Directory Structure

```
agentspeak_symbolic_ctf/
├── pygomas/                                   # Pygomas BDI execution platform & maps
└── SID_P1/                                    # AgentSpeak BDI code & plans
    ├── defender.asl                           # Base defender BDI agent rules
    ├── attacker.asl                           # Flag runner BDI agent rules
    └── team_manager.asl                       # Strategic role coordinator
```

---

## 👤 Author
* **Marcel Alabart Benoit** ([@Androm3d](https://github.com/Androm3d)) – *UPC-FIB*
