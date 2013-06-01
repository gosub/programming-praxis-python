# Word Frequencies
# Our interpretation of a problem solved by a classic unix pipeline
# Programming Praxis Exercise 14
# http://programmingpraxis.com/2009/03/10/word-frequencies/


from collections import Counter
import string
import re
import argparse
import sys

# MIN_WORD_LEN declares the minimal word length
# necessary to be counted, if not otherwise specified
MIN_WORD_LEN = 4


def find_most_common(words, count=10, minimum=MIN_WORD_LEN, ignore_case=True):
    if ignore_case:
        transformed = string.lower
    else:
        transformed = lambda x: x
    counter = Counter(transformed(word) for word in words
                      if len(word) >= minimum)
    return counter.most_common(count)


def list_of_words(text):
    regex = re.compile("\w+")
    words = regex.findall(text)
    return words


def show_words_and_count(word_count_list, words_only=False):
    for word, count in word_count_list:
        if words_only:
            print word
        else:
            print word, "\t", count


def main():
    description = "Prints the n most common words in the file, "
    description += "and the count of their occurrences, in descending order."

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-n', '--number', type=int, default=10,
                        help="Number of top occurrences to print")
    parser.add_argument('-m', '--min-word-len', type=int, default=3,
                        help="Minimum word length")
    parser.add_argument('-c', '--case', action='store_true', default=True,
                        help="Do not ignore case")
    parser.add_argument('-o', '--words-only', action='store_true',
                        default=False, help="Do not print word count")
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    args = parser.parse_args()

    text = args.infile.read()
    words = list_of_words(text)
    most_common = find_most_common(words, count=args.number,
                                   minimum=args.min_word_len,
                                   ignore_case=not args.case)
    show_words_and_count(most_common, words_only=args.words_only)


if __name__ == "__main__":
    main()
