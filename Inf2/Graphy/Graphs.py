#!/usr/bin/python
#-*-coding:utf-8-*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

Infinity=0
AdjecentMatrix=np.matrix(
[[0,2.,0,0,0,0,0,0,0,0,0,0,1.5,0],
[2.5,0,1.,0,0,5.,0,0,0,0,0,0,0,0],
[3.5,0,0,1.5,0,6.5,0,0,0,0,0,0,0,0],
[0,0,0,0,1.,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,4.,0,0,0,0,0,0,0],
[0,0,5.,2.5,0,0,5.,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,6.,0,0,0,0,12.,0],
[0,0,0,9.,0,0,6.5,0,2.,0,3.,0,0,1.5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1.5],
[0,0,0,0,0,0,0,0,3.5,0,0,5.,0,0],
[0,0,0,0,0,4.5,5.,3.5,0,2.,0,5.5,0,0],
[9.5,0,0,0,0,0,0,0,0,5.5,0,0,0,0],
[1.5,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,2.,0,0,0,0],
])


G=nx.from_numpy_matrix(AdjecentMatrix)
G=nx.DiGraph(G,directed=True)
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if 6 < d['weight']]
emedium = [(u, v) for (u, v, d) in G.edges(data=True) if 3 < d['weight'] <=6]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <=3 ]
#
pos = nx.spring_layout(G)  # positions for all nodes
#
#nx.draw_networkx_nodes(G, pos, node_size=300)

#
nx.draw_networkx_edges(G, pos, edgelist=elarge,width=1)
nx.draw_networkx_edges(G, pos, edgelist=emedium, width=0.5)
nx.draw_networkx_edges(G, pos, edgelist=esmall,width=0.25)


# labels
labels={}
for i in range(14):
    labels[i]=i+1
nx.draw_networkx_labels(G,pos,labels,font_size=16)



options = {
    'node_color': 'green',
    'node_size': 400,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 12,
}
nx.draw_networkx(G,pos,with_labels=False,**options)
plt.savefig("Graph14.png") # save as png
plt.show()

#  # display

