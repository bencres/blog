from manim import *

# This is very brute-force because I don't have time to properly learn Manim right now. 
# Check out the documentation for better practices. 

class VectorTest(Scene):
    def construct(self):
        # Create a plane. 
        plane = NumberPlane(x_range = [-5, 5, 1], y_range = [-5, 5, 1], x_length = 7, y_length = 7)
        plane.add_coordinates()
        plane.center()

        # Create the vector a. 
        vect1 = Line(start = plane.coords_to_point(0, 0), end = plane.coords_to_point(0.45, 0.89), stroke_color = YELLOW).add_tip(tip_length=0.1, tip_width = 0.1)
        vect1_name = MathTex("\\vec{a}").next_to(vect1, LEFT, buff=0.1).set_color(YELLOW)

        # Create the vector b. 
        vect2 = Line(start = plane.coords_to_point(0, 0), end = plane.coords_to_point(0.6, 0.8), stroke_color = RED).add_tip(tip_length = 0.1, tip_width = 0.1)
        vect2_name = MathTex("\\vec{b}").next_to(vect2, RIGHT, buff=0.1).set_color(RED)
        
        # Define the radius of the unit circle. 
        rad = plane.coords_to_point(1, 1) - plane.coords_to_point(0, 0)
        
        # Create the unit circle. 
        circ = Circle(radius = rad, color = GREEN).set_x(plane.coords_to_point(0, 0)[0]).set_y(plane.coords_to_point(0, 0)[1])
        
        # Add it all to be rendered. 
        self.add(plane, circ, vect1, vect1_name, vect2, vect2_name)