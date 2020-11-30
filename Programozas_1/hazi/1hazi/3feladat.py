def mgh_szamolas():
    db=0
    szo=input('Szavad:')
    szo.lower()
    mgh='aáeéiíoóöőuúüű'
    for i in szo:
        if i in mgh:
            db+=1
    return db

print(mgh_szamolas())