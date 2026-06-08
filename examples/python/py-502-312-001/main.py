word = "python"
guessed = ""
attempts = 6
while attempts > 0:
    letter = input("Буква: ").lower()
    if letter in word:
        guessed += letter
        print("Есть:", guessed)
        if all(ch in guessed for ch in word):
            print("Победа!")
            break
    else:
        attempts -= 1
        print("Осталось:", attempts)
else:
    print("Слово было:", word)
