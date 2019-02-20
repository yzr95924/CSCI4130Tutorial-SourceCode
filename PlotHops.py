import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
snap.PlotHops(Graph, "example", "Directed graph - hops", True, 1024)

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
snap.PlotHops(UGraph, "example", "Undirected graph - hops", False, 1024)

Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
snap.PlotHops(Network, "example", "Network - hops", True, 1024)