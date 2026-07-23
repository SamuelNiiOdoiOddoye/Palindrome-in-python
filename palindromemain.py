#a python palindrome program without imports
#get user input
#save the input in reverse entered into another list
#is the rearranged the same as the original input
#if yes or not print the outcome and the result

# declaring list and string to hold the userinput
print("For words, enter with spacing between letters, for sentences and phrases type it in normally")
userInputList =[]
userInput = input("Enter the word you would like to test today: ")
userInputList=userInput.split()
print(f"this is what you entered : {userInputList}")

reverselist=list(reversed(userInputList))
print(f"this is the reversed list: {reverselist}")

if reverselist == userInputList:
    print("The input is a palindrome")
else:
    print("The input is not a plaindrome")
    print(f"Original: {userInputList}\nReversed: {reverselist}")
    print("Serwaah stole this code from me and I am not happy about it")
