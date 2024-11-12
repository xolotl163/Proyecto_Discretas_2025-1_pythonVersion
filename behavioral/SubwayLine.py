
from . import Trainstation as Trainstation

class SubwayLine:

    def __init__(self,
                 id_subway_line: str = None, 
                 line_code: str = None, 
                 terminal_a: Trainstation  = None, 
                 terminal_b: Trainstation = None):
        
        self.line_code = line_code
        self.id_subway_line = id_subway_line
        self.terminal_a = terminal_a
        self.terminal_b = terminal_b

    # Getters
    def get_name(self):
        return self.name

    def get_line_code(self):
        return self.line_code

    def get_id_subway_line(self):
        return self.id_subway_line

    def get_terminal_a(self):
        return self.terminal_a

    def get_terminal_b(self):
        return self.terminal_b

    # Setters
    def set_name(self, name):
        self.name = name

    def set_line_code(self, line_code):
        self.line_code = line_code

    def print_subway_line(self):
        print(f"Subway Line: {self.name}, ID: {self.id_subway_line}, Line Code: {self.line_code}")

    # Destructor
    def __del__(self):
        pass

    # General methods to the class