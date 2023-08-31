import random

FIELD = 10

def create_coord():
    """Creates a FIELDxFIELD list of lists"""
    coord = []
    for i in range(FIELD):
        coord.append([])
        for j in range(FIELD):
            coord[i].append(".")
    return coord

def print_map(map):
    """Prints the list of lists - the coordinates of the game"""
    for row in map:
        for element in row:
            print(element, end = " ")
        print()

def place_ships(list_of_lists, x_values):
    """Function that replaces dots in the coordinates field with X - the ship coordinates"""
    for values in x_values:
        row_number = values[0]
        row_position = values[1]
        list_of_lists[row_number][row_position] = "x"

def select_ship_row():
    """Function that lets the user select the row of their ship"""
    while True:
        coordinates_ship_row = int(input("Write the coordinate for the row for your ship:"))
        if coordinates_ship_row < 0 or coordinates_ship_row > FIELD: 
            # the coordinate can't be negative or exceed the field
            print("Please input a coordinate that is lower than 9 and higher than 0")
        else:
            return coordinates_ship_row

def select_ship_row_position():
    """Function that lets the user select the row position of their ship"""
    while True:
        coordinates_ship_row_position = int(input("Write the coordinate for the row position for your ship:"))
        if coordinates_ship_row_position < 0 or coordinates_ship_row_position >= FIELD:  
            # the coordinate can't be negative or exceed the field
            print("Please input a coordinate that is lower than 9 and higher than 0")
        else:
            return coordinates_ship_row_position

def create_coordinate(list_of_coordinates, list_coordinates_2):    
    """Function that creates the coordinates of a user's ship, using the previos 2 functions: select_ship_row, select_ship_row_position"""    
    while True:
        coordinates_ship_row = select_ship_row()
        coordinates_ship_row_position = select_ship_row_position()
        tuple_coordinates = (coordinates_ship_row, coordinates_ship_row_position) # ship coordinates
        if tuple_coordinates in list_of_coordinates or tuple_coordinates in list_coordinates_2:
           print("Same coordinate value, input a different coordinate")
        else:
            return tuple_coordinates
        
def create_coordinate_pc(list_of_coordinates, list_coordinates_2):    
    """Function that creates the coordinates of a computer's ship, using a random function"""    
    while True:
        coordinates_ship_row_pc = random.randrange(0, FIELD)
        coordinates_ship_row_position_pc = random.randrange(0, FIELD)
        tuple_coordinates = (coordinates_ship_row_pc, coordinates_ship_row_position_pc) # ship coordinates
        if tuple_coordinates not in list_of_coordinates or tuple_coordinates not in list_coordinates_2:
            break
        else:
            return tuple_coordinates

def is_coord_next_to_each_other_2(list_coordinates):
    """Function checking if the coordinates of a two-space ship are next to each other vertically or horizontally. 
    y1, y2 are the row inputs for the user ship. x1, x2 are the row position inputs. In order to make sure that the
    ship is beign placed correctly, the row or row position inputs must be macthing and the difference between the row 
    position coordinates or the row coordinates must be equal to the the absolute value of 1"""
    y1 = list_coordinates[0][0] 
    y2 = list_coordinates[1][0]
    x1 = list_coordinates[1][1]
    x2 = list_coordinates[0][1]
    x_diff = abs(x1 - x2)
    y_diff = abs(y1 - y2)
    
    result = y1 == y2 and x_diff == 1
    result_2 = x1 == x2 and y_diff == 1 
    return result or result_2

def is_coord_next_to_each_other_3(list_coordinates):
    """Function similar in logic to is_coord_next_to_each_other_2, but devised for 3 space ships. The
    one difference that there is an extra check of the difference between row/row position being equal to the absolute
    value of 1 for the 1st and the 3d input. By doing that, the ship coordinates can be placed in any order, the 
    'direction' in which the ship is places can be changed."""
    y1 = list_coordinates[0][0]
    y2 = list_coordinates[1][0]
    y3 = list_coordinates[2][0]

    x1 = list_coordinates[0][1]
    x2 = list_coordinates[1][1]
    x3 = list_coordinates[2][1]

    x2_valid = abs(x1 - x2) == 1
    x3_valid = abs(x2 - x3) == 1 or abs(x1 - x3) == 1
    y2_valid = abs(y1 - y2) == 1
    y3_valid = abs(y2 - y3) == 1 or abs(y1 - y3) == 1

    result = y1 == y2 == y3 and x2_valid and x3_valid  
    result_2 = x1 == x2 == x3 and y2_valid and y3_valid
    return result or result_2 

def is_coord_next_to_each_other_5(list_coordinates):
    """Function similar to is_coord_next_to_each_other_2 and is_coord_next_to_each_other_3, but designed for 5 spaces ships.
    In this case, the 'direction' of the ship cannot be changed unlike for the 2 and 3 spaces ships"""
    y1 = list_coordinates[0][0]
    y2 = list_coordinates[1][0]
    y3 = list_coordinates[2][0]
    y4 = list_coordinates[3][0]
    y5 = list_coordinates[4][0]

    x1 = list_coordinates[0][1]
    x2 = list_coordinates[1][1]
    x3 = list_coordinates[2][1]
    x4 = list_coordinates[3][1]
    x5 = list_coordinates[4][1]

    x_diff = abs(x1 - x2) 
    x_diff_2 = abs(x2 - x3)
    x_diff_3 = abs(x3 - x4)
    x_diff_4 = abs(x4 - x5)
    y_diff = abs(y1 - y2)
    y_diff_2 = abs(y2 - y3)
    y_diff_3 = abs(y3 - y4)
    y_diff_4 = abs(y4 - y5)

    result = y1 == y2 == y3 == y4 == y5 and x_diff == 1 and x_diff_2 == 1 and x_diff_3 == 1 and x_diff_4 == 1
    result_2 = x1 == x2 == x3 == x4 == x5 and y_diff == 1 and y_diff_2 == 1 and y_diff_3 == 1 and y_diff_4 == 1
    return result or result_2 

def select_ship_position_2_space_ships():
    """This function creates 3 ships with 2 spaces"""
    list_of_coordinates = []
    for ship_count in range(3): # number of ships
        # repeats as long as user puts coordinates are not taken
        print("Place three two space ships on the board. The coordinates need to be next to each other")
        print("Ship: " + str(ship_count + 1))
        while True:
            list_coordinates_ship2 = []
            for _ in range(2): #number of spaces
                tuple_coordinates = create_coordinate(list_of_coordinates, list_coordinates_ship2)
                list_coordinates_ship2.append(tuple_coordinates)
            if is_coord_next_to_each_other_2(list_coordinates_ship2):
                list_of_coordinates += list_coordinates_ship2
                break
            else:
                print("Select different coordinates for your ship number" + str(ship_count + 1) + "- the coordinates are not next to each other.\n\
                      Start over with the coordinates of the ship.")
    return list_of_coordinates

def select_ship_position_3_space_ships():
    """This function creates 2 ships with 3 spaces"""
    list_of_coordinates = []
    for ship_count in range(2): # number of ships
        print("Place two space ships with 3 spaces on the board. The coordinates need to be next to each other")
        print("Ship: " + str(ship_count + 1))
        while True:
            list_coordinates_ship2 = []
            for _ in range(3): # number of spaces
                tuple_coordinates = create_coordinate(list_of_coordinates, list_coordinates_ship2)
                list_coordinates_ship2.append(tuple_coordinates)
            if is_coord_next_to_each_other_3(list_coordinates_ship2):
                list_of_coordinates += list_coordinates_ship2
                break
            else:
                print("Select different coordinates for your ship " + str(ship_count + 1) + "- the coordinates are not next to each other.\n\
                      Start over with the coordinates of the ship.")
    return list_of_coordinates


def select_ship_position_5_space_ships():
    """This function creates 1 ship with 5 spaces"""
    list_of_coordinates = []
    print("Place 1 space ships with 5 spaces on the board. The coordinates need to be next to each other")
    while True:
        list_coordinates_ship2 = []
        for _ in range(5): # number of spaces
            tuple_coordinates = create_coordinate(list_of_coordinates, list_coordinates_ship2)
            list_coordinates_ship2.append(tuple_coordinates)
        if is_coord_next_to_each_other_5(list_coordinates_ship2):
            list_of_coordinates += list_coordinates_ship2
            break
        else:
            print("Select different coordinates for your ship - the coordinates are not next to each other.\n\
                    Start over with the coordinates of the ship.")
    return list_of_coordinates

def select_ship_position_pc():
    list_of_coordinates = []
    for _ in range(3): # the possible number of ships is here
        while True:
            coordinates_ship_row_pc = random.randrange(0, FIELD)
            coordinates_ship_row_position_pc = random.randrange(0, FIELD)
            tuple_coordinates = (coordinates_ship_row_pc, coordinates_ship_row_position_pc)
            if tuple_coordinates not in list_of_coordinates:
                list_of_coordinates.append(tuple_coordinates)
                break 
    return list_of_coordinates

# def select_ship_position_2_space_ships_pc():
   # """This function creates 3 ships with 2 spaces for the computer"""
    #list_of_coordinates = []
    #for ship_count in range(3): # number of ships
     #   while True:
      #      list_coordinates_ship2 = []
       #     for _ in range(2): #number of spaces
        #        coordinates_ship_row_pc = random.randrange(0, FIELD)
         #       coordinates_ship_row_position_pc = random.randrange(0, FIELD)
          #      tuple_coordinates = (coordinates_ship_row_pc, coordinates_ship_row_position_pc)
           #     list_coordinates_ship2.append(tuple_coordinates)
            #    if tuple_coordinates not in list_of_coordinates or tuple_coordinates not in list_coordinates_ship2:
             #       list_of_coordinates.append(tuple_coordinates)
              #  elif is_coord_next_to_each_other_2(list_coordinates_ship2):
               #     list_of_coordinates += list_coordinates_ship2
                #    break
    #return list_of_coordinates



def player_missile_cordinates(map):
    """This function let's the player choose the coordinates that they want to hit. When a
    ship is hit, the coordinate is replaced with a O, when it's an empty hit, it's replaced wih an I"""
    while True:
        row = int(input("Write the row coordinate you want to hit: "))
        if row < 0 or row > FIELD:
            print("Please input a coordinate that is lower than 9 and higher than 0")
        else:
            break
    while True:
        place_in_row = int(input("Write a row position coordinate you want to hit: "))
        if place_in_row < 0 or place_in_row > FIELD:
            print("Please input a coordinate that is lower than 9 and higher than 0")
        else:
            break
    if "x" == map[row][place_in_row] :
        map[row][place_in_row] = "O"
        print("You destroyed a ship")
    else:
        print("Missed hit :( ")
        map[row][place_in_row] = "I"

def computer_missile_cordinates(map):
    """Let's the pc hit the user map, similar logic to function above"""
    row = random.randrange(FIELD)
    place_in_row = random.randrange(FIELD)
    place_in_row = random.randrange(FIELD)
    if "x" == map[row][place_in_row] :
        map[row][place_in_row] = "O"
    else:
        map[row][place_in_row] = "I"


def are_ships_alive(map):
    """Function that checks if there are ship parts left to be hit on a map"""
    for row in map:
        if "x" in row:
            return True
    return False


def main():
    pc_map = create_coord() 
    place_ships(pc_map, select_ship_position_pc())
    # place_ships(pc_map, select_ship_position_2_space_ships_pc())
    # print_map(pc_map)
    player_map = create_coord() 
    place_ships(player_map,select_ship_position_3_space_ships())
    print_map(player_map)
    place_ships(player_map, select_ship_position_2_space_ships())
    print_map(player_map)
    place_ships(player_map,select_ship_position_5_space_ships())
    print_map(player_map)
    while are_ships_alive(player_map) and are_ships_alive(pc_map):
        player_missile_cordinates(pc_map)
        computer_missile_cordinates(player_map)
        print_map(player_map)
    
    if are_ships_alive(player_map):
        print("You won")
    elif are_ships_alive(pc_map):
        print("You lost")
    else:
        print("It's a draw")

main()