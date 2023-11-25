import heapq


class WeightedCompleteGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        self.visited = [False] * num_vertices

    def add_edge(self, start, end, weight):
        self.adj_matrix[start][end] = weight
        self.adj_matrix[end][start] = weight

    def dfs(self, current_vertex, finish_vertex, visited_count, current_cost, optimal_path, optimal_cost):
        self.visited[current_vertex] = True
        visited_count += 1

        if visited_count == self.num_vertices and current_vertex == finish_vertex:
            if current_cost < optimal_cost:
                optimal_path.clear()
                optimal_path.extend(self.visited)
                optimal_cost = current_cost
            return

        for neighbor in range(self.num_vertices):
            if (
                not self.visited[neighbor] and
                self.adj_matrix[current_vertex][neighbor] != float('inf')
            ):
                self.dfs(neighbor, finish_vertex, visited_count, current_cost + self.adj_matrix[current_vertex][neighbor], optimal_path, optimal_cost)

        self.visited[current_vertex] = False

    def find_optimal_path(self, start_vertex, finish_vertex):
        optimal_path = [False] * self.num_vertices
        optimal_cost = float('inf')

        self.dfs(start_vertex, finish_vertex, 0, 0, optimal_path, optimal_cost)

        if optimal_cost != float('inf'):
            print(f"Optimal path cost from {start_vertex} to {finish_vertex}: {optimal_cost}")
            print("Optimal path:", [i for i, visited in enumerate(optimal_path) if visited])
