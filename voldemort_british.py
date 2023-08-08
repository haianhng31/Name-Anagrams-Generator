import anagram
import sys
from itertools import permutations
from collections import Counter

def prep_word(name, word_lst_ini):
    # Prep word_list for finding anagrams
    print(f"Length of initial word list = {len(word_lst_ini)}")
    word_lst = [word.lower() for word in word_lst_ini if len(word)==len(name)]
    print(f"Length of the new word list = {len(word_lst)}")
    return word_lst

def cv_map_word(word_lst):
    cv_map = []
    vowels = 'aeouiy'
    for word in word_lst:
        temp = ""
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        cv_map.append(temp)

    total = len(set(cv_map)) #number of unique c-v patterns
    target = 0.05 #target fraction to eliminate
    n = int(target*total) #number of items in target fraction
    count_pruned = Counter(cv_map).most_common(total - n) #returns the most common elements (words or tokens) and their counts as a list of tuples.

    filtered_cv_map = [pattern for pattern,_ in count_pruned]
    print("Length filtered_cv_map = {}".format(len(filtered_cv_map)))
    return filtered_cv_map

def cv_map_filter(name, filtered_cv_map):
    """Remove permutations of words based on unlikely cons-vowel combos."""
    filter_1 = set()
    perms = ["".join(i) for i in permutations(name)]
    vowels = 'aeouiy'
    for word in perms:
        temp = ""
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter_1.add(word)
    print("# choices after filter_1 = {}".format(len(filter_1)))
    return filter_1

def trigram_filter(word_lst,trigrams_filtered):
    # Remove unlikely trigrams from filter
    filter_temp = set()
    for word in word_lst:
        for trigram in trigrams_filtered:
            filter_temp.add(word) if trigram.lower() in word else None
    filter_2 = word_lst - filter_temp
    print("# choices after filter_2 = {}".format(len(filter_2)))
    return filter_2

def letter_pair_filter(word_lst):
    """Remove unlikely letter-pairs from permutations."""
    filter_temp = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv',
               'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd',
                          'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for word in word_lst:
        for r in rejects:
            if r in word:
                filter_temp.add(word)
        for fp in first_pair_rejects:
            if word.startswith(fp):
                filter_temp.add(word)
    filter_3 = word_lst - filter_temp
    print("# choices after filter_3 = {}".format(len(filter_3)))
    return filter_3

def view_by_letter(name, word_lst):
    print(f'Remaining letters = {name}')
    start_letter = input('Type a letter to start with: ')
    subset = [word for word in word_lst if word.startswith(start_letter)]
    print(*sorted(subset),sep = "\n")
    print(f'Number of choices starting with {start_letter} = {len(subset)}')
    try_again = input('Try again? Press Enter else any other keys to exit.')
    if try_again == "":
        view_by_letter(name,word_lst)
    else:
        sys.exit()


def main():
    name = 'tmvoordle'
    name = name.lower()

    word_lst_ini = anagram.load_file('2of4brif.txt')
    trigrams_filtered = anagram.load_file('least-likely_trigrams.txt')

    word_lst = prep_word(name, word_lst_ini)

    filtered_cv_map = cv_map_word(word_lst)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1,trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)

if __name__ == '__main__':
    main()


