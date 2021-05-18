# Kérjünk be egy kilométerben mért távolságadatot 
# a felhasználótól, és írjuk ki tengeri mérföldre átváltva! 
# (Egy tengeri mérföld 1852méter.)
távolság= float( input("Írd be a távolságot km -ben: "))
tengeri_mérföld=távolság/1.852
print( "Az adott távolság", tengeri_mérföld, "mérföld",sep="  ")