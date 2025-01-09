from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import wave
import numpy as np
import matplotlib.pyplot as plt

audio = AudioSegment.from_file("podcast_milk.mp3")
audio.export("podcast_milk.wav", format="wav")

# start_time = 10 * 1000
# end_time = 20 * 1000
# cropped_audio = audio[start_time:end_time]
#
# cropped_audio.export("cropped_output.wav", format="wav")

# segment1 = AudioSegment.from_file("podcast_chocolate.ogg")
# segment2 = AudioSegment.from_file("podcast_milk.wav")
#
# concatenated_audio = segment1 + segment2
#
# concatenated_audio.export("concatenated_output.wav", format="wav")

# with wave.open("podcast_milk.wav", "rb") as audio_file:
#     frames = audio_file.getnframes()
#     rate = audio_file.getframerate()
#     duration = frames / float(rate)
#     sample_rate = audio_file.getframerate()
#
#     print(f"Duration: {duration} seconds")
#     print(f"Sample rate: {sample_rate} Hz")


with wave.open("podcast_milk.wav", "rb") as audio_file:
    n_channels = audio_file.getnchannels()
    sample_width = audio_file.getsampwidth()
    n_frames = audio_file.getnframes()
    sample_rate = audio_file.getframerate()

    signal = audio_file.readframes(n_frames)
    signal = np.frombuffer(signal, dtype=np.int64)

    plt.figure(figsize=(10, 6))
    plt.plot(signal)
    plt.title("Waveform")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.show()

    amplitude = np.abs(signal).max()
    print(f"Max amplitude: {amplitude}")