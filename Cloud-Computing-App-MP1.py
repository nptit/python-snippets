__author__ = 'qxu'


import re
from collections import Counter

stop_words = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
                             "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
                             "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                             "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                             "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                             "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                             "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                             "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                             "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                             "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])

delimiters = r"[ \t,;.?!-:@\[\]\(\)\{\}_\*/]"

with open("cloudapp-mp1-input.txt") as fh:
    lines = fh.readlines()

text = []
for line in lines:
    text.extend(re.split(delimiters, line.rstrip()))

text = [w.lower() for w in text]
text = [w for w in text if w and w not in stop_words]


word_freq = Counter(text)
print word_freq.most_common(20)