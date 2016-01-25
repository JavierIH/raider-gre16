import raider
import time
import pygame

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

trims=[0,0,0,0,0,0,0,0,0,0,0,0,0,3,-2,-5,5,0,0,-5,0,0,0,0,0]
robot = raider.Raider(trims)
robot.home(-140, 30)
time.sleep(0.01)

while True:
    for event in pygame.event.get():
        pass

    # axisLX = joystick.get_axis(0)
    # axisLY = joystick.get_axis(1)
    # axisRX = joystick.get_axis(2)
    # axisRY = joystick.get_axis(3)
    # triggerR = joystick.get_axis(4)
    # triggerL = joystick.get_axis(5)
    buttonA = joystick.get_button(0)
    buttonB = joystick.get_button(1)
    buttonX = joystick.get_button(2)
    # buttonY = joystick.get_button(3)
    bumperL = joystick.get_button(4)
    bumperR = joystick.get_button(5)
    back = joystick.get_button(6)
    start = joystick.get_button(7)
    pad = joystick.get_hat(0)



    if start == 1:
        print 'get up'
        # robot.getUp()

    elif bumperL == 1:
        print 'step left'
        # robot.stepL()

    elif bumperR == 1:
        print 'step right'
        # robot.stepR()

    elif back == 1:
        print 'back get up'
        # robot.backGetUp()

    elif buttonX == 1:
        print 'left punch'
        # robot.punchL()

    elif buttonA == 1:
        print 'front punch'
        # robot.punchF()

    elif buttonB == 1:
        print 'right punch'
        # robot.punchR()

    elif pad[1] == 1:
        print 'walk'
        # robot.walkF()

    elif pad[1] == -1:
        print 'back'
        # robot.walkB()

    elif pad[0] == 1:
        print 'turnR'
        # robot.turnR()

    elif pad[0] == -1:
        print 'turnL'
        # robot.turnL()
    else:
        # robot.home()
        pass
    clock.tick(5000)
