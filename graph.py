
class Vertex(object):
   def __init__(self, graph, vertexId):
      self.graph = graph
      self.vertexId = vertexId
      self.outgoingEdges = set()
      self.incomingEdges = set()

   def __hash__(self):
      return hash(self.vertexId)
   def __repr__(self):
      return "Vertex(%s)" % (repr(self.vertexId),)
   def __str__(self):
      return repr(self)

   def outdegree(self):
      return len(self.outgoingEdges)

   def anyNext(self):
      return self.graph[list(self.outgoingEdges)[0][1]]


# a class for a directed graph
class Graph(object):
   def __init__(self, vertexIds):
      self.vertices = dict((name, Vertex(self, name)) for name in vertexIds)
      self.edges = set()

   def __getitem__(self, key):
      return self.vertices[key]

   def anyVertex(self):
      for k,v in self.vertices.items():
         return v

   def addEdge(self, source, target):
      self.edges.add((source, target))
      self[source].outgoingEdges.add((source, target))
      self[target].incomingEdges.add((source, target))

   def addEdges(self, edges):
      for e in edges:
         self.addEdge(*e)

   def delete(self, vertex):
      if type(vertex) is Vertex:
         vertex = vertex.vertexId

      involvedEdges = self[vertex].outgoingEdges | self[vertex].incomingEdges
      for (u,v) in involvedEdges:
         self[v].incomingEdges.remove((u,v))
         self[u].outgoingEdges.remove((u,v))
         self.edges.remove((u,v))

      del self.vertices[vertex]

   def __repr__(self):
      return repr(set(self.vertices.keys())) + ", " + repr(self.edges)
   def __str__(self):
      return repr(self)
