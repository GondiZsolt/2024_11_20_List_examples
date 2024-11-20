"""
Hozz létre két listát: [3, 1, 4] és [9, 7, 2]. 
Egyesítsd a két listát, és rendezd a lista elemeit növekvő sorrendbe!
"""
szamok1 = [3, 1, 4]
szamok2 = [9, 7, 2]

szamok1.extend(szamok2)
szamok1.sort()
print(szamok1)

# írasd ki az első és az utolsó elemet!
szamok1 = [3, 1, 4]
szamok2 = [9, 7, 2]

szamok1.extend(szamok2)
szamok1.sort()
print(szamok1)