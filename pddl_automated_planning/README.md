# 🚀 PDDL Automated Planning: Planetary Rover Exploration

A formal **Planning Domain Definition Language (PDDL 2.1)** implementation of autonomous planetary exploration missions, developed for the *Artificial Intelligence (IA)* curriculum at **UPC-FIB**.

[![PDDL](https://img.shields.io/badge/Language-PDDL%202.1-orange.svg)](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language)
[![Automated Planning](https://img.shields.io/badge/Domain-Automated%20Planning-blue.svg)](https://www.icaps-conference.org/)

---

## 🏛️ Domain Architecture & State Space

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ROVER EXPLORATION PDDL                            │
├───────────────────┬─────────────────────────────────────────────────────────┤
│ 🛰️ Actions        │ Navigate, Sample Soil/Rock, Calibrate Camera, Transmit  │
│ 📍 Predicates     │ At(r, w), Equipped(r), Empty(s), Communicated(data)     │
│ 🔋 Constraints    │ Battery depletion, store capacities & line-of-sight     │
│ ⚡ Solvers        │ FastForward (FF), Metric-FF & Temporal Metric Planners  │
└───────────────────┴─────────────────────────────────────────────────────────┘
```

---

## 🔬 STRIPS Action Model

### Navigate Operator:
$$\text{Navigate}(r, w_1, w_2): \begin{cases} \text{Precond}: & \text{At}(r, w_1) \wedge \text{CanTraverse}(r, w_1, w_2) \wedge \text{Visible}(w_1, w_2) \\ \text{Add}: & \text{At}(r, w_2) \\ \text{Del}: & \text{At}(r, w_1) \end{cases}$$

### Soil Sampling Operator:
$$\text{SampleSoil}(r, s, w): \begin{cases} \text{Precond}: & \text{At}(r, w) \wedge \text{EquippedSoil}(r) \wedge \text{Empty}(s) \\ \text{Add}: & \text{HaveSoilAnalysis}(r, w) \\ \text{Del}: & \text{Empty}(s) \end{cases}$$

---

## 📂 Files

* `rovers_domain.pddl`: Full STRIPS & typed domain definition.
* `problem_sample_analysis.pddl`: Benchmark mission scenario with 5 waypoints and sample transmission goals.
