A simple graph with basic functions.
To initialize a graph
g = Graph()

You can add nodes whith
node_a = g.add_node('a')

If you have a list of nodes 
g.add_nodes_from_list(['a', 'b', 'c'])

A simple function to make the graph full connected. The parameter fun is a simple function that has to return a float value.
g.make_full_connected(fun = lambda x, y: abs(x + y))

If you need the minimal search tree just do:
g.MST()
It returns a new graph
