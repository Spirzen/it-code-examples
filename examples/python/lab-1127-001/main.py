score = 0

def on_click():
    global score
    score += 1
    print("Мяу!")
    if score == 5:
        print("Устал…")
        return True
    return False

while True:
    input("Enter — клик по спрайту… ")
    if on_click():
        break
