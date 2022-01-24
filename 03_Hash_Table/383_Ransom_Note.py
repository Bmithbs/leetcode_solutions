# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.




def canConstruct(ransomNote, magazine):

    table = [0] * 26

    
    
    for i in magazine:
        table[ord(i) - ord('a')] += 1

    for i in ransomNote:
        table[ord(i) - ord('a')] -= 1

    for i in table:
        if i < 0: return False
    
    return True

if __name__ == '__main__':
    ransomNote = "fihjjjjei"

    magazine = "hjibagacbhadfaefdjaeaebgi"
    print(canConstruct(ransomNote, magazine))


    