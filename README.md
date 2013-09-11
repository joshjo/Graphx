Graphx
=========

Graphx is a graph implemented on Python. 

Installation
----------

```sh
git clone git@github.com:joshjo/Graphx.git
cd Graphx
python setup.py install
```

Use
----------
#### Create a simple graph
```sh
g = Graphx()
```
It creates a digraph. 

If you wish a directed graph:
```sh
g = Graphx(is_directed = True)
```
It's nice :D

#### Adding nodes
You can add nodes in 2 ways. Giving a the data of the node.
```sh
node_a = g.add_node('a')
```
As you can see it returns a Node instance wich is the second way of adding a node.

```sh
node_b = Node('b')
g.add_node(node_b, by_data = False)
```
If you hace a list of data you can insert directly using:
```sh
my_list = ['a', 'b', 'c', 'd']
g.add_nodes_from_list(my_list)
```

#### Adding edges
Just give the data of the begin and end Nodes.
```sh
g.add_edge('a', 'b', distance = 3)
```
Again, you can add edges giving nodes instance.
```sh
g.add_edge(node_a, node_b, distance = 3, by_data = False)
```

There are two extra functions meanwhile.
### Minimal Search Tree
Simple as:
```sh
g.MST()
```
It returns completely a new Graphx instance.

### Make the graph full connected
```sh
g.make_full_connected()
```
It uses the Prim algortihm.

