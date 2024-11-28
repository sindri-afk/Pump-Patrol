import pyfiglet

class Logo:
    def draw(self):
        ascii_banner = pyfiglet.figlet_format("Pump Patrol")
        print(ascii_banner)