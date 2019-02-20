import snap

# print extended statistics to file 'info-pngraph.txt'
Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
snap.PrintInfo(Graph, "Python type PNGraph", "info-pngraph.txt", False)

# print basic statistics to file 'info-pungraph.txt'
UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
snap.PrintInfo(UGraph, "Python type PUNGraph", "info-pungraph.txt")

# print basic statistics to standard output
Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
snap.PrintInfo(Network, "Python type PNEANet")