# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.




def canConstruct(ransomNote, magazine):

    from collections import Counter

    ransomNote_dict = Counter()
    magazine_dict = Counter()

    for i in ransomNote:
        ransomNote_dict[i] += 1
    for i in magazine:
        magazine_dict[i] += 1

    for i in ransomNote_dict.keys():
        if i not in magazine_dict.keys():
            return False
        elif i in magazine_dict.keys() and ransomNote_dict[i] > magazine_dict[i]:
            return False
    return True

if __name__ == '__main__':
    ransomNote = "a"

    magazine = "ba"
    print(canConstruct(ransomNote, magazine))


    