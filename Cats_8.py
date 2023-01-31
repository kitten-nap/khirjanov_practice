from math import pi

import pygame
from pygame.draw import *

pygame.init()

FPS = 30

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
gray = (153, 153, 153)
dark_brown = (85, 68, 0)
bright_brown = (128, 102, 0)
sky = (135, 205, 222)
window_color = (213, 255, 230)
orange = (200, 113, 55)
green = (136, 170, 0)
beige = (222, 170, 135)
bright_beige = (255, 204, 170)

screen_scale_x = 10
screen_scale_y = 10
x_max, y_max = 80 * screen_scale_x, 100 * screen_scale_y
screen = pygame.display.set_mode((x_max, y_max))

screen.fill(dark_brown)


def rect_angle(surface, color, rectangle, angle, width=0):
    """
    This function draws a tilted rectangle like rect() with angle from positive direction of X-axis
    counter-clockwise if angle > 0.
    :param surface:
    :param color:
    :param rectangle:
    :param angle:
    :param width:
    :return:
    """
    target_rect = pygame.Rect(rectangle)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


def ellipse_angle(surface, color, rectangle, angle, width=0):
    """
    This function draws a tilted ellipse like ellipse() with angle from positive direction of X-axis
    counter-clockwise if angle > 0.
    :param surface:
    :param color:
    :param rectangle:
    :param angle:
    :param width:
    :return:
    """
    target_rect = pygame.Rect(rectangle)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


# desk
rect(screen, bright_brown, [0, 47 * screen_scale_y, x_max, y_max - 47 * screen_scale_y])


def window(window_ref_point_x=450, window_ref_point_y=30, window_scale=10):
    """
    This function draws window. window_ref_point X and Y are where left top corner of the window is.
    :return:
    """
    # window
    window_length = 3.4 * window_scale * screen_scale_x
    window_height = 4.2 * window_scale * screen_scale_y

    rect(screen, window_color, [window_ref_point_x, window_ref_point_y, window_length, window_height])

    # sky
    left_1, top_1 = window_ref_point_x + 0.2 * window_scale * screen_scale_x,\
        window_ref_point_y + 0.15 * window_scale * screen_scale_y
    left_2, top_2 = window_ref_point_x + 1.8 * window_scale * screen_scale_x,\
        window_ref_point_y + 1.4 * window_scale * screen_scale_y
    sky_length = 1.4 * window_scale * screen_scale_x
    sky_height_min = 1 * window_scale * screen_scale_y
    sky_height_max = 2.6 * window_scale * screen_scale_y

    rect(screen, sky, [left_1, top_1, sky_length, sky_height_min])
    rect(screen, sky, [left_1, top_2, sky_length, sky_height_max])
    rect(screen, sky, [left_2, top_1, sky_length, sky_height_min])
    rect(screen, sky, [left_2, top_2, sky_length, sky_height_max])


window(53 * screen_scale_x, 7 * screen_scale_y, 7)
window(25 * screen_scale_x, 7 * screen_scale_y, 7)
window(-3 * screen_scale_x, 7 * screen_scale_y, 7)


def cat(cat_ref_point_x=x_max//2, cat_ref_point_y=y_max//2, cat_scale=10.0, cat_body_color=orange, cat_eye_color=green,
        body_orientation='left'):
    """
    This function draws a cat with defined scale, orientation, eye & body colors, x & y are coord. of centered top point
    of cat's body (the biggest ellipse). Orientation is a parameter which determines on which side of the cat
    it's head is: if body_orientation == 'left' then it's cat's left orientation, vise versa right orientation.
    Has 2 low level functions: body(), head().
    :param cat_ref_point_x:
    :param cat_ref_point_y:
    :param cat_scale:
    :param cat_body_color:
    :param cat_eye_color:
    :param body_orientation:
    :return:
    """
    # If n is even number, then left cat orientation
    # If n is odd number, then right cat orientation

    # n is a cat orientation parameter
    n = 0
    if body_orientation == 'right':
        n = 1
    elif body_orientation != 'left':
        print("ERROR: incorrect body_orientation has been given. 'left' or 'right' was expected")

    def body():
        """
        This function draws cat's body (without its head). Has 4 low level functions: tail(), right_forward_paw(),
        left_forward_paw(), left_back_paw().
        Has high level function: cat()
        :return:
        """
        def tail():
            """
            This function draws cat's tail depending on cat's orientation.
            Has high level function: body() -> cat()
            :return:
            """
            ellipse_angle(screen, cat_body_color,
                          [cat_ref_point_x + (-1)**n * 13 * cat_scale - n * 40 * cat_scale,
                           cat_ref_point_y + 12 * cat_scale,
                           40 * cat_scale, 12 * cat_scale], -(-1)**n * 30)
            ellipse_angle(screen, black,
                          [cat_ref_point_x + (-1)**n * 13 * cat_scale - n * 40 * cat_scale,
                           cat_ref_point_y + 12 * cat_scale,
                           40 * cat_scale, 12 * cat_scale], -(-1)**n * 30,
                          width=1)

        tail()

        # This is cat's body. Body has to be on an upper layer than cat's tail.
        ellipse(screen, cat_body_color,
                [cat_ref_point_x - 250 * cat_scale / 10, cat_ref_point_y + 0 * cat_scale / 10,
                 50 * cat_scale, 25 * cat_scale])
        ellipse(screen, black,
                [cat_ref_point_x - 250 * cat_scale / 10, cat_ref_point_y + 0 * cat_scale / 10,
                 50 * cat_scale, 25 * cat_scale],
                width=1)

        def right_forward_paw():
            """
            This function draws cat's right forward paw when the cat is left oriented and left forward paw when
            right oriented.
            Has high level function: body() -> cat()
            :return:
            """
            ellipse(screen, cat_body_color,
                    [cat_ref_point_x - (-1)**n * 30 * cat_scale - n * 7 * cat_scale, cat_ref_point_y + 8 * cat_scale,
                     7 * cat_scale, 13 * cat_scale])
            ellipse(screen, black,
                    [cat_ref_point_x - (-1)**n * 30 * cat_scale - n * 7 * cat_scale, cat_ref_point_y + 8 * cat_scale,
                     7 * cat_scale, 13 * cat_scale],
                    width=1)

        right_forward_paw()

        def left_forward_paw():
            """
            This function draws cat's left forward paw when the cat is left oriented and right forward paw when
            right oriented.
            Has high level function: body() -> cat()
            :return:
            """
            ellipse(screen, cat_body_color,
                    [cat_ref_point_x - (-1)**n * 24 * cat_scale - n * 13 * cat_scale,
                     cat_ref_point_y + 18.5 * cat_scale,
                     13 * cat_scale, 7 * cat_scale])
            ellipse(screen, black,
                    [cat_ref_point_x - (-1)**n * 24 * cat_scale - n * 13 * cat_scale,
                     cat_ref_point_y + 18.5 * cat_scale,
                     13 * cat_scale, 7 * cat_scale],
                    width=1)

        left_forward_paw()

        def left_back_paw():
            """
            This function draws cat's left back paw when the cat is left oriented and right back paw when
            right oriented.
            Has high level function: body() -> cat()
            :return:
            """
            circle(screen, cat_body_color,
                   [cat_ref_point_x + (-1)**n * 18 * cat_scale, cat_ref_point_y + 20 * cat_scale], 8 * cat_scale)
            circle(screen, black,
                   [cat_ref_point_x + (-1)**n * 18 * cat_scale, cat_ref_point_y + 20 * cat_scale],
                   8 * cat_scale,
                   width=1)

            ellipse(screen, cat_body_color,
                    [cat_ref_point_x + (-1)**n * 22 * cat_scale - n * 5 * cat_scale, cat_ref_point_y + 22 * cat_scale,
                     5 * cat_scale, 12 * cat_scale])
            ellipse(screen, black,
                    [cat_ref_point_x + (-1)**n * 22 * cat_scale - n * 5 * cat_scale,
                     cat_ref_point_y + 22 * cat_scale,
                     5 * cat_scale, 12 * cat_scale],
                    width=1)

        left_back_paw()
    body()

    def head():
        """
        This function draws cat's head. Has low level functions: left_eye(), right_eye(), nose(), mustache(),
        left_ear(), right_ear().
        Has high level function: cat()
        :return:
        """
        ellipse(screen, cat_body_color, [cat_ref_point_x - (-1)**n * 34 * cat_scale - n * 20 * cat_scale,
                                         cat_ref_point_y + 1 * cat_scale, 20 * cat_scale, 18 * cat_scale])

        ellipse(screen, black, [cat_ref_point_x - (-1)**n * 34 * cat_scale - n * 20 * cat_scale,
                                cat_ref_point_y + 1 * cat_scale, 20 * cat_scale, 18 * cat_scale], width=1)

        def left_eye():
            """
            This function draws cat's left eye when the cat is left oriented and right cat's eye when right oriented.
            Has high level function: head() -> cat()
            :return:
            """
            ellipse(screen, cat_eye_color, [cat_ref_point_x - (-1)**n * 31 * cat_scale - n * 5 * cat_scale,
                                            cat_ref_point_y + 7.5 * cat_scale, 5 * cat_scale, 6 * cat_scale])

            ellipse(screen, black, [cat_ref_point_x - (-1)**n * 31 * cat_scale - n * 5 * cat_scale,
                                    cat_ref_point_y + 7.5 * cat_scale, 5 * cat_scale, 6 * cat_scale],
                    width=1)

            ellipse(screen, black, [cat_ref_point_x - (-1)**n * 28.1 * cat_scale - n * 0.8 * cat_scale,
                                    cat_ref_point_y + 7.9 * cat_scale, 0.8 * cat_scale, 5.2 * cat_scale])

            ellipse_angle(screen, white, [cat_ref_point_x - (-1)**n * 30.5 * cat_scale - n * 3 * cat_scale,
                                          cat_ref_point_y + 8.8 * cat_scale, 3 * cat_scale, 1 * cat_scale],
                          angle=125-n*70)

        left_eye()

        def right_eye():
            """
            This function draws the cat's right eye when the cat is left oriented and left cat's eye when
            right oriented.
            Has high level function: head() -> cat().
            :return:
            """
            ellipse(screen, cat_eye_color, [cat_ref_point_x - (-1)**n * 22 * cat_scale - n * 5 * cat_scale,
                                            cat_ref_point_y + 7.5 * cat_scale,
                                            5 * cat_scale, 6 * cat_scale])

            ellipse(screen, black, [cat_ref_point_x - (-1)**n * 22 * cat_scale - n * 5 * cat_scale,
                                    cat_ref_point_y + 7.5 * cat_scale,
                                    5 * cat_scale, 6 * cat_scale],
                    width=1)

            ellipse(screen, black, [cat_ref_point_x - (-1)**n * 19 * cat_scale - n * 0.8 * cat_scale,
                                    cat_ref_point_y + 7.9 * cat_scale,
                                    0.8 * cat_scale, 5.2 * cat_scale])

            ellipse_angle(screen, white, [cat_ref_point_x - (-1)**n * 21.5 * cat_scale - n * 3 * cat_scale,
                                          cat_ref_point_y + 8.8 * cat_scale,
                                          3 * cat_scale, 1 * cat_scale],
                          angle=125-n*70)

        right_eye()

        def nose():
            """
            This function draws cat's nose. Has high level function: head() -> cat().
            :return:
            """
            polygon(screen, bright_beige, [(cat_ref_point_x - (-1)**n * 25 * cat_scale,
                                            cat_ref_point_y + 14 * cat_scale),

                                           (cat_ref_point_x - (-1)**n * 23 * cat_scale,
                                            cat_ref_point_y + 14 * cat_scale),

                                           (cat_ref_point_x - (-1)**n * 24 * cat_scale,
                                            cat_ref_point_y + 15 * cat_scale)])

            polygon(screen, black, [(cat_ref_point_x - (-1)**n * 25 * cat_scale,
                                     cat_ref_point_y + 14 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 23 * cat_scale,
                                     cat_ref_point_y + 14 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 24 * cat_scale,
                                     cat_ref_point_y + 15 * cat_scale)],
                    width=1)

            line(screen, black,
                 [cat_ref_point_x - (-1)**n * 24 * cat_scale,
                  cat_ref_point_y + 15 * cat_scale],
                 [cat_ref_point_x - (-1)**n * 24 * cat_scale,
                  cat_ref_point_y + 16.5 * cat_scale])
            arc(screen, black, [cat_ref_point_x - (-1)**n * 24 * cat_scale,
                                cat_ref_point_y + 15.5 * cat_scale,
                                2 * cat_scale, 2 * cat_scale],
                0.97 * pi, 1.75 * pi)
            arc(screen, black, [cat_ref_point_x - (-1)**n * 25.9 * cat_scale - n * 3.8 * cat_scale,
                                cat_ref_point_y + 15.5 * cat_scale,
                                2 * cat_scale, 2 * cat_scale],
                1.25 * pi, 0.05)

        nose()

        def mustaches():
            """
            This function draws cat's mustaches
            Has high level function: head() -> cat().
            :return:
            """
            arc(screen, black,
                [cat_ref_point_x - (28 + (-1)**n * 24) * cat_scale,
                 cat_ref_point_y + 14 * cat_scale,
                 30 * cat_scale, 13 * cat_scale], 0.3 * pi, 0.55 * pi)
            arc(screen, black,
                [cat_ref_point_x - (2 + (-1)**n * 24) * cat_scale,
                 cat_ref_point_y + 14 * cat_scale,
                 30 * cat_scale, 13 * cat_scale], 0.45 * pi, 0.7 * pi)

            arc(screen, black,
                [cat_ref_point_x - (20 + (-1)**n * 24) * cat_scale,
                 cat_ref_point_y + 15 * cat_scale,
                 20 * cat_scale, 8 * cat_scale], 0.3 * pi, 0.7 * pi)
            arc(screen, black,
                [cat_ref_point_x - (-1)**n * 24 * cat_scale,
                 cat_ref_point_y + 15 * cat_scale,
                 20 * cat_scale, 8 * cat_scale], 0.3 * pi, 0.7 * pi)

            arc(screen, black,
                [cat_ref_point_x - (23 + (-1)**n * 24) * cat_scale,
                 cat_ref_point_y + 16 * cat_scale,
                 30 * cat_scale, 13 * cat_scale], 0.42 * pi, 0.67 * pi)
            arc(screen, black,
                [cat_ref_point_x - (9 + (-1)**n * 24) * cat_scale,
                 cat_ref_point_y + 16 * cat_scale,
                 30 * cat_scale, 13 * cat_scale], 0.27 * pi, 0.54 * pi)

        mustaches()

        def left_ear():
            """
            This function draws cat's left ear when the cat is left oriented and left ear when right oriented.
            Has high level function: head() -> cat().
            :return:
            """
            polygon(screen, cat_body_color, [(cat_ref_point_x - (-1)**n * 33 * cat_scale,
                                              cat_ref_point_y + 7 * cat_scale),

                                             (cat_ref_point_x - (-1)**n * 29 * cat_scale,
                                              cat_ref_point_y + 3 * cat_scale),

                                             (cat_ref_point_x - (-1)**n * 35 * cat_scale,
                                              cat_ref_point_y)])

            polygon(screen, black, [(cat_ref_point_x - (-1)**n * 33 * cat_scale,
                                     cat_ref_point_y + 7 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 29 * cat_scale,
                                     cat_ref_point_y + 3 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 35 * cat_scale,
                                     cat_ref_point_y)],
                    width=1)

            polygon(screen, bright_beige, [(cat_ref_point_x - (-1)**n * 32.7 * cat_scale,
                                            cat_ref_point_y + 6 * cat_scale),

                                           (cat_ref_point_x - (-1)**n * 29.8 * cat_scale,
                                            cat_ref_point_y + 3 * cat_scale),

                                           (cat_ref_point_x - (-1)**n * 34.2 * cat_scale,
                                            cat_ref_point_y + 0.8 * cat_scale)])

            polygon(screen, black, [(cat_ref_point_x - (-1)**n * 32.7 * cat_scale,
                                     cat_ref_point_y + 6 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 29.7 * cat_scale,
                                     cat_ref_point_y + 3 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 34.2 * cat_scale,
                                     cat_ref_point_y + 0.8 * cat_scale)],
                    width=1)

        left_ear()

        def right_ear():
            """
            This function draws cat's right ear when the cat is left oriented and right ear when right oriented.
            Has high level function: head() -> cat().
            :return:
            """
            polygon(screen, cat_body_color, [(cat_ref_point_x - (-1)**n * 16 * cat_scale,
                                              cat_ref_point_y + 7 * cat_scale),

                                             (cat_ref_point_x - (-1)**n * 20 * cat_scale,
                                              cat_ref_point_y + 3 * cat_scale),

                                             (cat_ref_point_x - (-1)**n * 14 * cat_scale,
                                              cat_ref_point_y)])

            polygon(screen, black, [(cat_ref_point_x - (-1)**n * 16 * cat_scale,
                                     cat_ref_point_y + 7 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 20 * cat_scale,
                                     cat_ref_point_y + 3 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 14 * cat_scale,
                                     cat_ref_point_y)],
                    width=1)

            polygon(screen, bright_beige, [(cat_ref_point_x - (-1)**n * 16.3 * cat_scale,
                                            cat_ref_point_y + 6 * cat_scale),

                                           (cat_ref_point_x - (-1)**n * 19.3 * cat_scale,
                                            cat_ref_point_y + 3 * cat_scale),

                                           (cat_ref_point_x - (-1)**n * 14.8 * cat_scale,
                                            cat_ref_point_y + 0.8 * cat_scale)])

            polygon(screen, black, [(cat_ref_point_x - (-1)**n * 16.3 * cat_scale,
                                     cat_ref_point_y + 6 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 19.3 * cat_scale,
                                     cat_ref_point_y + 3 * cat_scale),

                                    (cat_ref_point_x - (-1)**n * 14.8 * cat_scale,
                                     cat_ref_point_y + 0.8 * cat_scale)], width=1)

        right_ear()
    head()


def bezier(x1: list, x2: list, x3: list, x4: list,
           y1: list, y2: list, y3: list, y4: list,
           curves_amount: int, curves_colour: tuple, line_thickness):
    """
    This function draws Bezier's curves in the amount of curves_amount pieces with 4 control points.
    x1 and y1 are start point coord., x4 and y4 are end point coord.
    x2, y2, x3, y3 are middle coord.
    :param x1:
    :param x2:
    :param x3:
    :param x4:
    :param y1:
    :param y2:
    :param y3:
    :param y4:
    :param curves_amount:
    :param curves_colour:
    :param line_thickness:
    :return:
    """
    for j in range(0, curves_amount):
        curve = []

        for i in map(lambda x: x / 100.0, range(0, 105, 5)):
            x = (1.0 - i) ** 3 * x1[j] + 3 * (1.0 - i) ** 2 * i * x2[j] + 3 * (1.0 - i) * i ** 2 * \
                x3[j] + i ** 3 * x4[j]
            y = (1.0 - i) ** 3 * y1[j] + 3 * (1.0 - i) ** 2 * i * y2[j] + 3 * (1.0 - i) * i ** 2 * \
                y3[j] + i ** 3 * y4[j]
            curve.append([x, y])

        lines(screen, curves_colour, False, curve, line_thickness)


def clew(clew_ref_point_x=x_max // 2 + 10 * screen_scale_x, clew_ref_point_y=y_max // 2 + 37 * screen_scale_y,
         clew_scale=5, clew_orientation="left"):
    """
    This function draws clew. clew_ref_point X and Y coord. are when center of clew circle is.
    Has low level function: clew_threads()
    :param clew_ref_point_x:
    :param clew_ref_point_y:
    :param clew_scale:
    :param clew_orientation:
    :return:
    """

    # m - clew_orientation parameter
    m = 0
    if clew_orientation == "right":
        m = 1
    elif clew_orientation != "left":
        print("ERROR: incorrect clew_orientation parameter has been given. 'left' or 'right' was expected")

    circle(screen, gray, [clew_ref_point_x, clew_ref_point_y], 8 * clew_scale)
    circle(screen, black, [clew_ref_point_x, clew_ref_point_y], 8 * clew_scale, width=1)

    def clew_threads():
        """
        This function draws threads inside and outside clew.
        Has 2 low level functions: clew_threads_outside(), clew_threads_inside()
        :return:
        """

        def clew_threads_outside():
            """
            This function draws threads outside clew.
            Has high level functions: clew_threads() -> clew().
            :return:
            """
            # this is outside threads coordinates
            x1, y1 = [clew_ref_point_x - (-1)**m * 6.2 * clew_scale,
                      clew_ref_point_x - (-1)**m * 19 * clew_scale],\
                [clew_ref_point_y + 5 * clew_scale,
                 clew_ref_point_y + 8 * clew_scale]

            x2, y2 = [clew_ref_point_x - (-1)**m * 10 * clew_scale,
                      clew_ref_point_x - (-1)**m * 20 * clew_scale],\
                [clew_ref_point_y + 9 * clew_scale,
                 clew_ref_point_y + 10 * clew_scale]

            x3, y3 = [clew_ref_point_x - (-1)**m * 16 * clew_scale,
                      clew_ref_point_x - (-1)**m * 24 * clew_scale],\
                [clew_ref_point_y + 4 * clew_scale,
                 clew_ref_point_y + 6 * clew_scale]

            x4, y4 = [clew_ref_point_x - (-1)**m * 19 * clew_scale,
                      clew_ref_point_x - (-1)**m * 29 * clew_scale],\
                [clew_ref_point_y + 8 * clew_scale,
                 clew_ref_point_y + 9 * clew_scale]

            bezier(x1, x2, x3, x4, y1, y2, y3, y4, len(x1), gray, 1 + clew_scale // 10)

        clew_threads_outside()

        def clew_threads_inside():
            """
            This function draws threads inside clew.
            Has high level functions: clew_threads() -> clew().
            :return:
            """
            # this is inside threads coordinates
            x1, y1 = [clew_ref_point_x + (-1)**m * 2.2 * clew_scale,
                      clew_ref_point_x - (-1)**m * 2 * clew_scale,
                      clew_ref_point_x - (-1)**m * 3.5 * clew_scale,
                      clew_ref_point_x - (-1)**m * 3 * clew_scale,
                      clew_ref_point_x - (-1)**m * 1.5 * clew_scale,
                      clew_ref_point_x + (-1)**m * 1.5 * clew_scale],\
                [clew_ref_point_y - 5 * clew_scale,
                 clew_ref_point_y - 5 * clew_scale,
                 clew_ref_point_y - 3.5 * clew_scale,
                 clew_ref_point_y - 1.5 * clew_scale,
                 clew_ref_point_y,
                 clew_ref_point_y + 2 * clew_scale]

            x2, y2 = [clew_ref_point_x + (-1)**m * 7.5 * clew_scale,
                      clew_ref_point_x + (-1)**m * 1.8 * clew_scale,
                      clew_ref_point_x,
                      clew_ref_point_x - (-1)**m * 4.5 * clew_scale,
                      clew_ref_point_x - (-1)**m * 4.5 * clew_scale,
                      clew_ref_point_x - (-1)**m * 0.5 * clew_scale],\
                [clew_ref_point_y - 2 * clew_scale,
                 clew_ref_point_y - 1 * clew_scale,
                 clew_ref_point_y + 0.5 * clew_scale,
                 clew_ref_point_y - 1 * clew_scale,
                 clew_ref_point_y + 2 * clew_scale,
                 clew_ref_point_y + 2.7 * clew_scale]

            x3, y3 = [clew_ref_point_x + (-1)**m * 5.2 * clew_scale,
                      clew_ref_point_x + (-1)**m * 5 * clew_scale,
                      clew_ref_point_x + (-1)**m * 4 * clew_scale,
                      clew_ref_point_x - (-1)**m * 6 * clew_scale,
                      clew_ref_point_x - (-1)**m * 3.5 * clew_scale,
                      clew_ref_point_x - (-1)**m * 0.5 * clew_scale],\
                [clew_ref_point_y,
                 clew_ref_point_y - 4.5 * clew_scale,
                 clew_ref_point_y - 4 * clew_scale,
                 clew_ref_point_y + 2 * clew_scale,
                 clew_ref_point_y + 3.5 * clew_scale,
                 clew_ref_point_y + 5.5 * clew_scale]

            x4, y4 = [clew_ref_point_x + (-1)**m * 6 * clew_scale,
                      clew_ref_point_x + (-1)**m * 4.5 * clew_scale,
                      clew_ref_point_x + (-1)**m * 3.5 * clew_scale,
                      clew_ref_point_x - (-1)**m * 5 * clew_scale,
                      clew_ref_point_x - (-1)**m * 3.5 * clew_scale,
                      clew_ref_point_x],\
                [clew_ref_point_y + 3 * clew_scale,
                 clew_ref_point_y + 5 * clew_scale,
                 clew_ref_point_y + 6 * clew_scale,
                 clew_ref_point_y + 5 * clew_scale,
                 clew_ref_point_y + 6 * clew_scale,
                 clew_ref_point_y + 6.7 * clew_scale]

            # curves_amount == len(x1)
            bezier(x1, x2, x3, x4, y1, y2, y3, y4, len(x1), black, 1 + clew_scale // 10)

        clew_threads_inside()

    clew_threads()


# Here we draw clews
clew(x_max // 2 - 13 * screen_scale_x, y_max // 2 + 6 * screen_scale_y, 4, 'left')
clew(x_max // 2 + 10 * screen_scale_x, y_max // 2 + 26 * screen_scale_y, 7, 'right')
clew(x_max // 2 + 27 * screen_scale_x, y_max // 2 + 21 * screen_scale_y, 4, 'right')
clew(x_max // 2 - 25 * screen_scale_x, y_max // 2 + 35 * screen_scale_y, 4, 'left')
clew(x_max // 2 - 5 * screen_scale_x, y_max // 2 + 38 * screen_scale_y, 10, 'left')
clew(x_max // 2 + 28 * screen_scale_x, y_max // 2 + 38 * screen_scale_y, 7, 'right')
clew(x_max // 2 + 15 * screen_scale_x, y_max // 2 + 45 * screen_scale_y, 4, 'left')


# Here we draw cats
cat(x_max // 2 + 130, y_max // 2, 5.0, orange, green, 'left')
cat(x_max // 2 - 250, y_max // 2 + 50, 2.0, orange, green, 'right')
cat(x_max // 2 - 200, y_max // 2 + 150, 5.0, dark_brown, sky, 'right')
cat(x_max // 2 + 320, y_max // 2 + 235, 2.0, orange, green, 'right')
cat(x_max // 2 - 220, y_max // 2 + 420, 2.0, dark_brown, sky, 'right')
cat(x_max // 2 + 300, y_max // 2 + 440, 2.0, dark_brown, sky, 'left')
cat(x_max // 2 + 110, y_max // 2 + 330, 2.0, orange, green, 'left')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pygame.display.flip()

pygame.quit()
