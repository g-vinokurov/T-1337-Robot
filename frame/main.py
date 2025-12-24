
from build123d import *
from ocp_vscode import show

lego_pip_count = 4

lego_pip_height     = 1.8
lego_pip_diameter   = 4.8
lego_brick_size     = 8.0
lego_brick_height   = 9.6
lego_hole_diameter  = 4.8
lego_wall_thickness = 1.2

lego_block_height = lego_brick_height + lego_pip_height
lego_block_length = lego_brick_size * lego_pip_count
lego_block_width  = lego_brick_size

with BuildPart() as lego:
    # Draw the bottom of the block
    with BuildSketch() as plan:
        # Start with a Rectangle the size of the block
        perimeter = Rectangle(width=lego_block_length, height=lego_block_width)

        # Subtract an offset to create the block walls
        offset(perimeter, -lego_wall_thickness, kind=Kind.INTERSECTION, mode=Mode.SUBTRACT)
     # Extrude this base sketch to the height of the walls
    extrude(amount=lego_brick_height - lego_wall_thickness)
    # Create a box on the top of the walls
    with Locations((0, 0, lego.vertices().sort_by(Axis.Z)[-1].Z)):
        # Create the top of the block
        Box(
            length=lego_block_length,
            width=lego_block_width,
            height=lego_wall_thickness,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
    # Create a workplane on the top of the block
    with BuildPart(lego.faces().sort_by(Axis.Z)[-1]):
        # Create a grid of pips
        with GridLocations(lego_brick_size, lego_brick_size, lego_pip_count, 1):
            Cylinder(
                radius=lego_pip_diameter / 2,
                height=lego_pip_height,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
            )

show(lego.part, names=["LEGO Technic 1x16 Brick"])
