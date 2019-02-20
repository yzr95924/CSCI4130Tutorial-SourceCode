import snap

Graph = snap.GenTree(snap.PNGraph, 3, 3)
[is_tree, root_id] = snap.IsTree(Graph)
print "The graph is a tree: %s " % is_tree
print "The graph has a root id: %d" % root_id

Network = snap.GenTree(snap.PNEANet, 3, 3)
[is_tree, root_id] = snap.IsTree(Network)
print "The graph is a tree: %s " % is_tree
print "The graph has a root id: %d" % root_id