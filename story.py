#!/usr/bin/env python3

import re
import subprocess
import sys

from albatross.reader import Reader
from albatross.plot import (J1, J2, Q1, Q2,
    TEST_LETTERS, EOCH1, SOCH2, EOCH2,
    SOCH3, CEDILLA, FEATURES,
    engraving_caption, ENGRAVING, ENGRAVING_TEST,
)


#TITLE = "Perspective of an Albatross"
TITLE = 'An Unfinished Novel of {wordcount} Words'
NL = '\n'
PAR = NL * 2

PNUM = re.compile(r'\d+$|CHAPTER 1$')
CHEAD = re.compile(r'CHAPTER \d+$')
NONALPHA = re.compile(r'[\W_]+')


class Book():
    def __init__(self, title):
        self.title = title
        self.chapters = {}
        self.pdf = 'output.pdf'
        self._pages = None

    def append(self, chapter, content):
        """Append content to chapter"""
        if chapter in self.chapters:
            self.chapters[chapter].append(content)
        else:
            self.chapters[chapter] = [content]

    def count(self):
        return len(self.to_markdown().split())

    @property
    def pages(self):
        if self._pages:
            return self._pages
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
        self._pages = pages
        return self._pages

    def get_page(self, n, line_no=None, letter=None):
        """
        Returns the text of page n.
        Or a specific line number,
        or a character in that line.
        """
        if line_no:
            line_no -= 1 if line_no > 0 else 0
            try:
                lines = [line for line in self.pages[n].split(NL) if line and not CHEAD.match(line)]
                line = lines[line_no]
                if letter:
                    letter -= 1 if letter > 0 else 0
                    return NONALPHA.sub('', line)[letter]
                else:
                    return line
            except IndexError as e:
                return "CURRENTLY EMPTY"
        return self.pages[n]

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

    def wc_chapters(self):
        counts = []
        for chapter in self.chapters:
            counts.append(len(' '.join(self.chapters[chapter]).split()))
        return counts


def get_sentences(text, n):
    # TODO: re-locate!!!
    return NL.join(text.split(NL)[:n])


def ordinal(n):
    if n == -1:
        return 'last'
    ords = ['zeroth', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    if n < -1:
        return f'{ords[abs(n)]} to last'
    if n == 20:
        return 'twentieth'
    if n > len(ords):
        return f'{n}th'
    return ords[n]


def quote(s):
    output = []
    for b in s.split(NL*2):
        output.append(f'> {b}')
    return PAR.join(output)


def tc(book, p, line, letter):
    """Generate test case results."""
    r = book.get_page(p, line, letter)
    if line == 1 and letter > 0:
        loc = f"on page {p} of this book"
    else:
        loc = f"of the {ordinal(line)} line on page {p}"
    return f"The {ordinal(letter)} letter {loc} is '{r}'."


def test_book_get(book):
    # TODO: re-locate!
    TA, TB = 6, 9
    cases = [
        (1, 1, 1),
        (2, 1, 1),
        (7, 2, 5),
        (7, -1, -1),
        (7, -1, -2),
        (7, -2, -1),
        (7, 1, -1),
        (10, 10, 10),
        (11, 10, 10),
        (21, -3, 10),
        (4, 20, 20),
        (5, 20, 20),
        (6, 20, 20),
        (7, 20, 20),
        (8, -1, -1),
        (23, -1, -1),  # tests off from here
        (41, -1, -1),
        (42, -1, -1),
        (43, -1, -1),
    ]
    statements = []
    for c in cases:
        r = tc(book, *c)
        statements.append(r.strip('.'))
        book.append(TB, r)
    result = book.get_page(*cases[2])
    content = TEST_LETTERS.format(
            chapter=TB,
            statements=statements,
            pages=cases[2][0] - 1,
            result=result)
    book.append(TA, content)


def story(seedfile):
    with open(seedfile, 'r') as f:
        start = f.read()

    reader = Reader()
    book = Book(TITLE)
    book.append(1, start)
    for i in range(2, 11):
        book.append(i, NL)

    a = reader.read(start, 'first_book')
    b = reader.read(get_sentences(a, 3))
    book.append(1, a)
    book.append(1, b)

    # First jump
    c = reader.read(get_sentences(b, 3))
    cpage = str(23)  # chapter 3 page number
    book.append(1, J1.replace('%%300%%', cpage))
    book.append(1, reader.read(get_sentences(c, 3), 'first_page'))

    # Second jump

    d = c  # TODO: make different from c!
    dpage = str(13) # TODO: needs to be looked up
    paragraphs = str(d.count(PAR))
    quote1 = f'{Q2}\n\n{quote(NL.join(d.split(NL)[:30]))}'
    letter_section = reader.describe_letters(b[:900])  # TODO: choose source!
    quote2 = letter_section[:3000] + '...'
    book.append(7, f'{Q1}{Q2}{PAR}{d}{letter_section}')
    section = J2.replace('%%QUOTE1%%', quote1).replace('%%paragraph%%', paragraphs).replace('%%700%%', dpage).replace('%%QUOTE2%%', quote2)
    book.append(1, section)
    chapter_count = len(book.chapters)
    chapter_count = 'ten'  # TODO: use num2words
    book.append(1, EOCH1.format(chapters=chapter_count))

    # Chapter 2
    content = SOCH2.format(chapters=chapter_count)
    ch2_read = reader.read(content.strip())
    content += ch2_read
    book.append(2, content)
    letters = ' - '.join(NONALPHA.sub('', ch2_read))
    book.append(2, EOCH2.format(letters=letters, letter_shapes=reader.describe_letters(content[:500].strip())))

    variables = {
        'cedilla_page': '??',
        'cedilla_count': '??',
        'cedilla_word': 'façade',
        'engraving_caption': engraving_caption,
        'engraving_page': 28,
        'title': TITLE,
        'test_chapter': 9,
    }

    # Chapter 3
    book.append(3, SOCH3)
    c = reader.read(NL.join(SOCH3.split(NL)[15:]))
    book.append(3, c)  # from ch.2
    book.append(3, FEATURES.format(**variables))

    # Chapter 8
    book.append(8, CEDILLA.format(**variables))

    # Insert stucture view test cases and commentary
    test_book_get(book)

    book.append(6, ENGRAVING.format(**variables))
    book.append(9, ENGRAVING_TEST.format(**variables))

    # re-set title:
    book.title = TITLE.format(wordcount=book.count())
    return book


if __name__ == '__main__':
    fname = sys.argv[1]
    book = story(fname)
    book.show()
