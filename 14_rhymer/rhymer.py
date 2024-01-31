#!/usr/bin/env python3
"""Make rhyming words"""

import argparse
import re
import string


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description='Make rhyming "words"')
    parser.add_argument('word',
                        type=str,
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    start, rest = stemmer(args.word)

    if rest:
        print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print(f'Cannot rhyme "{args.word}"')


def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""

    #    word = word.lower()
    #    stem_idx = len(word)
    #    for idx in range(len(word)):
    #        if word[idx] in 'aeiou':
    #            stem_idx = idx
    #            break
    #
    #    return (word[:stem_idx], word[stem_idx:])

    word = word.lower()
    vowels = 'aeiou'
    consonants = ''.join(
        [c for c in string.ascii_lowercase if c not in vowels])
    pattern = (
        '([' + consonants + ']+)?'  # capture one or more, optional
        '([' + vowels + '])'  # capture at least one vowel
        '(.*)'  # capture zero or more of anything
    )
    pattern = f'([{consonants}]+)?([{vowels}])(.*)'

    match = re.match(pattern, word)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)

    return (word, '')


def test_stemmer():
    """Test stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDZN') == ('rdzn', '')
    assert stemmer('123') == ('123', '')


if __name__ == '__main__':
    main()
