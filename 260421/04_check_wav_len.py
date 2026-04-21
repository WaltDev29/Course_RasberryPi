import numpy as np
import scipy.io.wavfile as wavfile
import pygame
import time

fileNamePath = 'output.wav'

# 샘플레이트 및 데이터를 통해 재생 시간을 구한다
samplerate, data = wavfile.read(fileNamePath)

times = data.shape[0] / samplerate

# 반올림 및 형변환을 통해 정수형태로 구한다
play_time = int(round(times))

print("file '{}' play time = {}".format(fileNamePath, play_time))

# 재생을 위한 pygame 초기화
pygame.mixer.init()

# 경로를 지정하여 객체를 생성하고 재생한다
p = pygame.mixer.Sound(fileNamePath)
p.play()

# 위에서 구한 파일의 길이 만큼 대기한다
time.sleep(play_time)