#!/usr/bin/env python3
"""Heap abuse"""

import argparse
import random


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2,
                        help='Number of adjectives')
    parser.add_argument('-n',
                        '--number',
                        metavar='insults',
                        type=int,
                        default=3,
                        help='Number of insults')
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        type=int,
                        default=None,
                        help='Random seed')

    args = parser.parse_args()
    check_args(args, parser)

    return args


def main():
    """Make a jazz noise here"""

    args = get_args()

    all_adjectives = """bankrupt base caterwauling corrupt cullionly detestable
                    dishonest false filthsome filthy foolish foul gross
                    heedless indistinguishable infected insatiate irksome
                    lascivious lecherous loathsome lubbery old peevish
                    rascaly rotten ruinous scurilous scurvy slanderous
                    sodden-witted thin-faced toad-spotted unmannered vile
                    wall-eyed""".split()
    all_nouns = """Judas Satan ape ass barbermonger beggar block boy braggart
               butt carbuncle coward coxcomb cur dandy degenerate fiend
               fishmonger fool gull harpy jack jolthead knave liar lunatic
               maw milksop minion ratcatcher recreant rogue scold slave
               swine traitor varlet villain worm""".split()

    random.seed(args.seed)

    for _ in range(args.number):
        adjectives = random.sample(all_adjectives, args.adjectives)
        noun = random.choice(all_nouns)
        print(f'You {", ".join(adjectives)} {noun}!')


def check_args(args, parser):
    """Checks if the command-line arguments are valid"""

    if args.adjectives <= 0:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number <= 0:
        parser.error(f'--number "{args.number}" must be > 0')


if __name__ == '__main__':
    main()
