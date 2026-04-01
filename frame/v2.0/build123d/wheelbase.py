
from build123d import *
from ocp_vscode import show

unit_size           = 8.0 # lego unit size
unit_height         = 9.6 # lego brick height
hole_inner_diameter = 4.8 # lego hole inner diameter
hole_outer_diameter = 6.2 # lego hole outer diameter

with BuildPart() as part:
    # База
    length = unit_size * 22
    width  = unit_size * 16
    height = unit_height
    Box(length, width, height)
    
    # Вырезы
    x_pos = unit_size * -11 + unit_size * 1.5
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 3
        width  = unit_size * 14
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 11 - unit_size * 1.5
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 3
        width  = unit_size * 14
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -3.5
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 5
        width  = unit_size * 14
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 3.5
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 5
        width  = unit_size * 14
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Отверстия под колёса (1-я сторона)
    z_pos = 0.8
    for i in range(1, 22):
        if i in (3, 4, 5, 10, 11, 12, 17, 18, 19):
            continue
        x_pos = unit_size * -11 + unit_size * i

        y_pos = unit_size * 8 - 0.4
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = hole_outer_diameter / 2
            height = 0.8
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
        y_pos = unit_size * 7 + 0.4
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = hole_outer_diameter / 2
            height = 0.8
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
        y_pos = unit_size * 7.5
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = hole_inner_diameter / 2 + 0.2
            height = unit_size
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
    
    # Отверстия под колёса (2-я сторона)
    z_pos = 0.8
    for i in range(1, 22):
        if i in (3, 4, 5, 10, 11, 12, 17, 18, 19):
            continue
        x_pos = unit_size * -11 + unit_size * i

        y_pos = unit_size * -8 + 0.4
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = hole_outer_diameter / 2
            height = 0.8
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
        y_pos = unit_size * -7 - 0.4
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = hole_outer_diameter / 2
            height = 0.8
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
        y_pos = unit_size * -7.5
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            radius = hole_inner_diameter / 2 + 0.2
            height = unit_size
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align, rotation=(90, 0, 0))
    
    # Опоры
    x_pos = 0
    y_pos = unit_size * 3.5
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 20
        width  = unit_size * 1
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = unit_size * -3.5
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 20
        width  = unit_size * 1
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Держатели аккумулятора
    x_pos = unit_size * -9.5
    y_pos = 0
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size
        width  = unit_size * 2
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 9.5
    y_pos = 0
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size
        width  = unit_size * 2
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -9.5
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size
        width  = unit_size * 6
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 9.5
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size
        width  = unit_size * 6
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 7
    y_pos = unit_size * 3.5
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 7
    y_pos = unit_size * -3.5
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -7
    y_pos = unit_size * 3.5
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -7
    y_pos = unit_size * -3.5
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = unit_size * 3.5
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = unit_size * -3.5
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    # Отсек для АКБ
    x_pos = 0
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 18
        width  = unit_size * 6
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Отверстия под крепежные винты
    points = [
        (unit_size * 0,    unit_size * 3.5,  unit_height),
        (unit_size * 0,    unit_size * -3.5, unit_height),
        (unit_size * 7,    unit_size * 3.5,  unit_height),
        (unit_size * 7,    unit_size * -3.5, unit_height),
        (unit_size * -7,   unit_size * 3.5,  unit_height),
        (unit_size * -7,   unit_size * -3.5, unit_height),
        (unit_size * -9.5,               0,  unit_height),
        (unit_size * 9.5,                0,  unit_height),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1.5
            height = unit_height * 3
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)

    roundable_edges = part.edges().filter_by(Axis.Z)
    fillet(roundable_edges, radius=2)

filename = f'{__file__.rstrip('.py')}'

show(part.part, names=[filename])
export_stl(part.part, f'{filename}.stl')
