
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
wall_height      = 22.4
vent_hole_height = 16
vent_hole_width  = 4

slot_height = 1.8

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

    # Делаем стенку на крышке (возле SD карты)
    # Толщина 2.4 мм
    x_pos = -lego_part_length / 2 + y_wall_thickness / 2
    y_pos = 0
    z_pos = z_pos + lego_wall_thickness / 2 + wall_height / 2
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = y_wall_thickness
        width  = lego_part_width
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Делаем стенку на крышке (возле пинов)
    # Толщина 4 мм
    x_pos = 0
    y_pos = lego_part_width / 2 - x_wall_thickness / 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = lego_part_length
        width  = x_wall_thickness
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Стенка возле USB и Ethernet разьёмов
    x_pos = lego_part_length / 2 - y_wall_thickness / 2
    y_pos = 0
    z_pos = z_pos - wall_height / 2 + 1.5
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = y_wall_thickness
        width  = lego_part_width
        height = 3
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    # Стенка возле HDMI разьёмов
    x_pos = 0
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = z_pos - 1.5 + 0.6
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = lego_part_length
        width  = x_wall_thickness
        height = 1.2
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = -lego_part_length / 2 + y_wall_thickness + 4
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = z_pos - 0.6 + wall_height / 2
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = 8
        width  = x_wall_thickness
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    x_pos = -lego_part_length / 2 + y_wall_thickness + 19 + 3
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = 6
        width  = x_wall_thickness
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)

    x_pos = -lego_part_length / 2 + y_wall_thickness + 33 + 3
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = 6
        width  = x_wall_thickness
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = -lego_part_length / 2 + y_wall_thickness + 47 + 3
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = 6
        width  = x_wall_thickness
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = -lego_part_length / 2 + y_wall_thickness + 62 + 15 + 0.8
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = 30 + 1.6
        width  = x_wall_thickness
        height = wall_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    x_pos = 0
    y_pos = -lego_part_width / 2 + x_wall_thickness / 2
    z_pos = z_pos + wall_height / 2 - 3.2
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        length = lego_part_length
        width  = x_wall_thickness
        height = 6.4
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    z_pos = z_pos + 3.2 - wall_height / 2
    
    # Вентиляция
    z_pos = z_pos - wall_height / 2 + vent_hole_height / 2
    for i in range(8):
        x_pos = -lego_part_length / 2 + y_wall_thickness / 2
        y_pos = -lego_part_width / 2 + x_wall_thickness + 2 + i * 7
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = y_wall_thickness
            width  = vent_hole_width
            height = vent_hole_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    x_pos = -lego_part_length / 2 + y_wall_thickness / 2
    y_pos = 0
    with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
        length = y_wall_thickness
        width  = 14
        height = vent_hole_height
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Box(length, width, height)
    
    for i in range(13):
        x_pos = -lego_part_length / 2 + y_wall_thickness + 2 + i * 7
        y_pos = lego_part_width / 2 - x_wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = vent_hole_width
            width  = x_wall_thickness
            height = vent_hole_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    # Штырики
    x_pos = -lego_part_length / 2 + y_wall_thickness + 6
    y_pos = -lego_part_width / 2 + x_wall_thickness + 3.5
    z_pos = z_pos - vent_hole_height / 2 + 3
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        radius = 0.9
        height = 6
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align)
    
    # Штырики
    x_pos = -lego_part_length / 2 + y_wall_thickness + 6
    y_pos = lego_part_width / 2 +- x_wall_thickness - 3.5
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        radius = 0.9
        height = 6
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align)

    # Штырики
    x_pos = -lego_part_length / 2 + y_wall_thickness + 64
    y_pos = -lego_part_width / 2 + x_wall_thickness + 3.5
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        radius = 0.9
        height = 6
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align)
    
    # Штырики
    x_pos = -lego_part_length / 2 + y_wall_thickness + 64
    y_pos = lego_part_width / 2 - x_wall_thickness - 3.5
    z_pos = z_pos
    with BuildPart(Location((x_pos, y_pos, z_pos))):
        radius = 0.9
        height = 6
        align  = (Align.CENTER, Align.CENTER, Align.CENTER)
        Cylinder(radius, height, align=align)
    
    # Прорези для крепежа верхних элементов
    z_pos = z_pos - 3 + wall_height - slot_height / 2
    for i in range(9):
        x_pos = -lego_part_length / 2 + (5.5 + 2.5) + i * 10
        y_pos = lego_part_width / 2 - x_wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = x_wall_thickness
            height = slot_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    z_pos = z_pos
    for i in range(9):
        x_pos = -lego_part_length / 2 + (5.5 + 2.5) + i * 10
        y_pos = -lego_part_width / 2 + x_wall_thickness / 2
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = 5
            width  = x_wall_thickness
            height = slot_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)
    
    z_pos = z_pos
    for i in range(5):
        x_pos = -lego_part_length / 2 + y_wall_thickness / 2
        y_pos = -lego_part_width / 2 + (9.5 + 2.5) + i * 10
        with BuildPart(Location((x_pos, y_pos, z_pos)), mode=Mode.SUBTRACT):
            length = y_wall_thickness
            width  = 5
            height = slot_height
            align  = (Align.CENTER, Align.CENTER, Align.CENTER)
            Box(length, width, height)


show(lego.part, names=["Lego Raspberry Pi 4 Box"])
export_stl(lego.part, "raspberry_pi_4_box.stl")
