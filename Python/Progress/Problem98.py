from itertools import combinations

def read_from_file(filename):
    words = open(filename, 'r')

    reference = ""
    for line in words:
        reference = line[:-1].split(",")

    words.close()
    return reference


def is_anagram(combo):
    (w1, w2) = combo
    # print(w1, w2)
    return sorted(w1) == sorted(w2)


def get_anagrams(reference):
    # Found max length of the list of words, it's 14, so here's 15 lists
    ref_by_len = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    # print(ref_by_len)

    for r in reference:
        # print(r, len(r))
        # print(ref_by_len[len(r)])
        i = len(r)
        ref_by_len[i].append(r)

    anagrams = {}

    for i in range(len(ref_by_len)):
        for combo in combinations(ref_by_len[i], 2):
            if is_anagram(combo):
                # print(combo)
                anagrams[combo[0]] = combo[1]

    # print(anagrams)
    # for key in anagrams.keys():
    #     print(key)
    return anagrams


def max_square_if_match(w1, w2):
    return -1


def main():
    reference = read_from_file('p098_words.txt')
    anagrams = get_anagrams(reference)
    maximum = 0
    for key in anagrams.keys():
        s = max_square_if_match(key, anagrams[key])
        if s > maximum:
            maximum = s

    return maximum



main()
