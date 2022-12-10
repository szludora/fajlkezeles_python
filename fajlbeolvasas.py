nevek = []
nemek = []
korok = []

def beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='utf-8')
    # print(fajlom)

    fejlec = fajlom.readline().strip()  # első sor beolvasása | strip kiveszi belőle a \n-t
    print(fejlec)

    sorok = fajlom.readlines()  # listaként tér vissza
    # print(sorok)

    fajlom.close()

    fajlfeldolgozas(sorok)


def fajlfeldolgozas(sorok):
    """itt dolgozom fel a kapott listát"""
    i = 0

    while i < len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(", ")
        print(sor)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(int(sor[2]))
        i += 1

    print(nevek)
    print(nemek)
    print(korok)
