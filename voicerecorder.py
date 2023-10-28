import winsound
import sounddevice as sd
import soundfile as sf
from tkinter import *
import wave as w

def Voice_rec():
    fs = 48000
    
    # seconds
    duration = 5
    myrecording =sd.rec(int(duration * fs),
                        samplerate = fs, channels = 2)
    sd.wait()
    
    # Save FLAC file at correct sampling rate
    return sf.write('my_Audio.flac', myrecording, fs)

# sourcery skip: avoid-builtin-shadow
master = Tk()
Label(master, text = "Voice Recorder : ").grid(row = 0, sticky = N, rowspan = 5)

b = Button(master, text = "Start", command = Voice_rec)
b.grid(row = 0, columnspan = 2, rowspan = 2, padx = 5, pady = 5)


mainloop()
list = [1,2,3,4]




