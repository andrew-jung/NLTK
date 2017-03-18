from nltk.book import *
from numpy import *

def lexical_diversity(text): # How many different words are used in a text.
    return len(text) / len(set(text))

def percentage(count, total): # Calculation of how much a word count vs total count.
    return 100 * count / total

sent1 = ['Call', 'me', 'Ishmael', '.']
print(len(sent1))
print(lexical_diversity(sent1))
print(percentage(text5.count("lol"), len(text5))) # Percentage of "lol"s in text5
print('\n')

list = ['Hello', 'my', 'name', 'is', 'Andrew']
print(sorted(list))
print(len(list))
print(lexical_diversity(list))
print(percentage(list.count('Andrew'), len(list)))

print(text5.index('lol'))
print(text5[121])
print(list[4:5])
print('\n')

saying = ['After', 'all', 'is', 'said', 'and', 'done',
          'more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
print(tokens[-2:])
print('\n')

fdist = FreqDist(text5) # FreqDist (frequency distribution) is the frequency of a vocabulary item in the text.
print(fdist) # Total number of words/outcomes
vocab1 = fdist.keys() # Distinct types in the text
print(fdist.most_common(50)) # There is no vocab1[:50] in Py3 either typecast to list or use most_common
print(fdist['lol']) # Returns count of string
print('\n')

# fdist.plot(50, cumulative=True)

# len(x) for x in text
# x.upper() for x in text
# Consider setting all 'elements' in list to lower/upper to differentiate between 'This' and 'this'

# TODO: Lesk Algorithm implement WSD? Or other project