from random import random, choice, randint
from collections import Counter

def graph_to_tuple(graph, key = lambda t: t[0]):
	return sorted([ (graph[node][edge], node, edge) for node in graph.keys() for edge in graph[node] ], key = key)

class Graphx:
	def __init__ (self, is_directed = False):
		self.graph = {}
		self.is_directed = is_directed
		self.full_connected = False

	def add_node (self, data):
		self.graph[data] = {}

	def add_edge (self, data, from_node, to_node):
		try:
			tmp1, tmp2 = self.graph[from_node], self.graph[to_node]			
		except:
			raise BaseException("'from_node' or 'to_node' doesn't exist.")
		tmp1.update({to_node:data})
		if not self.is_directed:
			tmp2.update({from_node:data})

	def edges (self): return graph_to_tuple (self.graph)

	def make_full_connected (self, array = [], fun = None):		
		for i in array: self.add_node(i)
		nodes = self.graph.keys()
		for i in nodes:
			for j in nodes:
				if i == j: continue
				distance = 0 if fun == None else fun(i, j)
				self.add_edge(distance, i, j)
		self.full_connected = True

	def make_knn (self, k):
		edges = graph_to_tuple(self.graph, key = lambda t: (t[1], t[0]))
		counter = Counter()
		for edge in edges:			
			if counter[edge[1]] >= k:
				del self.graph[edge[1]][edge[2]]
			counter[edge[1]] += 1

	def MST (self):
		Y = self.graph.keys()
		X = []
		mst = Graphx()
		edges = graph_to_tuple(self.graph)
		x = choice(Y)
		X.append(x), Y.remove(x)
		mst.add_node(x)
		while len(Y) > 0:
			for edge in edges:
				distance, from_node, to_node = edge[0], edge[1], edge[2]
				if (from_node in X) and (to_node in Y):
					mst.add_node (to_node)
					mst.add_edge (distance, from_node, to_node)
					X.append(to_node), Y.remove(to_node), edges.remove(edge)
					break
				elif (to_node in X) and (from_node in Y):
					mst.add_node (from_node)
					mst.add_edge (distance, to_node, from_node)
					X.append(from_node), Y.remove(from_node), edges.remove(edge)
					break
		return mst

	def nodes(self): return self.graph.keys()

if __name__ == '__main__':
	g = Graphx()
	g.graph = {'a': {'c': 0.06392587032381203, 'b': 0.23946025808650429, 'e': 0.06480403414170843, 'd': 0.0026144011652722288}, 'c': {'a': 0.06392587032381203, 'b': 0.24737540127027868, 'e': 0.8635607960307713, 'd': 0.00026374340418100495}, 'b': {'a': 0.23946025808650429, 'c': 0.24737540127027868, 'e': 0.9999847447746708, 'd': 0.5288620496272156}, 'e': {'a': 0.06480403414170843, 'c': 0.8635607960307713, 'b': 0.9999847447746708, 'd': 0.8739299535954806}, 'd': {'a': 0.0026144011652722288, 'c': 0.00026374340418100495, 'b': 0.5288620496272156, 'e': 0.8739299535954806}}
	# g.make_full_connected(array = ['a', 'b', 'c', 'd', 'e'], fun = lambda a,b: random())
	# print graph_to_tuple(g.graph)
	print 'graph', g.graph
	g.make_knn(k = 2)
	print 'knn  ', g.graph


	# mst = g.MST()
	# print 'mst  ', mst.graph
	