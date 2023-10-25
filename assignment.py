# Assignment 1

def leapyear():
    year = int(input("Enter a year: "))

    if year%4 ==0:
        print("Year",year,"is a leap year")
    else:
        print("year",year,"is NOT a leap year")

leapyear()

# Assignment 2

def lettercheck():
    letter = str(input("Enter your letter:"))
    vowels=['A','E','I','O','U','a','e','i','o','u']
    is_vowel = False
    if letter in vowels:
        isVowel = True
        print(letter,"is a vowel")
lettercheck()