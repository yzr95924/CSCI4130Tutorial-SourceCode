import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
snap.PlotShortPathDistr(Graph, "example", "Directed graph - shortest path")
snap.DrawGViz(Graph, snap.gvlDot, "graph.png", "graph 1")

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
snap.PlotShortPathDistr(UGraph, "example", "Undirected graph - shortest path")
snap.DrawGViz(UGraph, snap.gvlNeato, "graph_undirected.png", "graph 2", True)

Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
snap.PlotShortPathDistr(Network, "example", "Network - shortest path")