index=0
string = input("enter string : ")
while index < len(string):
    letter = string[len(string)-1-index]
    print(letter)
    index=index + 1
    