from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Optimized recursive approach: build paths recursively.
        If we've previously seen a destination in our path, do not visit it, as it will
        never be more optimal since there are no negative costs.
        """
        import heapq

        graph = {}
    
        for src, dst, cost in flights:
            if src not in graph:
                graph[src] = {}
            graph[src][dst] = cost
        
        # Optionally, ensure all nodes are included in the graph, even those without outgoing edges
        for src, dst, cost in flights:
            if dst not in graph:
                graph[dst] = {}
        
        # Dictionary to store the shortest distance to each node
        distances = {node: float('infinity') for node in graph}
        distances[src] = 0
        
        # Priority queue to store (distance, node, path_length) triples
        priority_queue = [(0, src, 0)]
        
        while priority_queue:
            current_distance, current_node, current_path_length = heapq.heappop(priority_queue)
            
            # If the path length exceeds the maximum allowed, skip this node
            if current_path_length > k:
                continue
            
            # If the popped node has a greater distance than the stored, skip it
            if current_distance > distances[current_node]:
                continue
            
            # Explore neighbors
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                new_path_length = current_path_length + 1
                
                # Only consider this path if it's better and within the allowed path length
                if distance < distances[neighbor] and new_path_length <= k + 1:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor, new_path_length))
        
        return distances

        # Build adjacency list from edge list.
        def edge_to_adjacency_list(edges):
            adj_list = defaultdict(dict)
            for (s, d, cost) in edges:
                adj_list[s][d] = cost
                # adj_list[d][s] = cost
            
            return adj_list

        adj_list = edge_to_adjacency_list(flights)

        distances = {node: float('inf') for node in adj_list}
        distances[src] = 0

        prio_q = [(0, src, 0)]

        while prio_q:
            curr_dist, curr_node, path_len = heapq.heappop(prio_q)
            if curr_dist > distances[curr_node]:
                continue

            for neighbor, weight in adj_list[curr_node].items():
                dist = curr_dist + weight
                new_path_length = path_e

                if dist < distances[neighbor] and path_len - 1 <= k:
                    distances[neighbor] = dist
                    heapq.heappush(prio_q, (dist, neighbor, path_len + 1))

                
        return distances




        
        """
        Begin with the brute force solution...find all flight paths that
        have no more than k stops.

        As expected, times out on leetcode submission.
        """
        # Build an adjacency matrix first.
        adj_matrix = [[-1 for _ in range(n)] for _ in range(n)]
        for s, d, price in flights:
            adj_matrix[s][d] = price

        # print(adj_matrix)
        for row in adj_matrix:
            print(row)

        # SUPER brute force. Obviously clean this wayyyy up later.
        def recurse_paths(path, paths, adj_matrix, src, dst, k):
            if k <= 0:
                return
            if adj_matrix[src][dst] != -1:
                paths.append(path + [dst])
            for i in range(len(adj_matrix[src])):
                if adj_matrix[src][i] != -1 and i not in path:
                    path.append(i)
                    recurse_paths(path, paths, adj_matrix, i, dst, k - 1)
                    path.pop()

        def path_cost(path, adj_matrix):
            cost = 0
            for i in range(1, len(path)):
                cost += adj_matrix[path[i - 1]][path[i]]
        
            return cost

        # Brute force find all paths of length k that go from src to dst.
        paths = []
        recurse_paths([src], paths, adj_matrix, src, dst, k + 1)
        path_costs = []
        print(f"\nPaths: {paths}")
        for path in paths:
            path_costs.append(path_cost(path, adj_matrix))
        print(f"\nPath costs: {path_costs}")
        if path_costs:
            return min(path_costs)
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
    print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))


        