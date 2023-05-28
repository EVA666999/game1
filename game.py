import getpass

def guess(word, guess_word):
    letters = []
    for char in guess_word:
        if char in word and char not in letters:
            letters.append(char)
    return letters

word = getpass.getpass("Введите слово, которое нужно угадать: ")

guessed_letters = []
correct_order = False
while sorted(guessed_letters) != sorted(word):
    guess_word = input("Введите вариант: ")
    result = guess(word, guess_word)
    guessed_letters.extend(result)
    print(sorted(guessed_letters))

    if list(word) == sorted(guessed_letters):
        correct_order = True
        break

if correct_order:
    print("Поздравляю, вы угадали слово!")
else:
    print("Вы угадали все буквы. Теперь угадайте слово, которое состоит из этих букв.")

guess_attempts = 3
while not correct_order and guess_attempts > 0:
    guess_word = input("Введите слово: ")
    if guess_word == word:
        print("Поздравляю, вы угадали слово!")
        break
    else:
        guess_attempts -= 1
        if guess_attempts > 0:
            print("Вы не угадали слово. Осталось попыток:", guess_attempts)
        else:
            print("У вас закончились попытки. Слово:", word)
