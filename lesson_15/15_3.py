def mult(x):
    if isinstance(x, tuple):
        sum_ = 0
        for i in x:
            sum_ += len(i)
        return (f'Total word length - {sum_} characters.')
    if isinstance(x, list):
        digg = 0
        lett = 0
        for h in x:
            for g in h:
                if g.isdigit():
                    digg += 1
                elif g.isalpha():
                    lett += 1
                else:
                    continue
        return (f'Letters - {lett} \\\// digits - {digg}.')
    if isinstance(x, int):
        x = str(x)
        fi = 0
        for r in x:
            if int(r) % 2 != 0:
                fi += 1
        return (f'ODD digits - {fi}.')
    if isinstance(x, str):
        lette = 0
        for d in x:
            if d.isalpha():
                lette += 1
        return (f'ALL letters - {lette}.')

#m = ('ergeg', 'rtpopcgf', 'ghlkldkfg', 'fgklkler')
#m = ['er$g,43e1g', 'rv6]tpo3m^46p.cre,67gf', 'g34hl.kld.45kfg', 'f2gk8/l6kle.r']
#m=1234567890
m = '4jdf8965k;g089lie;hgiul657l;d9045kl;jd^'

print(mult(m))
