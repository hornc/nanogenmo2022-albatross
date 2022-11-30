import re
from albatross.letters import describe


COMMON_WORDS = ['in', 'is', 'the']
VERBS = ['sits', 'read:']
CONJUNCTIONS = ['and', 'but']
MAX_WS = 4
NL = '\n'
DIGITS = re.compile('[0-9]+')

def article(s):
    if s[0] == "'":  # quoted letter name
        aan = 'an' if s[1].lower() in 'aefhilmnorsux' else 'a'
    else:
        aan = 'an' if s[0].lower() in 'aeiou' else 'a'
    return f'{aan} {s}'


def concat(text_list, sep=' '):
    return sep.join(text_list)


class Reader():
    def __init__(self):
        self.wordstate = 0

    def letter(self, c, adj='next', loc='', ccase='', punct=','):
        if c == '\n':
            return c * 2
        if c == ',':
            return 'Then there is a comma.'
        if c == ':':
            return 'Then there is a colon.'
        if c == '-':
            return 'Then there is a dash.'

        mod = '_' if ccase == 'italicised' else ''
        if ccase:
            ccase += ' '
        cc = f"{ccase}'{mod}{c}{mod}'"
        if loc:
            loc += ' '
        if adj == 'follow':
            r = f'followed by {article(cc)}'
        elif adj == 'then':
            r = f'then {article(cc)}'
        else:
            r = f'The {adj} letter encountered {loc}is {article(cc)}'
        return f'{r}{punct}'

    def word(self, w, adj='next', loc=''):
        #if w == 'reader':
        #    return self.selfref(w, adj, loc)
        w = w.strip('.').strip(',')
        if w in VERBS:
            return self.verb_word(w, adj, loc)
        if w in CONJUNCTIONS:
            return self.conj_word(w, adj, loc)
        if DIGITS.match(w):
            return self.number(w, adj, loc)

        if len(w) == 3 and w[0] == "'":
            # quoted letter
            return self.quoted_letter(w, adj, loc)
        elif len(w) == 1:
            return self.letter(w, adj, loc)
        if self.wordstate == 0:
            return self.spell_word(w, adj, loc)
        elif self.wordstate == 1:
            return self.list_word(w, adj, loc)
        elif self.wordstate == 3:
            return self.read_word(w, adj, loc)

        # default:
        return self.spell_word(w, adj, loc)

    def quoted_letter(self, w, adj='next', loc=''):
        w = f'capital {w}' if w.upper() == w else w
        return f'This is followed by {article(w)} enclosed in single quotation marks.'

    def number(self, w, adj='next', loc=''):
        w = DIGITS.match(w).group(0)
        d = 'single' if len(w) == 1 else len(w)
        return f"This is followed by the {d} digit number '{w}'."

    def spell_word(self, w, adj='next', loc=''):
        output = []
        case_last = None
        italics = False
        if '_' in w:
            w = w.replace('_', '')  # handle italics
            italics = True
        l = len(w)
        punct = ','
        for i, c in enumerate(w):
            if i == l - 1:
                adj = 'then'
                punct = '.'
            ccase = 'capital' if c.isupper() else 'lowercase'
            if ccase == case_last:
                ccase = ''
            else:
                case_last = ccase
            if italics:
                ccase = 'italicised'
            a = self.letter(c, adj, loc, ccase, punct)
            adj = 'follow'
            output.append(a)
        comment = self.comment(w)
        if comment:
            output.append(comment)
        return concat(output)

    def list_word(self, w, adj='next', loc=''):
        if not w:
            return ''
        output = []
        if w[0] == '_':
            form = ' in italics'
            w = w.strip('_')
            mod = '_'
        else:
            mod = ''
            form = ''
        output.append(f'{adj.capitalize()} there is a space followed by a new word{form}:')
        for c in w:
            output.append(f"'{mod}{c}{mod}' -")
        comment = self.comment(w)
        if comment:
            output.append(comment)
        return concat(output)

    def read_word(self, w, adj='next', loc=''):
        output = []
        mod = '_' if w.lower() == 'next' else ''  # emphasise next == next
        output.append(f"The next word {mod}is{mod} '{w}'.")
        output.append(self.comment(w))
        return concat(output)

    def conj_word(self, w, adj='next', loc=''):
        return  f"The next word is a conjunction: '{w}'."

    def verb_word(self, w, adj='next', loc=''):
        output = []
        output.append(f"The next word is a verb: '{w}'.")
        if w.startswith('read'):
            recent = 0
        else:
            recent = 1
        output.append(self.verb_comment(w, recent))
        return concat(output)

    def comment(self, w):
        """ Append some comment to the word just read..."""
        w = w.lower()
        comment = ''
        if w in COMMON_WORDS:
            comment = 'The reader knows this word well.'
        elif w == 'reader':
            comment = 'The reader nods at the reference to themself.'  # reflexive singular pronoun
        elif w == 'book':
            comment = "'Book' — _this_ book."
        elif self.wordstate == 3:
            comment = 'The reader nods again, and continues to read.'
        return comment

    def verb_comment(self, w, recent):
        """ Append some comment about a 'recent' action"""
        if recent == 0:
            r = '"Yes" the reader thinks, "This is what I am doing..."'
        if recent == 1:
            r = "The reader remembers taking this action very recently."
            r += " It just happened seconds ago."
        return r

    def read_sentence(self, sentence, context='next', loc=''):
        """Reader reads a single sentence."""
        text = sentence.split(' ')
        output = []
        if context.startswith('first'):
            self.wordstate = 0
            first = self.word(text[0], 'first', 'on the page')
            output.append(first)
            text = text[1:]
        for w in text:
            a = self.word(w)
            output.append(a)
            self.wordstate = (self.wordstate + 1) % MAX_WS
        if context == 'first_book':
            output[-1] = output[-1][:-1] + ', thus ending the first sentence of this peculiar book.\n\n'
        else:
            output.append('Then there is a period, ending the current sentence.\n\n')
        return concat(output, NL)

    def read(self, text, context=''):
        """
        Reader reads text.
        Each sentence is separated by a new line (NL).
        """
        text = text.split(NL)
        output = []
        if context in ('first_page', 'first_book'):
            first = self.read_sentence(text[0], context, 'on the page')
            self.wordstate += 1
            output.append(first)
            text = text[1:]
            context = 'next'
        for s in text:
            a = self.read_sentence(s)
            output.append(a)
            #self.wordstate = (self.wordstate + 1) % MAX_WS
        return concat(output)

    def describe_letters(self, text, context=''):
        """
        Reader describes the letters (symbols) of text.
        Each sentence is separated by a new line (NL).
        """
        output = describe(text)
        return concat(output)

