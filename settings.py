class Settings():
    """formal game settings"""

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.background_color = (20, 20, 20)
        self.caption_display = "Alien Occupation"

    def __repr__(self):
        """Show all settings to screee"""
        settings_display = f"Screen settings... \nScreen width: {self.screen_width} \nScreen height: {self.screen_height}\
        \nBackground color: {self.background_color} \nScreen Caption: {self.caption_display}"
        return settings_display

