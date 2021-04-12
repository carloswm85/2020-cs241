class Robot():
    '''
    Simple robot. It can recognize these commands (anything else will be ignored):
    It can move up, right, down, or left.
    It can fire its laser gun.
    It can inform its current status (position and fuel storaged).
    It can quit.
    
    '''
    def __init__(self):
        # Initial position and fuel storaged.
        # This robot moves in a x and y two dimensional axis.
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel = 100
        
    def command_list(self):
        # Available command list. The only commands recognizable by the robot.
        available_commands = ['up', 'right', 'down', 'left', 'fire', 'status', 'quit']
        command = input('Enter command: ')
        while command not in available_commands:
            # The following commented print() is useful for testing purposes.
            # print('Unavailable command. Available commands are: up, right, down, left. fire, status, quit')
            command = input('Enter command: ')
        return command
    
    # Both move(direction) and fire() member functions consume fuel.
    def move(self, direction):
        if self.fuel >= 5:
            self.fuel -= 5
            if direction == 'up':
                self.y_coordinate -= 1
            elif direction == 'right':
                self.x_coordinate += 1
            elif direction == 'down':
                self.y_coordinate += 1
            elif direction == 'left':
                self.x_coordinate -= 1
        else:
            print('Insufficient fuel to perform action')        
        
    def fire(self):
        if self.fuel >= 15:
            self.fuel -= 15
            print('Pew! Pew!')
        else:
            print('Insufficient fuel to perform action')     
    
    def status(self):
        print('({}, {}) - Fuel: {}'.format(self.x_coordinate, self.y_coordinate, self.fuel))
        
    
def main():
    # The main program will run, as long as run is True
    megaman = Robot()
    run = True
    
    while run:
        command = megaman.command_list()
        if command == 'up' or command == 'right' or command == 'down' or command == 'left':
            megaman.move(command)
        elif command == 'fire':
            megaman.fire()
        elif command == 'status':
            megaman.status()
        elif command == 'quit':
            run = False
    print('Goodbye.')
    
if __name__ == '__main__':
    main()