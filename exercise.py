VOWELS = 'aeiou'




def vowel_frequency(sentence: str) -> dict:
    """Return a dict with vowel frequency"""
    freq = {}
    for char in sentence:
        if char in VOWELS:
            freq[char] = sentence.count(char)
    return freq
            

if __name__ == '__main__':
    text = 'invat Python si imi place'
    print(vowel_frequency(text))
