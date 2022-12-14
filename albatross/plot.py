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
At the top of the page there is a quote, as if spoken by a character.
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

Finally, the reader sees a blank quarter of a page signalling the end of the second chapter.
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

engraving_caption = 'The Common Albatross (_Diomedea exulans_, Linn.)'

CEDILLA = '''
The reader is beginning to suspect that the title, "{title}", and the engraving on page {engraving_page}, with its reference to "{engraving_caption}", is a meaningless façade to give this book an illusion of hidden depth and meaning.
'''

FEATURES = '''
The reader scans through the pages looking for other interesting features. There is a single figure, an engraving, captioned "{engraving_caption}" on page {engraving_page}.

There are footnotes on pages %footnotes%. The repetitive nature of the descriptions limit the vocabulary somewhat, and there is a pattern to the typography, which has its own
restricted character. Page {cedilla_page} makes use of the word "{cedilla_word}", which contains a cedilla on the letter 'ç', which is a typographically interesting variation the reader is able to note.
"{cedilla_word}" is used in the book {cedilla_count} times. Other than that, the typeface appears to be that of basic Latin characters.
'''


ENGRAVING = '''
Chapter {test_chapter} also refers to this engraving:

![— {engraving_caption}](data/engraving.png)

and correctly notes this page number as being {engraving_page}.
'''


ENGRAVING_TEST = '''
There is an engraving of an albatross on page {engraving_page}. It is captioned "{engraving_caption}".
'''


TEST_LETTERS = '''From flicking through the pages earlier, the reader had noticed that chapter {chapter} starts with a number of statements about specific letters located throughout the book.
The first was that "{statements[0]}".
This appears to be correct.
Then "{statements[1]}".
Glancing at the facing page, this too is verified as correct.
"{statements[2]}"
Flicking forward {pages} pages, the reader finds that the fifth letter of the second line is indeed '{result}'.
'''

LAST_DAY = '''
## The Last Day.

"What has happend?", the reader thinks.
"This is the last chapter, and I have skipped through multiple blank pages -- entire empty chapters in fact."

"I was expecting more."

"There was supposed to be a build-up of conflict between myself and the narrator."

"A potential existential battle of wills, where I experiemented with controlling the narrator, in a similar fashion to how the narrator appeared to be controlling _my_ actions."

"I was supposed to test the power of the narrator, and catch them out making mistakes in their narration. I needed a chance to explore both paths of being a _compliant reader_, and an _adverserial reader_."

"Where were these sections?"

"I don't feel like I have done and experienced these things fully."

"It seemed so promising." The reader sighs.

"The mystery of the Albatross was somewhat (barely) introduced, but never got off the ground." The reader frowns, uncertain whether they even _noticed_ there was an albatross (introduced with the engraving on page {engraving_page}), or a mystery specific to it. Is this the narrator being overly presumptious? Have they been "caught out" right here?

"There were footnotes mentioned, but none appear in this version."

"There was supposed to be a nice cover, which tied into the Albatross mystery". The reader flips the book to the front -- the current cover is indeed blank.

"Up to this chapter there are only {bulkwordcount} words. Everyone knows that is only {percent}% of a _real_ novel.", the reader thinks with disdain.

While the reader is thinking these thoughts, {animal} appears out of nowhere and nuzzles up to the reader's legs.

"MEOW." it says, apologetically.

The reader smiles and pets it on the head, not too condescendingly.

"At least you tried."

With that, the reader looks down at the page in front of them and begins to read the final chapter in order to complete this book:

'''

FIN = '''
The reader looks up and stares at the {animal}.

"I was expecting a more satisfying resolution." they think.

## FIN.'''
