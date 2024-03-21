from parse_backtrace import parse_backtrace


class BacktraceAccumulator:
    """
    Builds a graph by accumulating GDB backtraces. Every time process is called,
    the graph is updated and the .dot (GraphViz) representation is returned.

    Attributes:
        graph (dict): Maps functions to an ordered set (a list) of functions they call.
        roots (set): A set containing the root nodes of the backtrace graph.
        hide_until_func (str): If not None, nodes on the path from a root to
                                this function will not be output.
    """

    def __init__(self):
        self.graph = {}
        self.roots = set()
        self.hide_until_func = None

    def subgraph_to_dot(self, node, dot_code, visited, show=False):
        """
        DFS traversal of the graph starting from node.

        If hide_until_func is not None, only start adding to dot_code once it is
        encountered on the traversal.
        """
        visited.add(node)

        if not self.hide_until_func or node == self.hide_until_func:
            show = True

        for neighbor in self.graph[node]:
            if show:
                dot_code.append(f'    "{node}" -> "{neighbor}"\n')
            if neighbor not in visited:
                self.subgraph_to_dot(neighbor, dot_code, visited, show)

    def update_graph(self, frames):
        """
        Add frames to internal graph.

        Assumes the frames are in reverse calling order, i.e. main is last, e.g.

        If a node already contains a neighbor, it is not added again. This
        preserves the order of adding backtraces, but not completely...
        """
        if len(frames) == 0:
            return

        self.roots.add(frames[-1])

        if frames[0] not in self.graph:
            self.graph[frames[0]] = []

        for i in range(len(frames) - 1):
            if frames[i + 1] not in self.graph:
                self.graph[frames[i + 1]] = []
            if frames[i] not in self.graph[frames[i + 1]]:
                self.graph[frames[i + 1]].append(frames[i])

    def generate_dot_code(self, frames):
        self.update_graph(frames)

        dot_code = ["digraph Backtrace {\n"]
        dot_code.append("    node [shape=box]\n")

        visited = set()
        for root in self.roots:
            self.subgraph_to_dot(root, dot_code, visited)

        dot_code.append("}")
        return "".join(dot_code)

    def process(self, backtrace):
        frames = parse_backtrace(backtrace)
        dot_code = self.generate_dot_code(frames)
        return dot_code
