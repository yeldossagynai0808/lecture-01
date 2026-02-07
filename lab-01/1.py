def analyse(text):
    count = 0
    vowels = 'aeiouy'

    for word in text.lower():
            if word in vowels:
                count += 1

    return count
    


print(analyse('Hello world'))
