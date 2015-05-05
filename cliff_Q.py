from __future__ import division

import cellular
import qlearn
import time
import sys

startCell = None
totalCount = 0
deathCount = 0
flag = False

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
    def __init__(self, eps, alph, gamm):
        self.ai = qlearn.QLearn(
            actions=range(directions), epsilon=eps, alpha=alph, gamma=gamm)
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
            global flag 
            deathCount = deathCount + 1
            totalCount = totalCount + 1
            print "deaths: %d total: %d" % (deathCount, totalCount)
            current = (float)(deathCount / totalCount)
            print ("current: %f") % current
            if totalCount == 100:
                flag = True
                print "TOTAL IS 100"
                return

            return cliffReward
        elif here.goal:
            self.score += 1
            global totalCount
            global deathCount
            global flag
            totalCount = totalCount + 1
            print "deaths: %d total: %d" % (deathCount, totalCount)
            current = (float)(deathCount / totalCount)
            print ("current: %f") % current
            if totalCount == 100:
                flag = True
                print "TOTAL is 100"
                return
            return goalReward
        else:
            #totalCount = totalCount + 1
            #print "normalReward"
            return normalReward


normalReward = -1
cliffReward = -100
goalReward = 0
directions = 4
world = cellular.World(Cell, directions=directions, filename='cliff.txt')

#wrap this in a function that looks something like this
#def start(epsilon, gamma)
def begin(eps1, alpha1, gamma1):
    #begin needs to take two parameters being alpha and gamma
    if startCell is None:
        print "You must indicate where the agent starts by putting a 'S' in the map file"
        sys.exit()
        #agent needs to take two parameters alpha and gamma when it is 
        #initialized here, and above, in line 45
    global flag
    global deathCount
    global totalCount
    global world
    flag = False
    deathCount = 0
    totalCount = 0
    agent = Agent(eps1, alpha1, gamma1)
    world.addAgent(agent, cell=startCell)

    pretraining = 0
    for i in range(pretraining):
        if i % 1000 == 0:
            print i, agent.score
            agent.score = 0
        world.update()
    
    world.display.activate(size=30)
    world.display.delay = 1
    
    while 1:
        if flag == True:
            print "Returning to simulate() in rl.py"
            world.reset()
            world = cellular.World(Cell, directions=directions, filename='cliff.txt')
            #this is where the ratio gets returned to simulate
            return (deathCount / totalCount)
        world.update()
