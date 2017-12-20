from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QOpenGLWidget
from circuit import draw_circuit
#from scenario.scenario import

class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)


    def initializeGL(self):
        glClearColor(0,0,0,0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.6, 0.6, 0.6, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1., 1., 1., 1.0])
        glLightfv(GL_LIGHT0, GL_POSITION, [1.5, 2.9, 2.0, 1.0])

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.5, 0.0, 0.0, 1.0])
        glEnable(GL_CULL_FACE)
        glFrontFace(GL_CCW)
        glShadeModel(GL_SMOOTH)


    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.5, 100)
        #gluLookAt(1.5,1.5,7, 1.5,1.5,0, 0,1,0)
        
        #gluLookAt(1,1,-3, 0,0,0, 0,2,0)
        '''Vista Proxima Entrada Circuito'''
        gluLookAt(40,2,51, 55,1,51, 0,1,0)
        '''Vista Superior'''
        #gluLookAt(80,100,50, 80,5,50, 82,0,0)

        #gluLookAt(0,20,0, 0, 0, 0, 2, 0, 0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        draw_circuit()

        
  
       