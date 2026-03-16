import sounddevice as sd
import scipy.io as sio
import scipy.io.wavfile
import pygame
import time

sample_rate = 44100  # 샘플레이트
seconds = 3  # 녹음시간
myrecording = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=2)
sd.wait()  # 녹음이 끝날때까지 대기
print("Recording Stop")
sio.wavfile.write('output.wav', sample_rate, myrecording)  # wav파일로 저장

pygame.mixer.init()
p = pygame.mixer.Sound('output.wav')
p.play()
time.sleep(3)