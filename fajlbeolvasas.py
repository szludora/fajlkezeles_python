nevek = []
nemek = []
korok = []


def uj_adat_bekeres():
    import random
    '''Bekéri az adatot konzolról, majd meghívja a másik függvényt, átadja neki a paramétereket'''

    nev = input("Neved?")

    nem = input("férfi/nő vagy?")
    while nem != "férfi" and nem != "nő":
        nem = input("férfi/nő vagy?")

    kor = int(random.random()*10)+70

    uj_adat_rogzitese(nev, nem, kor)


def uj_adat_rogzitese(nev, nem, kor):
    '''A kapott adatokat beírja a txt fájlba, bezárja a doksit, majd meghívja a beolvasás fv-t'''

    uj_adat = "\n" + nev + ", " + nem + ", " + str(kor)

    fajliras = open("teszt.txt", "a", encoding='utf-8')
    fajliras.write(uj_adat)
    fajliras.close()

    beolvas("teszt.txt")


def beolvas(fajlnev):
    '''megnyitja a doksit, meghívja a fajlfeldolgozas fv-t'''
    fajlom = open(fajlnev, "r", encoding='utf-8')

    fejlec = fajlom.readline().strip()  # első sor beolvasása | strip kiveszi belőle a \n-t
    print(fejlec)

    sorok = fajlom.readlines()  # listaként tér vissza
    # print(sorok)

    fajlfeldolgozas(sorok)
    fajlom.close()


def fajlfeldolgozas(sorok):
    '''itt adja a listához hozzá az adatokat'''

    i = 0

    while i < len(sorok):
        sor = sorok[i].strip().split(", ")
        # print(sor)    kiirathatom a sorokat is
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(sor[2])
        i += 1


def statisztika():

    ossz_eletkor = 0
    nonemu = 0
    legfiatalabb_no_kora = 99999

    i = 0
    while i < len(nevek):
        ossz_eletkor += int(korok[i])
        if nemek[i] == "nő":
            nonemu += 1
            if int(korok[i]) < legfiatalabb_no_kora:
                legfiatalabb_no_kora = int(korok[i])
        i += 1

    atlag_eletkor = ossz_eletkor / len(nevek)

    # print(nevek)
    # print(nemek)
    # print(korok)

    print(f"{len(nevek)} fő adata rögzítve (összesen {len(nemek) + len(nevek) + len(korok)} db adat tárolva).")

    print(f"Az átlagéletkor: {atlag_eletkor:.1f}\n"
          f"Nők száma: {nonemu}\n"
          f"Legfiatalabb nő: {legfiatalabb_no_kora} éves")


def elolvas(fajlnev):

    fajlom = open(fajlnev, "r", encoding='utf-8')
    sorok = fajlom.readlines()

    i = 0
    while i < len(sorok):
        print(sorok[i].strip())
        i += 1

    fajlom.close()