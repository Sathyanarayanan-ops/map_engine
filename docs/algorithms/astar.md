A* Algorithm (Single Destination)

1) Initialization:
 - Create a priority queue (open set) and add the start_node with a priority of 0.
 - Initialize g_score (cost to reach each node) for all nodes as infinity, except the start node (g_score[start_node] = 0).
 - Initialize f_score (estimated total cost to goal) for all nodes as infinity, except the start node (f_score[start_node] = heuristic(start_node, goal_node)).
 - Create an empty parent_map to reconstruct the path later.

2) Iterate Until Open Set is Empty:
 - Pop the node with the lowest f_score from the open set (current_node).
 - If current_node == goal_node, reconstruct the path using parent_map and return it.
3) For Each Neighbor of the Current Node:
 - Calculate the tentative g_score (distance to this neighbor via current_node).
 - If the tentative g_score is smaller than the previously recorded g_score for the neighbor:
 - Update the parent_map to point to current_node for the neighbor.
 - Update the neighbor’s g_score.
 - Update the neighbor’s f_score as g_score + heuristic(neighbor, goal_node).
 - Add the neighbor to the open set if it’s not already there.
4) No Path Found:
 - If the open set becomes empty without reaching the goal, return None.