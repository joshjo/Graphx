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

```sh
node_b = Node('b')
g.add_node(node_b, by_data = False)
```

#### Adding edges
Just give the data of the begin and end Nodes.
```sh
g.add_edge(3, 'a', 'b')
```
It add an edge from node 'a' to node 'b' with a distance 3.
You can be more explicit and do:
```sh
g.add_edge(distance = 3, from_node = 'a', to_node = 'b')

## There are three extra functions meanwhile.
### Minimal Spanning Tree MST
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

### k best distances
```sh
g.make_knn(k = 3)
```
It modifies the graph and return the k best distances.
