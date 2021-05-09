import networkx as nx

def graph_twisted_torus(G,x,y,shift):
    G.clear()
    G = nx.grid_2d_graph(x, y, periodic=False, create_using=None)       #simple 2D graph without wraparound
    for row in range(y):
        for col in range(x):
            G.add_edge((col,row),(((col+1)%x),row))              #connect to next column
            if row != y-1:
                G.add_edge((col,row),(col,(row+1)%y))               #connect to next row except for last row
            else:
                G.add_edge((col,row),((col-shift)%x,(row+1)%y))     #connect to next row but shifted column for last row
    return G

# def graph_4_connected(G,x,y):
#     G.clear()
#     G = nx.grid_2d_graph(x,y,periodic = False,create_using = None)
#     for row in range(y):
#         for col in range(x):
#             G.add_edge((col,row),((col+1)%x,row))   #connect to the next column
#             if row !=y-1:
#                 G.add_edge((col,row),(col,(row+1)%y))    #connect to the pixel below except for the last pixel
#             # this completes adding the edges since the edges are bidirectional and we have already added edges
#             # to pixels on the left and on top
#     return G

# def graph_8_connected(G,x,y):
#     G.clear()
#     G = nx.grid_2d_graph(x,y,periodic = False,create_using = None)
#     for row in range(y):
#         for col in range(x):
#             G.add_edge((col,row),((col+1)%x,row))   #coonect to the next column
#             if row !=y-1:
#                 G.add_edge((col,row),(col,(row+1)%y))    #connect to the pixel below except for the last pixel
#             # this completes adding the edges since the edges are bidirectional and we have already added edges
#             # to pixels on the left and on top
#     return G