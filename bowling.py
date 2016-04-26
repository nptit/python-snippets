""" Task

Your task is to write a function for calculating the score of a 10 pin bowling
game. The input for the function is a list of pins knocked down per roll for
one player. Output is the player's total score.

Rules

General rules

Rules of bowling in a nutshell:

A game consists of 10 frames. In each frame the player rolls 1 or 2 balls,
except for the 10th frame, where the player rolls 2 or 3 balls. The total
score is the sum of your scores for the 10 frames. 

a. If you knock down fewer than 10 pins with 2 balls, your frame score is the number 
of pins knocked down 

b. If you knock down all 10 pins with 2 balls (spare), you score the amount of pins
knocked down plus a bonus - amount of pins knocked down with the next ball 

c. If you knock down all 10 pins with 1 ball (strike), you score the amount of pins
knocked down plus a bonus - amount of pins knocked down with the next 2 balls

Rules for 10th frame

As the 10th frame is the last one, in case of spare or strike there will be no
next balls for the bonus. To account for that:

a. if the last frame is a spare, player rolls 1 bonus ball. 

b. if the last frame is a strike, player rolls 2 bonus balls. 

These bonus balls on 10th frame are only counted as a bonus to the respective spare or strike.

More information

http://en.wikipedia.org/wiki/Ten-pin_bowling#Scoring

Input

You may assume that the input is always valid. This means:

input list length is correct number of pins knocked out per roll is valid """


g1 = [(0, 1), (10), (5, 5), (6, 2), (10,), (10,), (9, 1), (5, 5), (3, 6), (5, 5, 5)] # score =146
g2 = [(10,)]*12 # score = 300

def list2tuples(lst):
	""" given a list of pins, turn it in 10 tuples/frames """
	frames = []
	i = 0
	while len(frames) < 9:
		if lst[i] == 10:
			frames.append((10,))
			i += 1
		else:
			frames.append((lst[i],lst[i+1]))
			i += 2

	frames.append(tuple(lst[i:]))

	return frames


def cal_score(frames):
	scores = []
	for i in range(9):
		f = frames[i]
		if sum(f) < 10:
			scores.append(sum(f))
		elif sum(f) == 10 and len(f) == 1:
			# add current score and scores of next two balls
			if len(frames[i+1]) == 1:
				scores.append(20 + frames[i+2][0])
			else: 
				scores.append(10 + sum(frames[i+1][0:2]))
		elif sum(f) == 10 and len(f) == 2:
			# add current score and next ball
			scores.append(10 + frames[i+1][0])
		else:
			raise Exception("Incorrect implementation")

	return sum(scores)+sum(frames[9])



g3 = [3, 3, 4, 5, 3, 6, 10, 6, 3, 5, 1, 0, 2, 4, 6, 4, 3, 6, 4, 2] # score= 93
g1 = [0, 1, 10, 5, 5, 6, 2, 10, 10, 9, 1, 5, 5, 3, 6, 5, 5, 5] # score =146
g2 = [10]*12
gg3 = list2tuples(g3)
print cal_score(gg3)
print cal_score(list2tuples(g1))
print cal_score(list2tuples(g2))
