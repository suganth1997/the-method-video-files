from math import sqrt
from manim import *

class IntroScene(MovingCameraScene):
    def construct(self):
        archimedes = ImageMobject('Archimedes.jpg').scale(0.25).to_edge(RIGHT)

        archimedes_quote_1 = Text("Mathematics reveals its secrets only to those who approach it with pure love,", font_size=20).to_edge(UP).to_edge(LEFT)
        archimedes_quote_2 = Text("for its own beauty.", font_size=20).next_to(archimedes_quote_1, DOWN).to_edge(LEFT)
        
        archimedes_name = Text("~ Archimedes", slant=ITALIC, font_size=18).next_to(archimedes_quote_2, DOWN).to_edge(RIGHT)

        self.play(Create(archimedes_quote_1))

        self.play(Create(archimedes_quote_2))

        self.play(Create(archimedes_name))

        self.play(FadeIn(archimedes))

        self.wait(2)

        self.play(Uncreate(archimedes_quote_1), Uncreate(archimedes_quote_2), Uncreate(archimedes_name))

        self.play(archimedes.animate.to_corner(UP + RIGHT))

        fulcrum = Polygon(ORIGIN, (LEFT+DOWN)/2, (RIGHT+DOWN)/2, fill_opacity=1)

        lever = Line(3*LEFT, 3*RIGHT, color=BLUE)

        left_circle = Circle(0.3, color=BLUE, fill_opacity=1).move_to(3*LEFT)

        right_circle = Circle(0.15, color=BLUE, fill_opacity=1).move_to(3*RIGHT)

        center = Dot(color=BLUE)

        lever_and_all = VGroup(lever, left_circle, right_circle)

        fulcrum_and_lever = VGroup(fulcrum, center, lever_and_all)

        lever_law = Text("Law of Levers", font_size=20).to_corner(LEFT+UP)

        cup = VGroup(Line(LEFT+UP, (LEFT+DOWN)), Line((LEFT+DOWN), (RIGHT+DOWN)), Line((RIGHT+DOWN), RIGHT+UP))

        water_level = Line(LEFT, RIGHT)
        
        self.play(Create(fulcrum), Create(center))

        # self.play(Create(lever), Create(center), Create(left_circle), Create(right_circle))

        self.play(Create(lever_and_all))

        self.play(lever_and_all.animate.rotate(PI/12, about_point=ORIGIN))

        self.play(lever_and_all.animate.rotate(-PI/12, about_point=ORIGIN))

        self.play(lever_and_all.animate.shift(RIGHT))

        self.play(Create(lever_law), fulcrum_and_lever.animate.shift((LEFT+UP)*2.25))

        self.play(Create(cup))

        self.wait(2)