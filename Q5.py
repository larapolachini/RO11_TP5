"""Reinforcement Learning Algorithm — Value Iteration for Task 1 (x=y=0.25, gamma=0.9)
S0:  a1->S1 (1), a2->S2 (1)
S1:  a0->S1 (1-x), a0->S3 (x)
S2:  a0->S0 (1-y), a0->S3 (y)
S3:  a0->S0 (1)
"""

import numpy as np

N_STATES = 4        # S0,S1,S2,S3 -> 0..3
N_ACTIONS = 3       # a0,a1,a2 -> 0..2

def T(state_0: int, action: int, state_1: int, x: float = 0.25, y: float = 0.25) -> float:
    """Transition model T(s,a,s')."""
    if not (0 <= state_0 < N_STATES and 0 <= state_1 < N_STATES and 0 <= action < N_ACTIONS):
        return 0.0

    if action == 0:  # a0
        # NOTE: S0 has no a0 in this variant → S0 row all zeros
        transition_matrix = np.array([
            [0,   0,   0,   0],      # S0 (invalid a0 → zero probs)
            [0, 1-x,  0,   x],       # S1 via a0 -> S1/S3
            [1-y, 0,   0,   y],      # S2 via a0 -> S0/S3
            [1,   0,   0,   0],      # S3 via a0 -> S0
        ], dtype=float)
    elif action == 1:  # a1
        transition_matrix = np.array([
            [0, 1, 0, 0],            # S0 --a1--> S1
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ], dtype=float)
    elif action == 2:  # a2
        transition_matrix = np.array([
            [0, 0, 1, 0],            # S0 --a2--> S2
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ], dtype=float)
    else:
        return 0.0

    return float(transition_matrix[state_0, state_1])

def R(state: int) -> float:
    """Rewards: R(S3)=10, R(S2)=1, else 0."""
    if not (0 <= state < N_STATES):
        return 0.0
    return 10.0 if state == 3 else (1.0 if state == 2 else 0.0)

def q_value(V_prev: np.ndarray, state: int, action: int,
            gamma: float = 0.9, x: float = 0.25, y: float = 0.25) -> float:
    """Q(s,a | V_prev) = R(s) + γ Σ_{s'} T(s,a,s') V_prev[s']"""
    return R(state) + gamma * sum(
        T(state, action, s1, x, y) * V_prev[s1] for s1 in range(N_STATES)
    )

def learning(gamma: float = 0.9, threshold: float = 1e-4,
             x: float = 0.25, y: float = 0.25):
    V_current = np.zeros(N_STATES, dtype=float)
    policy = np.zeros(N_STATES, dtype=int)
    iterations = 0

    # Valid actions per state (S0 only a1,a2)
    valid_actions = {
        0: [1, 2],   # S0: a1,a2
        1: [0],      # S1: a0
        2: [0],      # S2: a0
        3: [0],      # S3: a0
    }

    while True:
        V_prev = V_current.copy()
        delta = 0.0

        for s in range(N_STATES):
            q_vals = [q_value(V_prev, s, a, gamma, x, y) for a in valid_actions[s]]
            best_idx = int(np.argmax(q_vals))
            V_current[s] = q_vals[best_idx]
            policy[s] = valid_actions[s][best_idx]
            delta = max(delta, abs(V_current[s] - V_prev[s]))

        iterations += 1
        if delta < threshold:
            break

    return V_current, policy, iterations

def main() -> None:
    V_optimal, policy_optimal, iterations = learning(gamma=0.9, threshold=1e-4, x=0.25, y=0.25)
    action_names = {0: "a0", 1: "a1", 2: "a2"}
    print("V*:", np.round(V_optimal, 6))
    print("π*:", [action_names[a] for a in policy_optimal])
    print("iterations:", iterations)

if __name__ == "__main__":
    main()
