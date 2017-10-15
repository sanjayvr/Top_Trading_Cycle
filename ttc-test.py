from graph import *
from toptradingcycle import *

if __name__ == "__main__":
   from unittest import test

   # integers are houses, chars are agents
   agents = {'a','b','c','d','e','f'}
   houses = {1,2,3,4,5,6,}

   # test extracting agents from a cycle
   G = Graph([1,'a',2,'b',3,'c',4,'d',5,'e',6,'f'])
   G.addEdges([(1,'a'), ('a',2), (2,'b'), ('b',3), (3,'c'), ('c',1),
               (4,'d'), ('d',5), (5,'e'), ('e',4), (6,'f'), ('f',6)])

   oneCycle = G[6]
   twoCycle = G[4]
   threeCycle = G[1]

   test({G['f']}, getAgents(G, oneCycle, agents))
   test({G['d'],G['e']}, getAgents(G, twoCycle, agents))
   test({G['a'],G['b'],G['c']}, getAgents(G, threeCycle, agents))

   # test getting an arbitrary cycle
   G = Graph([1,'a',2,'b',3,'c',4,'d',5,'e',6,'f'])
   # a graph which is a single cycle plus a tail
   G.addEdges([(1,'a'), ('a',2), (2,'b'), ('b',3), (3,'c'), ('c',4),
               (4,'d'), ('d',5), (5,'e'), ('e',6), (6,'f'), ('f',4)])

   test({G['f'], G['d'], G['e']}, getAgents(G, anyCycle(G), agents))

   # preferences form a disjoint union of cycles
   # on the very first round
   agentPreferences = {
      'a': [2,3,4,5,6,1],
      'b': [3,4,5,6,1,2],
      'c': [1,2,3,4,5,6],
      'd': [5,6,1,2,3,4],
      'e': [4,1,2,3,5,6],
      'f': [6,1,2,3,4,5],
   }
   initialOwnership = {1:'a', 2:'b', 3:'c', 4:'d',5:'e',6:'f'}
   test({'a': 2, 'b':3, 'c':1, 'd':5, 'e':4, 'f':6},
      topTradingCycles(agents, houses, agentPreferences, initialOwnership))


   # preferences form only 2-cycles in every round
   agentPreferences = {
      'a': [1,2,3,4,5,6],
      'b': [1,2,3,4,5,6],
      'c': [1,2,3,4,5,6],
      'd': [1,2,3,4,5,6],
      'e': [1,2,3,4,5,6],
      'f': [1,2,3,4,5,6],
   }
   initialOwnership = {1:'a', 2:'b', 3:'c', 4:'d',5:'e',6:'f'}
   test({'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6},
      topTradingCycles(agents, houses, agentPreferences, initialOwnership))

   # top three preferences of d,e,f are removed in the first cycle
   agentPreferences = {
      'a': [2,1,3,4,5,6],
      'b': [3,2,1,4,5,6],
      'c': [1,2,3,4,5,6],
      'd': [1,2,3,4,5,6],
      'e': [1,2,3,4,5,6],
      'f': [1,2,3,4,5,6],
   }
   initialOwnership = {1:'a', 2:'b', 3:'c', 4:'d',5:'e',6:'f'}
   test({'a': 2, 'b':3, 'c':1, 'd':4, 'e':5, 'f':6},
      topTradingCycles(agents, houses, agentPreferences, initialOwnership))
