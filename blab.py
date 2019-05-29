from argparse import ArgumentParser
from json import load
from random import choice


def get_arg_parser():
    parser = ArgumentParser()
    parser.add_argument('-n',
                        default=1,
                        type=int,
                        help='Number of phrases to generate.')
    return parser


def load_list(path):
    with open(path, 'r') as fd:
        return load(fd)


def get_word_lists():
    adjectives = load_list('adjectives.json')['adjs']
    adverbs = load_list('adverbs.json')['adverbs']
    nouns = load_list('nouns.json')['nouns']
    return (adjectives, adverbs, nouns)


def get_phrase_parts(word_lists):
    adjectives, adverbs, nouns = word_lists
    return [choice(adverbs), choice(adjectives), choice(nouns)]


def format_phrase(parts):
    return '{}.'.format(' '.join(parts).capitalize())


if __name__ == '__main__':
    parser = get_arg_parser()
    args = parser.parse_args()

    # Generate phrases.
    word_lists = get_word_lists()
    for i in range(args.n):
        parts = get_phrase_parts(word_lists)
        print(format_phrase(parts))
