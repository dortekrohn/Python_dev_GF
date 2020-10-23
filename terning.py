#Skrevet af Dorte Krohn
#Importer modulet random til at generere et tilfældigt tal
import random

#1 del af opgaven
print("Opgave 1")
kast = random.randint(1, 6)
print("Din terning slog " + str(kast))

#2 del af opgaven
print("Opgave 2")
fireKast = []    #En tom liste til de fire kast
i = 0    #En tæller
sum = 0    #En sum-beholder

while i < 4:
    kast = random.randint(1, 6)
    fireKast.append(kast)
    print(fireKast[i])
    sum = sum + fireKast[i]
    i += 1

print("Dine 4 terninger slog ialt " + str(sum) + " øjne.")


#3 del af opgaven
print("Opgave 3")
valg = int(input("Hvor mange terninger vil du slå med? "))   #Brugerinput, hvor mange terninger.

summen = 0
mangeKast = []
n = 0

while n < valg:
    kast = random.randint(1, 6)
    mangeKast.append(kast)
    print(mangeKast[n])
    summen = summen + mangeKast[n]
    n += 1

print("Dine "+ str(valg) + " terninger slog ialt " + str(summen) + " øjne.")
