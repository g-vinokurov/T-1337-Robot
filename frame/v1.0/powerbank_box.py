
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

wall_thickness = 1.2
wall_height    = 22.4

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

    # Делаем стенку на крышке
    # Толщина 1.2 мм
    x_pos = -lego_part_length / 2 + wall_thickness / 2
    y_pos = 0
    z_pos = z_pos + lego_wall_thickness / 2 + wall_height / 2
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = wall_thickness
        width  = lego_part_width
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = lego_part_width / 2 - wall_thickness / 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = lego_part_length
        width  = wall_thickness
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = -lego_part_width / 2 + wall_thickness / 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = lego_part_length
        width  = wall_thickness
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Стенка возле разьёмов
    x_pos = lego_part_length / 2 - wall_thickness / 2
    y_pos = -lego_part_width / 2 + wall_thickness + 15
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = wall_thickness
        width  = 2
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = x_pos
    y_pos = -lego_part_width / 2 + wall_thickness + 32
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = wall_thickness
        width  = 2
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = x_pos
    y_pos = -lego_part_width / 2 + wall_thickness + 47
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = wall_thickness
        width  = 2
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = x_pos
    y_pos = -lego_part_width / 2 + wall_thickness + 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = wall_thickness
        width  = 4
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = x_pos
    y_pos = lego_part_width / 2 - wall_thickness - 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = wall_thickness
        width  = 4
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = x_pos
    y_pos = 0
    z_pos = z_pos + wall_height / 2 - 4.8
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = wall_thickness
        width  = lego_part_width
        height = 9.6
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = x_pos
    y_pos = 0
    z_pos = z_pos + 4.8 - wall_height + 1
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = wall_thickness
        width  = lego_part_width
        height = 2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Прорези для крепежа верхних элементов
    z_pos = z_pos - 1 + wall_height - wall_thickness / 2
    for i in range(14):
        x_pos = -lego_part_length / 2 + (2 + 5) + i * 10
        y_pos = -lego_part_width / 2 + wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = wall_thickness
            height = wall_thickness
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    for i in range(14):
        x_pos = -lego_part_length / 2 + (2 + 5) + i * 10
        y_pos = lego_part_width / 2 - wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = wall_thickness
            height = wall_thickness
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    for i in range(7):
        x_pos = -lego_part_length / 2 + wall_thickness / 2
        y_pos = -lego_part_width / 2 + 6 + i * 10
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = wall_thickness
            width  = 5
            height = wall_thickness
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    for i in range(7):
        x_pos = lego_part_length / 2 - wall_thickness / 2
        y_pos = -lego_part_width / 2 + 6 + i * 10
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = wall_thickness
            width  = 5
            height = wall_thickness
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    z_pos = z_pos + wall_thickness / 2 - wall_height / 2
    for i in range(14):
        x_pos = -lego_part_length / 2 + 2 + 5 + i * 10
        y_pos = -lego_part_width / 2 + wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = wall_thickness
            height = 12
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    for i in range(14):
        x_pos = -lego_part_length / 2 + 2 + 5 + i * 10
        y_pos = lego_part_width / 2 - wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = wall_thickness
            height = 12
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    for i in range(14):
        x_pos = -lego_part_length / 2 + wall_thickness / 2
        y_pos = -lego_part_width / 2 + 1 + 5 + i * 10
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = wall_thickness
            width  = 5
            height = 12
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)

show(lego.part, names=["Lego Powerbank Box"])
export_stl(lego.part, "powerbank_box.stl")
