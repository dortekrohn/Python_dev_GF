print("Dette program udskriver alle heltal, der ender på 7, inden for rækken 0-1000")
liste=[]

for tal in range(7, 1001, 10):
    liste.append(tal)
    #print(tal, end=', ')
    
print(liste, end=', ')

x = len(liste)
print("\n Der er ")
print(x)
print(' tal i listen.\n')
print('\n Summen af tallene er ')
print(sum(liste))

print('\n')
print("Og her kommer alle de tal, der ender på 13")
for nummer in range(13, 1000, 100):
    print(nummer, end=', ')
