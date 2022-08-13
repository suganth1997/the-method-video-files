from math import cos, sin, sqrt, tan, atan, pi
from random import triangular
from typing_extensions import runtime
from click import style
from manim import *

class ConcludeScene(Scene):
    def construct(self):
        archimedes_quote_1 = Text("Mathematics reveals its secrets only to those who approach it with pure love,", font_size=20).to_edge(LEFT)
        archimedes_quote_2 = Text("for its own beauty.", font_size=20).next_to(archimedes_quote_1, DOWN).to_edge(LEFT)
        
        archimedes_name = Text("~ Archimedes", slant=ITALIC, font_size=18).next_to(archimedes_quote_2, DOWN).to_edge(RIGHT)

        self.play(Write(archimedes_quote_1))

        self.play(Write(archimedes_quote_2))

        self.play(Write(archimedes_name))

        self.wait(10)
