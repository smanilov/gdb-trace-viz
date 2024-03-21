import re


def parse_function_name(function_part):
    function_name = ""
    template_bracket_count = 0
    for char in function_part:
        if char == "(":
            if not function_name.endswith("operator") and template_bracket_count == 0:
                break
        elif char == "<":
            template_bracket_count += 1
        elif char == ">":
            template_bracket_count -= 1
        function_name += char
    return function_name.strip()


def parse_backtrace(backtrace):
    frames = []
    for line in backtrace.splitlines():
        match = re.match(r'#\d+\s+(?:0x[a-f0-9]+\s+in )?(.+)', line)
        if match:
            function_part = match.group(1)
            function_name = parse_function_name(function_part)
            frames.append(function_name)
    return frames

