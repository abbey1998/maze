import numpy as np
import cv2
import random

print("What is the size of the maze you want?")
print("example:- 5,4")
maze_size = input()

block_size = 16

horizontal = np.zeros((maze_size[1]-1,maze_size[0]))
vertical = np.zeros((maze_size[1],maze_size[0]-1))

maze = np.zeros((maze_size[1]*block_size+1,maze_size[0]*block_size+1))
cv2.line(maze,(0,0),(0,maze_size[1]*block_size),(255,255,255),1)
cv2.line(maze,(0,0),(maze_size[0]*block_size,0),(255,255,255),1)
cv2.line(maze,(maze_size[0]*block_size,maze_size[1]*block_size),(0,maze_size[1]*block_size),(255,255,255),1)
cv2.line(maze,(maze_size[0]*block_size,maze_size[1]*block_size),(maze_size[0]*block_size,0),(255,255,255),1)

for i in range(maze_size[1]-1):
	for j in range(maze_size[0]):
		horizontal[i][j] = random.choice([1, 0])
		if (horizontal[i][j] == 1):
			cv2.line(maze, (block_size*j,block_size*(i+1)), (block_size*(j+1),block_size*(i+1)) ,(255,255,255), 1)

for i in range(maze_size[0]-1):
	for j in range(maze_size[1]):
		vertical[j][i] = random.choice([1, 0])
		if (vertical[j][i] == 1):
			cv2.line(maze, (block_size*(i+1),block_size*j), (block_size*(i+1),block_size*(j+1)) ,(255,255,255), 1)

cv2.imwrite('Output.jpeg', maze)

print(horizontal)
print(vertical)