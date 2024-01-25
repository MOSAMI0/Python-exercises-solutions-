def reversed_sen(sentence):
    reversed_sentence = ""
    for i in range(len(sentence) - 1, -1, -1):
        reversed_sentence += sentence[i]

    print("Reversed sentence:", reversed_sentence)
sentence = input("Enter a sentence: ")
reversed_sen(sentence)
