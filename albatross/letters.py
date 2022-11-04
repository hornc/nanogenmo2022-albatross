

def listify(descriptions):
    return [f'Then {d}.' for d in descriptions]


def letter(c):
    return f"a description of the shape of the letter '{c}'"


def describe(text):
    """
    Describe the letterforms of text.
    Input: text, a list of sentences.
    Returns: a list of sentences.
    """
    output = []
    for s in text:
        for c in s:
            output.append(letter(c))
    return listify(output)

