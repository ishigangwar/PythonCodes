def wrap(string, max_width):
    wrapped = textwrap.wrap(string, width=max_width)
    return "\n".join(wrapped)