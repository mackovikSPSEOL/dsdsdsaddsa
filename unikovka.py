import random
zivot = 3
smer_prava = "doprava"
smer_leva = "doleva"
smer_rovne = "rovne"
smer_zpet = "zpet"
inventar = "nic"
print("Vítej v mé únikové hře.\n")
print("Jsi ztracený, musíš najít východ ven a máš pouze 3 životy.\n")
konec_hry = False
while not konec_hry:
    #M-0
    uzivateluv_input = input("\n máš tři směry který si vybereš?(doleva, doprava, rovne):\n")
    
    if zivot == 0:
        konec_hry = "smrt"
        break;
    #M-1
    if uzivateluv_input == "rovne":
        print("\n Rozhodl ses jít rovně, není tu nic jen nějaké pozůstatky kostí..")
        uzivateluv_input_2 = input("není tu nic jiného takže kam půjdeš teď? (rovne, zpet):")
        if uzivateluv_input_2 == "zpet":
            uzivateluv_input = "zadny"

        #M-2
        elif uzivateluv_input_2 == "rovne":

            #pokud ma klic => M-3
            if inventar == "klic":
                print("odemykáš dveře a utíkáš ven povedlo se ti utíct...")
                konec_hry = "utek"
                break;
            
            #pokud nema klic => M-0
            if inventar == "nic":
                print("jsou tu zamčené dveře a nemáš nic u sebe")
                print("musíš se vrátit na začátek")
                uzivateluv_input = "nic"
    #M-7
    if uzivateluv_input == "doprava":
        print("je tu někdo.. blíží se k tobě")
        uzivateluv_boj = input("pokusíš se utéct nebo bojovat (utek, bojovat):")
        if uzivateluv_boj == "utek":
            sance = random.randint(0,1)
            if sance == 1: 
                print("povedlo se ti utéct, jsi zpět")
                uzivateluv_input = "nic"
            elif sance == 0:
                print("nepovedlo se ti utéct -1 život, ale jsi zpět\n")
                zivot = zivot - 1
                print(f"aktuální počet životů:{zivot}.")
                uzivateluv_input = "nic"

        elif uzivateluv_boj == "bojovat":
            sance = random.randint(0,1)
            if sance == 1: 
                print("povedlo se ti ho zabít, jdeš zpět")
                uzivateluv_input = "nic"
            elif sance == 0:
                print("prohrál si boj, -1 život\n")
                zivot = zivot - 1
                print(f"aktuální počet životů:{zivot}.")
                uzivateluv_input = "nic"

    #M-5
    if uzivateluv_input == "doleva":
        uzivateluv_boj = "boj" 
        print("pokousíš bojovat s nějakým stínem.\n")
        sance = random.randint(0,1)
        if sance == 1:
            uzivateluv_input_2= input("tento boj si vyhrál, mužeš jít dál nebo zpět(doleva, zpet):")
        elif sance == 0:
            zivot = zivot - 1
            print(f"aktuální počet životů:{zivot}.")
            uzivateluv_input_2 = input("tento boj si prohrál -1 život, mužeš jít dál nebo zpět(doleva, zpet):")
            
        #M-6
        if uzivateluv_input_2 == "doleva":
            print("našel jsi KLÍČ, teď rychle utíkej zpět ke dveřím!\n")
            inventar = "klic"
            uzivateluv_input_2 = "zpet"
        if uzivateluv_input_2 == "zpet":
            print("jsi zase na začátku... kudy teď?\n")
            uzivateluv_input = "nic"



        
        
           
                
                






if konec_hry == "utek":
    print("vyhrál jsi, konec hry!\n")
    if zivot == 1:
        print("zůstal ti 1 život.")
    if zivot >= 2:
        print(f"zůstaly ti {zivot} životy.")

elif konec_hry == "smrt":
    print("prohrál jsi, konec hry\n")
else:
    print("chyba")
    print(f"uzivateluv input je {uzivateluv_input}")
    print(f"uzivateluv input_2 je {uzivateluv_input_2}")
    print(f"sance = {sance}")
    print(f"inventar = {inventar}")



