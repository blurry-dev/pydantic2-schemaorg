import jinja2

jinja_env = jinja2.Environment(keep_trailing_newline=True)


# jinja2 filter format long descriptions from schema.org
def format_description(_input: str, max_width=88):
    formatted_input = _input.replace('"', '\\"')
    lines: list[list[str]] = [[]]
    splitted_input: list[str] = formatted_input.split()
    cursor, word_cursor = 0, 0
    # word wrap
    while word_cursor < len(splitted_input):
        if cursor > max_width:
            lines.append([])
            cursor = 0
        lines[-1].append(splitted_input[word_cursor])
        cursor += len(splitted_input[word_cursor])
        word_cursor += 1

    return " ".join([" ".join(line) for line in lines])


# jinja2 filter format long descriptions from schema.org as docstrings
def format_docstring(_input: str, max_width=88):
    formatted_input = _input.replace('"', '\\"')
    lines: list[list[str]] = [[]]
    splitted_input: list[str] = formatted_input.split()
    cursor, word_cursor = 0, 0
    # word wrap
    while word_cursor < len(splitted_input):
        if cursor > max_width:
            lines.append([])
            cursor = 0
        lines[-1].append(splitted_input[word_cursor])
        cursor += len(splitted_input[word_cursor])
        word_cursor += 1

    return "\n     ".join([" ".join(line) for line in lines])


# jinja2 filter format long descriptions from schema.org
def python_safe(_input: str):
    if _input in {"class", "def", "from", "import", "return", "yield"}:
        return f"{_input}_"
    elif _input[0].isdigit():
        return f"_{_input}"
    else:
        return _input


jinja_env.filters["format_description"] = format_description
jinja_env.filters["format_docstring"] = format_docstring
jinja_env.filters["python_safe"] = python_safe
