from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,30)
    gluLookAt(8,9,10,
             0,0,0,
             0,1,0
             )
    glClearColor(1,1,1,1)


step = 0
moving = True
##vertices
def xyz():
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex(0,0,0)
    glVertex(10,0,0)

    glColor3f(0,1,0)
    glVertex(0,0,0)
    glVertex(0,10,0)

    glColor3f(0,0,0)
    glVertex(0,0,0)
    glVertex(0,0,10)
    glEnd()

def draw():
    global step
    global moving


    ##inits
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    #road
    glLoadIdentity()
    glColor3f(0.45,0.45,0.45)
    glBegin(GL_POLYGON)
    glVertex(12 ,2,0)
    glVertex(12 ,-5,0)
    glVertex(-50,-5,0)
    glVertex(-50,2,0)
    glEnd()





    #####

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(1.7, -1, -0.3)
    glVertex(1.7, -1, 0.3)
    glVertex(-1.7, -1, 0.3)
    glVertex(-1.7, -1, -0.3)
    glEnd()

    
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(5, -1, -0.3)
    glVertex(5, -1, 0.3)
    glVertex(8.3, -1, 0.3)
    glVertex(8.3, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-5, -1, -0.3)
    glVertex(-5, -1, 0.3)
    glVertex(-8.3, -1, 0.3)
    glVertex(-8.3, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-15, -1, -0.3)
    glVertex(-15, -1, 0.3)
    glVertex(-25, -1, 0.3)
    glVertex(-25, -1, -0.3)
    glEnd()
    ####


    


   

    #sides
    
    glColor3f(0.8,0.56,0.36)
    glBegin(GL_POLYGON)
    glVertex(12 ,-5,0)
    glVertex(0 ,-5,11)
    glVertex(-50,-5,0)
    glEnd()


    
    glColor3f(0.52,0.80,0.98)  
    glBegin(GL_POLYGON)
    glVertex(13,2,0)
    glVertex(12,50,50)
    glVertex(-50,-50,50)
    glVertex(-50,2,0)
    glEnd()


    




    ##Car_Body
    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(step,0,0)  #animation
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.44,0.184,0.21)
    glTranslate(step,1.25,0) #animation
    glScale(0.5,0.2,0.5)
    glutSolidCube(5)

    

    ##Car_Scouts

    glLoadIdentity()
    glColor3f(1,1,0)
    glTranslate(step+2.5,0,0.6)
    glutSolidSphere(0.25,100,100)


    glLoadIdentity()
    glColor3f(1,1,0)
    glTranslate(step+2.5,0,-0.6)
    glutSolidSphere(0.25,100,100)
    
    
    
    



    ##Car_Tires
    
    glLoadIdentity()
    glColor3f(0.5,0.6,0.7)
    
    glTranslate(step+1.5,-0.625,1.25)
    
    glutSolidTorus(0.25,0.5,10,10)

    
    glLoadIdentity()
    glColor3f(0.5,0.6,0.7)
    glTranslate(step-1.5,-0.625,1.25)
    glutSolidTorus(0.25,0.5,10,10)


   
    

    #vertices
    #glLoadIdentity()
    #xyz()










    if moving:
        step += 0.02
        if step > 5:
                moving = False
    else:
        step -= 0.025
        if step < -13:
            moving = True


    

    
    glutSwapBuffers()

    



glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
init()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
