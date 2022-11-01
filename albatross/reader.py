
COMMON_WORDS = ['in', 'the']
VERBS = ['sits', 'read:']
CONJUNCTIONS = ['and']
MAX_WS = 4

def article(s):
    if s[0] == "'":  # quoted letter name
        aan = 'an' if s[1].lower() in 'aefhilmnorsux' else 'a'
    else:
        aan = 'an' if s[0].lower() in 'aeiou' else 'a'
    return f'{aan} {s}'


def concat(text_list):
    return ' '.join(text_list)


class Reader():
    def __init__(self):
        self.wordstate = 0

    def letter(self, c, adj='next', loc='', ccase='', punct=','):
        if c == '\n':
            return c * 2
        if c in "'_":
            return ''
        if c == ' ':
            return 'Then there is a space.'
        if c == '.':
            self.wordstate = 0
            return 'then there is a period, ending the current sentence.\n\n'
        if c == ',':
            return 'Then there is a comma.'
        if c == ':':
            return 'Then there is a colon.'

        if ccase:
            ccase += ' '
        cc = f"{ccase}'{c}'"
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
        w = w.strip()
        if w in VERBS:
            return self.verb_word(w, adj, loc)
        if w in CONJUNCTIONS:
            return self.conj_word(w, adj, loc)

        if self.wordstate == 0:
            return self.spell_word(w, adj, loc)
        elif self.wordstate == 1:
            return self.list_word(w, adj, loc)
        elif self.wordstate == 3:
            return self.read_word(w, adj, loc)

        # default:
        return self.spell_word(w, adj, loc)

    def spell_word(self, w, adj='next', loc=''):
        output = []
        case_last = None
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
            a = self.letter(c, adj, loc, ccase, punct)
            adj = 'follow'
            output.append(a)
        comment = self.comment(w)
        if comment:
            output.append(comment)
        return concat(output)

    def list_word(self, w, adj='next', loc=''):
        output = []
        output.append("Next there is a space followed by a new word:")
        for c in w:
            output.append(f"'{c}' -")
        comment = self.comment(w)
        if comment:
            output.append(comment)
        return concat(output)

    def read_word(self, w, adj='next', loc=''):
        output = []
        output.append(f"The next word is '{w}'.")
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
            comment = ', _this_ book.'
        elif self.wordstate == 3:
            comment = 'The reader nods again, and continues to read.'
        return comment

    def verb_comment(self, w, recent):
        """ Append some comment about a 'recent' action"""
        if recent == 0:
            r = '"Yes" the reader thinks, "This is what I am _still_ doing..."'
        if recent == 1:
            r = "The reader remembers taking this action very recently."
            r += " It just happened seconds ago."
        return r


    def read(self, text):
        """Reader reads text."""
        text = text.split(' ')
        output = []
        first = self.word(text[0], 'first', 'on the page')
        self.wordstate += 1
        output.append(first)
        for w in text[1:]:
            a = self.word(w)
            if a:
                output.append(a)
                self.wordstate = (self.wordstate + 1) % MAX_WS
        return concat(output)

