def razr(x):
    vol=[]
    vol.append(x // 86400)
    vol.append(x//3600)
    vol.append(x//60)
    vol.append(x%60)



    return vol
print(razr(1234809))