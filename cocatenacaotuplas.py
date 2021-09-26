# Cocatenação de Tuplas

endereco_puc = ("Rua ", 4, "Prado Velho", "Curitiba", "PR")
print(id(endereco_puc))
endereco_puc += ("Brasil",) # A ',' é para ser considerado tupla
print(endereco_puc)
print(id(endereco_puc))