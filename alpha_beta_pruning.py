import math
import networkx as nx
import matplotlib.pyplot as plt

visited_nodes = []
pruned_nodes = []
leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]

def alpha_beta_search(depth, node_idx, is_maximizing, alpha, beta):
    visited_nodes.append(node_idx)
    
    # Leaf node reached
    if depth == 3:
        return leaf_values[node_idx]
        
    if is_maximizing:
        best_val = -math.inf
        for i in range(2):
            val = alpha_beta_search(depth + 1, node_idx * 2 + i, False, alpha, beta)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if alpha >= beta:
                pruned_nodes.append(node_idx)
                break
        return best_val
    else:
        best_val = math.inf
        for i in range(2):
            val = alpha_beta_search(depth + 1, node_idx * 2 + i, True, alpha, beta)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if alpha >= beta:
                pruned_nodes.append(node_idx)
                break
        return best_val

if __name__ == "__main__":
    optimal_value = alpha_beta_search(0, 0, True, -math.inf, math.inf)
    print("Calculated Optimal Value:", optimal_value)
    
    # Visualization
    graph = nx.Graph()
    edges_list = [
        ("Root", "Left"), ("Root", "Right"),
        ("Left", "L-Left"), ("Left", "L-Right"),
        ("Right", "R-Left"), ("Right", "R-Right")
    ]
    graph.add_edges_from(edges_list)
    
    node_colors = []
    for node in graph.nodes():
        if node in ["Left", "Right"]:
            node_colors.append("lightcoral")
        else:
            node_colors.append("lightgreen")
            
    nx.draw(graph, with_labels=True, node_color=node_colors, node_size=2500, font_weight='bold')
    plt.title("Alpha-Beta Pruning Game Tree")
    
    # Save image to Output-Screenshots directory
    plt.savefig("Output-Screenshots/alpha_beta_output.png")
    print("Graph saved as Output-Screenshots/alpha_beta_output.png")
    # Uncomment the following line to show the graph interactively
    # plt.show()
