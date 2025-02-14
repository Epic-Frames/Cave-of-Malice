class Text ():
    def __init__(self, x, y, text, font, color, SCREEN_X, SCREEN_Y):
        self.text = text
        self.font = font
        self.color = color

        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_width, self.text_height = self.text_surface.get_size()

        if x is None:
            self.x = (SCREEN_X / 2) - (self.text_width / 2)
        else:
            self.x = x

        if y is None:
            self.y = (SCREEN_Y / 2) - (self.text_height / 2)
        else:
            self.y = y


    def blink(self, screen, seconds, frame, halfFrames, startpoint, time):
        frames = seconds * 30

        if frame == None:
            self.color = (0, 0, 0)
            frame = 0
        if halfFrames == None:
            halfFrames = frames / 2

        if halfFrames == 0:
            var = 250 / (frames / 2)
        else:
            var = 250 / halfFrames

        if time >= startpoint:
            if frame < halfFrames:
                self.color = tuple(min(255, self.color[i] + var) for i in range(3))
                self.text_surface = self.font.render(self.text, True, self.color)
                screen.blit(self.text_surface, (self.x, self.y))
                frame += 1
            elif frame > 0:
                self.color = tuple(max(0, self.color[i] - var) for i in range(3))
                self.text_surface = self.font.render(self.text, True, self.color)
                screen.blit(self.text_surface, (self.x, self.y))
                frame -= 1
                halfFrames = 0
            else:
                return 0, 0
        
        return frame, halfFrames


    def get_width(self):
        width, _ = self.text_surface.get_size()
        return width
    

    def get_height(self):
        _, height = self.text_surface.get_size()
        return height


    def show(self, screen):
        screen.blit(self.text_surface, (self.x, self.y))
    

    def update_text(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.color)
