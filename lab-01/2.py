def analyse(text):
    vowels = 'aeiouy'
    unique_vowels = []
    found_words = []
    current_word = ""

    text = text.lower

    for ch in text:
        if ch in vowels and ch not in unique_vowels:
            unique_vowels.append(ch)

        if ch.isalpha():
            current_word += ch
        else:
            if len(current_word) >= 5:
                if current_word[0] == current_word[-1]:
                    found_word.append(current_word)
            current_word = ""
    if len(current_word) >= 5:
        if current_word[0] == current_word[-1]:
            if current_word not in found_words:
                found_words.append(current_word)
    return(len(unique_vowels), " ".join(fouund_word))

print(analyse('Level madam Anna went to kayak racecar!'))
