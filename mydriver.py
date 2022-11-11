from rose.common import actions, obstacles

driver_name = "driver 1"

obstacle_dict = {obstacles.PENGUIN:10, obstacles.CRACK:5, obstacles.WATER:4, obstacles.TRASH:0, obstacles.BIKE:0, obstacles.BARRIER:0, obstacles.NONE:0}
good_obs = [obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER]

def get_lane(world, posx, posy):
    return world.get((posx, posy-1))



def drive(world):
    carX = world.car.x
    carY = world.car.y

    print(get_lane(0, carY), get_lane(1, carY), get_lane(2, carY))
    return actions.NONE    


