import random
import string
import time




vysledek = []
konec = 0

while True:
    delka_slova2 = random.randint(1,12)
    if konec == 1:
        break;
    nastaveni_textu = input("vyberte jednu z možností podle které chcete nastavit kritéria,(paragraf, slova, stranky):")

    while nastaveni_textu not in ["paragraf","slova","stranky"]:
        nastaveni_textu = input("vyberte jednu z možností podle které chcete nastavit kritéria,(paragraf, slova, stranky):")

    delka_slova = input("jak dlouhe mají být slova?(pokud nahodně napište ""random""):")


    
    while delka_slova.isalpha() or not delka_slova:
        if delka_slova == "random":
            break
        print("toto není číslo")
        delka_slova = input("jak dlouhe mají být slova?(pokud nahodně napište ""random""):")


        





    while nastaveni_textu == "paragraf" or nastaveni_textu == "slova" or nastaveni_textu == "stranky":



        if nastaveni_textu == "paragraf":
            print("\n")
            pocet_paragrafu = input("vložte číslo, které definuje počet paragrafů:")
            while not pocet_paragrafu or pocet_paragrafu.isalpha():
                print("tohle není číslo, neumíš psát")
                pocet_paragrafu = input("vložte číslo, které definuje počet paragrafů:")

            pocet_paragrafu =int(pocet_paragrafu)
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

            break


        elif nastaveni_textu == "slova":
            print("\n")
            pocet_slov = input("zadejte číslo, které definuje počet slov:")
            while not pocet_slov or pocet_slov.isalpha():
                print("tohle není číslo, fakt si marný")
                pocet_slov = input("zadejte číslo, které definuje počet slov:")
            pocet_slov = int(pocet_slov)
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
            pocet_stran = input("zadejte číslo, které definuje počet stran(A4):")
            while not pocet_stran or pocet_stran.isalpha():
                print("o co se furt snažíš?")
                pocet_stran = input("zadejte číslo, které definuje počet stran(A4):")
            pocet_stran = int(pocet_stran)
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

    








