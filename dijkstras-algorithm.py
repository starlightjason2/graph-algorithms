import math

class Vertex:
    value = ""
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value
    def __eq__(self, other):
        return self.value == other.value
    def __hash__(self):
        return hash(self.value)
    
class Edge:
    vertices = []
    weight = 1
    def __init__(self, vertexA, vertexB, weight=1):
        self.vertices = sorted([vertexA, vertexB], key=lambda v: v.value)
        self.weight = weight
    def __repr__(self):
        return f"\nVertices:{self.vertices} Weight {self.weight}"
    def __eq__(self, other):
        return self.vertices == other.vertices

class Graph:
    vertices = []
    edges = []

    def __init__(self, vertices):
        self.vertices = vertices
    
    def add_edge(self, edge):
        # check to see edge doesn't exist
        if edge.vertices not in [edge.vertices for edge in self.edges]:
            self.edges.append(edge)

    def get_edges_for_vertex(self, v):
        """
        Given a vertex, get all edges connecting it
        :return: a tuple containing connecting edges and vertices
        """
        return [edge for edge in self.edges if v in edge.vertices]
    
    
    def dijkstras_algo(self, starting_vertex, target_vertex):
        # set inital distances
        dist = {}
        for vertex in self.vertices:
            dist[vertex]=math.inf
        dist[starting_vertex] = 0

        unvisited_vertices = self.vertices
        visited = []
        curr = starting_vertex
        print(f"Looking for shortest path between {starting_vertex} and {target_vertex}")

        while dist[curr] != math.inf:
            print(f"Current vertex: {curr}\n Unvisited: {unvisited_vertices}\n Current distances: {dist}\n")
            connecting_edges = self.get_edges_for_vertex(curr)                    
            # interate through each edge between curr and something else
            for edge in connecting_edges:
                # the other vertex in the edge is the first vertex that isn't curr
                other = next(filter(lambda v: v != curr, edge.vertices))
                if other in unvisited_vertices:                
                    y = dist[curr] + edge.weight                
                    dist[other] = min(y, dist[other])
            unvisited_vertices.remove(curr)
            visited.append(curr)
            if len(unvisited_vertices) == 0: break
            # find unvisited node with lowest distance
            # get tuples of distances like (vertex, distance)
            unvisited_dists = [(vertex, dist[vertex]) for vertex in unvisited_vertices]
            # sort them such that the first item is the closest
            closest_vertices = sorted(unvisited_dists, key=lambda item: item[1])
            curr = closest_vertices[0][0]
        print(f"Algorithm complete. Distances: {dist}. Visited nodes in order: {visited}")

    def __repr__(self):
        return f"Vertices: {self.vertices} \nEdges: {self.edges}"



vertices = [Vertex('a'),
            Vertex('b'),
            Vertex('c'),
            Vertex('d'),
            Vertex('e'),
            Vertex('f'),
            Vertex('g'),
            Vertex('z'),
        ]
graph = Graph(vertices)

# v0​↔v1​ (weight 4)
graph.add_edge(Edge(Vertex('a'), Vertex('b'), 4))
# v1​↔v3​ (weight 6)
graph.add_edge(Edge(Vertex('a'), Vertex('c'), 3))
# v3​↔v5​ (weight 3)
graph.add_edge(Edge(Vertex('b'), Vertex('c'), 2))
# v5​↔v7​ (weight 7)
graph.add_edge(Edge(Vertex('b'), Vertex('d'), 5))
# v7​↔v9​ (weight 5)
graph.add_edge(Edge(Vertex('c'), Vertex('d'), 3))
# v0​↔v2​ (weight 2)
graph.add_edge(Edge(Vertex('c'), Vertex('e'), 6))
# v2​↔v4​ (weight 8)
graph.add_edge(Edge(Vertex('d'), Vertex('e'), 1))
graph.add_edge(Edge(Vertex('d'), Vertex('f'), 5))
# v4​↔v6​ (weight 3)
graph.add_edge(Edge(Vertex('e'), Vertex('g'), 5))
# v6​↔v8​ (weight 6)
graph.add_edge(Edge(Vertex('f'), Vertex('g'), 2))
# v8​↔v9​ (weight 4)
graph.add_edge(Edge(Vertex('z'), Vertex('g'), 4))
# v3​↔v8​ (weight 7)
graph.add_edge(Edge(Vertex('z'), Vertex('f'), 7))

graph.dijkstras_algo(vertices[0], vertices[-1])
