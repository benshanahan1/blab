from random import randint
from re import sub

n_adv   = 6276
n_adj   = 28479
n_noun  = 90963
pattern = r"\s+"  # remove non-space whitespace
output  = []

with open("adverbs.txt") as f:
    adv_idx = randint(1, n_adv)
    for i, line in enumerate(f):
        line = sub(pattern, "", line)
        if i == adv_idx:
            output.append(line)
            break

with open("adjectives.txt") as f:
    adj_idx = randint(1, n_adj)
    for i, line in enumerate(f):
        line = sub(pattern, "", line)
        if i == adj_idx:
            output.append(line)
            break

with open("nouns.txt") as f:
    noun_idx = randint(1, n_noun)
    for i, line in enumerate(f):
        line = sub(pattern, "", line)
        if i == noun_idx:
            output.append(line)
            break

print(" ".join(output).title())