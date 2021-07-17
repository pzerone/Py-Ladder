class Plr():

    def __init__(self, name,current_position):
        self.name = name
        self.current_position = current_position
        

    def first_move(self, die_value):
        self.die_value = die_value

        if die_value == 1:
            current_position = 1
        else:
            current_position = 0
        return(current_position)

    def main_move(self, die_value, current_position):
         self.die_value = die_value

         current_position = current_position + die_value
         return (current_position)


    def end_move(self, die_value,current_position):
        self.die_value = die_value

        if current_position + die_value == 100 or current_position + die_value <=100:
            current_position = current_position + die_value
        else:
            current_position = current_position
        return (current_position)