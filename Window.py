from ctypes import windll
import pygame
SetWindowPos = windll.user32.SetWindowPos
screen = pygame.display.set_mode((100,100), pygame.NOFRAME)
SetWindowPos(pygame.display.get_wm_info()[screen], -2, x, y, 0, 0, 0x0001)