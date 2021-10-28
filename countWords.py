introString= input("Enter your Introduction:")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount=characterCount+1
    if(i==" "):
        wordCount = wordCount+1
        print("number of words in the string:")
        print(wordCount)
        print("number of charecters in the string")
    print(characterCount)
