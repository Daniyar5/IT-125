import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

import tkinter as tk
from tkinter import filedialog
import threading

class Dictaphone:
    def __init__(self, sample_rate=44100, channels=2):
        self.sample_rate = sample_rate
        self.channels = channels
        self.audio_data = None
        self.is_recording = False
    
    def record(self, duration=None):
        self.is_recording = True
        print('Начата запись....')

        if duration:
            self.audio_data = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=self.channels)
            sd.wait()
            self.is_recording = False
            print('Запись завершена')
        else:
            self.audio_data = []
            with sd.InputStream(samplerate=self.sample_rate, channels=self.channels, callback=self.callback):
                while self.is_recording:
                    sd.sleep(100)
    
    def callback(self, indata, frames, time, status):
        self.audio_data.append(indata.copy())
    
    def stop(self):
        self.is_recording = False
        if isinstance(self.audio_data, list):
            self.audio_data = np.concatenate(self.audio_data, axis=0)
        print('Запись остановлена')
    
    def save(self, filename='output.wav'):
        if self.audio_data is not None:
            write(filename, self.sample_rate, (self.audio_data * 32767).astype(np.int16))  # Convert to proper PCM format
            print(f'Файл сохранен как: {filename}')
        else:
            print('Нет данных для сохранения....')

class DictaphoneApp:
    def __init__(self, master):
        self.master = master
        master.title('Диктофон')
        master.geometry('640x420')

        self.dictaphone = Dictaphone()

        self.record_btn = tk.Button(master, text='Record', command=self.start_recording)
        self.record_btn.pack(pady=5)

        self.stop_btn = tk.Button(master, text='Stop', command=self.stop_recording)
        self.stop_btn.pack(pady=5)

        self.save_btn = tk.Button(master, text='Save', command=self.save_recording)
        self.save_btn.pack(pady=5)

    def start_recording(self):
        thread = threading.Thread(target=self.dictaphone.record)
        thread.start()

    def stop_recording(self):
        self.dictaphone.stop()

    def save_recording(self):  # Added missing method
        filename = filedialog.asksaveasfilename(defaultextension='.wav', filetypes=[("WAV files", '*.wav')])
        if filename:
            self.dictaphone.save(filename)

if __name__ == '__main__':
    root = tk.Tk()
    app = DictaphoneApp(root)
    root.mainloop()