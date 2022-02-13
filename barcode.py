
from PIL import Image, ImageDraw
import math

img = Image.new("1", (128 * 10, 64*10), color=1)

d = ImageDraw.Draw(img)


def __orientation(x0, y0, x1, y1, x2, y2):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.

    val = (y1 - y0) * (x2 - x1) - (x1 - x0) * (y2 - y1)

    if val > 0:

        # Clockwise orientation
        return 1
    elif val < 0:
        # Counterclockwise orientation
        return 2
    else:
        # Collinear orientation
        return 0


# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def __do_intersect(x0, y0, x1, y1, x2, y2, x3, y3):
    # Find the 4 orientations required for
    # the general and special cases
    o0 = __orientation(x0, y0, x1, y1, x2, y2)
    o1 = __orientation(x0, y0, x1, y1, x3, y3)
    o2 = __orientation(x2, y2, x3, y3, x0, y0)
    o3 = __orientation(x2, y2, x3, y3, x1, y1)

    # General case
    if (o0 != o1) and (o2 != o3):
        return True

    return False


def write_glcd_pixel(x, y, color):

    if x == 0 and y == 0:
        print("oi")

    if not 63 >= y >= 0 or not 127 >= x >= 0:
        return
    y = 63 - y
    color = not color
    for i in range(10):
        for j in range(10):
            img.putpixel((x * 10 + i, y * 10 + j), color)


def draw_line(xa, ya, xb, yb):

    distancia_vertical = yb - ya
    distancia_horizontal = xb - xa

    if not distancia_horizontal and not distancia_vertical:
        # Origem e destino são o mesmo ponto
        # Desenha somente um ponto
        write_glcd_pixel(xa, ya, 1)
        return

    maior_distancia_abs = max(abs(distancia_vertical), abs(distancia_horizontal))

    incremento_x = distancia_horizontal / maior_distancia_abs
    incremento_y = distancia_vertical / maior_distancia_abs

    x = xa
    y = ya
    for i in range(maior_distancia_abs + 1):
        write_glcd_pixel(round(x), round(y), 1)
        x += incremento_x
        y += incremento_y


def draw_circle(xc, yc, r, fill):

    for dx in range(-r, r + 1):
        dy = round(math.sqrt(r**2 - dx**2))

        if fill:
            for ddy in range(dy):
                write_glcd_pixel(xc + dx, yc + ddy, 1)
                write_glcd_pixel(xc - dx, yc - ddy, 1)
        else:
            write_glcd_pixel(xc + dx, yc + dy, 1)
            write_glcd_pixel(xc - dx, yc - dy, 1)

    for dy in range(-r, r + 1):
        dx = round(math.sqrt(r ** 2 - dy ** 2))

        if fill:
            for ddx in range(dx):
                write_glcd_pixel(xc + ddx, yc + dy, 1)
                write_glcd_pixel(xc - ddx, yc - dy, 1)
        else:
            write_glcd_pixel(xc + dx, yc + dy, 1)
            write_glcd_pixel(xc - dx, yc - dy, 1)


def draw_math_function(func, x_origin_offset, y_origin_offset, arg_min, arg_max, x_scale, y_scale):

    if arg_max < arg_min:
        return

    x_min = round(arg_min/x_scale)
    x_max = round(arg_max/x_scale)

    previous_x = x_min
    previous_y = round(func(arg_min)/y_scale)

    for x in range(x_min, x_max + 1):
        y = round(func(x * x_scale)/y_scale)
        draw_line(previous_x + x_origin_offset, previous_y + y_origin_offset, x + x_origin_offset, y + y_origin_offset)
        previous_x = x
        previous_y = y


def draw_triangle(x0, y0, x1, y1, x2, y2, fill):

    if not fill:
        draw_line(x0, y0, x1, y1)
        draw_line(x1, y1, x2, y2)
        draw_line(x2, y2, x0, y0)

    else:

        distancia_vertical = y1 - y0
        distancia_horizontal = x1 - x0

        if not distancia_horizontal and not distancia_vertical:
            # Origem e destino são o mesmo ponto
            # Desenha uma reta
            draw_line(x0, y0, x1, y1)
            draw_line(x1, y1, x2, y2)
            return

        maior_distancia_abs = max(abs(distancia_vertical), abs(distancia_horizontal))

        incremento_x = distancia_horizontal / maior_distancia_abs
        incremento_y = distancia_vertical / maior_distancia_abs

        x = x0
        y = y0
        for i in range(maior_distancia_abs + 1):
            draw_line(math.floor(x), math.floor(y), x2, y2)
            draw_line(math.ceil(x), math.ceil(y), x2, y2)
            x += incremento_x
            y += incremento_y


def draw_quadrilateral(x0, y0, x1, y1, x2, y2, x3, y3):

    points = [[x0, y0], [x1, y1], [x2, y2], [x3, y3]]

    for origin_point_index in range(len(points)):
        for destination_point_index in range(origin_point_index + 1, len(points)):

            for index in [0, 1, 2, 3]:
                if index != origin_point_index and index != destination_point_index:
                    other_origin_point_index = index
            for index in [3, 2, 1, 0]:
                if index != origin_point_index and index != destination_point_index:
                    other_destination_point_index = index

            # Checa se a reta ligando o ponto de origem ao ponto de destino é interceptada por qualquer outra
            if not __do_intersect(
                    *points[origin_point_index], *points[destination_point_index],
                    *points[other_origin_point_index], *points[other_destination_point_index]
            ):
                draw_line(*points[origin_point_index], *points[destination_point_index])



draw_quadrilateral(1, 1, 1, 30, 30, 1, 30, 30)

#draw_triangle(30, 30, 36, 30, 33, 40, 0)
#draw_math_function(lambda x: x, 1, 1, 0, 0, 1, 1)
#draw_math_function(math.sin, 0, 30, 0, 15 * math.pi, 0.2, 0.04)
#draw_math_function(lambda x: x**3/10000, 63, 32, -63, 64, 1, 1)

# draw_line(0, 30, 127, 30)
# draw_line(20, 0, 20, 63)

img.show()




