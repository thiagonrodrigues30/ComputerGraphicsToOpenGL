from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QOpenGLWidget
from opengl.scenario.gl_scenario import *

class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)


    def initializeGL(self):
        glClearColor(0,0,0,0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
        glLightfv(GL_LIGHT0, GL_POSITION, [1.5, 2.9, 2.0, 1.0])
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 1.)

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.4, 0.4, 0.4, 1.0])
        glEnable(GL_CULL_FACE)
        glFrontFace(GL_CCW)
        glShadeModel(GL_SMOOTH)


    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        #gluPerspective(70, width / height, 0.5, 100)
        #gluPerspective(90, width / height, 0.5, 200)
        gluPerspective(45, width / height, 0.5, 200)
        #gluLookAt(1, 1, 2,  6, 8, 0, 4, 5, 3)
        #gluLookAt(2.5,1.5,2.0, 0,1.5,2, 0,1,0)
        #gluLookAt(0, 8, -10,  1, 1, 15,  0, 5, 3)
        #gluLookAt(75, 10, 75,   7, -2, 7,   35, 10, 35)
        gluLookAt(75, 175, 75,   75, 10, 75,   35, 10, 35)


        # essa deveria ser a camera, pois desloca apenas o z
        #gluLookAt(0, 0, 10,   0, 0, -3,  0, 3, -3)



    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        #draw_scenario()
        draw_scenario_corrida()
