
from build123d import *
from ocp_vscode import show

lego_pip_count_y = 8
lego_pip_count_x = 12

lego_pip_height     = 1.8
lego_pip_diameter   = 4.8
lego_unit_size      = 8.0
lego_brick_height   = 9.6
lego_wall_thickness = 1.2
lego_support_outer_diameter = 6.5
lego_support_inner_diameter = 4.8
lego_plate_height       = 3.2
lego_plate_inner_height = lego_plate_height - lego_wall_thickness

x_wall_thickness = 4
y_wall_thickness = 2.4
slot_height = 1.8

lego_part_length = lego_unit_size * lego_pip_count_x
lego_part_width  = lego_unit_size * lego_pip_count_y


with BuildPart() as lego:
    # Создаем основную форму
    length = lego_part_length
    width  = lego_part_width
    height = slot_height
    Box(length, width, height)

    # Прорези для крепежа верхних элементов
    x_pos = -lego_part_length / 2 + 2.75
    y_pos = lego_part_width / 2 - x_wall_thickness / 2
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = 5.5
        width  = x_wall_thickness
        height = slot_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    for i in range(8):
        x_pos = -lego_part_length / 2 + (5.5 + 2.5 + 5) + i * 10
        y_pos = lego_part_width / 2 - x_wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = x_wall_thickness
            height = slot_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    x_pos = lego_part_length / 2 - 2.75
    y_pos = lego_part_width / 2 - x_wall_thickness / 2
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = 5.5
        width  = x_wall_thickness
        height = slot_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = -lego_part_length / 2 + 2.75
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = 5.5
        width  = x_wall_thickness
        height = slot_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    z_pos = z_pos
    for i in range(8):
        x_pos = -lego_part_length / 2 + (5.5 + 2.5 + 5) + i * 10
        y_pos = -lego_part_width / 2 + x_wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = x_wall_thickness
            height = slot_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    x_pos = lego_part_length / 2 - 2.75
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = 5.5
        width  = x_wall_thickness
        height = slot_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = -lego_part_length / 2 + y_wall_thickness / 2
    y_pos = -lego_part_width / 2 + 2.25
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = y_wall_thickness
        width  = 4.5
        height = slot_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    z_pos = z_pos
    for i in range(6):
        x_pos = -lego_part_length / 2 + y_wall_thickness / 2
        y_pos = -lego_part_width / 2 + (4.5 + 2.5) + i * 10
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = y_wall_thickness
            width  = 5
            height = slot_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
   
    x_pos = -lego_part_length / 2 + y_wall_thickness / 2
    y_pos = lego_part_width / 2 - 2.25
    z_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = y_wall_thickness
        width  = 4.5
        height = slot_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    z_pos = slot_height / 2 + lego_pip_height / 2
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


show(lego.part, names=["Lego Raspberry Pi 4 Cap"])
export_stl(lego.part, "raspberry_pi_4_cap.stl")
