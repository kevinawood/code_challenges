class Settings():

    def __init__(self):
        '''Initialise game settings'''
        # Screen settings
        self.screen_width = 800
        self.screen_height = 400
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        #Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
