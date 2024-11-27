import math

def get_adjacent_edge(graph, vertex_a, vertex_b):
    for edge in graph.edges:
        if Edge(vertex_a, vertex_b) == edge:
            return edge
    return None
        

def dijkstras_algo(graph, starting_vertex, target_vertex):
    # set inital distances
    dist = {}
    for vertex in graph.vertices:
        dist[vertex]=math.inf
    dist[starting_vertex] = 0

    unvisited_vertices = graph.vertices
    visited = []


    curr = starting_vertex
    print(f"Looking for shortest path between {starting_vertex} and {target_vertex}")

    while dist[curr] != math.inf and target_vertex in unvisited_vertices:
        print(f"Current vertex: {curr}\n Unvisited: {unvisited_vertices}\n Current distances: {dist}\n\n")
        for unvisited_vertex in unvisited_vertices:
            adjacent_edge = get_adjacent_edge(graph, curr, unvisited_vertex)
            if (adjacent_edge):
                y = dist[curr] + adjacent_edge.weight
                dist[unvisited_vertex] = min(y, dist[unvisited_vertex])
                
        unvisited_vertices.remove(curr)
        visited.append(curr)
        # find unvisited node with lowest distance
        min_distance = min([dist[unvisited_vertex] for unvisited_vertex in unvisited_vertices])
        closest_vertices = [vertex for vertex, distance in dist.items() if distance == min_distance]
        curr = closest_vertices[0]
    
    print(f"Algorithm complete. Distances: {dist}. Visited nodes in order: {visited}")




def get_sorted_vertices(vertices): 
    return sorted(vertices, key=lambda v: v.value)

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
        self.vertices = get_sorted_vertices([vertexA, vertexB])
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

    def __repr__(self):
        return f"Vertices: {self.vertices} \nEdges: {self.edges}"

vertices = [Vertex('d'),
            Vertex('e'),
            Vertex('f'),
            Vertex('g'),
            Vertex('h'),
            Vertex('i'),
            Vertex('j'),
            Vertex('k'),
            Vertex('l'),
            Vertex('m'),
            Vertex('n'),
            Vertex('o'),            
            Vertex('p'),   
            Vertex('q'),
            Vertex('r'),
        ]
graph = Graph(vertices)



graph.add_edge(Edge(Vertex('d'), Vertex('g'), 16))
graph.add_edge(Edge(Vertex('d'), Vertex('e'), 18))
graph.add_edge(Edge(Vertex('d'), Vertex('h'), 15))
graph.add_edge(Edge(Vertex('e'), Vertex('f'), 9))
graph.add_edge(Edge(Vertex('e'), Vertex('h'), 25))
graph.add_edge(Edge(Vertex('e'), Vertex('d'), 18))
graph.add_edge(Edge(Vertex('f'), Vertex('e'), 9))
graph.add_edge(Edge(Vertex('f'), Vertex('h'), 29))
graph.add_edge(Edge(Vertex('g'), Vertex('d'), 16))
graph.add_edge(Edge(Vertex('g'), Vertex('h'), 31))
graph.add_edge(Edge(Vertex('g'), Vertex('j'), 23))
graph.add_edge(Edge(Vertex('h'), Vertex('d'), 15))
graph.add_edge(Edge(Vertex('h'), Vertex('e'), 25))
graph.add_edge(Edge(Vertex('h'), Vertex('g'), 31))
graph.add_edge(Edge(Vertex('h'), Vertex('j'), 13))
graph.add_edge(Edge(Vertex('h'), Vertex('k'), 10))
graph.add_edge(Edge(Vertex('h'), Vertex('i'), 27))
graph.add_edge(Edge(Vertex('h'), Vertex('f'), 29))
graph.add_edge(Edge(Vertex('j'), Vertex('g'), 23))
graph.add_edge(Edge(Vertex('j'), Vertex('h'), 13))
graph.add_edge(Edge(Vertex('j'), Vertex('k'), 28))
graph.add_edge(Edge(Vertex('j'), Vertex('n'), 33))
graph.add_edge(Edge(Vertex('k'), Vertex('j'), 28))
graph.add_edge(Edge(Vertex('k'), Vertex('h'), 10))
graph.add_edge(Edge(Vertex('k'), Vertex('n'), 14))
graph.add_edge(Edge(Vertex('k'), Vertex('o'), 34))
graph.add_edge(Edge(Vertex('k'), Vertex('i'), 26))
graph.add_edge(Edge(Vertex('k'), Vertex('m'), 11))
graph.add_edge(Edge(Vertex('m'), Vertex('k'), 11))
graph.add_edge(Edge(Vertex('m'), Vertex('n'), 17))
graph.add_edge(Edge(Vertex('m'), Vertex('q'), 12))
graph.add_edge(Edge(Vertex('n'), Vertex('m'), 17))
graph.add_edge(Edge(Vertex('n'), Vertex('k'), 14))
graph.add_edge(Edge(Vertex('n'), Vertex('o'), 30))
graph.add_edge(Edge(Vertex('n'), Vertex('p'), 32))
graph.add_edge(Edge(Vertex('n'), Vertex('r'), 20))
graph.add_edge(Edge(Vertex('o'), Vertex('n'), 30))
graph.add_edge(Edge(Vertex('o'), Vertex('k'), 34))
graph.add_edge(Edge(Vertex('o'), Vertex('r'), 24))
graph.add_edge(Edge(Vertex('o'), Vertex('l'), 35))
graph.add_edge(Edge(Vertex('o'), Vertex('q'), 19))
graph.add_edge(Edge(Vertex('p'), Vertex('n'), 32))
graph.add_edge(Edge(Vertex('p'), Vertex('q'), 21))
graph.add_edge(Edge(Vertex('q'), Vertex('p'), 21))
graph.add_edge(Edge(Vertex('q'), Vertex('m'), 12))
graph.add_edge(Edge(Vertex('q'), Vertex('o'), 19))
graph.add_edge(Edge(Vertex('q'), Vertex('r'), 22))
graph.add_edge(Edge(Vertex('r'), Vertex('o'), 22))
graph.add_edge(Edge(Vertex('r'), Vertex('q'), 24))

dijkstras_algo(graph, vertices[2], vertices[13])
