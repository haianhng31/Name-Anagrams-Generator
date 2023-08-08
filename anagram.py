import sys

def load_file(file):
    try:
        with open(file) as f:
            word_lst = []
            for word in f:
                word = word.strip().lower()
                word_lst.append(word)
            return word_lst

    except OSError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)


# initial = (input('Type a word: ')).lower()
# sorted_initial = sorted(initial)
# word_lst = load_file('2of4brif.txt')
# anagram_lst = []
# for word in word_lst:
#     if sorted_initial == sorted(word) and word != initial:
#         anagram_lst.append(word)
#
# if anagram_lst:
#     print('Anagrams =',*anagram_lst,sep='\n')
# if not anagram_lst:
#     print("You need a larger dictionary or a new name.")




