


import numpy as np
from scipy.io import wavfile
import scipy as sc

import math




def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave


def freqFromDistanceFromA4(distance):
    base_freq = 440 #Frequency of Note A4
    freq = 2**((distance)/12) * base_freq



# returns -1 if not close
def closeToThisPositiveInteger(givenNum, acceptedError=10e-4):
    floor = math.floor(givenNum)
    ceil = math.ceil(givenNum)
    
    if (abs(givenNum - floor) < acceptedError):
        return floor
    
    if (abs(givenNum-ceil) < acceptedError):
        return ceil

    return -1


def multiplyToWholeNumber (givenList, acceptedError=10e-4):
    returningNumerators = givenList.copy()
    returningDenominators = [1 for i in givenList]

    for i in range(len(givenList)):
        while(closeToThisPositiveInteger(returningNumerators[i], acceptedError) == -1):
            returningDenominators[i] += 1
            returningNumerators[i] += givenList[i]
        returningNumerators[i] = closeToThisPositiveInteger(returningNumerators[i], acceptedError)
    
    returningFractions = list(zip(returningNumerators, returningDenominators))
    return returningFractions



# Tu je float64 ker float128 ne deluje za windows
razmerjaVsehNotLestvice = np.arange(0,36, dtype=np.float64)
# print(razmerjaVsehNotLestvice)
# print(razmerjaVsehNotLestvice/12)
# print(2**(razmerjaVsehNotLestvice/12))
razmerjaVsehNotLestvice = 2**(razmerjaVsehNotLestvice/12)

# Tu je 10e-4, ker pri -6 se ze zgodi tak inflation stevilk da je tezko interpretirat
# No ne, -3 in -2 data actually lepe rezultate.
print("-3 napaka:")
mnoziDoklerNiLepoStevilo = multiplyToWholeNumber(razmerjaVsehNotLestvice, 10e-3)

print(mnoziDoklerNiLepoStevilo[0:12])
print(mnoziDoklerNiLepoStevilo[12:24])
print(mnoziDoklerNiLepoStevilo[24:36])



print("-2 napaka:")
mnoziDoklerNiLepoStevilo = multiplyToWholeNumber(razmerjaVsehNotLestvice, 10e-2)

print(mnoziDoklerNiLepoStevilo[0:12])
print(mnoziDoklerNiLepoStevilo[12:24])
print(mnoziDoklerNiLepoStevilo[24:36])
