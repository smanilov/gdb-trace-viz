import sys
import subprocess

from backtrace_accumulator import BacktraceAccumulator


def save_dot_to_png(dot_code):
    output_file = "backtrace"
    with open(output_file + ".dot", "w") as dot_file:
        dot_file.write(dot_code)
    subprocess.run(["dot", "-Tpng", output_file + ".dot", "-o", output_file + ".png"])
    print(f"Backtrace saved as DOT: {output_file}.dot")
    print(f"Backtrace converted to PNG: {output_file}.png")


def process_and_output_png(backtrace, accumulator):
    dot_code = accumulator.process(backtrace)
    save_dot_to_png(dot_code)


if __name__ == "__main__":
    backtrace = ""
    accumulator = BacktraceAccumulator()

    for line in sys.stdin:
        if line.strip() == "UNHIDE":
            accumulator.hide_until_func = None
            process_and_output_png(backtrace, accumulator)
        if line.startswith("HIDE UNTIL"):
            accumulator.hide_until_func = line.split(" ", 2)[2].strip()
            process_and_output_png(backtrace, accumulator)
        elif line.strip() == "BREAK" or line == "":
            process_and_output_png(backtrace, accumulator)
            backtrace = ""
        else:
            backtrace += line

    accumulator.process(backtrace)
