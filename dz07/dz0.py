def is_rithm(words, vowels):
    words = words.split()
    sum_of_vowels = []
    for word in words:
        syllables = 0
        for i in word:
            if i in vowels:
                syllables += 1
        sum_of_vowels.append(syllables)
    return len(sum_of_vowels) == sum_of_vowels.count(sum_of_vowels[0])

poem = "пара-ра-рам рам-пам-папам па-ра-па-да"
vowel_letters = 'аеёиоуыэюя'

if is_rithm(poem, vowel_letters):
    print('Парам пам-пам')
else:
    print('Пам парам')