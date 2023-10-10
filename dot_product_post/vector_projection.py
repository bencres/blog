from manim import *

# This is very brute-force because I don't have time to properly learn Manim right now. 
# Check out the documentation for better practices. 

class VectorUnitCircle(Scene):
    def construct(self):

        # Create a plane.
        plane = NumberPlane(x_range = [-1 ,1, 0.2], y_range = [-1, 1, 0.2], x_length = 7, y_length = 7)
        plane.add_coordinates()
        plane.center()
        
        # Create the a vector.
        vect1 = Line(start = plane.coords_to_point(0, 0), end = plane.coords_to_point(1, 0), stroke_color = YELLOW).add_tip(tip_length=0.25, tip_width = 0.25)
        vect1_name = MathTex("\\vec{a}").next_to(vect1, UP).set_color(YELLOW)
        vect1_name.font_size = 64

        # Create the b vector. 
        vect2 = Line(start = plane.coords_to_point(0, 0), end = plane.coords_to_point(0.6, 0.8), stroke_color = RED).add_tip(tip_length = 0.25, tip_width = 0.25)
        vect2_name = MathTex("\\vec{b}").next_to(vect2, LEFT, buff = -0.8).set_color(RED)
        vect2_name.font_size = 64
        
        # Create the x component of vector b. 
        vect3 = DashedLine(start = plane.coords_to_point(0, 0), end = plane.coords_to_point(0.6, 0), stroke_color = RED, stroke_width = 5).add_tip(tip_length = 0.2, tip_width = 0.2)
        vect3_name = MathTex("\\vec{b}\\cos{\\theta}").next_to(vect3, DOWN, buff = 0.1).set_color(RED)
        vect3_name.font_size = 32

        # Create the line to project vector b on vector a.         
        line = DashedLine(start = plane.coords_to_point(0.6, 0), end = plane.coords_to_point(0.6, 0.8), stroke_color = RED)

        # Create the angle between the vectors. 
        angle = Angle(vect1, vect2, radius=0.3, stroke_color = GREEN)
        angle_name = MathTex("\\theta").next_to(angle, RIGHT, buff = -0.1).set_color(GREEN)
        angle_name.font_size = 32
        angle_name.shift(0.1)
        
        # Define the radius of the unit circle. 
        rad = plane.coords_to_point(1, 1) - plane.coords_to_point(0, 0)
        
        # Create the unit circle. 
        circ = Circle(radius = rad, color = GREEN).set_x(plane.coords_to_point(0, 0)[0]).set_y(plane.coords_to_point(0, 0)[1])
        
        # Add it all to be rendered. 
        self.add(plane, circ, vect1, vect1_name, vect2, vect2_name, vect3, vect3_name, line, angle, angle_name)
        