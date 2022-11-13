from rose.common import actions, obstacles

driver_name = "driver 1"

obstacle_dict = {obstacles.PENGUIN:10, obstacles.CRACK:5, obstacles.WATER:4, obstacles.TRASH:-10, obstacles.BIKE:-10, obstacles.BARRIER:-10, obstacles.NONE:0}
good_obs = [obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER, obstacles.NONE]
good_obs2 = [obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER]

def get_lane(world, posx, posy): # this function returns the sum of multipule objects within a lane starting from a given y position
    sum1 = 0
    for i in range(posy):
        sum1 += obstacle_dict[world.get((posx, i))]
    return sum1
def can_turn(world, lane, car_y):
    return world.get((lane, car_y-1)) == obstacles.NONE or world.get((lane, car_y-1)) == obstacles.PENGUIN

def drive(world):
    car_x = world.car.x
    car_y = world.car.y
    can_right = False
    can_left = False

    front_obs = world.get((car_x, car_y-1))
    front_obs2 = world.get((car_x, car_y-2))
    if car_x < 3:
        left_lane = 0
        middle_lane = 1
        right_lane = 2
    else:
        left_lane = 3
        middle_lane = 4
        right_lane = 5

    if front_obs == obstacles.PENGUIN:
        return actions.PICKUP
    if front_obs == obstacles.WATER:
        return actions.BRAKE
    if front_obs == obstacles.CRACK:
        return actions.JUMP

    # handles the situations where the car is about to crash into a bad obstacle
    if front_obs not in good_obs:
        if car_x == middle_lane:
            left_obs = world.get((car_x-1, car_y-1))
            right_obs = world.get((car_x + 1, car_y - 1))
            left_obs2 = world.get((car_x - 1, car_y - 2))
            right_obs2 =  world.get((car_x + 1, car_y - 2))

            if left_obs == right_obs:
                if right_obs2 > left_obs2:
                    return actions.RIGHT
                else:
                    return actions.LEFT
            elif left_obs + left_obs2 > right_obs + right_obs2:
                return actions.LEFT
            else:
                return actions.RIGHT
        elif car_x == right_lane:
            return actions.LEFT
        else:
            return actions.RIGHT


    if car_x == middle_lane:
        left_obs = world.get((car_x-1, car_y-1))
        right_obs = world.get((car_x + 1, car_y - 1))
        left_obs2 = world.get((car_x - 1, car_y - 2))
        right_obs2 =  world.get((car_x + 1, car_y - 2))

        if left_obs == right_obs == obstacles.NONE:
            if left_obs == right_obs == obstacles.NONE and right_obs2 in good_obs2 and left_obs2 in good_obs2:
                if obstacle_dict[right_obs2] > obstacles.dict[left_obs2]:
                    return actions.RIGHT
                else:
                    return actions.LEFT
        if left_obs == right_obs == obstacles.NONE and right_obs2 in good_obs2:
            return actions.RIGHT
        if left_obs == right_obs == obstacles.NONE and left_obs2  in good_obs2:
            return actions.LEFT

    elif car_x == left_lane:

        right_obs = world.get((car_x + 1, car_y - 1))
        right_obs2 =  world.get((car_x + 1, car_y - 2))


        if right_obs == obstacles.NONE and right_obs2 in good_obs2 and (front_obs in good_obs2 or front_obs2 in good_obs2):
            if obstacles.dict[right_obs2] > obstacles.dict[front_obs]:
                return actions.RIGHT
            return actions.NONE
        if right_obs == obstacles.NONE and right_obs2 in good_obs2:
            return actions.RIGHT

    elif car_x == right_lane:

        left_obs = world.get((car_x-1, car_y-1))
        left_obs2 = world.get((car_x - 1, car_y - 2))


        if left_obs == obstacles.NONE and left_obs2 in good_obs2 and (front_obs in good_obs2 or front_obs2 in good_obs2):
            if obstacles.dict[left_obs2] > obstacles.dict[front_obs]:
                return actions.RIGHT
            return actions.NONE
        if left_obs == obstacles.NONE and left_obs2 in good_obs2:
            return actions.RIGHT

    if car_x == left_lane:
        right_obs = world.get((car_x + 1, car_y - 1))
        if front_obs == obstacles.NONE and front_obs2 == obstacles.NONE and right_obs == obstacles.NONE :
            return actions.LEFT
    if car_x == right_lane:
        left_obs = world.get((car_x-1, car_y-1))
        left_obs2 = world.get((car_x - 1, car_y - 2))


        if left_obs == obstacles.NONE and left_obs2 in good_obs2 and (front_obs in good_obs2 or front_obs2 in good_obs2):
            if obstacles.dict[left_obs2] > obstacles.dict[front_obs]:
                return actions.RIGHT
            return actions.NONE
        if left_obs == obstacles.NONE and left_obs2 in good_obs2:
            return actions.RIGHT

    if car_x == left_lane:
        right_obs = world.get((car_x + 1, car_y - 1))
        if front_obs == obstacles.NONE and front_obs2 == obstacles.NONE and right_obs == obstacles.NONE :
            return actions.LEFT
    if car_x == right_lane:
        left_obs = world.get((car_x - 1, car_y - 1))
        if front_obs == obstacles.NONE and front_obs2 == obstacles.NONE and left_obs == obstacles.NONE:
            return actions.RIGHT


    return actions.NONE
