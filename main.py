import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 1), ('E', 4)],
    'C': [('A', 3), ('E', 1)],
    'D': [('B', 1), ('F', 2)],
    'E': [('B', 4), ('C', 1), ('F', 1)],
    'F': [('D', 2), ('E', 1)]
}

heuristic = {
    'A': 5, 'B': 3, 'C': 4,
    'D': 2, 'E': 1, 'F': 0
}

def a_star(start, goal):
    pq = [(0, start)]
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for neighbor, weight in graph[current]:
            new_cost = g_cost[current] + weight

            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(pq, (f_cost, neighbor))
                parent[neighbor] = current

    path = []
    node = goal

    if node not in parent:
        return None, float('inf'), None

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path, g_cost[goal], parent


def predict_time(distance):
    speed = 40
    return round((distance / speed) * 60, 2)


# MAIN
print("\n🧭 Smart Navigation System")
print("Nodes:", list(graph.keys()))

start = input("Enter Start Node: ").upper()
goal = input("Enter Goal Node: ").upper()

if start not in graph or goal not in graph:
    print("❌ Invalid input!")
else:
    path, dist, parent = a_star(start, goal)

    if path:
        print("\n✅ SHORTEST PATH FOUND")
        print("➡ Path:", " → ".join(path))

        print("\n📊 Step-by-step:")
        total = 0
        for i in range(len(path)-1):
            current = path[i]
            next_node = path[i+1]

            # find distance between nodes
            for neighbor, weight in graph[current]:
                if neighbor == next_node:
                    print(f"{current} → {next_node} = {weight}")
                    total += weight

        print("\n📏 Total Distance:", total)
        print("⏱️ Estimated Time:", predict_time(total), "minutes")

    else:
        print("❌ No path found!")
