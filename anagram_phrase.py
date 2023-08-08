import anagram
import sys
from collections import Counter

word_lst = anagram.load_file('2of4brif.txt')
word_lst.append('a')
word_lst.append('i')
word_list = sorted(word_lst)


def find_anagrams(name,word_lst):
    name_count = Counter(name)
    anagram_lst = []

    for word in word_lst:
        word_count = Counter(word)
        if all(name_count[letter] >= word_count[letter] for letter in word):
            anagram_lst.append(word)
            # for charac, i in word_count.items():
            #     target_count[charac] -= i

    print(*anagram_lst,sep="\n")
    print()
    print(f'Remaining letters = {name}')
    print(f'Number of remaining letters = {len(name)}')
    print(f'Number of remaining anagrams = {len(anagram_lst)}')
    print()


def process_choice(name):
    # start over or choose a choice
    while True:
        choice = input("Make a choice else Enter to start over or # to end: ")
        if choice == "":
            main()
        if choice == "#":
            sys.exit()
        else:
            candidate = choice.lower().strip()
        leftover_name = list(name)
        if all(letter in leftover_name for letter in candidate):
            for letter in candidate:
                leftover_name.remove(letter)
            break
        else:
            print("Won't work! Make another choice.", file=sys.stderr)

        '''
        for letter in candidate:
            if letter in leftover_name:
                leftover_name.remove(letter)
        if len(name) - len(leftover_name) == len(candidate):
            break
        else:
            print("Won't work! Make another choice.", file=sys.stderr)'''
    name = "".join(leftover_name)
    return choice, name


def main():
    # get name from users
    name = (input('What is your name? ')).strip().lower()
    name = name.replace("-"," ")

    limit = len(name)
    phrase = ""
    running = True

    while running:
        if len(phrase) < limit:
            anagrams = find_anagrams(name,word_lst)
            choice, name = process_choice(name)
            phrase += choice + " "
            print(f"Current anagram phrase = {phrase}")
            print()
        else:
            print("\n***** FINISHED!!! *****\n")
            print(f"Anagram of name = {phrase}")
            try_again = input('Try again? (Press Enter else "n" to quit)\n ')
            if try_again == "":
                main()
            if try_again == "n":
                running = False
                sys.exit()

if __name__ == '__main__':
    main()





