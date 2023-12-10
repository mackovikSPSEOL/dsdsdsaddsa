import random
import string
import time

vysledek = []
konec = 0

while True:
    if konec == 1:
        break;
    nastaveni_textu = input("vyberte jednu z možností podle které chcete nastavit kritéria,(paragraf, slova, stranky):")
    delka_slova = input("jak dlouhe mají být slova?(pokud nahodně napište ""random""):")

    if delka_slova == "random":
        delka_slova2 = random.randint(1,12)
    
    
        





    while nastaveni_textu == "paragraf" or nastaveni_textu == "slova" or nastaveni_textu == "stranky":



        if nastaveni_textu == "paragraf":
            print("\n")
            pocet_paragrafu = int(input("vložte číslo, které definuje počet paragrafů:"))
            pocet_slov = pocet_paragrafu * random.randint(60,130)
            if delka_slova == "random":
                for neco in range(pocet_slov):
                    nove_slovo = ''.join(random.choice(string.ascii_lowercase) for neco in range(delka_slova2))
                    delka_slova2 = random.randint(1,12)
                    vysledek.append(nove_slovo)
            else:
                for neco in range(pocet_slov):
                    nove_slovo = ''.join(random.choice(string.ascii_lowercase) for neco in range(int(delka_slova)))
                    vysledek.append(nove_slovo)

            break;


        elif nastaveni_textu == "slova":
            print("\n")
            pocet_slov = int(input("zadejte číslo, které definuje počet slov:"))

            if delka_slova == "random":
                for neco in range(pocet_slov):
                    nove_slovo = ''.join(random.choice(string.ascii_lowercase) for neco in range(delka_slova2))
                    delka_slova2 = random.randint(1,12)
                    vysledek.append(nove_slovo)
            else:
                for neco in range(pocet_slov):
                    nove_slovo = ''.join(random.choice(string.ascii_lowercase) for neco in range(int(delka_slova)))
                    vysledek.append(nove_slovo)
            break;
    



        elif nastaveni_textu == "stranky":
            print("\n")
            pocet_stran = int(input("zadejte číslo, které definuje počet stran(A4):"))
            pocet_slov = pocet_stran * random.randint(200,250)
            if delka_slova == "random":
                for neco in range(pocet_slov):
                    nove_slovo = ''.join(random.choice(string.ascii_lowercase) for neco in range(delka_slova2))
                    delka_slova2 = random.randint(1,12)
                    vysledek.append(nove_slovo)
            else:
                for neco in range(pocet_slov):
                    nove_slovo = ''.join(random.choice(string.ascii_lowercase) for neco in range(int(delka_slova)))
                    vysledek.append(nove_slovo)
            break;

    if nastaveni_textu == "paragraf" or nastaveni_textu == "slova" or nastaveni_textu == "stranky":
        x = 6 
        while x <= 6 and x >= 1:
            print(f"\n")
            x -= 1
            time.sleep(1)
            print(f"už zbývá {x} sekund.")
        print("\n \t")
        print(' '.join(vysledek))

        while True:
            uzivateluv_vyber = input("chcete vytvořit textový soubor? (ano, ne):")
            if uzivateluv_vyber == "ano":
                nazev_souboru = input(str("jak se má textový soubor jmenovat?:"))
                nazev_souboru += ".txt"
                with open(nazev_souboru, 'w') as file:
                    file.write(str(vysledek))
                    print(f"byla vytvořena šložka s názvem {nazev_souboru}")
                    print("\n KONEC PROGRAMU, děkuji za pozornost:)")
                    konec = 1
                    break;
            elif uzivateluv_vyber == "ne":
                print("dobře, nevytvářím textový soubor s tímto textem.")
                konec = 1
                break;
                
            else:
                print("někde se stala chyba, asi neumíš psát. ") 
        
        



else:
   
    print("špatně, nedokážeš napsat ani jednu z vybraných možností?")

    








