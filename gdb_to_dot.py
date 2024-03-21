import sys
import subprocess
from parse_backtrace import parse_backtrace


def subgraph_to_dot(graph, node, hide_until_func, dot_code, visited=None, show=False):
    if visited is None:
        visited = set()

    visited.add(node)

    if not hide_until_func or node == hide_until_func:
        show = True

    for neighbor in graph[node]:
        if show:
            dot_code.append(f'    "{node}" -> "{neighbor}"\n')
        if neighbor not in visited:
            subgraph_to_dot(graph, neighbor, hide_until_func, dot_code, visited, show)


def generate_dot_tree(frames, graph, roots, hide_until_func):
    dot_code = ["digraph Backtrace {\n"]
    dot_code.append("    node [shape=box]\n")

    if len(frames) > 0:
        if frames[0] not in graph:
            graph[frames[0]] = []

        for i in range(len(frames) - 1):
            if frames[i+1] not in graph:
                graph[frames[i+1]] = []
            if frames[i] not in graph[frames[i+1]]:
                graph[frames[i+1]].append(frames[i])

        roots.add(frames[-1])

    for root in roots:
        subgraph_to_dot(graph, root, hide_until_func, dot_code)

    dot_code.append("}")
    return ''.join(dot_code)


def convert_backtrace_to_dot(backtrace, graph, roots, hide_until_func):
    frames = parse_backtrace(backtrace)
    dot_tree = generate_dot_tree(frames, graph, roots, hide_until_func)
    return dot_tree


def save_dot_to_png(dot_code, output_file):
    with open(output_file + ".dot", "w") as dot_file:
        dot_file.write(dot_code)
    subprocess.run(["dot", "-Tpng", output_file + ".dot", "-o", output_file + ".png"])
    print(f"Backtrace saved as DOT: {output_file}.dot")
    print(f"Backtrace converted to PNG: {output_file}.png")


def process_backtrace(backtrace, graph, roots, hide_until_func):
    dot_tree = convert_backtrace_to_dot(backtrace, graph, roots, hide_until_func)
    output_file = "backtrace"
    save_dot_to_png(dot_tree, output_file)


if __name__ == "__main__":
    backtrace = ""
    graph = {}
    roots = set()
    hide_until_func = None

    for line in sys.stdin:
        if line.strip() == "UNHIDE":
            hide_until_func = None
            process_backtrace(backtrace, graph, roots, hide_until_func)
        if line.startswith("HIDE UNTIL"):
            hide_until_func = line.split(" ", 2)[2].strip()
            process_backtrace(backtrace, graph, roots, hide_until_func)
        elif line.strip() == "BREAK" or line == "":
            process_backtrace(backtrace, graph, roots, hide_until_func)
            backtrace = ""
        else:
            backtrace += line

    # Process any remaining backtrace after end of input
    if backtrace:
        process_backtrace(backtrace, graph, hide_until_func)
