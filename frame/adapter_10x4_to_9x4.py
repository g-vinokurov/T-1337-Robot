
from build123d import *
from ocp_vscode import show

lego_pip_count_y = 4
lego_pip_count_x = 10

lego_pip_height     = 1.8
lego_pip_diameter   = 4.8
lego_unit_size      = 8.0
lego_brick_height   = 9.6
lego_wall_thickness = 1.2
lego_support_outer_diameter = 6.5
lego_support_inner_diameter = 4.8
lego_plate_height       = 3.2
lego_plate_inner_height = lego_plate_height - lego_wall_thickness

lego_part_length = lego_unit_size * lego_pip_count_x
lego_part_width  = lego_unit_size * lego_pip_count_y


with BuildPart() as lego:
    # Создаем основную форму
    length = lego_part_length
    width  = lego_part_width
    height = lego_plate_inner_height
    Box(length, width, height)
    
    # Вырезаем внутреннюю часть
    with BuildPart(mode=Mode.SUBTRACT):
        length = lego_part_length - 2 * lego_wall_thickness
        width  = lego_part_width - 2 * lego_wall_thickness
        height = lego_plate_inner_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height, align=align)
    
    # Закрепляющие цилиндры
    for i in range(lego_pip_count_x - 1):
        for j in range(lego_pip_count_y - 1):
            x_pos = -lego_part_length / 2 + (i + 1) * lego_unit_size
            y_pos = -lego_part_width  / 2 + (j + 1) * lego_unit_size
            
            with BuildPart(Location((x_pos, y_pos, 0))):
                radius = lego_support_outer_diameter / 2
                height = lego_plate_inner_height
                align  = (Align.CENTER, Align.CENTER, Align.CENTER)
                Cylinder(radius, height, align=align)
            
            # Цилиндр полый у нас
            with BuildPart(Location((x_pos, y_pos, 0)), mode=Mode.SUBTRACT):
                radius = lego_support_inner_diameter / 2
                height = lego_plate_inner_height
                align  = (Align.CENTER, Align.CENTER, Align.CENTER)
                Cylinder(radius, height, align=align)
    
    # Крышка
    x_pos = 0
    y_pos = 0
    z_pos = lego_plate_inner_height / 2 + lego_wall_thickness / 2
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = lego_part_length
        width  = lego_part_width
        height = lego_wall_thickness
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    z_pos = z_pos + lego_wall_thickness / 2 + lego_pip_height / 2
    # Pips
    for i in range(lego_pip_count_x - 1):
        for j in range(lego_pip_count_y):
            x_pos = -lego_part_length / 2 + (i + 1) * lego_unit_size
            y_pos = -lego_part_width  / 2 + lego_unit_size / 2 + j * lego_unit_size
            
            with BuildPart(Location((x_pos, y_pos, z_pos))):
                radius = lego_pip_diameter / 2
                height = lego_pip_height
                align  = (Align.CENTER, Align.CENTER, Align.CENTER)
                Cylinder(radius, height, align=align)


show(lego.part, names=["Lego Adapter 10x4 to 9x4"])
export_stl(lego.part, "adapter_10x4_to_9x4.stl")
