import numpy as np

# Define states and observations
weather_states = ("Rain", "Sun")
observations = ["walk", "shop", "clean"]

# Initial state probabilities
start_prob = {"Rain": 0.6, "Sun": 0.4}

# Transition probabilities
trans_prob = {
    "Rain": {"Rain": 0.7, "Sun": 0.3},
    "Sun": {"Rain": 0.4, "Sun": 0.6},
}

# Emission probabilities
emit_prob = {
    "Rain": {"walk": 0.1, "shop": 0.4, "clean": 0.5},
    "Sun": {"walk": 0.6, "shop": 0.3, "clean": 0.1},
}

def viterbi_algorithm(obs):
    V = [{}]
    
    # Initialize base cases (t == 0)
    for state in weather_states:
        V[0][state] = start_prob[state] * emit_prob[state][obs[0]]
        
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        for state in weather_states:
            V[t][state] = max(
                V[t - 1][prev_state] * trans_prob[prev_state][state] * emit_prob[state][obs[t]]
                for prev_state in weather_states
            )
            
    # Print the step-by-step probabilities
    for t in range(len(V)):
        print(f"Step {t+1} Probabilities: {V[t]}")

if __name__ == "__main__":
    viterbi_algorithm(observations)
