#!/usr/bin/env python3

import sys
import numpy as np

def Dijkstra(nodes, edges, source):
    """Dijkstra shortest path algorithm
 
    Args:
        nodes (:obj:`list` of :obj:`str`): names of all nodes. 
        edges (:obj:`list` of :obj:`list`): graph adjacency matrix.
        source (:obj:`int`): source node index.

    Returns:
    """

    # shortest path previous nodes
    prev = np.array([None] * len(nodes))
    visited = np.array([False] * len(nodes)) 
    # shortest distances to every node
    dist = np.array([inf] * len(nodes))
    dist[source] = 0

    while not np.all(visited):
        # among unvisited nodes find the node
        # with minimal distance to the source
        min_dist = np.amin(dist[~visited])

        # get the node index
        for i, d in enumerate(dist):
            if d == min_dist and not visited[i]:
                node_idx = i
                break
        
        # check all paths
        node_edges = edges[node_idx]
        for i, w in enumerate(node_edges):
            if w != -1:
                alt = min_dist + w
                if alt < dist[i]:
                    dist[i] = alt
                    prev[i] = nodes[node_idx]

        visited[node_idx] = True

    return prev, dist


inf = sys.maxsize
nodes_ = np.array(['A', 'B', 'C', 'D', 'E'])
edges_ = [[ 0, 6, -1,  1, -1],
          [ 6, 0,  5,  2,  2],
          [-1, 5,  0, -1,  5],
          [ 1, 2, -1,  0,  1],
          [-1, 2,  5,  1,  0]]
edges_ = np.asarray(edges_)
source_idx_ = 2

prev, dist = Dijkstra(nodes_, edges_, source_idx_)
print(prev, dist)
