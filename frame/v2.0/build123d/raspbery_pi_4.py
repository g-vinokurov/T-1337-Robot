
from build123d import *
from ocp_vscode import show

unit_size           = 8.0 # lego unit size
unit_height         = 9.6 # lego brick height
hole_inner_diameter = 4.8 # lego hole inner diameter
hole_outer_diameter = 6.2 # lego hole outer diameter

with BuildPart() as part:
    # База
    length = unit_size * 12
    width  = unit_size * 9
    height = unit_height
    Box(length, width, height)

    # Вырезы
    x_pos = 0
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 9
        width  = unit_size * 5
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    # Стенки
    x_pos = 0
    y_pos = unit_size * 4 + 1.0
    z_pos = unit_height * 1
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 12
        width  = unit_size - 2.0
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 4.5
    y_pos = unit_size * -4 - 1.0
    z_pos = unit_height * 1
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 3
        width  = unit_size - 2.0
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -5.5 - 1.0
    y_pos = 0
    z_pos = unit_height * 1
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size - 2.0
        width  = unit_size * 9
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -5.5
    y_pos = 0
    z_pos = unit_height * 1
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size
        width  = unit_size * 2
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = unit_size * 4
    z_pos = unit_height * 1
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 6
        width  = unit_size
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    # Отверстия под монтажные винты для платы
    points = [
        (unit_size * -5 + 3.5,      24.5, 0),
        (unit_size * -5 + 3.5,     -24.5, 0),
        (unit_size * -5 + 3.5 + 58, 24.5, 0),
        (unit_size * -5 + 3.5 + 58,-24.5, 0),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1
            height = unit_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)
    
    # Утоплялки под монтажные винты для платы
    points = [
        (unit_size * -5 + 3.5,      24.5, -unit_height / 2 + 1),
        (unit_size * -5 + 3.5,     -24.5, -unit_height / 2 + 1),
        (unit_size * -5 + 3.5 + 58, 24.5, -unit_height / 2 + 1),
        (unit_size * -5 + 3.5 + 58,-24.5, -unit_height / 2 + 1),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 2
            height = 2
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)
    
    # Отверстия под монтажные винты (3 mm)
    points = [
        (unit_size * -5.5, 0, 0),
        (0, unit_size * -3, 0),
        (0, unit_size * 3, 0),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1.5
            height = unit_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)
    
    # Утоплялки под монтажные винты (3 mm)
    points = [
        (unit_size * -5.5, 0, unit_height / 2 - 1.5),
        (0, unit_size * -3, unit_height / 2 - 1.5),
        (0, unit_size * 3, unit_height / 2 - 1.5),
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
