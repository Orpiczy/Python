#!/usr/bin/python
# -*- coding: utf-8 -*-

=nx.from_numpy_matrix(AdjecentMatrix)
G=nx.DiGraph(G,directed=True)
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if 4 < d['weight']]
emedium = [(u, v) for (u, v, d) in G.edges(data=True) if 2 < d['weight'] <=4]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <=2 ]
#
pos = nx.spring_layout(G)  # positions for all nodes
#
nx.draw_networkx_nodes(G, pos, node_size=400)

#
nx.draw_networkx_edges(G, pos, edgelist=elarge,width=1)
nx.draw_networkx_edges(G, pos, edgelist=emedium, width=1)
nx.draw_networkx_edges(G, pos, edgelist=esmall,width=1)


# labels
labels={}
for i in range(14):
    labels[i]=i+1
nx.draw_networkx_labels(G,pos,labels,font_size=16)



options = {
    'node_color': 'blue',
    'node_size': 100,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 12,
}
nx.draw_networkx(G,pos,with_labels=False,**options)
plt.show()
# plt.savefig("Graph14.png") # save as png
#  # display

