import sys
import subprocess
from parse_backtrace import parse_backtrace


def generate_dot_tree(frames, edges):
    dot_code = "digraph Backtrace {\n"
    dot_code += "    node [shape=box]\n"

    for i in range(len(frames) - 1):
        edges.add(f'    "{frames[i+1]}" -> "{frames[i]}"\n')

    for edge in edges:
        dot_code += edge

    dot_code += "}"
    return dot_code


def convert_backtrace_to_dot(backtrace, edges):
    frames = parse_backtrace(backtrace)
    dot_tree = generate_dot_tree(frames, edges)
    return dot_tree


def save_dot_to_png(dot_code, output_file):
    with open(output_file + ".dot", "w") as dot_file:
        dot_file.write(dot_code)
    subprocess.run(["dot", "-Tpng", output_file + ".dot", "-o", output_file + ".png"])
    print(f"Backtrace converted to PNG: {output_file}.png")


def process_backtrace(backtrace, edges):
    dot_tree = convert_backtrace_to_dot(backtrace, edges)
    output_file = "backtrace"
    save_dot_to_png(dot_tree, output_file)


if __name__ == "__main__":
    backtrace = ""
    edges = set()
    for line in sys.stdin:
        if line.strip() == "BREAK" or line == "":
            if backtrace:
                process_backtrace(backtrace, edges)
                backtrace = ""
        else:
            backtrace += line

    # Process any remaining backtrace after end of input
    if backtrace:
        process_backtrace(backtrace, edges)
