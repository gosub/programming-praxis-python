# Mark V. Shaney
# Generate parodies of a text using a Markov chain
# Programming Praxis Exercise 11
# http://programmingpraxis.com/2009/02/27/mark-v-shaney/

import random
from collections import defaultdict

# PREFIX is the number of words used by
# the markov chain to find the next word
PREFIX = 2


def train_on(text):
    """ Return a dictionary whose keys are alle the tuple of len PREFIX
    of consecutive words inside text, and whose value is the list of
    every single word which follows that tuple inside the text. For ex:
    {('Happy', 'birthday'): ['to', 'dear'] ...} """
    words = text.split()
    assert len(words) > PREFIX
    training = defaultdict(list)
    for i in range(0, len(words) - PREFIX):
        duo = tuple(words[i:i + PREFIX])
        following = words[i + PREFIX]
        training[duo].append(following)
    return training


def mark_v_shaney(training_set, words=150):
    "Generate a text of n words using a markov chain."
    parody, word_count = "", 0
    pre, post = None, None
    while word_count < words:
        if pre not in training_set:
            pre = random.choice(training_set.keys())
            parody += " ".join(pre)
            word_count += PREFIX
        post = random.choice(training_set[pre])
        parody += " " + post
        word_count += 1
        pre = tuple(list(pre[1:]) + [post])
    return parody


def main(filename, words):
    "Create a parody of the text in filename"
    content = open(filename).read()
    training = train_on(content)
    print mark_v_shaney(training, words)


if __name__ == '__main__':
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    words = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    if filename:
        main(filename, words)
    else:
        print "Usage: python mark_v_shaney.py filename [word_count]"
        print "May I suggest http://www.gutenberg.org/ebooks/200 ?"
