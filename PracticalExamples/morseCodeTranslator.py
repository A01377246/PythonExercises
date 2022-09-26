

def translateToMorse(String):
    capitalizedString = String.upper()

    morseDictionary = {"A": "._", "B": "_...", "C":"_._.", "D": "_..", "E": ".", "F": ".._.", "G": "_ _.", "H": "....", "I": "..", "J":"._ _ _",
    "K":"_._", "L":"._..","M":"_ _", "N":"_.", "O": "_ _ _", "P":"._ _.", "Q":"__._", "R":"._.","S":"...","T":"_","U":".._","V":"..._","W":".__", "X":"_.._", "Y":"_.__", "Z":"__..",
    1:". _ _ _ _", 2: ".. _ _ _", 3: "... _ _ ", 4:".... _", 5:".....", 6:"_.....", 7:"_ _....", 8:"_ _ _ ..", 9:"_ _ _ _ .",0:"_ _ _ _ _", " ": "...", ",": "_ _.._ _"}

    morseEncodedString = ""
    for character in capitalizedString:
        if character in morseDictionary.keys():
            morseEncodedString += morseDictionary[character]
            morseEncodedString += " "

    return morseEncodedString

def main():
    print(translateToMorse("Hi"))
    print(translateToMorse("Let us count up to three: 1 2 3 "))
    print(translateToMorse("I like Python"))

main()