
from build123d import *
from ocp_vscode import show

lego_pip_count_y = 9
lego_pip_count_x = 18

lego_pip_height     = 1.8
lego_pip_diameter   = 4.8
lego_unit_size      = 8.0
lego_brick_height   = 9.6
lego_wall_thickness = 1.2
lego_support_outer_diameter = 6.5
lego_support_inner_diameter = 4.8
lego_plate_height       = 3.2
lego_plate_inner_height = lego_plate_height - lego_wall_thickness

wall_thickness = 1.8
wall_height    = 16

lego_part_length = lego_unit_size * lego_pip_count_x
lego_part_width  = lego_unit_size * lego_pip_count_y


with BuildPart() as lego:
    # Создаем основную форму
    length = lego_part_length
    width  = lego_part_width
    height = wall_thickness
    Box(length, width, height)
    
    # Прорези для крепежа верхних элементов
    z_pos = 0
    for i in range(15):
        x_pos = -lego_part_length / 2 + 2 + i * 10
        y_pos = -lego_part_width / 2 + wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = wall_thickness
            height = wall_thickness
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    for i in range(15):
        x_pos = -lego_part_length / 2 + 2 + i * 10
        y_pos = lego_part_width / 2 - wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = wall_thickness
            height = wall_thickness
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    for i in range(8):
        x_pos = -lego_part_length / 2 + wall_thickness / 2
        y_pos = -lego_part_width / 2 + 1 + i * 10
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = wall_thickness
            width  = 5
            height = wall_thickness
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    for i in range(8):
        x_pos = lego_part_length / 2 - wall_thickness / 2
        y_pos = -lego_part_width / 2 + 1 + i * 10
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = wall_thickness
            width  = 5
            height = wall_thickness
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    z_pos = wall_thickness / 2 + lego_pip_height / 2
    # Pips
    for i in range(lego_pip_count_x - 1):
        for j in range(lego_pip_count_y - 1):
            x_pos = -lego_part_length / 2 + (i + 1) * lego_unit_size
            y_pos = -lego_part_width  / 2 + (j + 1) * lego_unit_size
            
            with BuildPart(Location((x_pos, y_pos, z_pos))):
                radius = lego_pip_diameter / 2
                height = lego_pip_height
                align  = (Align.CENTER, Align.CENTER, Align.CENTER)
                Cylinder(radius, height, align=align)
            


show(lego.part, names=["Lego Powerbank Cap"])
export_stl(lego.part, "powerbank_cap.stl")
