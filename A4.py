"""
4. Write a function that takes a sentence as input from the user and calculates the frequency of each 
letter. Use a variable of dictionary type to maintain the count. 
"""
def checkFrequency(sentence):
    freq = {}
    for ch in sentence:
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    return freq



sen = input("Enter a sentence: ")
result = checkFrequency(sen)

print("Frequency is:")
for key, val in result.items():
    print(f"{key} = {val}")