import json
import tracery
from tracery.modifiers import base_english


def listify(descriptions):
    desc = []
    final = len(descriptions) - 1
    for i, d in enumerate(descriptions):
        if not d.strip():  # whitespace, e.g. paragraph sep.
            desc.append(d)
            i -= 1
        elif i == 0:
            desc.append(f'First there appears {d}.')
        elif i == 1:
            desc.append(f'This is followed by {d}.')
        elif i == final:
            desc.append(f'Finally, {d}.')
        elif (i & 8) and (i & 1):  # pretty arbitrary logic, experiment
            desc.append(f'Next, {d}.')
        else:
            desc.append(f'Then {d}.')
    return desc


class Describer:
    def __init__(self, data_file):
        with open(data_file) as f:
            self.rules = json.load(f)
        self.grammar = tracery.Grammar(self.rules)
        self.grammar.add_modifiers(base_english)

    def letter(self, c):
        if ord(c) == 10:
            c = 'newline'
        elif c == ' ':
            c = 'gap'
        elif c == '.':
            c = 'period'
        elif c == '"':
            c = 'quotes'
        if c in self.rules:
            return self.grammar.flatten(f'#{c}#')
        raise Exception(f'MISSING LETTER: "{c}" = {ord(c) if len(c) == 1 else c}')
        return f"a description of the shape of the letter '{c}'"


def describe(text):
    """
    Describe the letterforms of text.
    Input: text, a list of sentences.
    Returns: a list of sentences.
    """
    # https://www.infor.uva.es/~descuder/docencia/IG/letterform_anatomy.pdf
    letter_rules = 'data/letters.json'
    describe = Describer(letter_rules)

    output = []
    for s in text:
        for c in s:
            output.append(describe.letter(c))
            if c == '\n':  # add paragraph break after each sentenece has been described
                output.append('\n\n')
    return listify(output)

