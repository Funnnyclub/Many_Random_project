me_str = "Ебать копать мандарины и валера"
me_int = 23
dn = ["abd","bbbs","abrakadabra"]

with open(file = 'pass.txt', mode = 'a', encoding= "utf-8") as file:
    file.writelines([line + '\n' for line in dn])