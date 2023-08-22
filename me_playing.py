def count_letter_e(word):
    for letter in word:
        total_e = 0
        if letter == "e":
            total_e = int(total_e) + 1
        return (total_e)
    
this = input("enter a word ")
letter_count = count_letter_e(this)
print(letter_count)

# this doesnt work and I don't know why



