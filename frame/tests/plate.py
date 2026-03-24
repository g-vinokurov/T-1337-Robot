
from build123d import *
from ocp_vscode import show

t1337_pip_height          = 1.8 # lego pip height
t1337_pip_size            = 4.8 # lego pip size
t1337_unit_size           = 8.0 # lego unit size
t1337_brick_height        = 9.6 # lego brick height
t1337_hole_inner_diameter = 4.8 # lego hole inner diameter
t1337_hole_outer_diameter = 6.2 # lego hole outer diameter
t1337_plate_height        = 3.2

x_units = 4
y_units = 8

part_length = x_units * t1337_unit_size
part_width  = y_units * t1337_unit_size
part_height = t1337_plate_height

with BuildPart() as t1337:
    # Base part
    length = part_length - 0.2
    width  = part_width  - 0.2
    height = part_height - 0.2
    Box(length, width, height)
    
    # Bottom
    z_pos = -(part_height - 0.2) / 2 + t1337_pip_height / 2
    for i in range(x_units):
        for j in range(y_units):
            x_pos = -part_length / 2 + t1337_unit_size / 2 + i * t1337_unit_size
            y_pos = -part_width / 2 + t1337_unit_size / 2 + j * t1337_unit_size
        
            with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
                length = t1337_pip_size   + 0.18
                width  = t1337_pip_size   + 0.18
                height = t1337_pip_height + 0.18
                align  = (Align.CENTER, Align.CENTER, Align.CENTER)
                Box(length, width, height)
    
    # Top
    z_pos = (part_height - 0.2) / 2 + (t1337_pip_height - 0.2) / 2
    for i in range(x_units):
        for j in range(y_units):
            x_pos = -part_length / 2 + t1337_unit_size / 2 + i * t1337_unit_size
            y_pos = -part_width / 2 + t1337_unit_size / 2 + j * t1337_unit_size
        
            with BuildPart(Location((x_pos, y_pos, z_pos))):
                length = t1337_pip_size   - 0.2
                width  = t1337_pip_size   - 0.2
                height = t1337_pip_height - 0.2
                align  = (Align.CENTER, Align.CENTER, Align.CENTER)
                Box(length, width, height)


filename = f'{__file__.rstrip('.py')}_{x_units}x{y_units}'

show(t1337.part, names=[filename])
export_stl(t1337.part, f'{filename}.stl')
