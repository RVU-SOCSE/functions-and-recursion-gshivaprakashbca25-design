#NAME-G.SHIVAPRAKASH
#USN-1RUA25BCA0031
#PROGRAM TO COUNT NUMBER OF WORDS

def count_words(sentence):
    words = sentence.split()
    return len(words)

text = input("Enter a sentence: ")
print("Number of words:", count_words(text))
