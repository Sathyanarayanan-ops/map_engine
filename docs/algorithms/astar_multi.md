Multi-Stop A* Algorithm

1) Input:
A graph, graph.
A list of nodes, route, where route = [start, stop1, stop2, ..., stopN, goal].

2) Validation:
If route has fewer than 2 nodes, raise an error since a start and goal are required.

3) Initialize the Complete Path:
Create an empty list, complete_path.

4) Iterate Through Each Pair of Nodes in the Route:
For i in 0 to len(route) - 2:
Let start_node = route[i] and goal_node = route[i + 1].
Use the single-destination A* (astar_pathfinding) to compute the shortest path between start_node and goal_node.

5) Handle No Path Found:
If astar_pathfinding returns None for any segment, print an error message, and return None.

6) Merge Segments:
Append the result of astar_pathfinding for each segment to complete_path.
Ensure no duplicate nodes at segment boundaries by appending only segment_path[1:] for subsequent segments.

7) Return the Complete Path:
After iterating through all segments, return the combined complete_path.