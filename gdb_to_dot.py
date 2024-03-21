import sys
import subprocess
from parse_backtrace import parse_backtrace


class BacktraceProcessor:
    def __init__(self):
        self.graph = {}
        self.roots = set()
        self.hide_until_func = None

    def subgraph_to_dot(self, node, dot_code, visited=None, show=False):
        if visited is None:
            visited = set()

        visited.add(node)

        if not self.hide_until_func or node == self.hide_until_func:
            show = True

        for neighbor in self.graph[node]:
            if show:
                dot_code.append(f'    "{node}" -> "{neighbor}"\n')
            if neighbor not in visited:
                self.subgraph_to_dot(neighbor, dot_code, visited, show)

    def generate_dot_tree(self, frames):
        dot_code = ["digraph Backtrace {\n"]
        dot_code.append("    node [shape=box]\n")

        if len(frames) > 0:
            if frames[0] not in self.graph:
                self.graph[frames[0]] = []

            for i in range(len(frames) - 1):
                if frames[i + 1] not in self.graph:
                    self.graph[frames[i + 1]] = []
                if frames[i] not in self.graph[frames[i + 1]]:
                    self.graph[frames[i + 1]].append(frames[i])

            self.roots.add(frames[-1])

        for root in self.roots:
            self.subgraph_to_dot(root, dot_code)

        dot_code.append("}")
        return "".join(dot_code)

    def convert_backtrace_to_dot(self, backtrace):
        frames = parse_backtrace(backtrace)
        dot_tree = self.generate_dot_tree(frames)
        return dot_tree

    def save_dot_to_png(self, dot_code, output_file):
        with open(output_file + ".dot", "w") as dot_file:
            dot_file.write(dot_code)
        subprocess.run(
            ["dot", "-Tpng", output_file + ".dot", "-o", output_file + ".png"]
        )
        print(f"Backtrace saved as DOT: {output_file}.dot")
        print(f"Backtrace converted to PNG: {output_file}.png")

    def process(self, backtrace):
        dot_tree = self.convert_backtrace_to_dot(backtrace)
        output_file = "backtrace"
        self.save_dot_to_png(dot_tree, output_file)


if __name__ == "__main__":
    backtrace = ""
    processor = BacktraceProcessor()

    for line in sys.stdin:
        if line.strip() == "UNHIDE":
            processor.hide_until_func = None
            processor.process(backtrace)
        if line.startswith("HIDE UNTIL"):
            processor.hide_until_func = line.split(" ", 2)[2].strip()
            processor.process(backtrace)
        elif line.strip() == "BREAK" or line == "":
            processor.process(backtrace)
            backtrace = ""
        else:
            backtrace += line

    processor.process(backtrace)
