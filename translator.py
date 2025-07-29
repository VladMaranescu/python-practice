def translate(phrase):
    translation=" "
    for letter in phrase:
        if letter in "AEIOUaieou":
            translation=translation+"g"
        else:
            translation=translation+letter     
    return translation

print(translate(input("Enter a phrase"))) 
        