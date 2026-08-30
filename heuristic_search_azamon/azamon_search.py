#!/usr/bin/env python3
"""
Azamon Logistics: Combinatorial Optimization via Local Search & Simulated Annealing
"""
import numpy as np
import math
import random

class AzamonState:
    def __init__(self, num_packages=100, num_transports=10):
        self.num_packages = num_packages
        self.num_transports = num_transports
        # Assign each package to a random transport
        self.assignment = np.random.randint(0, num_transports, size=num_packages)
        self.package_weights = np.random.uniform(1.0, 50.0, size=num_packages)
        self.transport_capacities = np.full(num_transports, 350.0)

    def compute_cost(self):
        cost = 0.0
        transport_loads = np.zeros(self.num_transports)
        for p, t in enumerate(self.assignment):
            transport_loads[t] += self.package_weights[p]

        # Capacity penalty + transport cost
        for t in range(self.num_transports):
            if transport_loads[t] > self.transport_capacities[t]:
                cost += (transport_loads[t] - self.transport_capacities[t]) * 100.0 # Heavy penalty
            cost += transport_loads[t] * 1.5 # Operational transport fee
        return cost

    def get_neighbor(self):
        neighbor = AzamonState(self.num_packages, self.num_transports)
        neighbor.assignment = np.copy(self.assignment)
        neighbor.package_weights = self.package_weights
        neighbor.transport_capacities = self.transport_capacities

        # Operator: Move random package to different transport
        p = np.random.randint(0, self.num_packages)
        new_t = np.random.randint(0, self.num_transports)
        neighbor.assignment[p] = new_t
        return neighbor

def simulated_annealing(initial_state, initial_temp=1000.0, cooling_rate=0.995, max_steps=5000):
    current_state = initial_state
    current_cost = current_state.compute_cost()
    best_state = current_state
    best_cost = current_cost
    temp = initial_temp

    for step in range(max_steps):
        neighbor = current_state.get_neighbor()
        neighbor_cost = neighbor.compute_cost()
        delta = neighbor_cost - current_cost

        if delta < 0 or np.random.rand() < math.exp(-delta / max(temp, 1e-8)):
            current_state = neighbor
            current_cost = neighbor_cost
            if current_cost < best_cost:
                best_state = neighbor
                best_cost = current_cost

        temp *= cooling_rate
        if temp < 1e-4:
            break

    return best_state, best_cost

if __name__ == '__main__':
    state = AzamonState()
    print(f"Initial Random Assignment Cost: {state.compute_cost():.2f}")
    best_s, best_c = simulated_annealing(state)
    print(f"Optimized Solution Cost after Simulated Annealing: {best_c:.2f}")
