
from build123d import *
from ocp_vscode import show

t1337_pip_height          = 1.8 # lego pip height
t1337_pip_size            = 4.8 # lego pip size
t1337_unit_size           = 8.0 # lego unit size
t1337_brick_height        = 9.6 # lego brick height
t1337_hole_inner_diameter = 4.8 # lego hole inner diameter
t1337_hole_outer_diameter = 6.2 # lego hole outer diameter

x_units = 22
y_units = 1

part_length = x_units * t1337_unit_size
part_width  = y_units * t1337_unit_size
part_height = t1337_brick_height

with BuildPart() as t1337:
    # Base part
    length = part_length
    width  = part_width
    height = part_height
    Box(length, width, height)
    
    # Holes
    z_pos = 0.8
    for i in range(1, x_units):
        x_pos = -part_length / 2 + t1337_unit_size * i

        y_pos = t1337_unit_size / 2 - 0.4
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = t1337_hole_outer_diameter / 2
            height = 0.8
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
        y_pos = -t1337_unit_size / 2 + 0.4
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = t1337_hole_outer_diameter / 2
            height = 0.8
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
        y_pos = 0
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = t1337_hole_inner_diameter / 2
            height = t1337_unit_size
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
    
    # Bottom
    z_pos = -part_height / 2 + t1337_pip_height / 2
    y_pos = 0
    for i in range(x_units):
        x_pos = -part_length / 2 + t1337_unit_size / 2 + i * t1337_unit_size
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = t1337_pip_size
            width  = t1337_pip_size
            height = t1337_pip_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    # Top
    z_pos = part_height / 2 + t1337_pip_height / 2
    y_pos = 0
    for i in range(x_units):
        x_pos = -part_length / 2 + t1337_unit_size / 2 + i * t1337_unit_size
        with BuildPart(Location((x_pos, y_pos, z_pos))):
            length = t1337_pip_size
            width  = t1337_pip_size
            height = t1337_pip_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)


show(t1337.part, names=[__file__.rstrip('.py')])
export_stl(t1337.part, f"{__file__.rstrip('.py')}.stl")
