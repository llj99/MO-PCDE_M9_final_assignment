def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word =  new_word + word[i] + "_"
    return new_word

word = "Python"
print(add_underscores(word))

