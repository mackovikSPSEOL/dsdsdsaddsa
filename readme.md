# Hrací kostky naprogramovány podle Matyáše Mackovíka!

## Postup
Postupoval jsem tak, že jsem udělal 3 kola 
pro každý kolo je vlastní proměnná ("prvni_hod_kostek_1", "prvni_hod_kostek_2", atd.).
taky obsahuje proměnnou ("prvni_kolo","druhe_kolo", "treti_kolo") pro počet jednotlivých kol a to z důvodu, kdyby bylo potřeba něco nadále implementovat. Může to působit velice nepřehledně, ale pro budoucí práci se to však může hodit. Vím že to šlo jednodušší cestou ale takhle mi to přišlo ideální. Kód obsahuje velice mnoho podmínek. Například pokud se aspoň jedna kostka v daném kole = 1, tak to přičte body a v této se objevuje další podmínka kde pokud se obě kostky rovnají 1, tak to přičte další body. Během zpracovávání tohoto úkolu jsem chtěl použit funkci "def" jenže jsem již nenašel způsob jak, ale v přístím úkolu bych této funkce chtěl využít pro jeho lepší přehlednost. 
Největší problém pro mě byl naprogramování stejných čísel 3-6x a ocenil bych rady, jakými by to šlo udělat jednodušší.

## Funkčnost
V tomto kódu, jsem použil na můj vkus až moc podmínek a je mi zcela jasné, že to šlo udělat velice jednoduchým způsobem, který mě nenapadl.