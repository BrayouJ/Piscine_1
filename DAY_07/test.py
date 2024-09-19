word_list = ["babb", "acc", "dddd", "acbd", "ccacd"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter_counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

x = 0

for i in alphabet:
    x += 1
    y = 0
    for j in word_list:
        y += 1
        for k in word_list[y-1]:
            if i == k:
                letter_counter[x-1] += 1
print(letter_counter)
print(letter_counter.index(max(letter_counter)))