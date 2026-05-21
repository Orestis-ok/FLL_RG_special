######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route2(): 

    PortView_Battery()
    # MoveStraight_Distance (300,300,450,True,True,Stop.BRAKE)
    # PointTurn_Angle (300, 300, 90, True, Stop.BRAKE)
    # MoveSteering_Seconds(300, 20, 300)
    # leftArm.run_time(300, 300, then=Stop.BRAKE, wait=True)

    MoveSteering_Seconds(600, 20, 1000)
    MoveSteering_Seconds(600, 10, 450)

    

