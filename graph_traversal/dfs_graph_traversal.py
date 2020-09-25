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




def graph_dfs_recursive(v, result=[], visited={}):
    if not v:
      return NotImplemented
    result.append(v)
    visited[v] = True
    print(result, visited)
    for v_t in graph_adj_list[v]:
        if v_t not in visited.keys():
            graph_dfs_recursive(v_t, result, visited)
    return result


assert graph_dfs_recursive("A") == ["A", "B", "D", "E", "C", "F"]


# "A": ["B", "C"],
# "B": ["A", "D"],
# "C": ["A", "E"],
# "D": ["B", "E", "F"],
# "E": ["C", "D", "F"],
# "F": ["D", "E"]

# //          A
# //        /   \
# //       B     C
# //       |     |
# //       D --- E
# //        \   /
# //          F

def graph_dfs_iterative(v):

  stack = [v]
  result = []
  visited = {v:True}
  while len(stack) > 0:   
    out_vertex = stack.pop() 
    result.append(out_vertex)   
    for v_t in graph_adj_list[out_vertex]:
      if v_t not in visited.keys():
        stack.append(v_t)
        visited[v_t] = True
  print(result)
  return result



assert graph_dfs_iterative("A") == ["A","C","E","F","D","B"]