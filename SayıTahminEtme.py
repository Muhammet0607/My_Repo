import random   

r1 = random.randint(1, 3)

while True:
        
        tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))
        print("sayı: ", r1)

        if tahmin == r1:
            print("Doğru Tahmin");
            break;
        else:
            print("Yanlış Tahmin Tekrar Deneyiniz");
    

