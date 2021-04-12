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
SCREE_TITLE = 'Asteroids Game, by Carlos W. Mercado, for CS241, Spring Semester 2020 ☺'

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_TIME_NEXTONE = 10.0

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15
BIG_ROCK_SCORE = 1

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5
MEDIUM_ROCK_SCORE = 2

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2
SMALL_ROCK_SCORE = 3

# HAS-A section
'''
Point and Velocity classes are owned
by FlyingObject class and its sub-classes.
'''


class Point:

    def __init__(self):
        self.x_coordinate = 100
        self.y_coordinate = 100


class Velocity:

    def __init__(self):
        self.dx = 0
        self.dy = 0


# IS-A Section
'''
Main parent class: From ABC superclass: FlyingObject
1st child class: Asteroid, Ship, Bullet
2nd child class: From Asteroid: BigRock, MediumRock, SmallRock
'''


# This is an abstract class
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


# This is an abstract class
class Asteroid(FlyingObject):

    def __init__(self, img):
        super().__init__(img)
        self.radius = BIG_ROCK_RADIUS

    def break_apart(self, asteroids):
        pass


# At the beginning of the game there are just 5 rocks, and each one scores 1 point
# Every time a BigRock is destroyed, it generates 2 medium rocks and 1 small one.
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


# Every destroyed MediumRock scores 2 points
# Every time a BigRock is destroyed, it generates 2 small rocks
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


# Every destroyed MediumRock scores 3 points
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


# Ship's velocity adds to bullet's velocity. For this purpose the bullet's constructor
# requires a ship object. Also the ship's position is required.
class Bullet(FlyingObject):

    def __init__(self, ship: Ship):
        super().__init__("images/laser.png")
        self.angle = ship.angle
        self.speed = ship.speed + BULLET_SPEED
        self.radius = BULLET_RADIUS
        self.center.x_coordinate = ship.center.x_coordinate + SHIP_RADIUS * math.cos(math.radians(self.angle))
        self.center.y_coordinate = ship.center.y_coordinate + SHIP_RADIUS * math.sin(math.radians(self.angle))
        self.life = BULLET_LIFE
        self.ship_velocity_dx = ship.velocity.dx
        self.ship_velocity_dy = ship.velocity.dy

    def fire(self, ship):
        self.velocity.dx = math.cos(math.radians(ship.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(ship.angle)) * self.speed

    # The bullet dies after 60 frames.
    def advance(self):
        self.center.x_coordinate += (self.velocity.dx + self.ship_velocity_dx)
        self.center.y_coordinate += (self.velocity.dy + self.ship_velocity_dy)
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


# View Section
'''
→ FROM main(): window, instance of arcade.Window(), the its view is changed to
one of the following classes.
    Main parent class: arcade.View
    Children: MenuView, PauseView, GameOverView, YouWinView, GameView
    GameView contains the whole logic for the main game.
    
Every view changes over different events (keyboard events, or in game events).
'''


# Start the game, Close the game
class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("ASTEROIDS",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 + 80,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center")
        arcade.draw_text("By Carlos W. Mercado, for CS241",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 + 60,
                         arcade.color.GRAY,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("SPRING Semester, 2020",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 + 35,
                         arcade.color.GRAY,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press ENTER to start",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 5,
                         arcade.color.GRAY,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("ESCAPE to play again",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.GRAY,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Q to quit the game",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 55,
                         arcade.color.GRAY,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("P to pause the game",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 80,
                         arcade.color.GRAY,
                         font_size=20, anchor_x="center")

        arcade.draw_text("ARROWS to move the ship",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 120,
                         arcade.color.GRAY,
                         font_size=20, anchor_x="center")
        arcade.draw_text("SPACEBAR to shoot laser",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 145,
                         arcade.color.GRAY,
                         font_size=20, anchor_x="center")
        arcade.draw_text("Hold SPACEBAR for machine gun mode",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 170,
                         arcade.color.GRAY,
                         font_size=20, anchor_x="center")

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.ENTER:  # starts the game
            game = GameView()
            self.window.show_view(game)
        if key == arcade.key.Q:  # closes the game's main window
            arcade.close_window()


# Pause, GameOver the restart, Close the game
class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("PAUSED",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.WHITE,
                         font_size=50,
                         anchor_x="center")

        arcade.draw_text("P to unpause the game",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

        arcade.draw_text("ESCAPE to play again",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

        arcade.draw_text("Q to quit the game",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.P:  # unpause the game, the game is pause in the GameView class
            self.window.show_view(self.game_view)
        if key == arcade.key.ESCAPE:  # sends to the game over screen
            game = GameOverView()
            self.window.show_view(game)
        if key == arcade.key.Q:  # closes the game
            arcade.close_window()


# Opens main menu, Close the game
class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RED)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("GAME OVER",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE,
                         font_size=50,
                         anchor_x="center")

        arcade.draw_text("ESCAPE to play again",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

        arcade.draw_text("Q to quit game",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:  # from game over screen to menu screen
            game = MenuView()
            self.window.show_view(game)
        if key == arcade.key.Q:     # closes the game
            arcade.close_window()


# Open main menu, Close the game
class YouWinView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.score = score

    def on_show(self):
        arcade.set_background_color(arcade.color.KELLY_GREEN)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("YOU WIN",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30,
                         arcade.color.WHITE,
                         font_size=50,
                         anchor_x="center")

        arcade.draw_text("Your score was: {}".format(self.score),
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE,
                         font_size=30,
                         anchor_x="center")

        arcade.draw_text("ESCAPE to play again",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

        arcade.draw_text("Q to quit game",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:  # send to the menu screen
            game = MenuView()
            self.window.show_view(game)
        if key == arcade.key.Q:     # closes the game
            arcade.close_window()

# MAIN CLASS IN THE PROGRAM
# This class handles the game and the event handlers
class GameView(arcade.View):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.
    """

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        # TODO: declare anything here you need the game class to track
        self.held_keys = set()
        self.score = 0
        self.lives = 2
        self.time_next_bullet = BULLET_TIME_NEXTONE
        self.bullets = []
        self.asteroids = []
        self.ships = []

        ship = Ship()
        self.ships.append(ship)

        self.asteroids.clear()
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

        # Draw score and life counter
        self.draw_score()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # TODO: Tell everything to advance or move forward one step in time

        # The following loops also keep track of the objects while they move from off the screen.
        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.is_off_screen()

            if asteroid.alive is False:
                self.asteroids.remove(asteroid)

        for bullet in self.bullets:
            bullet.advance()
            bullet.is_off_screen()

            if bullet.alive is False:
                self.bullets.remove(bullet)

        for ship in self.ships:
            ship.advance()
            ship.is_off_screen()

        # The player wins the game when there are no more asteroids left in the game.
        if len(self.asteroids) == 0:
            game = YouWinView(self.score)
            self.window.show_view(game)

        # For Machine Gun Mode, it is possible to fire a new bullet after BULLET_TIME_NEXTONE
        self.time_next_bullet -= 1
        if self.time_next_bullet < 0:
            self.time_next_bullet = BULLET_TIME_NEXTONE

        # TODO: Check for collisions and keys on keyboard, on time
        self.check_keys()
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

        # RESTARTING THE GAME while in the GameView
        if arcade.key.ESCAPE in self.held_keys:
            game = MenuView()
            self.window.show_view(game)

        # Machine gun mode...
        if arcade.key.SPACE in self.held_keys:
            # Track of time is kept
            if self.time_next_bullet == 0:
                bullet = Bullet(self.ships[0])
                bullet.fire(self.ships[0])
                self.bullets.append(bullet)

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

        # PAUSE the game
        if key == arcade.key.P:
            game = PauseView(self)
            self.window.show_view(game)

        # Game Over because the player wants to
        if key == arcade.key.Q:
            game = GameOverView()
            self.window.show_view(game)

        # If you want to play again while IN GAME, you lose. No giving up!
        if key == arcade.key.ESCAPE:
            game = GameOverView()
            self.window.show_view(game)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        Necessary for all keys.
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
                        # it's a hit!
                        bullet.alive = False
                        asteroid.alive = False

                        # SCORING
                        if type(asteroid).__name__ == 'BigRock':
                            self.score += BIG_ROCK_SCORE
                        if type(asteroid).__name__ == 'MediumRock':
                            self.score += MEDIUM_ROCK_SCORE
                        if type(asteroid).__name__ == 'SmallRock':
                            self.score += SMALL_ROCK_SCORE

                        # Some asteroids produce more asteroids!
                        asteroid.break_apart(self.asteroids)

        # SHIP Vs ASTEROIDS
        for asteroid in self.asteroids:
            for ship in self.ships:
                if ship.alive and asteroid.alive:
                    too_close = ship.radius + asteroid.radius

                    if (abs(ship.center.x_coordinate - asteroid.center.x_coordinate) < too_close and
                            abs(ship.center.y_coordinate - asteroid.center.y_coordinate) < too_close):
                        # its a hit!
                        asteroid.alive = False
                        self.lives -= 1

                        # If the ship is hit 2 times is GAME OVER, babe!
                        if self.lives < 1:
                            ship.alive = False
                            game = GameOverView()
                            self.window.show_view(game)

        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or asteroids from the list, also the ship.
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

    def draw_score(self):
        """
        Puts the current score on the screen, and lives
        """
        score_text = "Score: {} \n" \
                     "Lives: {}".format(self.score, self.lives)
        start_x = 10
        start_y = SCREEN_HEIGHT - 40
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=15, color=arcade.color.WHITE)


# Creates the game and starts it going
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREE_TITLE)
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == '__main__':
    main()
