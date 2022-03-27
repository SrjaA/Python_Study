def seasoz(m):
    month=[(12,1,2),(3,4,5),(6,7,8),(9,10,11)]
    if m in month[1]:
        return "It's spring!"
    if m in month[2]:
        return 'This is SUMMER!'
    if m in month[3]:
        return "It's Autumn :("
    if m in month[0]:
        return 'Winter! (brrr)'
    else: return "There is no such month. Or are you an Aztec?"
print(seasoz(int(input('input number of month:\n'))))


