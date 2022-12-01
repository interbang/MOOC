story = " "
word1 = " "
while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    elif word1 != word:
        word1 = word
    else:
        break
   
    story += word + " "

print(story)
        
  
