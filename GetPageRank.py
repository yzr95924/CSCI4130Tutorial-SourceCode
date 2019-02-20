import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
PRankH = snap.TIntFltH()
snap.GetPageRank(Graph, PRankH)
for item in PRankH:
    print item, PRankH[item]

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
PRankH = snap.TIntFltH()
snap.GetPageRank(UGraph, PRankH)
for item in PRankH:
    print item, PRankH[item]

Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
PRankH = snap.TIntFltH()
snap.GetPageRank(Network, PRankH)
for item in PRankH:
    print item, PRankH[item]