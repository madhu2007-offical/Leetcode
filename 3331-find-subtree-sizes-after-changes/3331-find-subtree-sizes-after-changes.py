import sys

# Increase recursion depth for skewed trees up to 10^5 nodes
sys.setrecursionlimit(200000)


class Solution:

  def findSubtreeSizes(self, parent, s):
    n = len(parent)

    # 1. Build the initial tree
    adj = [[] for _ in range(n)]
    for i in range(1, n):
      adj[parent[i]].append(i)

    new_parent = list(parent)
    last_seen = [-1] * 26

    # 2. First DFS to find the closest matching ancestor for each node
    def find_parents(u):
      char_idx = ord(s[u]) - ord('a')
      prev_ancestor = last_seen[char_idx]

      if prev_ancestor != -1:
        new_parent[u] = prev_ancestor

      last_seen[char_idx] = u
      for v in adj[u]:
        find_parents(v)

      # Backtrack
      last_seen[char_idx] = prev_ancestor

    find_parents(0)

    # 3. Build the modified tree using new_parent
    new_adj = [[] for _ in range(n)]
    for i in range(1, n):
      new_adj[new_parent[i]].append(i)

    ans = [1] * n

    # 4. Second DFS to compute subtree sizes
    def calc_sizes(u):
      for v in new_adj[u]:
        calc_sizes(v)
        ans[u] += ans[v]

    calc_sizes(0)
    return ans