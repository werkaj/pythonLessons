def add_frac(frac1, frac2):
    return [frac1[0]*frac2[1] + frac2[0]*frac1[1] ,frac1[1]*frac2[1]]        # frac1 + frac2

def sub_frac(frac1, frac2):
    return [frac1[0]*frac2[1] - frac2[0]*frac1[1] ,frac1[1]*frac2[1]]          # frac1 - frac2

def mul_frac(frac1, frac2):
    return [frac1[0]*frac2[0], frac1[1]*frac2[1]]        # frac1 * frac2

def div_frac(frac1, frac2):
    return [frac1[0]*frac2[1], frac1[1]*frac2[0]]        # frac1 / frac2

def is_positive(frac):
    return (frac[0]>0 and frac[1]> 0) or (frac[0]<0 and frac[1]< 0)            # bool, czy dodatni

def is_zero(frac):
    return frac[0]==0                 # bool, typu [0, x]

def cmp_frac(frac1, frac2):
    if(frac1[0]*frac2[1]<frac2[0]*frac1[1]):
        return -1
    elif(frac1[0]*frac2[1]>frac2[0]*frac1[1]):
        return 1
    else:
         return 0        # -1 | 0 | +1

def frac2float(frac):               # konwersja do float
    return float(frac[0]/frac[1])

def tear_down(frac):
    return frac[0]//frac[1]