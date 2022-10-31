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


def read(text):
    """Reader reads text."""
    return text


def story(seedfile):
    with open(fname, 'r') as f:
        start = f.read()

    book = Book(TITLE)
    book.append(1, start)
    book.append(1, read(start))
    return book


if __name__ == '__main__':
    fname = sys.argv[1]
    book = story(fname)
    book.show()
