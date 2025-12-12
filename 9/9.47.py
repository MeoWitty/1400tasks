for byk in range(0, 11):
    for korova in range(0, 21):
        telenok = 100 - byk - korova
        if byk * 10 + korova * 5 + telenok * 0.5 == 100:
            print(byk, korova, telenok)