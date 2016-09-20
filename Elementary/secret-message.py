def find_message(text):
    uppers = []

    for letter in text:
        if letter.isupper():
            uppers.append(letter)

    uppers = ''.join(uppers)

    if len(uppers) == 0:
        return ""

    return uppers

#1 vytvořím prázdný list uppers
#2 pro písmeno v textu platí, že když je velké, připojím ho k listu uppers
#3 spojím list písmen do stringu (tj. mám string, kde jsou pouze velká písmena)
#4 pokud je string s velkými písmeny prázdný, vracím ""


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"