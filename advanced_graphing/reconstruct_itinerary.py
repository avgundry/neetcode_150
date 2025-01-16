from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(set)
        stops = set([tick[1] for tick in tickets])
        for pair in tickets:
            adj[pair[0]].add(pair[1])
        print(adj)
        print(stops)

        out = []
        self.dfs(out, stops, adj, ["JFK"])
        # while adj:
        #     nxt = min(adj[curr])
        #     del adj[curr]
        #     out.append(curr)
        #     curr = nxt

        return min(out)

    def dfs(self, out, stops, adj, path):
        curr = path[-1]
        # If we've seen every stop, exit.
        if len(stops) == 0:
            out.append(path)
            return

        for nxt in adj[curr]:
            if nxt in stops:
                self.dfs(out, stops - set([nxt]), adj, path + [nxt])




if __name__ == "__main__":
    s = Solution()
    print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))