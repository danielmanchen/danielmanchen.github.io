import arcade
import random

import arcade.key
import arcade.sprite_list

SPRITE_SIZE = 32
MAZE_WIDTH = 20
MAZE_HEIGHT = 20
SCREEN_WIDTH = MAZE_WIDTH - 1
SCREEN_HEIGHT = MAZE_HEIGHT - 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GREEN)
        self.wall_list = None
        self.path_list = None
        self.solution_list = []
        self.solution_sprite_list = None
        self.player_sprite = None
        self.goal_sprite = None
        self.test_sprite = None
        self.can_solve = False
        self.game_over = False


    def setup(self):
        self.can_solve = False
        self.wall_list = arcade.SpriteList()
        self.path_list = arcade.SpriteList()
        self.solution_sprite_list = arcade.SpriteList()

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
        
        self.maze_solver()

        
        
        
        if self.can_solve == True:
            for i in self.solution_list:
                
                for j in self.path_list:
                    if i.get("position") == j.position:
                        self.path_list.remove(j)
                
        
    def on_draw(self):
        if self.can_solve == False or (self.player_sprite.position == self.goal_sprite.position):
            self.solution_list = []
            self.setup()
        arcade.start_render()
        self.wall_list.draw()

        self.path_list.draw()
        
        
        self.player_sprite.draw()
        self.goal_sprite.draw()
        
        self.solution_sprite_list.draw() 
        
        
          
        

    
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
    
    def maze_solver(self):
        start = self.player_sprite.position
        goal = self.goal_sprite.position
        total_avail = []
        open_list = []
        closed_list = []

        for sprite in self.path_list:
            g_value = self.g_value(self.player_sprite, sprite)
            h_value = self.hueristic(sprite)
            total_avail.append({"position" : sprite.position,
                                "f-value" : g_value + h_value,
                                "g-value" : g_value,
                                "h-value" : h_value,
                                "neighbors" : None,
                                "parent" : None})
        startNode = None
        for node in total_avail:
            if node.get("position") == start:
                startNode = node
                open_list.append(startNode)
                break
        
        while len(open_list) > 0:
            current = min(open_list, key=lambda x:x["f-value"])
            # checks if the goal has been found
            if current["position"] == goal:
                
                print("found path")
                for i in closed_list:
                    self.solution_list.append(i)
                    print(i["position"])
                
                    
                self.can_solve = True
                
                break  
            current["neighbors"] = self.get_neighbors(current, total_avail)
            closed_list.append(current)
            open_list.remove(current)
            
            for neighbor in current["neighbors"]:
                
                if neighbor in closed_list:
                    break
                if neighbor not in open_list:
                    open_list.append(neighbor)
                    open_list[open_list.index(neighbor)]["parent"] = current
                    
                if neighbor in open_list:
                    if neighbor["g-value"] < current["g-value"]:
                        open_list[open_list.index(neighbor)]["parent"] = current
            if len(open_list) <= 0:
                print("Could not find path")
                self.can_solve = False
                break


               


           
               

    def get_neighbors(self, node, open_list):
        neighbors = []
        left = (node["position"][0] - 32, node["position"][1] + 0)
        right = (node["position"][0] + 32, node["position"][1] + 0)
        up = (node["position"][0] + 0, node["position"][1] + 32)
        down = (node["position"][0] + 0, node["position"][1] - 32)
        for node in open_list:
            if node.get("position") == left:
                neighbors.append(node)
            if node.get("position") == right:
                neighbors.append(node)
            if node.get("position") == up:
                neighbors.append(node)
            if node.get("position") == down:
                neighbors.append(node)
        return neighbors
        
        
        

        
        
        


    def g_value(self, start, current):
        return arcade.get_distance_between_sprites(start, current)
    
    # The hueristic "H value" for the A* algorithm      
    def hueristic(self, node):
        dx = abs(node.position[0] - self.goal_sprite.position[0])
        dy = abs(node.position[1] - self.goal_sprite.position[1])
        return 1 * (dx + dy)


def main():
    game = MyGame(MAZE_WIDTH * SPRITE_SIZE, MAZE_HEIGHT * SPRITE_SIZE, "Maze Pathing")
    game.setup()
    
    arcade.run()

if __name__ == "__main__":
    main()