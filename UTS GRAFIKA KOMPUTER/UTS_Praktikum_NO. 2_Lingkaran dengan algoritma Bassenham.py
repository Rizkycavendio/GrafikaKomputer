# Muhammad Rizky Cavendio - 20051397011
# UTS - Grafika Komputer

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    glPointSize(5)

def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def bresenham_circle_drawing(r):
    x_position = -50
    y_position = 50

    x = 0
    y = r

    d = 3 - 2 * r

    plot(x + x_position, y + y_position)

    while y > x:

        if d < 0:
            x += 1
            d += 4 * x + 6
        else:
            x += 1
            y -= 1
            d += (4 * (x - y)) + 10

        plot(x + x_position, y + y_position)

        plot(x + x_position, -y + y_position)

        plot(-x + x_position, -y + y_position)

        plot(-x + x_position, y + y_position)


        plot(y + x_position, x + y_position)

        plot(-y + x_position, x + y_position)

        plot(-y + x_position, -x + y_position)

        plot(y + x_position, -x + y_position)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1.0, 1.0)

    glBegin(GL_LINES)

    glVertex2f(-100, 0)
    glVertex2f(100, 0)

    glVertex2f(0, -100)
    glVertex2f(0, 100)

    glEnd()

    bresenham_circle_drawing(40)

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Algoritma basenham untuk menggambar lingkaran")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()


main()