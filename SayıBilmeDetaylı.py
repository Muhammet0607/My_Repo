from turtle import back, clear
import include
import random
import os
import time


sayı=random.randint(1,10)

hak=5

while True:
   
   evetler=["evet","Evet","EVET","E","e","yes","he"]
   
  
   

   try:
       a=int(input ("1-10 arası sayı tahmin edin: "))

       print(f"Girdiğiniz sayı: {a} \n")
       if a>1 and a<10:
        
         if a==sayı:
             print("Tebrikler bildiniz \n")
             break
             
        

         else:
             hak=hak-1
             if hak==0:
                 print("Hakkınız bitti")
                 break

             print("Yanlış Tahmin Tekrar deneyin \n")
             
            

       else:
          
           os.system("cls")
           print(f'"{a}"'+", 1-10 arasında bir sayımı?")
           b=input()
           

           if b in evetler:
               print("Matematik öğrenip bidaha gel \n")
               break
           else:
                print("o zaman doğru sayı gir \n")

   except ValueError:
       print("Lütfen sayı giriniz \n")

   
   


   
      