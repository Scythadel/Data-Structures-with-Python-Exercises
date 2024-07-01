def vowel_count(word: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    word_list = list(word)
    for i in vowels:
        for j in word_list:
            if i == j:
                count = count + 1
    return count

print(vowel_count('jeep'))