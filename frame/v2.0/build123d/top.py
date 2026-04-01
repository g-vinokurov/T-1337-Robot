
from build123d import *
from ocp_vscode import show

unit_size           = 8.0 # lego unit size
unit_height         = 9.6 # lego brick height
hole_inner_diameter = 4.8 # lego hole inner diameter
hole_outer_diameter = 6.2 # lego hole outer diameter

with BuildPart() as part:
    # База
    length = unit_size * 26
    width  = unit_size * 10
    height = unit_height * 2
    Box(length, width, height)
    
    # Вырезы
    x_pos = unit_size * -9
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 8
        width  = unit_size * 6
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 9
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 8
        width  = unit_size * 6
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = 44
        width  = 22
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = unit_size * -2.5
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 26
        width  = unit_size * 5
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -7.5
    y_pos = 0
    z_pos = unit_height
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 7
        width  = unit_size * 10
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 7.5
    y_pos = 0
    z_pos = unit_height
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 7
        width  = unit_size * 10
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = unit_size * 4
    z_pos = unit_height
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 8
        width  = unit_size * 2
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Отверстия под крепежные винты
    points = [
        (unit_size * -12, unit_size * 4,  0),
        (unit_size * -12, unit_size * -4, 0),
        (unit_size * 12,  unit_size * 4,  0),
        (unit_size * 12,  unit_size * -4, 0),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1.5
            height = unit_height * 2
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)
    
    # Утоплялки под крепежные винты
    z_pos = unit_height / 2
    points = [
        (unit_size * -12, unit_size * 4,  z_pos),
        (unit_size * -12, unit_size * -4, z_pos),
        (unit_size * 12,  unit_size * 4,  z_pos),
        (unit_size * 12,  unit_size * -4, z_pos),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 3
            height = unit_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)

    roundable_edges = part.edges().filter_by(Axis.Z)
    fillet(roundable_edges, radius=2)

filename = f'{__file__[:-3]}'

show(part.part, names=[filename])
export_stl(part.part, f'{filename}.stl')
