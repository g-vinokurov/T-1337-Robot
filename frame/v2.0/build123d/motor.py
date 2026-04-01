
from build123d import *
from ocp_vscode import show

unit_size           = 8.0 # lego unit size
unit_height         = 9.6 # lego brick height
hole_inner_diameter = 4.8 # lego hole inner diameter
hole_outer_diameter = 6.2 # lego hole outer diameter

with BuildPart() as part:
    # База
    length = unit_size * 16
    width  = unit_size * 12
    height = unit_height
    Box(length, width, height)

    # Вырезы
    x_pos = 0
    y_pos = unit_size * 4
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 6
        width  = unit_size * 4
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = unit_size * -4
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 4
        width  = unit_size * 4
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -6.5
    y_pos = unit_size * 5
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 3
        width  = unit_size * 2
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 6.5
    y_pos = unit_size * 5
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 3
        width  = unit_size * 2
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -6.5
    y_pos = unit_size * -4
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 3
        width  = unit_size * 4
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 6.5
    y_pos = unit_size * -4
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 3
        width  = unit_size * 4
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -7
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 2
        width  = unit_size * 4
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 7
    y_pos = 0
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = unit_size * 2
        width  = unit_size * 4
        height = unit_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    # Стенки
    x_pos = unit_size * -5.5
    y_pos = unit_size * 0
    z_pos = unit_height * (1/2 + (2+1/3) / 2)
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size
        width  = unit_size * 2
        height = unit_height * (2+1/3)
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 5.5
    y_pos = unit_size * 0
    z_pos = unit_height * (1/2 + (2+1/3) / 2)
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size
        width  = unit_size * 2
        height = unit_height * (2+1/3)
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 7.5
    y_pos = unit_size * 3
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size
        width  = unit_size * 2
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -7.5
    y_pos = unit_size * 3
    z_pos = unit_height * 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size
        width  = unit_size * 2
        height = unit_height * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * -3.5
    y_pos = unit_size * -5
    z_pos = unit_height * (1/2 + (2+1/3) / 2)
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 3
        width  = unit_size * 2
        height = unit_height * (2+1/3)
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 3.5
    y_pos = unit_size * -5
    z_pos = unit_height * (1/2 + (2+1/3) / 2)
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 3
        width  = unit_size * 2
        height = unit_height * (2+1/3)
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    x_pos = unit_size * -4
    y_pos = unit_size * 5.5
    z_pos = unit_height * (1/2 + (2+1/3) / 2)
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size * 1
        height = unit_height * (2+1/3)
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = unit_size * 4
    y_pos = unit_size * 5.5
    z_pos = unit_height * (1/2 + (2+1/3) / 2)
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = unit_size * 2
        width  = unit_size * 1
        height = unit_height * (2+1/3)
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    # Отверстия под валы моторов
    x_pos = unit_size * -8 + 0.4
    y_pos = unit_size * 3
    z_pos = unit_height / 2 + 12
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(0, 90, 0))
        
    x_pos = unit_size * -7 - 0.4
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(0, 90, 0))
        
    x_pos = unit_size * -7.5
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_inner_diameter / 2 + 0.2
        height = unit_size
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(0, 90, 0))
    
    x_pos = unit_size * 8 - 0.4
    y_pos = unit_size * 3
    z_pos = unit_height / 2 + 12
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(0, 90, 0))
        
    x_pos = unit_size * 7 + 0.4
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(0, 90, 0))
        
    x_pos = unit_size * 7.5
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_inner_diameter / 2 + 0.2
        height = unit_size
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(0, 90, 0))

    # Отверстия под провода к моторам
    # left
    x_pos = unit_size * -2.5
    y_pos = unit_size * -4 - 0.4
    z_pos = unit_height
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
    y_pos = unit_size * -6 + 0.4
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
    y_pos = unit_size * -5
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_inner_diameter / 2 + 0.2
        height = unit_size * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
    
    x_pos = unit_size * -2.5
    y_pos = unit_size * -4 - 0.4
    z_pos = unit_height * 2
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
    y_pos = unit_size * -6 + 0.4
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
    y_pos = unit_size * -5
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_inner_diameter / 2 + 0.2
        height = unit_size * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
    
    # right
    x_pos = unit_size * 2.5
    y_pos = unit_size * -4 - 0.4
    z_pos = unit_height
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
    y_pos = unit_size * -6 + 0.4
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
    y_pos = unit_size * -5
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_inner_diameter / 2 + 0.2
        height = unit_size * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
    
    x_pos = unit_size * 2.5
    y_pos = unit_size * -4 - 0.4
    z_pos = unit_height * 2
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
    y_pos = unit_size * -6 + 0.4
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_outer_diameter / 2
        height = 0.8
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
        
    y_pos = unit_size * -5
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        radius = hole_inner_diameter / 2 + 0.2
        height = unit_size * 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align, rotation=(90, 0, 0))
    
    # Отверстия под крепежные винты
    z_pos = unit_height * (1/2 + (2+1/3) - 1)
    points = [
        # Stamina
        (unit_size * 1, unit_size * 1,  0),
        (unit_size * 1, unit_size * -1, 0),
        (unit_size * -1,unit_size * 1,  0),
        (unit_size * -1,unit_size * -1, 0),
        # Top
        (unit_size * -5.5, 0, z_pos),
        (unit_size * 5.5, 0, z_pos),
        (unit_size * -4, unit_size * -5, z_pos),
        (unit_size * 4, unit_size * -5, z_pos),
        (unit_size * -4, unit_size * 5.5, z_pos),
        (unit_size * 4, unit_size * 5.5, z_pos),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1.5
            height = unit_height * 2
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)

    roundable_edges = part.edges().filter_by(Axis.Z)
    fillet(roundable_edges, radius=1.5)

filename = f'{__file__.rstrip('.py')}'

show(part.part, names=[filename])
export_stl(part.part, f'{filename}.stl')
