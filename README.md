# Artificial Intelligence Assignment

**Name:** Probal Protim Hazarika  
**Roll No:** 220710007046  

This repository contains Python implementations of three fundamental Artificial Intelligence algorithms assigned for this project. Below is an explanation of each algorithm and how it is implemented in the codebase.

---

## 1. Alpha-Beta Pruning
**File:** `alpha_beta_pruning.py`

### Description
Alpha-Beta Pruning is an optimization technique used for the Minimax algorithm in game theory and AI. It significantly reduces the number of nodes evaluated in the game tree by pruning branches that cannot possibly influence the final decision. This allows the search to evaluate deeper trees in the same amount of time.

### Implementation Details
- **Tree Structure:** The program builds a game tree from an array of leaf node values `[3, 5, 6, 9, 1, 2, 0, -1]`.
- **Search:** A recursive depth-first search is performed, keeping track of two values: `alpha` (the best value the maximizer can guarantee) and `beta` (the best value the minimizer can guarantee).
- **Visualization:** I have used the `networkx` and `matplotlib` libraries to visually map the game tree structure and demonstrate the paths evaluated.
- **Proof of Work:** An output plot of the tree is available in the `Output-Screenshots` folder as `alpha_beta_output.png`.

---

## 2. Hidden Markov Model (HMM)
**File:** `hmm_viterbi.py`

### Description
A Hidden Markov Model is a statistical Markov model where the system being modeled is assumed to be a Markov process with unobservable (hidden) states. This question uses the **Viterbi Algorithm** to decode the most likely sequence of hidden states given a sequence of observable events.

### Implementation Details
- **Scenario:** The program attempts to deduce the hidden weather states ("Rain", "Sun") based on a sequence of daily activities or observations ("walk", "shop", "clean").
- **Probabilities:** Defines initial starting probabilities, transition probabilities (the likelihood of the weather changing), and emission probabilities (the likelihood of an activity occurring given the weather).
- **Viterbi Algorithm:** Iterates through the observations step-by-step, calculating and storing the maximum probability path to reach each state recursively.
- **Proof of Work:** The step-by-step terminal execution log is captured as `hmm_output.png` in the `Output-Screenshots` folder.

---

## 3. Tic-Tac-Toe using Minimax Algorithm
**File:** `tic_tac_toe.py`

### Description
The Minimax algorithm is a backtracking algorithm used in decision-making and game theory to find the optimal move for a player, assuming the opponent also plays optimally. This project implements a fully playable Tic-Tac-Toe game where a human plays against an unbeatable AI.

### Implementation Details
- **Algorithm:** Every time it is the AI's turn, it simulates all possible future board states until the end of the game, scoring +1 for an AI win, -1 for a Human win, and 0 for a draw. The AI then makes the move that maximizes its score.
- **GUI:** The project uses Python's standard `tkinter` library to generate a playable, graphical grid interface for the game.
- **Proof of Work:** A screenshot of a completed match where the AI wins is saved as `tic_tac_toe_output.png` inside the `Output-Screenshots` folder.
