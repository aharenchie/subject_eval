"""PyAudio : Play a wave file."""

import pyaudio
import wave
import sys

def main_func(data_dir):
    soud_list=['A02.wav','A05.wav','A06.wav']
    CHUNK = 1024

    for soud in soud_list:
        soud_name = data_dir+soud
        wf = wave.open(soud_name, 'rb')
        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()
    
        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # read data
        data = wf.readframes(CHUNK)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()
            
        # close PyAudio (5)
        p.terminate()

