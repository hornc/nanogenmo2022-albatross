
def article(s):
    aan = 'an' if s[0].lower() in 'aeiou' else 'a'
    return f'{aan} {s}'


class Reader():

    def letter(self, c, adj='next', loc=''):
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

    def read(self, text):
        """Reader reads text."""
        output = []
        first = self.letter(text[0], 'first', 'on the page')
        output.append(first)
        for c in text[1:]:
            a = self.letter(c)
            if a:
                output.append(a)
        return ' '.join(output)

