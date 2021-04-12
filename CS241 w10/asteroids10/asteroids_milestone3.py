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
        self.x_coordinate = 100
        self.y_coordinate = 100


class Velocity:

    def __init__(self):
        self.dx = 0
        self.dy = 0


class FlyingObject(ABC):

    def __init__(self, img):

        self.texture = arcade.load_texture(img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.image = img
        self.radius = 0.0

        self.center = Point()
        self.velocity = Velocity()

        self.angle = 0.0
        self.speed = 0.0
        self.alpha = 255
        self.alive = True

    def advance(self):
        self.center.x_coordinate += self.velocity.dx * self.speed
        self.center.y_coordinate += self.velocity.dy * self.speed

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x_coordinate,
                                      self.center.y_coordinate,
                                      self.width, self.height,
                                      self.texture,
                                      self.angle,
                                      self.alpha)

    def is_off_screen(self):
        if self.center.x_coordinate > SCREEN_WIDTH:
            self.center.x_coordinate -= SCREEN_WIDTH
        if self.center.x_coordinate < 0:
            self.center.x_coordinate += SCREEN_WIDTH
        if self.center.y_coordinate > SCREEN_HEIGHT:
            self.center.y_coordinate -= SCREEN_HEIGHT
        if self.center.y_coordinate < 0:
            self.center.y_coordinate += SCREEN_HEIGHT


class Asteroid(FlyingObject):

    def __init__(self, img):
        super().__init__(img)
        self.radius = BIG_ROCK_RADIUS

    def break_apart(self, asteroids):
        pass


class BigRock(Asteroid):

    def __init__(self):
        super().__init__("images/big_rock.png")
        self.center.x = random.randint(0, SCREEN_WIDTH)
        self.center.y = random.randint(0, SCREEN_HEIGHT)
        self.angle = random.randint(1, 360)
        self.speed = BIG_ROCK_SPEED

        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed

    def advance(self):
        super().advance()
        self.angle += BIG_ROCK_SPIN

    def break_apart(self, asteroids):
        medium_asteroid = MediumRock(self)
        medium_asteroid.velocity.dy += 2
        asteroids.append(medium_asteroid)

        medium_asteroid = MediumRock(self)
        medium_asteroid.velocity.dy -= 2
        asteroids.append(medium_asteroid)

        small_asteroid = SmallRock(self)
        small_asteroid.velocity.dx += 5
        asteroids.append(small_asteroid)


class MediumRock(Asteroid):
    def __init__(self, asteroid: BigRock):
        super().__init__("images/medium_rock.png")
        self.radius = MEDIUM_ROCK_RADIUS
        self.center.x_coordinate = asteroid.center.x_coordinate
        self.center.y_coordinate = asteroid.center.y_coordinate
        self.speed = BIG_ROCK_SPEED
        self.angle = random.randint(1, 360)
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed

    def advance(self):
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN

    def break_apart(self, asteroids):
        small_asteroid = SmallRock(self)
        small_asteroid.velocity.dy += 1.5
        small_asteroid.velocity.dx += 1.5
        asteroids.append(small_asteroid)

        small_asteroid = SmallRock(self)
        small_asteroid.velocity.dy -= 1.5
        small_asteroid.velocity.dx -= 1.5
        asteroids.append(small_asteroid)

class SmallRock(Asteroid):
    def __init__(self, asteroid: BigRock):
        super().__init__("images/small_rock.png")
        self.radius = SMALL_ROCK_RADIUS
        self.center.x_coordinate = asteroid.center.x_coordinate
        self.center.y_coordinate = asteroid.center.y_coordinate

        self.speed = BIG_ROCK_SPEED
        self.angle = random.randint(1, 360)
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed

    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN


class Ship(FlyingObject):

    def __init__(self):
        super().__init__("images/ship.png")
        self.angle = 0
        self.center.x_coordinate = SCREEN_WIDTH / 2
        self.center.y_coordinate = SCREEN_HEIGHT / 2
        self.radius = SHIP_RADIUS
        self.speed = SHIP_THRUST_AMOUNT

    def thrust(self):
        self.velocity.dx += math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy += math.sin(math.radians(self.angle)) * self.speed

    def rotate_right(self):
        self.angle -= SHIP_TURN_AMOUNT

    def rotate_left(self):
        self.angle += SHIP_TURN_AMOUNT

    def un_thrust(self):
        self.velocity.dx -= math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy -= math.sin(math.radians(self.angle)) * self.speed


class Bullet(FlyingObject):

    def __init__(self, ship: Ship):
        super().__init__("images/laser.png")
        self.angle = ship.angle
        self.speed = ship.speed + BULLET_SPEED
        self.radius = BULLET_RADIUS

        self.life = BULLET_LIFE
        self.center.x_coordinate = ship.center.x_coordinate + 2 * SHIP_RADIUS * math.cos(math.radians(self.angle))
        self.center.y_coordinate = ship.center.y_coordinate + 2 * SHIP_RADIUS * math.sin(math.radians(self.angle))

    def fire(self, ship):
        self.velocity.dx = math.cos(math.radians(self.angle))
        self.velocity.dy = math.sin(math.radians(self.angle))
        print('Speed is: {}'.format(self.speed))

    def advance(self):
        super().advance()
        self.life -= 1
        if self.life < 0:
            self.alive = False

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x_coordinate,
                                      self.center.y_coordinate,
                                      self.width, self.height,
                                      self.texture,
                                      self.angle,
                                      self.alpha)


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
        super().__init__(width, height, 'Asteroids Game')
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track

        self.bullets = []
        self.asteroids = []
        self.ships = []

        ship = Ship()
        self.ships.append(ship)

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

        for asteroid in self.asteroids:
            asteroid.draw()

        for bullet in self.bullets:
            bullet.draw()

        for ship in self.ships:
            ship.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collisions()
        # TODO: Tell everything to advance or move forward one step in time

        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.is_off_screen()

            if asteroid.alive is False:
                self.arteroids.remove(asteroid)

        for bullet in self.bullets:
            bullet.advance()
            bullet.is_off_screen()

            if bullet.alive is False:
                self.bullets.remove(bullet)

        for ship in self.ships:
            ship.advance()
            ship.is_off_screen()

        # TODO: Check for collisions
        self.check_collisions()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.UP in self.held_keys:
            for ship in self.ships:
                ship.thrust()

        if arcade.key.DOWN in self.held_keys:
            for ship in self.ships:
                ship.un_thrust()

        if arcade.key.RIGHT in self.held_keys:
            for ship in self.ships:
                ship.rotate_right()

        if arcade.key.LEFT in self.held_keys:
            for ship in self.ships:
                ship.rotate_left()

        if arcade.key.ESCAPE in self.held_keys:
            for asteroid in self.asteroids:
                self.asteroids.remove(asteroid)
            for ship in self.ships:
                ship.angle = 90

        # Machine gun mode...
        if arcade.key.SPACE in self.held_keys:
            pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ships[0].alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet(self.ships[0])
                bullet.fire(self.ships[0])

                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    def check_collisions(self):
        """
        Checks to see if bullets have hit asteroids.
        Removes dead items.
        :return:
        """

        # BULLETS Vs ASTEROIDS
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x_coordinate - asteroid.center.x_coordinate) < too_close and
                            abs(bullet.center.y_coordinate - asteroid.center.y_coordinate) < too_close):
                        # its a hit!
                        bullet.alive = False
                        asteroid.alive = False

                        asteroid.break_apart(self.asteroids)

        # SHIP Vs ASTEROIDS
        for asteroid in self.asteroids:
            for ship in self.ships:
                if ship.alive and asteroid.alive:
                    too_close = ship.radius + asteroid.radius

                    if (abs(ship.center.x_coordinate - asteroid.center.x_coordinate) < too_close and
                            abs(ship.center.y_coordinate - asteroid.center.y_coordinate) < too_close):
                        # its a hit!
                        # ship.alive = False
                        asteroid.alive = False

        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or asteroids from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

        for ship in self.ships:
            if not ship.alive:
                self.ships.remove(ship)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
