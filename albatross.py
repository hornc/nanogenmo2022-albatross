#!/usr/bin/env python3

import sys
#import tracery

TITLE = "Perspective of an Albatross"

class Book():
    def __init__(self, title):
        self.title = title
        self.chapters = {}

    def append(self, chapter, content):
        """Append content to chapter"""
        if chapter in self.chapters:
            self.chapters[chapter].append(content)
        else:
            self.chapters[chapter] = [content]

    def show(self):
        """Ouput Book to STDOUT."""
        print(self.title, '\n')
        for k, c in self.chapters.items():
            print(f'CHAPTER {k}\n')
            print('\n'.join(c))


def article(s):
    aan = 'an' if s[0].lower() in 'aeiou' else 'a'
    return f'{aan} {s}'


def letter(c, adj='next', loc=''):
    if c == '\n':
        return c * 2
    if c in "'i_":
        return ''
    if c == ' ':
        return 'Then there is a space.'
    if c == '.':
        return 'Then there is a period, ending the current sentence.\n\n'
    if c == ',':
        return 'Then there is a comma.'
    if c == ':':
        return 'Then there is a colon.'
    ccase = 'capital' if c.isupper() else 'lowercase'
    cc = f"{ccase} '{c}'"
    if loc:
        loc += ' '
    return f'The {adj} letter encountered {loc}is {article(cc)}.'


def read(text):
    """Reader reads text."""
    output = []
    first = letter(text[0], 'first', 'on the page')
    output.append(first)
    for c in text[1:]:
        a = letter(c)
        if a:
            output.append(a)
    return ' '.join(output)


def story(seedfile):
    with open(fname, 'r') as f:
        start = f.read()

    book = Book(TITLE)
    book.append(1, start)
    a = read(start)
    b = read(a)
    book.append(1, a)
    book.append(1, b)
    return book


if __name__ == '__main__':
    fname = sys.argv[1]
    book = story(fname)
    book.show()
