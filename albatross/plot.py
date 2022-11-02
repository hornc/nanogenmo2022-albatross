SEED = ''

J1 = '''
"Reading lists of letters used in the words of every sentence is tiring." thinks the reader, "Surely the whole book can\'t be like this?"
Frowning, they flick forward through the pages. A chapter heading briefly catches their eye: "Chapter 2".
It's gone.
They stop at page %%300%% and start to read:
'''

RR = 'resigned resumption'


Q1 = '''
"This flow of words and letters, recognizable yet not directly meaningful, has a somewhat soporific effect. There is a rhythm to them; a plodding familliarity, yet there is something alien, perhaps 
ominous. Where is it all leading? Is there anything to uncover, or is it all effectively empty terrain?"
'''

Q2 = f'''
With a {RR} of their reading, the reader presses on.
'''

J2 = f'''
Yes, more of the same.
Exasperated, the reader jumps forward again, to page %%700%%.
Midway on the page there is a quote, as if spoken by a character.
  "This is new..."

> {Q1}

It appears to be the narration of a reader's internal thoughts.
But which reader?
This hasn't happend.
Yet?

Immediately following the quote is a {RR} (the text on the page actually uses the words "{RR}") of the tedious sentence descriptions for %%paragraph%% paragraphs:

> %%QUOTE1%%

and so on...

But then the style changes to describing the _letter forms_, down to the curves and uprights of the type:

> %%QUOTE2%%

and so it continues — seemingly for many pages.
The reader shakes their head in bewilderment.
'''

