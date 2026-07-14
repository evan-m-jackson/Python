def render_template(template: str, context: dict) -> str:
    """Render a template string by substituting ${expr} with evaluated expressions.

    >>> render_template("Hello ${name}", {"name": "'World'"})
    'Hello World'
    """
    import re

    def replace(match):
        expr = match.group(1)
        return str(eval(expr, context))

    return re.sub(r"\$\{(.*?)\}", replace, template)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
