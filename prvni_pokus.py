def check_entry():
    result = int(input("Zadejte číslo: "))
    return result


cislo = check_entry()

if cislo % 2 == 0:
    print("Zadané číslo je sudé.")
else:
    print("Zadané číslo je liché.")
