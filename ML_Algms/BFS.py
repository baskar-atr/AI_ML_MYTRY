# Neighbour nodes created
graph = {
    '8': ['1', '2'],
    '1': ['7', '6'],
    '2': ['4', '5']
}
visited = []
queue = []


def bfs(visited, queue, node):
    visited.append(node)
    queue.append(node)
# Iterate the Queue until its empty
    while queue:
        c = queue.pop(0)
        print(c, end="")
        # Check if the graph as neighbor nodes
        if c in graph:
            for neighbour in graph[c]:
                # If the Neighbor is not visited, visit and add in to Q
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


bfs(visited, queue, '8')
