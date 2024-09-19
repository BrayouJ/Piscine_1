import random

with open("word_list_01.txt", "r") as word_file:
    word_data = word_file.read() 
    word_data = word_data.split("\n")

with open("best_scores.txt", "r") as file:
    best_score = file.read()
    if best_score:
        best_score = int(best_score)
    else:
        best_score = 0

def hangman():

    word_list = ["tiger", "butterfly", "lion", "dolphin", "rabbit", "chicken","monkey","frog","cricket","mouse","otter", "bear"]
    word = random.choice(word_list)

    #IA

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    IA_letter_counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letter = ""
    x = 0

    def AI_Advice():
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                IA_letter_counter[i] = 0
        hint = alphabet[IA_letter_counter.index(max(IA_letter_counter))]
        print(" ", hint.upper(), "  advised")

    for i in alphabet:
        x += 1
        y = 0
        for j in word_list:
            y += 1
            for k in word_list[y-1]:
                if i == k:
                    IA_letter_counter[x-1] += 1

    #Fin IA

    penality = 0
    guesser = []   
    letter_count = 0

    for i in word:
        guesser.append("_")

    while penality < 100:
        if letter_count != 0:
            print("Found ", letter_count, "'"+ letter.upper()+ "'")
        print(' '.join(guesser).upper(), end="  ")
        AI_Advice()
        if penality > 1:
            print(penality, " penalties")
        if penality == 1:
            print(penality, " penalty")
        letter = input("Choose a letter or guess the word: ").lower()
        if letter == word:
            print("You win!")
            exit()
        elif len(letter) > 1:
            if letter != word:
                penality += 5
        elif letter in word:
            letter_check = 0
            letter_count = 0
            for i in word:
                letter_check += 1
                if i == letter:
                    guesser[letter_check - 1] = letter
                    letter_count += 1
        else:
            penality += 3
            letter_count = 0
            print("No '" + letter.upper() + "' found.")
    if penality == 100:
        print("You Lose")
        exit()