
from build123d import *
from ocp_vscode import show

unit_size           = 8.0 # lego unit size
unit_height         = 9.6 # lego brick height
hole_inner_diameter = 4.8 # lego hole inner diameter
hole_outer_diameter = 6.2 # lego hole outer diameter

with BuildPart() as part:
    # База
    length = unit_size * 32
    width  = unit_size * 8
    height = unit_height
    Box(length, width, height)

    # Вырезы
    x_pos = unit_size * -13
    y_pos = unit_size * 3
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 6
        width  = unit_size * 2
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 13
    y_pos = unit_size * 3
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 6
        width  = unit_size * 2
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -13
    y_pos = unit_size * -3
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 6
        width  = unit_size * 2
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 13
    y_pos = unit_size * -3
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 6
        width  = unit_size * 2
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 6
        width  = unit_size * 5.5
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 17.5
        width  = unit_size * 4
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Отверстия под крепежные винты
    points = [
        # Wheelbase
        (unit_size * 0,    unit_size * 3.5,  0),
        (unit_size * 0,    unit_size * -3.5, 0),
        (unit_size * 7,    unit_size * 3.5,  0),
        (unit_size * 7,    unit_size * -3.5, 0),
        (unit_size * -7,   unit_size * 3.5,  0),
        (unit_size * -7,   unit_size * -3.5, 0),
        (unit_size * -9.5,               0,  0),
        (unit_size * 9.5,                0,  0),
        # Engines
        (unit_size * 12.0, unit_size * 1.5,  0),
        (unit_size * 12.0, unit_size * -1.5, 0),
        (unit_size * -12.0,unit_size * 1.5,  0),
        (unit_size * -12.0,unit_size * -1.5, 0),
        (unit_size * 14.0, unit_size * 1.5,  0),
        (unit_size * 14.0, unit_size * -1.5, 0),
        (unit_size * -14.0,unit_size * 1.5,  0),
        (unit_size * -14.0,unit_size * -1.5, 0),
        (unit_size * 13.0, unit_size * 1,    0),
        (unit_size * 13.0, unit_size * -1,   0),
        (unit_size * -13.0,unit_size * 1,    0),
        (unit_size * -13.0,unit_size * -1,   0),
        # Arduino
        (unit_size * -5, 24.15, 0),
        (unit_size * -5 - 1.2, -24.15, 0),
        (unit_size * -5 + 75, 24.15, 0),
        (unit_size * -5 -1.2 + 82.6, -24.15, 0),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1.5
            height = unit_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)
    
    # Утоплялки под крепежные винты
    z_pos = unit_height / 2 - 1.5
    points = [
        # Wheelbase
        (unit_size * 0,    unit_size * 3.5,  z_pos),
        (unit_size * 0,    unit_size * -3.5, z_pos),
        (unit_size * 7,    unit_size * 3.5,  z_pos),
        (unit_size * 7,    unit_size * -3.5, z_pos),
        (unit_size * -7,   unit_size * 3.5,  z_pos),
        (unit_size * -7,   unit_size * -3.5, z_pos),
        (unit_size * -9.5,               0,  z_pos),
        (unit_size * 9.5,                0,  z_pos),
        # Arduino
        (unit_size * -5, 24.15, -z_pos),
        (unit_size * -5 - 1.2, -24.15, -z_pos),
        (unit_size * -5 + 75, 24.15, -z_pos),
        (unit_size * -5 -1.2 + 82.6, -24.15, -z_pos),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 3
            height = 3
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)

    roundable_edges = part.edges().filter_by(Axis.Z)
    fillet(roundable_edges, radius=2)

filename = f'{__file__.rstrip('.py')}'

show(part.part, names=[filename])
export_stl(part.part, f'{filename}.stl')
