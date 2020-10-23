#Skrevet af Dorte Krohn
uge = ("søndag", "mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag")   #Tuple til at holde de 7 ugedage. 
                                                                                #Jeg har valgt tuple-listen, fordi den er sorteret og ikke kan ændres

#Lav et program hvor brugeren indtaster et tal fra 1-7 og programmet så fortæller hvad dag det er:

dag = input("Skriv et tal mellem 1 og 7. Så får du at vide hvilken dag, det er: ")

#fx. 2 -> Mandag    , 4 -> Onsdag

dag = int(dag) - 1   #Skift datatypen fra streng til heltal og træk 1 fra for at få den rigtige dag. Tuples starter med index 0.
if dag > 0 and dag < 8:
    print(uge[dag])
else:
    print("Du kan kun vælge et tal mellem 1 og 7.")
