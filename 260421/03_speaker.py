import pygame
import time
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'test.wav')

pygame.mixer.init()

p = pygame.mixer.Sound(file_path)
channel = p.play()

# 재생 끝날 때까지 대기
time.sleep(5)