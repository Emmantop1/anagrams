
def find_anagrams(word, anagram):
    word=word.lower()
    anagram=anagram.lower()
    word=word.replace(" ", "")
    anagram=anagram.replace(" ", "")
    return sorted(word)==sorted(anagram)

    # if sorted(word)==sorted(anagram):
    #     return True
    # else:
    #     return False

print("can we qualify 'hello' as anagram to 'check' :", find_anagrams("hello", "check"))
print("can we qualify 'below' as anagram to 'elbow' :", find_anagrams("below", "elbow"))
