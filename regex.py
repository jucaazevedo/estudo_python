import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
y = re.findall("ain", txt)
z = re.split("ain", txt)
h = re.sub("ain", "juca", txt)

print(type(x))
print(x)
print(y)
print(z)
print(h)

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())


#Split the string at the first white-space character:

x = re.split("\s", str, 1)
print(x)

#Replace the first two occurrences of a white-space character with the digit 9:

x = re.sub("\s", "9", str, 2)
print(x)

#Search for an upper case "S" character in the beginning of a word, and print its position:

x = re.search(r"\bS\w+", str)
print(x.span())

#The string property returns the search string:

x = re.search(r"\bS\w+", str)
print(x.string)


#Search for an upper case "S" character in the beginning of a word, and print the word:

x = re.search(r"\bS\w+", str)
print(x.group())

