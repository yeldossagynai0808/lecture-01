def analyse(text):
    count = 0
    vowels = 'aeiouy'

    for ch in text.lower():
        if ch in vowels:
            count += 1

    return count

print(analyse('Hello'))
