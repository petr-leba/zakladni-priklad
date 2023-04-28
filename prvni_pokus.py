def check_entry(a):
    try:
        result = int(a)
    except ValueError:
        raise ValueError("Zadaná hodnota není číslo.")
    return result


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def chentry():
    vstup = input("Zadejte číslo: ")
    try:
        result = int(vstup)
    except ValueError:
        raise ValueError("Zadaná hodnota není číslo.")

    return result


vstup = "1234"
cislo = check_entry(vstup)
cislo = chentry()

if is_even(cislo):
    print("Zadané číslo je sudé.")
else:
    print("Zadané číslo je liché.")
