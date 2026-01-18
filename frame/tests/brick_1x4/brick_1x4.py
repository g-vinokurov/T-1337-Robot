
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
lego_wall_height  = lego_brick_height - lego_wall_thickness

with BuildPart() as lego:
    # Создаем основную форму
    length = lego_block_length
    width  = lego_brick_size
    height = lego_wall_height
    Box(length, width, height)
    
    # Вырезаем внутреннюю часть (делаем полым)
    with BuildPart(mode=Mode.SUBTRACT):
        length = lego_block_length - 2 * lego_wall_thickness
        width  = lego_brick_size - 2 * lego_wall_thickness
        height = lego_wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height, align=align)
    
    # Закрепляющие цилиндры
    for i in range(lego_pip_count - 1):
        # Вычисляем позицию по X
        x_pos = -lego_block_length / 2 + (i + 1) * lego_brick_size
        
        # Создаем цилиндр
        with BuildPart(Location((x_pos, 0, 0))):
            radius = 1.6
            height = lego_wall_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Cylinder(radius, height, align=align)
    
    # Верхняя часть (крышка)
    # Ищем максимальную Z-координату (верхние вершины блока)
    with BuildPart(Location((0, 0, lego.vertices().sort_by(Axis.Z)[-1].Z))):
        length = lego_block_length
        width  = lego_brick_size
        height = lego_wall_thickness
        align  = (Align.CENTER, Align.CENTER, Align.MIN)
        Box(length, width, height)
    
    # Create a workplane on the top of the block
    with BuildPart(lego.faces().sort_by(Axis.Z)[-1]):
        # Create a grid of pips
        with GridLocations(lego_brick_size, lego_brick_size, lego_pip_count, 1):
            Cylinder(
                radius=lego_pip_diameter / 2,
                height=lego_pip_height,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
            )


show(lego.part, names=["LEGO 1x4 Brick"])
export_stl(lego.part, "brick_1x4.stl")
