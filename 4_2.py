class graph:
    def __init__(self, graph):
        self.graph = graph

    def are_nodes_connected(self, n1, n2):
        return (self.direct_path(n1, n2, []) or self.direct_path(n2, n1, []))

    def direct_path(self, n1, n2, travelled=[]):
        if n1 is n2:
            return True
        for node in self.graph[n1]:
            print node
            print travelled
            if node not in travelled:
                travelled.append(node)
                connected = self.direct_path(node, n2, travelled)
                if connected:
                    return True
            else:
                print "already travelled"
        return False


def main():
    graph_dictionary = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }

    my_graph = graph(graph_dictionary)

    # print my_graph.are_nodes_connected('A', 'A')  # true
    # print my_graph.are_nodes_connected('A', 'D')  # true
    # print my_graph.are_nodes_connected('A', 'E')  # false
    # print my_graph.are_nodes_connected('F', 'C')  # true
    print my_graph.are_nodes_connected('C', 'F')  # true

main()
