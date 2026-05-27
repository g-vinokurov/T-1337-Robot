
from build123d import *
from ocp_vscode import show

unit_size           = 8.0 # lego unit size
unit_height         = 9.6 # lego brick height
hole_inner_diameter = 4.8 # lego hole inner diameter
hole_outer_diameter = 6.2 # lego hole outer diameter

with BuildPart() as part:
    # База
    length = unit_size * 20
    width  = unit_size * 7
    height = unit_height
    Box(length, width, height)

    # Вырез
    x_pos = unit_size * 6.5
    y_pos = unit_size * 2.75
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 7
        width  = unit_size * 1.5
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 6.5
    y_pos = unit_size * -2.75
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 7
        width  = unit_size * 1.5
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    # Стенки
    x_pos = unit_size * 2.5
    y_pos = unit_size * 0
    z_pos = unit_height * 1.25
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 1
        width  = unit_size * 2
        height = unit_height * 1.5
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -3
    y_pos = unit_size * -3
    z_pos = unit_height * 1.25
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size * 1
        height = unit_height * 1.5
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -3
    y_pos = unit_size * 3
    z_pos = unit_height * 1.25
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size * 1
        height = unit_height * 1.5
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -9.5
    y_pos = unit_size * 0
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 1
        width  = unit_size * 2
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Отверстие под винт для камеры (1/4")
    x_pos = unit_size * 3 + 25
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = 3.1
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align)

    # Отверстия под крепежные винты для платы (3 mm)
    points = [
        (unit_size * 2.5, 0, 0),
        (unit_size * -3, unit_size * -3, 0),
        (unit_size * -3, unit_size * 3, 0),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1.5
            height = unit_height * 10
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)
    
    # Отверстия под крепежные для всей башни (3 mm)
    points = [
        (0   - unit_height * 2.5, 10,  0),
        (0   - unit_height * 2.5, -10, 0),
        (10  - unit_height * 2.5, 0,  0),
        (-10 - unit_height * 2.5, 0, 0),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1.5
            height = unit_height * 10
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)
    
    # Утоплялки
    points = [
        (0   - unit_height * 2.5, 10, unit_height / 2 - 1.5),
        (0   - unit_height * 2.5, -10, unit_height / 2 - 1.5),
        (10  - unit_height * 2.5, 0,  unit_height / 2 - 1.5),
        (-10 - unit_height * 2.5, 0, unit_height / 2 - 1.5),
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
