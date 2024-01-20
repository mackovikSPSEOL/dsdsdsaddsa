import random
import time
pocet_bodu = 0

aktualni_pocet_bodu = 0
cisla_hrace=[]
prvni_kolo = input("\n zmáčkněte ENTER pro start hry!")
hodnota = 0


prvni_hod_kostek_1 = random.randint(1,6)
prvni_hod_kostek_2 = random.randint(1,6)


hodnota = prvni_hod_kostek_1

print(f"padlo ti {prvni_hod_kostek_1} a {prvni_hod_kostek_2}")
if prvni_hod_kostek_1 == 1 or prvni_hod_kostek_2 == 1:
    pocet_bodu = pocet_bodu + 100
    if prvni_hod_kostek_1 == 1 and prvni_hod_kostek_2 == 1:
        pocet_bodu = pocet_bodu + 100
    

elif prvni_hod_kostek_1 == 5 or prvni_hod_kostek_2 == 5:
    pocet_bodu = pocet_bodu + 50
    if prvni_hod_kostek_1 == 5 and prvni_hod_kostek_2 == 5:
        pocet_bodu = pocet_bodu + 50




cisla_hrace.append(prvni_hod_kostek_1) 
cisla_hrace.append(prvni_hod_kostek_2) 

print(f" tvůj aktuální počet bodů je {pocet_bodu}")

druhy_kolo = input("\n jedeme druhé kolo(zmáčkni enter) ")

druhy_hod_kostek_1 = random.randint(1,6)
druhy_hod_kostek_2 = random.randint(1,6)


if druhy_hod_kostek_1 == 1 or druhy_hod_kostek_2 == 1:
    pocet_bodu = pocet_bodu + 100
    if druhy_hod_kostek_1 == 1 and druhy_hod_kostek_2 == 1:
        pocet_bodu = pocet_bodu + 100
    

elif druhy_hod_kostek_1 == 5 or druhy_hod_kostek_2 == 5:
    pocet_bodu = pocet_bodu + 50
    if druhy_hod_kostek_1 == 5 and druhy_hod_kostek_2 == 5:
        pocet_bodu = pocet_bodu + 50
    




cisla_hrace.append(druhy_hod_kostek_1)
cisla_hrace.append(druhy_hod_kostek_2)

print(f"\n teď padly čísla {druhy_hod_kostek_1} a {druhy_hod_kostek_2}")
print(f" tvůj aktuální počet bodů je {pocet_bodu}")
treti_kolo = input("\n třetí a taky poslední kolo, hodně štěstí! (enter)")

treti_hod_kostek1 = random.randint(1,6)
treti_hod_kostek2 = random.randint(1,6)

cisla_hrace.append(treti_hod_kostek1)
cisla_hrace.append(treti_hod_kostek2)


if treti_hod_kostek1 == 1 or treti_hod_kostek2 == 1:
    pocet_bodu = pocet_bodu + 100
    if treti_hod_kostek1 == 1 and treti_hod_kostek2 == 1:
        pocet_bodu = pocet_bodu + 100
    

elif treti_hod_kostek1 == 5 or treti_hod_kostek2 == 5:
    pocet_bodu = pocet_bodu + 50
    if treti_hod_kostek1 == 5 and treti_hod_kostek2 == 5:
        pocet_bodu = pocet_bodu + 50
    
print(f"Poslední kolo a padlo ti číslo {treti_hod_kostek1} a {treti_hod_kostek2}!")


if prvni_hod_kostek_1 == prvni_hod_kostek_2 and hodnota != 1:
    
    if druhy_hod_kostek_1 == prvni_hod_kostek_1 or druhy_hod_kostek_2 == prvni_hod_kostek_1:
        if druhy_hod_kostek_1 == prvni_hod_kostek_1 and druhy_hod_kostek_2 == prvni_hod_kostek_1:
            if treti_hod_kostek1 == prvni_hod_kostek_1 and treti_hod_kostek2 == prvni_hod_kostek_1:
                pocet_bodu = pocet_bodu + hodnota * 800
            if treti_hod_kostek1 == prvni_hod_kostek_1 or treti_hod_kostek2 == prvni_hod_kostek_1:
                pocet_bodu = pocet_bodu + hodnota * 400
            pocet_bodu = pocet_bodu + hodnota * 100
       

if prvni_hod_kostek_1 == 1 and prvni_hod_kostek_2 == 1:

    if druhy_hod_kostek_2 == 1 or druhy_hod_kostek_2 == 1:

        if druhy_hod_kostek_2 == 1 and druhy_hod_kostek_2 == 1:
            if treti_hod_kostek1 == 1 or treti_hod_kostek2 == 1:

                if treti_hod_kostek1 == 1 and treti_hod_kostek2 == 1: 
                    pocet_bodu = pocet_bodu + 8000

                pocet_bodu = pocet_bodu + 4000
            pocet_bodu = pocet_bodu + 2000
        pocet_bodu = pocet_bodu + 1000

if prvni_hod_kostek_1 == prvni_hod_kostek_2:
    if druhy_hod_kostek_1 == druhy_hod_kostek_2:
        if treti_hod_kostek1 == treti_hod_kostek2:
            pocet_bodu = pocet_bodu + 1000


postupka = [1,2,3,4,5,6]
postupka_kostek = [prvni_hod_kostek_1, prvni_hod_kostek_2, druhy_hod_kostek_1, druhy_hod_kostek_2, treti_hod_kostek1, treti_hod_kostek2]

if sorted(postupka_kostek) == postupka:
    pocet_bodu = pocet_bodu + 1500


print("\n KONEC hry")
print(f"Tvůj finalní počet bodů:{pocet_bodu}!")


            
        






    