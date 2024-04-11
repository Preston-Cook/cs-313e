# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Preston Cook

# Student UT EID: plc886

# Course Name: CS 313E

# Unique Number: 50775

# Output: True or False
def are_anagrams(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    hashmap1 = {}
    hashmap2 = {}

    for i in range(len(str1)):
        hashmap1[str1[i]] = hashmap1.get(str1[i], 0) + 1
        hashmap2[str2[i]] = hashmap2.get(str2[i], 0) + 1

    return hashmap1 == hashmap2

# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst


def anagram_families(lst: list[str]) -> int:
    groups: dict[str, list[str]] = {}

    for word in lst:
        added = False
        for key_word in groups:
            if are_anagrams(key_word, word):
                groups[key_word].append(word)
                added = True
                break

        if not added:
            groups[word] = [word]

    return len(groups)


def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for _ in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)


if __name__ == "__main__":
    main()
