
from build123d import *
from ocp_vscode import show

unit_size           = 8.0 # lego unit size
unit_height         = 9.6 # lego brick height
hole_inner_diameter = 4.8 # lego hole inner diameter
hole_outer_diameter = 6.2 # lego hole outer diameter

with BuildPart() as part:
    # База
    length = unit_size * 18
    width  = unit_size * 2
    height = unit_height
    Box(length, width, height)
    
    # Отверстия под крепежные винты
    points = [
        (unit_size * -2.5, unit_size / 2,  0),
        (unit_size * -2.5, -unit_size / 2, 0),
        (unit_size * 2.5,  unit_size / 2,  0),
        (unit_size * 2.5,  -unit_size / 2, 0),
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
        (unit_size * -2.5, unit_size / 2, z_pos),
        (unit_size * -2.5, -unit_size / 2, z_pos),
        (unit_size * 2.5,  unit_size / 2,  z_pos),
        (unit_size * 2.5,  -unit_size / 2, z_pos),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 3
            height = 3
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)


    roundable_edges = part.edges().filter_by(Axis.Z)
    fillet(roundable_edges, radius=2)

filename = f'{__file__[:-3]}'

show(part.part, names=[filename])
export_stl(part.part, f'{filename}.stl')
