import cellular
import qlearn
import time
import sys

startCell = None
totalCount = 0
deathCount = 0
threshold = .05

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
            current = (float)(deathCount / totalCount)
            if(current <= threshold):
                print "THRESHOLD REACHED"
            return cliffReward
        elif here.goal:
            self.score += 1
            global totalCount
            global deathCount
            totalCount = totalCount + 1
            print "deaths: %d total: %d" % (deathCount, totalCount)
            if(current <= threshold):
                print "THRESHOLD REACHED"
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

while 1:
    world.update()
