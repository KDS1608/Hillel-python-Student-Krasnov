string = input(" ")

print(string[:string.find(" ")], string.replace("n", "N"),  string[string.rfind(" ")+1:])