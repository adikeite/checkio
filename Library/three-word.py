def checkio(words):
    list = words.split()

    count = 0

    for word in list:

        if word.isalpha():
            count += 1

            if count == 3:
                return True
        else:
            count = 0

    return False

#1 Rozdělím string na jednotlivá slova
#2 Vytvořím count s počáteční hodnotou 0
#3 Pokud slovo v listu obsahuje písmeno, přičtu 1 do count, pokud count == 3, vracím True
#4 Pokud slovo neobsahuje písmeno, nepřičítám do count nic
#5 Jinak vracím False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
