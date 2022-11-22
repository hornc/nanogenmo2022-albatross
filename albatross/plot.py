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

EOCH1 = '''
Flicking through the entire book, the reader notices that there are {chapters} chapters.
The first ends here, so the reader turns the page.
'''

SOCH2 = '''
The reader has just turned the page, having finished reading the first chapter of the {chapters} which make up this book.
They determined this recently by flicking through the pages looking for chapter headings, like the "CHAPTER 2" at the top of this page.

Below this heading they read:

'''

EOCH2 = '''
The reader is lulled into a trance by the almost meaningless repetition of self-descriptive words.
The words begin to lose meaning, if they ever had any to begin with.

The letters flow past:
{letters}.

Soon these too lose their meaning as symbols and there are just the shapes, printed in black ink on the paper:
{letter_shapes}

Finally, the reader sees a blank three-quarters of a page signalling the end of the second chapter.
The empty space breaks the monotony and the page can be turned.
'''

# Can this be encoded?
SOCH3 = '''
"CHAPTER 3" it reads at the top of page.
""CHAPTER 3"" begins the first sentence.
A twice-quoted "CHAPTER 3" begins the second sentence.
The third sentence does not begin with "CHAPTER 3", but contains it anyway.
As does the fourth.
The fourth sentence avoids it altogether.
As does the sixth.
And seventh.
And eighth.
And ninth, and so on.
The last three sentences begin with conjunctions, the reader notes, which make them improper sentences?
Does it matter?
It is not the worst sin committed by this book.
The fourteenth sentence mentions "CHAPTER 3" again — for no reason discernable to the reader.
From a quick glance through the remaining {pages} pages of this chapter it does not appear again.
This chapter _is_ referenced later, but the reader is not directly aware of this yet.
Having read and analysed the first fourteen sentences of this chapter the reader chooses to ignore the footnote at the bottom of this page and continue reading:

'''


CEDILLA = '''
The reader is beginning to suspect that the title, "{title}", and the engraving on page {engraving_page} is a meaningless façade to give this book an illusion of hidden depth and meaning.
'''


engraving_caption = 'The Common Albatross (_Diomedea exulans_, Linn.)'

ENGRAVING = '''
Chapter {test_chapter} also refers to this engraving:

![— {engraving_caption}](data/engraving.png)

and correctly notes this page number as being {engraving_page}.
'''.replace('{engraving_caption}', engraving_caption)


ENGRAVING_TEST = '''
There is an engraving of an albatross on page {engraving_page}. It is captioned "{engraving_caption}".
'''.replace('{engraving_caption}', engraving_caption)


TEST_LETTERS = '''From flicking through the pages earlier, the reader had noticed that chapter {chapter} starts with a number of statements about specific letters located throughout the book.
The first was that "{statements[0]}".
This appears to be correct.
Then "{statements[1]}".
Glancing at the facing page, this too is verified as correct.
"{statements[2]}"
Flicking forward {pages} pages, the reader finds that the fifth letter of the second line is indeed '{result}'.
'''
