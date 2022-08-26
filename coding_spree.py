# writing a program that captalizes the first letter of each word in a sentence

sentence = input("Write a sentence: ")
sentence = sentence.split()
new_sentence = ""

for word in sentence:
    word_ = word.capitalize()
    new_sentence = new_sentence + " " + word_
print(new_sentence.lstrip())


