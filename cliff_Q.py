from __future__ import division

import cellular
import qlearn
import time
import sys

startCell = None
totalCount = 0
deathCount = 0
threshold = .95

alphaArray = [.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0]
gammaArray = [0,.1,.2,3,.4,.5,.6,.7,.8,.9,1.0,.9,.9,.9,.9,.9,.9,.9,.9,.9,.9]
epsilonArray = [.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1]
alphaGammaArrayIndex = 0

############################
finalRatio = []
finalAge = []
index = 0
############################

class Cell(cellular.Cell):
    def __init__(self):
        self.cliff = False
        self.goal = False
        self.wall = False

    def colour(self):
        if self.cliff:
            return 'red'
        if self.goal:
            return 'green'
        if self.wall:
            return 'black'
        else:
            return 'white'

    def load(self, data):
        global startCell
        if data == 'S':
            startCell = self
        if data == '.':
            self.wall = True
        if data == 'X':
            self.cliff = True
        if data == 'G':
            self.goal = True


class Agent(cellular.Agent):
    def __init__(self):
        self.ai = qlearn.QLearn(
            actions=range(directions), epsilon=0.1, alpha=0.1, gamma=0.9)
        self.lastAction = None
        self.score = 0

    def colour(self):
        return 'blue'

    def update(self):
        reward = self.calcReward()
        state = self.calcState()
        action = self.ai.chooseAction(state)
        if self.lastAction is not None:
            self.ai.learn(self.lastState, self.lastAction, reward, state)
        self.lastState = state
        self.lastAction = action

        here = self.cell
        if here.goal or here.cliff:
            self.cell = startCell
            self.lastAction = None
        else:
            self.goInDirection(action)

    def calcState(self):
        return self.cell.x, self.cell.y

    def calcReward(self):
        here = self.cell

        if here.cliff:
            global deathCount
            global totalCount
            deathCount = deathCount + 1
            totalCount = totalCount + 1
            print "deaths: %d total: %d" % (deathCount, totalCount)
            return cliffReward

        elif here.goal:
            self.score += 1
            global totalCount
            global deathCount
            global alphaGammaArrayIndex
            totalCount = totalCount + 1
            print "deaths: %d total: %d" % (deathCount, totalCount)
            current = (float)(deathCount / totalCount)
            if(current <= threshold):
                alphaGammaArrayIndex = alphaGammaArrayIndex + 1
                ######################################
                index = index + 1
                finalRatio.append(current)
                ######################################
                return
            return goalReward

        else:
            return normalReward


normalReward = -1
cliffReward = -100
goalReward = 0
directions = 4
world = cellular.World(Cell, directions=directions, filename='cliff.txt')

def begin(eps, alph, gamm):
    if startCell is None:
        print "You must indicate where the agent starts by putting a 'S' in the map file"
        sys.exit()
    agent = Agent()
    world.addAgent(agent, cell=startCell)

    pretraining = 0
    for i in range(pretraining):
        if i % 1000 == 0:
            print i, agent.score
            agent.score = 0
        world.update()

    world.display.activate(size=30)
    world.display.delay = 1
    age = 0
    while 1:
        ######################################
        if age == 0:
            finalAge.append(age)
        else:
            finalAge[index] = age
        age = age + 1
        #######################################
        world.update()

while True:
    begin(epsilonArray[alphaGammaArrayIndex], alphaArray[alphaGammaArrayIndex], gammaArray[alphaGammaArrayIndex])

