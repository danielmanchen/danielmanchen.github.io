import arcade
import random

import arcade.key
import arcade.sprite_list

SPRITE_SIZE = 32
MAZE_WIDTH = 10
MAZE_HEIGHT = 10
SCREEN_WIDTH = MAZE_WIDTH - 1
SCREEN_HEIGHT = MAZE_HEIGHT - 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.wall_list = None
        self.path_list = None
        
        self.player_sprite = None
        


    def setup(self):
       
        self.wall_list = arcade.SpriteList()
        self.path_list = arcade.SpriteList()
        

        # Generate the maze using a simple algorithm (e.g., randomized Prim's algorithm)
        for row in range(MAZE_HEIGHT):
            
            for column in range(MAZE_WIDTH):
                if random.random() < 0.4:  # 30% chance of creating a wall
                    wall = arcade.SpriteSolidColor(SPRITE_SIZE, SPRITE_SIZE, arcade.color.GRAY)
                    wall.center_x = column * SPRITE_SIZE + SPRITE_SIZE / 2
                    wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                    self.wall_list.append(wall)
                else:
                    path = arcade.SpriteSolidColor(SPRITE_SIZE, SPRITE_SIZE, arcade.color.BLUE)
                    path.center_x = column * SPRITE_SIZE + SPRITE_SIZE / 2
                    path.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                    self.path_list.append(path)
        
        # Set up the player sprite
        start = random.choice(self.path_list)
        goal = random.choice(self.path_list)

        self.player_sprite = arcade.SpriteSolidColor(SPRITE_SIZE, SPRITE_SIZE, arcade.color.WHITE)
        self.player_sprite.center_x = start.center_x
        self.player_sprite.center_y = start.center_y

        self.goal_sprite = arcade.SpriteSolidColor(SPRITE_SIZE, SPRITE_SIZE, arcade.color.RED)
        self.goal_sprite.center_x = goal.center_x
        self.goal_sprite.center_y = goal.center_y
        
        
            
                
                
        

        
        
        
        

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.path_list.draw()
        self.player_sprite.draw()
        self.goal_sprite.draw()
        
        if self.player_sprite.position == self.goal_sprite.position:
            self.setup()
          
        

    
    def on_key_press(self, key, modifiers):
        #Called whenever a key is pressed.
        x_position = self.player_sprite.center_x
        y_position = self.player_sprite.center_y

        if key == arcade.key.UP:
            if self.player_sprite.top < MAZE_HEIGHT * SPRITE_SIZE:
                self.move_player(x_position, y_position, 0, 32)
        elif key == arcade.key.DOWN:
            if self.player_sprite.bottom > 0:
                self.move_player(x_position, y_position, 0, -32)
        elif key == arcade.key.LEFT:
            if self.player_sprite.left > 0:
                self.move_player(x_position, y_position, -32, 0)
        elif key == arcade.key.RIGHT:
            if self.player_sprite.right < MAZE_WIDTH * SPRITE_SIZE:
                self.move_player(x_position, y_position, 32, 0)
        

    def move_player(self, x_position, y_position, move_x, move_y):
        self.player_sprite.set_position(x_position + move_x, y_position + move_y)
        
        for i in self.wall_list:
            if i.position == self.player_sprite.position:
                self.player_sprite.set_position(x_position, y_position)
def main():
    game = MyGame(MAZE_WIDTH * SPRITE_SIZE, MAZE_HEIGHT * SPRITE_SIZE, "Maze Pathing")
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()