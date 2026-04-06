def bmi_hesaplayici():
    boy = float(input("Boyunuzu metre cinsinden girin: "))
    kilo = float(input("Kilonuzu kilogram cinsinden girin: "))
    bmi = kilo / (boy ** 2)
    print("Vücut Kitle İndeksiniz: ",bmi)
    if bmi < 18.5:
        print("Zayıf.")
    elif 18.5 <= bmi < 24.9:
        print("Normal.")
    elif 25 <= bmi < 29.9:
        print("Fazla Kilolu.")
    else:
        print("Obez.")


bmi_hesaplayici()
