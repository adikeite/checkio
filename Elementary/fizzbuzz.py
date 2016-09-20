def checkio(number):
    if number % 15 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

    return checkio(number)

#1 Pokud je číslo dělitelné 3 a 5 zároveň, tj. 15, vracím "Fizz Buzz"
#2 Pokud je číslo dělitelné 3, vracím "Fizz"
#3 Pokud je číslo dělitelné 5, vracím "Buzz"
#4 Pokud není číslo dělitelné ani 3 ani 5 ani 3 a 5 zároveň, vracím číslo jako string


# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"