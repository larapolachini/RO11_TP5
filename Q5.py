"""Reinforcement Learning Algorithm"""

import numpy as np


N_STATES = 4
N_ACTION = 3


def T(state_0: int, action: int, state_1: int, x: float = 0.25, y: float = 0.25) -> float:
    """
    Return transition value of action from state_0 to state_1.

    Args:
        state_0 (int) : number of initial state.
        action (int) : number of action done.
        state_1 (int) : number of final state.
        x (float) : transition constant. Default value is 0.25.
        y (float) : transition constant. Default value is 0.25.
    """
    if state_0 < 0 or state_1 < 0 or state_0 > N_STATES or state_1 > N_STATES:
        return None

    transition_matrix = np.zeros((N_STATES, N_STATES))

    match action:
        case 0:
            transition_matrix = np.array([
                [0, 0, 0, 0],
                [0, 1-x, 0, x],
                [1-y, 0, 0, y],
                [1, 0, 0, 0],
            ])

        case 1:
            transition_matrix = np.array([
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ])

        case 2:
            transition_matrix = np.array([
                [0, 0, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ])

        case _:
            return None

    return transition_matrix[state_0][state_1]



def R(state: int) -> float:
    """
    Return reward of a state.

    Args:
        state (int) : number of state.
    """
    if state < 0 or state > N_STATES:
        return None

    match state:
        case 3:
            return 10

        case 2:
            return 1

        case _:
            return 0



def V(V_previous: np.ndarray[float], state: int, action:int, gamma: float = 0.9) -> float:
    """
    Return current value of a state.

    Args:
        V_previous (np.ndarray[float]) : array of previous iteration V values.
        state (int) : number of state.
        action (int) : number of action.
        gamma (float) : state value constante. Default value is 0.9.
    """
    if state < 0 or state > N_STATES:
        return None

    return R(state) + gamma * sum(
        T(state, action, state_next) * V_previous[state] for state_next in range(N_STATES)
    )



def learning(
        gamma: float = 0.9, threshold: float = 1e-4
    ) -> list[np.ndarray[float], np.ndarray[float], int]:
    """
    Return reinforcement learning results values and iterations.

    Args:
        gamma (float) : state value constante. Default value is 0.9.
        threshold (float) : reinforcement learning threshold. Default value is 1e-4.
    """
    V_current = np.zeros(N_STATES)
    policy = np.zeros(N_STATES, dtype=int)
    iterations = 0

    while True:
        delta = 0
        V_previous = V_current.copy()

        for state in range(N_STATES):
            action_values = []

            for action in range(N_ACTION):
                action_values.append(V(V_previous, state, action, gamma))

            V_current[state] = max(action_values)
            policy[state] = np.argmax(action_values)
            delta = max(delta, abs(V_current[state] - V_previous[state]))

        iterations += 1

        if delta < threshold:
            break


    return V_current, policy, iterations




def main() -> None:
    V_optimal, policy_optimial, iterations = learning()

    print(V_optimal)
    print(policy_optimial)
    print(iterations)



if __name__ == "__main__":
    main()
    


        