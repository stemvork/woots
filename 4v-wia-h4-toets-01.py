import numpy, datetime, scipy
vraag = 2021012901
seed = vraag+(datetime.date.today()-datetime.date(1,1,1)).days
# numpy.random.seed(seed)

def combinatie(n,k):
    return str(n)+"C"+str(k)

# Telwoorden[0] en rangwoorden[1] in een dictionary
telwoorden  = "nul,een,twee,drie,vier,vijf,zes,zeven,acht,negen,tien,elf,twaalf".split(',')
rangwoorden = "nulde,eerste,tweede,derde,vierde,vijfde,zesde,zevende,achtste,\
        negende,tiende,elfde,twaalfde".split(',')
getalwoorden = {k: (a, b) for k, (a, b) in enumerate(zip(telwoorden,rangwoorden))}
print(f"Getalwoorden\n Een: {getalwoorden[1]} \n")

# Opgave 1a
ida = random(4,7,1) # 4 t/m 7
rij = getalwoorden[ida][1] # vierde t/m zevende
combinaties = ", ".join([combinatie(ida-1,i) for i in range(0,ida)]) # vierde: 3C0, 3C1, 3C2, 3C#
wcombinaties = ", ".join([str(int(scipy.special.comb(ida-1,i))) for i in range(0,ida)])
print(f"Opgave 1a\n Rij: {rij}\n Antwoord: {combinaties} ({wcombinaties}).\n")

# Opgave 1b
idb = random(2,9,1) # twee t/m tien
A = getalwoorden[idb][0] # vier
B = getalwoorden[11-idb][0] # zeven
aantal = combinatie(11,idb) + " of " + combinatie(11,11-idb)
waantal = str(int(scipy.special.comb(11,idb)))
print(f"Opgave 1b\n Er zijn {A} A's en {B} B's.\n Aantal: {aantal} ({waantal}).\n")
