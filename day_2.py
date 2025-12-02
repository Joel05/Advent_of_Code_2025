input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

real_input = "2200670-2267527,265-409,38866-50720,7697424-7724736,33303664-33374980,687053-834889,953123-983345,3691832-3890175,26544-37124,7219840722-7219900143,7575626241-7575840141,1-18,1995-2479,101904-163230,97916763-98009247,52011-79060,31-49,4578-6831,3310890-3365637,414256-608125,552-1005,16995-24728,6985-10895,878311-912296,59-93,9978301-10012088,17302200-17437063,1786628373-1786840083,6955834840-6955903320,983351-1034902,842824238-842861540,14027173-14217812"

split_input = real_input.split(",")

id_pairs = []

solution = 0

set = False

for id_range in split_input:  #Jede ID auswählen
    id_pairs.append(id_range.split("-"))

for id_pair in id_pairs:
    for id in range(int(id_pair[0]), int(id_pair[1])+1, 1):
        set = False
        for windowsize in range(1, len(str(id))//2+1):
            if (set== True):
                break
            for position in range(0, len(str(id))-windowsize):
                #if (str(id)[position:position+windowsize] == str(id)[position+windowsize:position+2*windowsize]):
                #    print(id)
                #print(str(id).count(str(id)[position:position+windowsize]), id)
                # if ((str(id).count(str(id)[position:position+windowsize]) == 2) and (windowsize*2 == len(str(id)))): #Überprüfen wie oft das aktuelle Fenster im ganzen String vorkommt
                #     solution += id
                #     print(id)
                #     break
                if ((str(id).count(str(id)[position:position+windowsize]) * windowsize == len(str(id)))):
                    solution += id
                    set = True
                    break


print(solution)
#Ansatz: Fenster definieren, und damit über String fahren, und duplicates suchen, Fenster jeden Schritt immer größer machen, bis es mehr als die Hälfte abdeckt

#Anzahl der duplicates suchen. Anzahl der duplicates * Länge der duplicates == Länge der ID, dann besteht die ID nur aus duplicates