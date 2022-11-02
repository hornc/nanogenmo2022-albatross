#!/usr/bin/env python3

import sys

from albatross.reader import Reader
from albatross.plot import J1, J2


TITLE = "Perspective of an Albatross"
NL = '\n'


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

def get_sentences(text, n):
    return NL.join(text.split(NL)[:n])


def story(seedfile):
    with open(fname, 'r') as f:
        start = f.read()

    reader = Reader()
    book = Book(TITLE)
    book.append(1, start)
    a = reader.read(start, 'first_book')
    b = reader.read(get_sentences(a, 3))
    book.append(1, a)
    book.append(1, b)
    book.append(1, J1)
    book.append(1, J2)

    book.append(2, '{placeholder}')
    book.append(3, '{placeholder}')
    book.append(4, '{placeholder}')
    return book


if __name__ == '__main__':
    fname = sys.argv[1]
    book = story(fname)
    book.show()
