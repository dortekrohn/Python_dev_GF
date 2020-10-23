#Skrevet af Dorte Krohn
# Lav et program hvor brugeren kan indtaste et tal 'n' og programmet udregner summen af heltallene fra og med 1 til og med 'n'.

# bed brugeren indtaste et heltal og gem det i en variabel
# Variablen bruges som stop-betingelse i en løkke

valg = input("Skriv et heltal: ")
sum = 0   #variablen sum bruges til at tælle tallet 1 op for hver gang løkken kører
ialt = 0   #variablen ialt bruges til at lægge tallen fra 1 til valg sammen 

# I løkken lægges tallene fra 1 til variablen sammen. Jeg skifter datatype på variablen valg for at kunne regne med den.

while sum < int(valg) :
    sum = sum + 1
    ialt = ialt + sum

print("Summen fra 1 til " + str(valg) + " er: " + str(ialt))

# Resultatet udskrives til brugeren på skærmen

