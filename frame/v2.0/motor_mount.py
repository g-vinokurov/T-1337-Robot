
from build123d import *
from ocp_vscode import show

unit_size           = 8.0 # lego unit size
unit_height         = 9.6 # lego brick height
hole_inner_diameter = 4.8 # lego hole inner diameter
hole_outer_diameter = 6.2 # lego hole outer diameter

with BuildPart() as part:
    # База
    length = unit_size * 8
    width  = unit_size * 4
    height = unit_height / 3
    Box(length, width, height)
    
    # Отверстия под крепежные винты
    points = [
        # Engines
        (unit_size * 0.5,  unit_size * 1.5,  0),
        (unit_size * 0.5,  unit_size * -1.5, 0),
        (unit_size * 2.5,  unit_size * 1.5,  0),
        (unit_size * 2.5,  unit_size * -1.5, 0),
        (unit_size * 1.5,  unit_size * 1,    0),
        (unit_size * 1.5,  unit_size * -1,   0),
        (unit_size * -0.5, unit_size * 1.5,  0),
        (unit_size * -0.5, unit_size * -1.5, 0),
        (unit_size * -2.5, unit_size * 1.5,  0),
        (unit_size * -2.5, unit_size * -1.5, 0),
        (unit_size * -1.5, unit_size * 1,    0),
        (unit_size * -1.5, unit_size * -1,   0),
    ]
    for point in points:
        with BuildPart(Location(point), mode=Mode.SUBTRACT):
            radius = 1.5
            height = unit_height / 3
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)

    roundable_edges = part.edges().filter_by(Axis.Z)
    fillet(roundable_edges, radius=2)

filename = f'{__file__.rstrip('.py')}'

show(part.part, names=[filename])
export_stl(part.part, f'{filename}.stl')
