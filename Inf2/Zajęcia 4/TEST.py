def load_multigraph_from_file(filename: str):
    file = open(filename, 'r+')
    graph_detail = []
    for each in file:

        if each.isspace():
            continue

        each = each.split()
        each_tuple = ()

        for count, n in enumerate(each):
            if count == 2:
                each_tuple = each_tuple + (float(n),)
                continue
            each_tuple = each_tuple + (int(n),)
        graph_detail.append(each_tuple)

    print(graph_detail)


load_multigraph_from_file('dijkstra_multi_2.dat')