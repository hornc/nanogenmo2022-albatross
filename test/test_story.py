from story import story

SEED = 'data/start.txt'
TARGET = 50000


def test_wordcount():
    book = story(SEED)
    count = book.count()
    print('Count:', count)
    p = count / TARGET
    assert count > TARGET, f"{p:%} complete!"


def test_chapter_sizes():
    print()
    book = story(SEED)
    chapters = book.wc_chapters()
    ctarget = TARGET // len(chapters)
    for i, c in enumerate(chapters):
        print(f'{i + 1}:\t{c: >5}\t{c / ctarget: >7.2%}')


def test_generated_content():
    book = story(SEED)
    words = book.to_markdown()
    count = len(words.split(' '))

    with open('albatross/plot.py', 'r') as f:
        plot = f.read()
    plot_words = len(plot.split())
    print('Plot words:', plot_words)
    gp = (count - plot_words) / count * 100
    print(f'Generated percentage: {int(gp)}%')
    assert gp > 50  # Assert that at least half of the output has been generated
