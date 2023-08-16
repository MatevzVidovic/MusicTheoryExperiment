


import numpy as np
from scipy.io import wavfile
import scipy as sc


# https://towardsdatascience.com/music-in-python-2f054deb41f4

import numpy as np

def get_piano_notes():   
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 440 #Frequency of Note A4
    keys = np.array([x+str(y) for y in range(0,9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == 'A0')[0][0]
    end = np.where(keys == 'C8')[0][0]
    keys = keys[start:end+1]
    
    note_freqs = dict(zip(keys, [2**((n+1-49)/12)*base_freq for n in range(len(keys))]))
    note_freqs_backwards = (zip([2**((n+1-49)/12)*base_freq for n in range(len(keys))], keys))

    note_freqs[''] = 0.0 # stop
    return note_freqs, note_freqs_backwards

import numpy as np

def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave








def lists_identical(first, second):
    for i in range(len(first)):
        if first[i] != second[i]:
            return False
    return True


allKeysThatWork = list()


# Get middle C frequency
note_freqs, note_freqs_breversed = get_piano_notes()
frequency = note_freqs['C4']

octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
key_constant = '4'


# Okej, kaj tocno je moj plan tukaj?

# Imel bom neko zaporedje korakov, neko mantiso. So polkoraki in koraki.
# V smislu polkorakov se to zaporedje sesteje v n (ki je vec kot 12).
# Izbrali bomo, kateri ton bo zaceten - tonic.
# Nasli bomo, kateri vsi toni potem pripadajo v njegovo lestvico, ce gremo samo po teh korakih, ki se sestejejo v n.
# Potem pa ta note, na katerega smo ravno pristali kot n-ti half step naprej, postane novi tonic za to mantiso.
# In ce ta proces ponavljamo, a bomo eventually dobili vse tone? Pac to e vprasanje.

# Samo kako dolgo zdaj to ponavljat, preden vemo for sure?
# Dokler ton, ki mora biti naslednji tonik, ni enkrat že bil tonik.
# Od takrat naprej bo pattern isti.
# Pa to se zagotovo zgodi v 12 iteracijah ker potem že zmanjka možnih tonov za tonike.

# Narediti moram major in minor razmake. Potem pa za vsako dodam na koncu ali začetku en cel ton.
# In sprobam, če pri 12tih tonih (niti ni važno, kater je začetni), ta pattern potem deluje.

# in potem dodam še en cel ton na začetek ali konec. Itd. do recimo tega, da sem dodal 6 celih tonov in je zdaj span že za dve oktavi.

# In če pattern deluje, potem naredim za vseh 12 tonov kot začetnih lestvice, in jih naredim v music files z njihovim pravim imenom.






is_in_for_each = [False] * 12
is_in_for_each_previous = is_in_for_each

for startingNote in range(0, 12):

    ix = startingNote
    relative_note = ix % 12

    is_in_for_each[relative_note] = True

    while (not (lists_identical(is_in_for_each, is_in_for_each_previous))):
        ix += 1
        relative_note = ix % 12
        relative_note[ix] = True


    if not lists_identical(is_in_for_each, octave):
        allKeysThatWork.append(is_in_for_each)




# Pure sine wave
sine_wave = get_sine_wave(frequency, duration=2, amplitude=2048)
wavfile.write('pure_c.wav', rate=44100, data=sine_wave.astype(np.int16))