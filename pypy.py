import pygame
import random
import time
import math
from classes import *

pygame.init()
bg = "field.png"
screen = pygame.display.set_mode((780, 496))
background = pygame.image.load(bg).convert()
done = False

'''-----------------------------------------------

	389, 750 para o robô sempre aparecer à direita
	30, 389 para o robô sempre aparecer à esquerda
	30, 750 para o robô ter possibilidade de aparecer nos dois lados do campo

------------------------------------------------'''

#direção de spawn do robô em X e Y
xDirection = random.randint(389, 750) #30, 750
yDirection = random.randint(30, 450)
xBall, yBall = 390, 245


def sweep():
	if ((colision.x - xBall) <= colision.diametro):
		print("Estou vendo a bola! Minha distância até ela é de X = %d" % ((colision.x - xBall)))

	if(robot.x > xBall + 5):
		robot.x -= 1
		colision.x -= 1
		kick.x -= 1


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			done = True
		sweep()

	screen.fill((0, 0, 0))
	color = (255, 102, 0)
	robColor = (0, 0, 255)
	golColor = (255, 255, 255)
	areaColor = (0, 0, 0)
	screen.blit(background, (0,0))

	colisionRange = pygame.draw.circle(screen, colision.colisionColor, (colision.x, colision.y), colision.diametro, colision.espessura)
	kickRange = pygame.draw.circle(screen, kick.kickColor, (kick.x, kick.y), kick.diametro, kick.espessura)
	ball = pygame.draw.circle(screen, color, (xBall, yBall), 5)
	robot = pygame.draw.rect(screen, robColor, pygame.Rect(robot.x, robot.y, 20, 20))
	goal2 = pygame.draw.rect(screen, golColor, pygame.Rect(745, 223.5, 1, 50)) #gol da direita
	goal1 = pygame.draw.rect(screen, golColor, pygame.Rect(33, 223.5, 1, 50)) #gol da esquerda
	areaA = pygame.draw.rect(screen, golColor, pygame.Rect(389, 17, 1, 50)) #área da esquerda
	areaB = pygame.draw.rect(screen, golColor, pygame.Rect(389, 428, 1, 50)) #área da direita
	pygame.display.flip()
