# Data type

number = 25  # int
second = 56.78  # float
text = "Hello there" # string
ispythoninteresting = True # bool

# store multiple values in a single variable
cars = ["toyota", "nissam", "vw"] # List - ordered and changeable
fruits = ("banana","orange","apple") # Tuple - ordered and unchangeable
countries = {"Kenya","Tunisia","Algeria"} # Set - Unordered and unchangeable
details = {
    "firstname" : "Bill",
    "age" : 26,
    "course" : "web development",
    "nationality" : "Kenya"
} # Dictionary - key-value pair

print(second)
print(text)
print(ispythoninteresting)
print(cars)
print(countries)
print(details)
print(details["course"])
print(details["age"])

# Determine a data type
print(type(details))
print(type(countries))


# type casting - converting one data type to another
print(float(number))
print(int(second))
