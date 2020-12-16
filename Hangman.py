import random
list_word = ['python', 'java', 'kotlin', 'javascript']
word = list_word[random.randrange(0, len(list_word))]
heart = 8
text = ""

print("H A N G M A N \n")
while True:
    status = ""
    for i in word:
        if i in text:
            print(i, end=" ")
            status += "1"
        else:
            print("_", end=" ")
            status += "0"
    input_text = str(input("\nInput a letter: > ").strip())
    if input_text in text:
        print("No improvements")
    else:
        text += input_text
    if "0" not in status:
        print("You guessed the word! \n You survived! ")
        break
    if input_text not in word:
        print("No such letter in the word ")
        heart -= 1
    if heart <= 0:
        print("You are hanged! ")
        break
