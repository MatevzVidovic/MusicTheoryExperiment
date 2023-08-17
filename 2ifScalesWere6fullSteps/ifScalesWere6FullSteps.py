


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
note_freqs, note_freqs_reversed = get_piano_notes()
# frequency = note_freqs['C4']

octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
key_constant = '4'



boolNotes = [True, False] * 6



def makefileScale(boolNotes, startingTonic):
    
    final_sine = np.empty(0)
    for i in range(startingTonic, 12):
        if(boolNotes[i]):
            currNote = octave[i] + "4"
            frequency = note_freqs[currNote]
            sine_wave = get_sine_wave(frequency, duration=1, amplitude=2048)
            final_sine = np.concatenate((final_sine, sine_wave))
    
    for i in range(0, startingTonic):
        if(boolNotes[i]):
            currNote = octave[i] + "5"
            frequency = note_freqs[currNote]
            sine_wave = get_sine_wave(frequency, duration=1, amplitude=2048)
            final_sine = np.concatenate((final_sine, sine_wave))
    
    # se dodajanje tonika se na konec, da se lepo razveze
    currNote = octave[startingTonic] + "5"
    frequency = note_freqs[currNote]
    sine_wave = get_sine_wave(frequency, duration=1, amplitude=2048)
    final_sine = np.concatenate((final_sine, sine_wave))
    

    name = octave[startingTonic] +"_" + str(startingTonic) + ("onlyFullNotes") + ".wav"
    wavfile.write(name, rate=44100, data=final_sine.astype(np.int16))
    return


def main():
    # numOfHalfsteps = int(input("Number of half steps in the scale: "))
    for i in range(12):
        makefileScale(boolNotes, i)
main()


        












# is_in_for_each = [False] * 12
# is_in_for_each_previous = is_in_for_each

# for startingNote in range(0, 12):

#     ix = startingNote
#     relative_note = ix % 12

#     is_in_for_each[relative_note] = True

#     while (not (lists_identical(is_in_for_each, is_in_for_each_previous))):
#         ix += 1
#         relative_note = ix % 12
#         relative_note[ix] = True


#     if not lists_identical(is_in_for_each, octave):
#         allKeysThatWork.append(is_in_for_each)




# # Pure sine wave
# sine_wave = get_sine_wave(frequency, duration=2, amplitude=2048)
# print(sine_wave)
# sine_wave2 = get_sine_wave(frequency*2, duration=2, amplitude=202)
# final_sine = np.concatenate((sine_wave, sine_wave2))
# print(final_sine)

# wavfile.write('pure_c.wav', rate=44100, data=final_sine.astype(np.int16))