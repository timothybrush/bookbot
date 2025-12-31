from collections import Counter

def get_char_count(text):
    return Counter(text.lower())

def get_num_words(text):
    return len(text.split())

#def get_num_characters(text):
#    counts = {}
#    for ch in text:
#        counts[ch] = counts.get(ch, 0) + 1
#    return counts

