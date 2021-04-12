"""
File: asteroids08.py
Original Author: Br. Burton
Designed to be completed by others

This program implements the asteroids08 game.
"""
import math
from abc import ABC
from abc import abstractmethod
import random
import arcade

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class Point:

    def __init__(self):
        self.x_coordinate = 0
        self.y_coordinate = 0


class Velocity:

    def __init__(self):
        self.dx = 0
        self.dy = 0


class FlyingObject(ABC):

    def __init__(self, img):

        self.texture = arcade.load_texture(img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.radius = SHIP_RADIUS
        self.image = img

        self.center = Point()
        self.velocity = Velocity()

        self.angle = 0
        self.speed = 0
        self.direction = 0
        self.alpha = 255
        self.alive = True

        self.velocity.velocity_dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.velocity_dy = math.sin(math.radians(self.direction)) * self.speed

    def advance(self):
        self.center.x_coordinate += self.velocity.dx
        self.center.y_coordinate += self.velocity.dy

    def is_alive(self):
        return self.alive

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x_coordinate, self.center.y_coordinate,
                                      self.width, self.height,
                                      self.texture,
                                      self.angle,
                                      self.alpha)

    def is_off_screen(self, screen_width, screen_height):
        return True


class Asteroid(FlyingObject):

    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed

    def hit(self):
        pass

class SmallRock(Asteroid):
    def __init__(self):
        super().__init__("images/small_rock.png")


class MediumRock(Asteroid):
    def __init__(self):
        super().__init__("images/medium_rock.png")


class BigRock(Asteroid):
    def __init__(self):
        super().__init__("images/big_rock.png")
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed


class Ship(FlyingObject):
    def __init__(self):
        super().__init__("images/ship.png")
        self.angle = 1
        self.center.x_coordinate = SCREEN_WIDTH / 2
        self.center.y_coordinate = SCREEN_HEIGHT / 2
        self.radius = SHIP_RADIUS


class Laser(FlyingObject):
    def __init__(self):
        super().__init__("images/laser.png")

    def fire(self, angle):
        pass

    def advance(self):
        pass

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        #self.ship = Ship()
        self.laser = []
        self.asteroids = []

        for item in range(INITIAL_ROCK_COUNT):
            asteroid = BigRock()
            self.asteroids.append(asteroid)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        # self.ship.draw()

        for asteroid in self.asteroids:
            asteroid.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time

        for asteroid in self.asteroids:
            asteroid.advance()

        # TODO: Check for collisions

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
