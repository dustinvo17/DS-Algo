graph_adj_list = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "D", "F"],
    "F": ["D", "E"]
}
# //          A
# //        /   \
# //       B     C
# //       |     |
# //       D --- E
# //        \   /
# //          F

def bfs_graph(v):
  queue = [v]
  result = []
  visited = {v:True}
  while len(queue) > 0:
    out_vertex = queue.pop(0)
    result.append(out_vertex)
    for v_t in graph_adj_list[out_vertex]:
      if v_t not in visited.keys():
        visited[v_t] = True
        queue.append(v_t)
  return result

assert bfs_graph('A') == ["A","B","C","D","E","F"]