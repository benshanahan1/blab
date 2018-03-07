from random import randint

n_adv  = 6276
n_adj  = 28479
n_noun = 90963
adverbs    = [randint(1, n_adv)]
adjectives = [randint(1, n_adj), randint(1, n_adj)]
nouns      = [randint(1, n_noun)]
sorted_adverbs    = sorted(adverbs)
sorted_adjectives = sorted(adjectives)
sorted_nouns      = sorted(nouns)

output = ""

with open("adverbs.txt") as f:
    for i, line in enumerate(f):
        if i == sorted_adverbs[0]:
            output += line
        elif i > sorted_adverbs[0]:
            break

with open("adjectives.txt") as f:
    for i, line in enumerate(f):
        if i == sorted_adjectives[0]:
	    output += line 
        elif i == sorted_adjectives[1]:
            output += line
        elif i > sorted_adjectives[1]:
	    break

with open("nouns.txt") as f:
    for i, line in enumerate(f):
        if i == sorted_nouns[0]:
	    output += line
	elif i > sorted_nouns[0]:
	    break

print(" ".join(output.split("\r\n")).title())
