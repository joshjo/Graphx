from random import random, choice, randint
from copy import copy
from collections import deque, Counter

class Node(object):
	def __init__ (self, data):
		self.data = data
		self.edges = set()

	def __repr__ (self):
		return str (self.data)

	def __cmp__ (self, other):
		if type (other) == Node:
			return cmp(self.data, other.data)
		else:
			raise TypeError("Node cannot be compared to %s" % str(type(other)))

	def __eq__(self, other): 
		if type(other) == Node and cmp(self.data, other.data) == 0:
			return True
		return False

	def __ne__ (self, other):
			return not self.__eq__(other)


	def __hash__ (self):
		return hash(self.data)

class Edge(object):
	def __init__ (self, from_node, to_node, data):
		self.data = data
		self.from_node = from_node
		self.to_node = to_node

	def __cmp__ (self, other):		
		if self.data < other.data: return -1
		if self.data == other.data: return 0
		return 1

	def __repr__ (self):
		return "| data: " + str (self.data) + ", from node: " +  str (self.from_node.data) + ", to node: " + str (self.to_node.data) + " |"

	def __hash__ (self):
		return hash(self.from_node) ^ hash(self.data) ^ hash(self.to_node)

class Graphx(object):
	def __init__ (self, is_directed = False):
		self.edges = set()
		self.nodes = set()
		self.graph = {}
		self.is_directed = is_directed

	def add_edge (self, from_node, to_node, distance = 0, by_data = True):
		if by_data:
			from_node = self.find_node(from_node)			
			to_node = self.find_node(to_node)
		if from_node is None or to_node is None:			
			return False
		new_edge = Edge(from_node, to_node, distance)
		from_node.edges.add (new_edge)
		self.edges.add (new_edge)
		if self.is_directed is False:
			other_edge = Edge(to_node, from_node, distance)
			to_node.edges.add(other_edge)
			self.edges.add (other_edge)
		return True

	def add_node (self, data, by_data = True):
		if by_data:
			node = Node (data)
			self.nodes.add ( node )
			return node
		else:
			self.nodes.add (data)
			return data

	def add_nodes_from_list (self, L):
		for node in L:
			self.add_node (node)

	def get_best_path (self, begin, target):
		begin_node = self.find_node(begin)
		target_node = self.find_node(target)
		if begin_node == None or target_node == None:
			raise BaseException("Begin or target node doesn't exist.")
		matrix = {}		
		for i_node in self.nodes:
			tmp = {}
			for j_node in self.nodes:
				tmp[j_node] = float ("inf")
			matrix[i_node] = tmp

		for edge in self.edges:
			print edge
		# 	matrix[edge.from_node][edge.to_node] = edge.data
		# 	matrix[edge.to_node][edge.from_node] = edge.data

		# for i_node in self.nodes:
		# 	for j_node in self.nodes:
		# 		for k_node in self.nodes:
		# 			dt = matrix[i_node][j_node] + matrix[k_node][j_node]
		# 			print dt
		# 			if matrix[i_node][j_node] > dt:
		# 				matrix[i_node][j_node] = dt

		print matrix

	def find_node (self, node, by_data = True):
		for n in self.nodes:
			if by_data:
				if n.data == node: return n
			else:
				if n == node: return n
		return None

	def make_full_connected (self, fun = None):
		if len(self.edges) > 0:
			raise BaseException("** Error: Please delete all the edges first")
		elif self.is_directed is True:
			raise BaseException("** Error: Please make it digraf. Set atribute is_directed = False")
		for i_node in self.nodes:
			for j_node in self.nodes:
				if i_node == j_node: continue
				distance = 0 if fun == None else fun(i_node.data, j_node.data)
				self.add_edge(i_node, j_node, by_data = False, distance = distance)

	def MST (self):
		Y = list (self.nodes)
		X = []
		mst = Graphx()
		edges = sorted(list(self.edges))
		x = choice(Y)
		X.append(x), Y.remove(x)
		mst.add_node (x.data)
		while len(Y) > 0:
			for edge in edges:				
				if edge.from_node in X and edge.to_node in Y:
					mst.add_node (edge.to_node.data)
					mst.add_edge (from_node = edge.from_node.data, to_node = edge.to_node.data, distance = edge.data)
					X.append(edge.to_node), Y.remove(edge.to_node), edges.remove(edge)
					break
				elif edge.to_node in X and edge.from_node in Y:
					mst.add_node (edge.from_node.data)
					mst.add_edge (from_node = edge.to_node.data, to_node = edge.from_node.data, distance = edge.data)
					X.append(edge.from_node), Y.remove(edge.from_node), edges.remove(edge)
					break
		return mst

if __name__ == '__main__':
	g = Graphx()
	n1 = g.add_node(1)
	n2 = g.add_node(2)
	n3 = g.add_node(3)
	n4 = g.add_node(4)
	g.make_full_connected(fun = lambda x, y: abs(x - y))
	# print g.nodes
	# print g.edges

	# print type (g)
	# g.get_best_path(1, 2)
	# print g.nodes
	# g.add_edge(from_node = n1, to_node = n2, by_data = False, distance = 0.7)
	# g.add_edge(from_node = n2, to_node = n3, by_data = False, distance = 0.4)
	# g.add_edge(from_node = n2, to_node = n4, by_data = False, distance = 0.6)
	# g.add_edge(from_node = n1, to_node = n4, by_data = False, distance = 0.2)
	# g.add_edge(from_node = n4, to_node = n3, by_data = False, distance = 0.3)
	# print "g.nodes", g.nodes
	# print "g.edges", g.edges
	# print "--------------------- MST -----------------------"
	# mst = g.MST()
	# print "mst.nodes", mst.nodes
	# print "mst.edges", mst.edges
	# print "edges", g.edges
	# print "-----------------------"
	# print "nodes", g.nodes.sort()