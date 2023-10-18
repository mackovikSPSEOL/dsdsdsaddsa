smer_prava = "doprava"
smer_leva = "doleva"
smer_rovne = "rovne"
smer_zpet = "zpet"
inventar = "nic"
print("Vítej v mé únikové hře.\n")
print("Jsi ztracený a musíš najít východ ven\n")
konec_hry = False
while not konec_hry:
    uzivateluv_input = input("\n máš čtyři směry který si vybereš?(doleva, doprava, rovne):")
    
    #M-1
    if uzivateluv_input == "rovne":
        print("Rozhodl ses jít rovně, není tu nic jen nějaké pozůstatky kostí..")
        uzivateluv_input_2 = input("\n není tu nic jiného takže kam půjdeš teď? (rovne, zpet):")
        if uzivateluv_input_2 == "zpet":
            uzivateluv_input = "zadny"
        #M-2
        elif uzivateluv_input_2 == "rovne":
            print("jsou tu zamčené dveře a nemáš nic u sebe")


