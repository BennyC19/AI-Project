import pyaudio
import wave 
import time
import numpy as np
import wave
import io
from scipy.signal import find_peaks

# use webrtcvad in the future. This method works for now but may need to be updated.

class microphone_access:
    
    number_of_microphones = 0
    number_of_activated_microphones = 0
    maximum_microphones = 10

    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.threshold = None

    def ambient_noise_calculator(self):

        stream = self.audio.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            input=True,
                            frames_per_buffer=1024)
        
        start_time = time.time()
        passed = 0
        frames = []

        while passed < 5:
            data = stream.read(1024)
            frames.append(data)
            passed = time.time() - start_time

        stream.stop_stream()
        stream.close()

        audio_signal = np.frombuffer(b''.join(frames), dtype=np.int16)

        peaks, _ = find_peaks(audio_signal, height=0)
        positive_peak_values = np.maximum(0, audio_signal[peaks])
        
        moving_average = np.convolve(positive_peak_values, np.ones(5000) / 5000, mode='valid')
        
        peak_ambience = np.max(moving_average)

        self.threshold = peak_ambience
        print("Done calculating Ambient Noise")

    def record_message(self):
        
        stream = self.audio.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            input=True,
                            frames_per_buffer=1024)
        
        countdown = 10
        listening = True
        recording = True
        listening_frames = []
        frames = []
        start_time = time.time()
        
        while listening:
            data = stream.read(1024)
            listening_frames.append(data)
            passed = time.time() - start_time
            if (passed >= 1):
                audio_signal = np.frombuffer(b''.join(listening_frames), dtype=np.int16)
                peaks, _ = find_peaks(audio_signal, height=0)
                positive_peak_values = np.maximum(0, audio_signal[peaks])
                if (len(positive_peak_values) * 0.55 < np.sum(positive_peak_values > self.threshold)): # if voice detected
                    listening = False
                    print("found voice")
                else: # voice is not detected
                    start_time = time.time()
                    listening_frames.clear()

        start_time = time.time()
        
        while recording:
            frames = listening_frames
            data_second_loop = stream.read(1024)
            frames.append(data_second_loop)
            passed = time.time() - start_time
            if (passed >= 1):

                start_time = time.time()
                audio_signal = np.frombuffer(b''.join(frames), dtype=np.int16)
                peaks, _ = find_peaks(audio_signal, height=0)
                positive_peak_values = np.maximum(0, audio_signal[peaks])
                if (len(positive_peak_values) * 0.75 < np.sum(positive_peak_values > self.threshold)): # if voice detected
                    countdown = 6
                else:
                    countdown -= 1
                    if (countdown <= 0):
                        recording = False
        
        stream.stop_stream()
        stream.close()

        message = b''.join(frames)

        return message 
