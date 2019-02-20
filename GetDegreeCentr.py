import snap

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
for NI in UGraph.Nodes():
    DegCentr = snap.GetDegreeCentr(UGraph, NI.GetId())
    print "node: %d centrality: %f" % (NI.GetId(), DegCentr)