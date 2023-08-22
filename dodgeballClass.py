import config
import pygame
import os

class Dodgeball:
    def __init__(self, direction, number):
        self.direction = direction
        self.__id = number
        self.safe = True
        self.traveling = False
        self.stick = False

        # valid initialization checks
        if direction == 'RIGHT' or direction == 'LEFT': pass
        else: raise TypeError("Invalid 'direction' during Dodgeball object instantiation")
        if self.__id < 0 or self.__id > config.DODGEBALL_NUMBERS:
            raise TypeError("Invalid 'number' during Dodgeball object instantiation")
        

        # spawn location and spacing
        if direction == 'RIGHT':
            SPAWN_X = config.WIDTH - config.SPAWN_SIDE_PADDING - config.DODGEBALL_SIZE
        else:
            SPAWN_X = config.SPAWN_SIDE_PADDING
        SPAWN_Y = config.SPAWN_TOP_PADDING + config.DODGEBALL_SIZE * number
        if self.__id > 0: 
            SPAWN_Y = SPAWN_Y + config.SPAWN_BETWEEN_BALL_PADDING * number
        self.__spawn = (SPAWN_X, SPAWN_Y)

        # load image and hitbox
        DODGEBALL_IMAGE = pygame.image.load(os.path.join('Assets', 'dodgeball.png')).convert_alpha()
        self.ball = pygame.transform.scale(DODGEBALL_IMAGE, (config.DODGEBALL_SIZE, config.DODGEBALL_SIZE))
        self.hitbox = pygame.Rect(self.__spawn[0], self.__spawn[1], config.DODGEBALL_SIZE, config.DODGEBALL_SIZE)

    def _Stick(self, player):
        # makes ball stick to player
        if self.stick:
            if player.player_section == 'RIGHT':
                player.Get_Ball(self.__id).hitbox.x = player.hitbox.x - 8
                player.Get_Ball(self.__id).hitbox.y = (player.hitbox.y + config.PLAYER_HEIGHT // 2 - 10)
            else:
                player.Get_Ball(self.__id).hitbox.x = (player.hitbox.x + config.PLAYER_WIDTH - 10)
                player.Get_Ball(self.__id).hitbox.y = (player.hitbox.y + config.PLAYER_HEIGHT // 2)

    def __Delete(self, player):
        self.hitbox.x = self.__spawn[0]
        self.hitbox.y = self.__spawn[1]
        self.traveling = False
        self.stick = False
        return
    
    def _Get_Id(self):
        return self.__id

    def _Travel(self, player):
        if player.player_section == 'LEFT':
            self.hitbox.x += config.DODGEBALL_VELOCITY
        else:
            self.hitbox.x -= config.DODGEBALL_VELOCITY 
        
        if self.hitbox.x > config.WIDTH - config.DODGEBALL_SIZE or self.hitbox.x < 0:
            self.__Delete(player)
            