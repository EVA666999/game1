import getpass

def gues(word, gues_word):
    words = []
    for char in gues_word:
        if char in word:
            words.append(char)
    return list(set(words))

word = getpass.getpass("Введите слово, которое нужно угадать: ")

guessed_letters = set()
correct_order = False
while sorted(guessed_letters) != sorted(word):
    gues_word = input("Введите вариант: ")
    result = gues(word, gues_word)
    guessed_letters.update(result)
    print(sorted(list(guessed_letters)))

    if list(word) == sorted(list(guessed_letters)):
        correct_order = True
        break

if correct_order:
    print("Поздравляю, вы угадали слово!")
else:
    print("Ты угадал все буквы, теперь угадай слово, которое состоит из этих букв")

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
            print("У вас закончились попытки. Слово: ", word)
