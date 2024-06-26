import pygame

class Sound:
    def __init__(self):
        # Initialize Pygame mixer
        pygame.mixer.init()

        # Load sounds
        self.sound_effects = {
            'draw': pygame.mixer.Sound('Sound/draw.wav'),
            'heal': pygame.mixer.Sound('Sound/heal.wav'),
            'attack': pygame.mixer.Sound('Sound/attack.wav'),
            'block': pygame.mixer.Sound('Sound/block.wav'),
            'enemy_attack': pygame.mixer.Sound('Sound/enemy_attack.wav')
            # Add more sounds as needed
        }

        # Load music tracks
        self.music_tracks = {
            'Start': 'Sound/Start.wav',
            'Easy': 'Sound/Easy.wav',
            'Medium': 'Sound/Medium.wav',
            'Hard': 'Sound/Hard.wav',
            # Add more music tracks as needed
        }

    def play_sound(self, sound_key):
        if sound_key in self.sound_effects:
            self.sound_effects[sound_key].play()

    def play_music(self, music_key):
        if music_key in self.music_tracks:
            pygame.mixer.music.load(self.music_tracks[music_key])
            pygame.mixer.music.play(-1)  # Loop indefinitely

    def stop_music(self):
        pygame.mixer.music.stop()

    def switch_music(self, music_key):
        """Switches the music to the specified track."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        self.play_music(music_key)