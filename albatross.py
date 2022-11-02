#!/usr/bin/env python3

import re
import subprocess
import sys

from albatross.reader import Reader
from albatross.plot import J1, J2


TITLE = "Perspective of an Albatross"
NL = '\n'

PNUM = re.compile(r'\d+$|CHAPTER 1$')

class Book():
    def __init__(self, title):
        self.title = title
        self.chapters = {}
        self.pdf = 'output.pdf'

    def append(self, chapter, content):
        """Append content to chapter"""
        if chapter in self.chapters:
            self.chapters[chapter].append(content)
        else:
            self.chapters[chapter] = [content]

    def get_page(self, n):
        """Returns the text of page n."""
        # TODO: memoise pages
        # Save current book state to pdf and convert to txt to determine current page breaks...
        self.to_pdf()
        subprocess.run(['pdftotext', self.pdf, 'pdf.txt'], capture_output=True)
        pages = []
        pb = ''
        with open('pdf.txt', 'r') as f:
            for line in f:
                line = line.lstrip()
                if not line:
                    continue
                if PNUM.match(line):  # page number found
                    pages.append(pb)
                    pb = ''
                else:
                    pb += line
        p = pages[n]
        return p

    def show(self):
        """Ouput Book to STDOUT."""
        print(self.to_markdown())

    def to_markdown(self):
        output = [f'# {self.title}',
            '\\pagenumbering{gobble}']
        for k, c in self.chapters.items():
            output.append('\\newpage')
            output.append(f'\n## CHAPTER {k}\n\n')
            if k == 1:
                output += ['\\newpage', '\\pagenumbering{arabic}']
            output += c
        return NL.join(output)

    def to_pdf(self):
         md = self.to_markdown()
         with open('output.md', 'w') as f:
             f.write(md)
         subprocess.run(['pandoc', 'output.md', '-o', self.pdf], capture_output=True)


def get_sentences(text, n):
    # TODO: refactor!!!
    return NL.join(text.split(NL)[:n])


def test_book_get(book):
    # TODO: refactor!!!
    TA = 6
    TB = 9

    a = f"The first letter on page 1 of this book is '{book.get_page(1)[0]}'."
    n = 2
    c = book.get_page(2)[0]
    b = f"The first letter on page {n} of this book is '{c}'."
    d = book.get_page(7).split(NL)[3].replace(' ', '')[5]
    tc3 = f"The fifth letter of the third line on page 7 is '{d}'."
    book.append(TB, a)
    book.append(TB, b)
    book.append(TB, tc3)
    book.append(TA, f'''From flicking through the pages earlier, the reader had noticed that chapter {TB} starts with a number of statements about specific letters located throughout the book.
The first was that "{a}".
This appears to be correct.
Then "{b}".
Glancing at the facing page, this too is verified as correct.
"{tc3}; flicking forward {7-1} pages, the reader finds that the fifth letter of the third line is indeed '{d}'.
    ''')


def story(seedfile):
    with open(fname, 'r') as f:
        start = f.read()

    reader = Reader()
    book = Book(TITLE)
    book.append(1, start)
    for i in range(2, 13):
        book.append(i, f'[placeholder chapter {i} start text]\n')

    a = reader.read(start, 'first_book')
    b = reader.read(get_sentences(a, 3))
    book.append(1, a)
    book.append(1, b)
    book.append(1, J1)

    c = reader.read(get_sentences(b, 3))
    book.append(1, reader.read(get_sentences(c, 3), 'first_page'))

    book.append(3, c)
    book.append(1, J2)

    test_book_get(book)

    return book


if __name__ == '__main__':
    fname = sys.argv[1]
    book = story(fname)
    book.show()
