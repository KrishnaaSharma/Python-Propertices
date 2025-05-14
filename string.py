
#string Method

text = "Captain America: Brave New World"

print("Uppercase:" ,text.upper())
print("LowerCase:", text.lower())
print("casefold:", text.casefold())
print("Capitalized:", text.capitalize())
print("Title:", text.title())

print()

text2 = '   Avengers      '

print("Stripped:", text2.strip())
print("Left Stripped:", text2.lstrip())
print("Right Stripped:", text2.rstrip())

print()
text3 = "Eisha is good girls"

print("Start with  eisha:", text3.startswith("Eisha")) # True
print("End with girls:", text3.endswith("good"))# Flase
print("replace eisha with enna: ", text3.replace("Eisha"," Anna")) # Anna is good girls

print()











