from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pyrender
from pyrr import Matrix44, Vector3
from pyrender import MetallicRoughnessMaterial
from pywavefront import Wavefront
import time
# Definir variáveis globais para a posição da câmera
xPos = 0
yPos = 0
zPos = 0
xRot = 0
yRot = 0

def keyPressed(key, x, y):
    global xPos, yPos, zPos
    if key == b'w':
        zPos += 0.1
    elif key == b's':
        zPos -= 0.1
    elif key == b'a':
        xPos -= 0.1
    elif key == b'd':
        xPos += 0.1
    glutPostRedisplay()

def mouseMoved(x, y):
    global xRot, yRot
    xRot += (y - glutGet(GLUT_WINDOW_HEIGHT)/2) / 5
    yRot += (x - glutGet(GLUT_WINDOW_WIDTH)/2) / 5
    glutPostRedisplay()

def loadModels():
    models = []
    models.append(Wavefront('C:/Users/Rayssa/Desktop/laboratorio/obj/lab.obj', 'C:/Users/Rayssa/Desktop/laboratorio/obj/lab.mtl'))
    models.append(Wavefront('C:/Users/Rayssa/Desktop/laboratorio/obj/armario.obj'))
    models.append(Wavefront('C:/Users/Rayssa/Desktop/laboratorio/obj/cadeira.obj'))
    models.append(Wavefront('C:/Users/Rayssa/Desktop/laboratorio/obj/laptop.obj'))
    models.append(Wavefront('C:/Users/Rayssa/Desktop/laboratorio/obj/luminaria.obj'))
    return models

def main():
    global scene
    scene = pyrender.Scene(bg_color=[0, 0, 0, 0])
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lab Navigation")
    glutDisplayFunc(drawScene)
    glutKeyboardFunc(keyPressed)
    glutPassiveMotionFunc(mouseMoved)
    glEnable(GL_DEPTH_TEST)
    
    models = loadModels() # Carrega os modelos
    
    # posição da câmera
    camera_pos = [0.0, 0.0, 10.0]
    # ponto que a câmera aponta
    camera_target = [0.0, 0.0, 0.0]
    # vetor que define a direção "up" da câmera
    up_vector = [0.0, 1.0, 0.0]
    # constrói uma matriz de visualização a partir da posição, do ponto que a câmera aponta e do vetor "up"
    view_matrix = Matrix44.look_at(camera_pos, camera_target, up_vector)
    # define a câmera na cena
    scene.set_camera(pyrender.IntrinsicsCamera(800, 600, 60, zfar=1000.0), pose=view_matrix)
    
    # posição da luz
    light_pos = [10.0, 10.0, 10.0]
    # define a luz na cena
    scene.add(pyrender.PointLight(color=[1.0, 1.0, 1.0], intensity=1.0), pose=Matrix44.from_translation(light_pos))
    

    # Define a posição e orientação dos modelos na cena
    models[0].position = [0.0, 0.0, 0.0]
    models[0].scale = [1.0, 1.0, 1.0]
    models[0].rotation = Matrix44.from_z_rotation(0.0)
    scene.add(models[0])

    models[1].position = [-2.0, 0.0, 0.0]
    models[1].scale = [1.0, 1.0, 1.0]
    models[1].rotation = Matrix44.from_z_rotation(0.0)
    scene.add(models[1])

    models[2].position = [2.0, 0.0, 0.0]
    models[2].scale = [1.0, 1.0, 1.0]
    models[2].rotation = Matrix44.from_z_rotation(0.0)
    scene.add(models[2])

    models[3].position = [0.0, -1.0, 0.0]
    models[3].scale = [1.0, 1.0, 1.0]
    models[3].rotation = Matrix44.from_z_rotation(0.0)
    scene.add(models[3])


    models[4].position = [0.0, 1.0, 0.0]
    models[4].scale = [1.0, 1.0, 1.0]
    models[4].rotation = Matrix44.from_z_rotation(0.0)
    scene.add(models[4])

    pyrender.Viewer(scene, use_raymond_lighting=True)
    glutMainLoop()

    if name == "main":main()

time.sleep(5) # pausa por 5 segundos
nome = input("Qual é o seu nome? ")
print("Olá,", nome)
input("Pressione Enter para sair")


#Este programa cria uma cena 3D usando a biblioteca `pyrender` e 
#permite que o usuário navegue pela cena usando as teclas W, A, S e D para mover a câmera e o mouse para girar a câmera. 
#A cena consiste em cinco modelos carregados a partir de arquivos `.obj`, posicionados e orientados na cena usando matrizes de transformação 4x4.
#O programa cria uma instância da classe `pyrender.Scene` e adiciona a câmera e a luz à cena usando as 
#funções `set_camera()` e `add()`, respectivamente. Em seguida, os modelos são carregados a partir dos arquivos `.obj` 
#usando a classe `pywavefront.Wavefront`. Cada modelo é posicionado e orientado na cena usando matrizes de transformação e adicionado à cena usando a função `add()`.
#Finalmente, o programa cria uma instância da classe `pyrender.Viewer` e inicia o loop de eventos usando a função 
#`glutMainLoop()`. A classe `pyrender.Viewer` permite que o usuário visualize e interaja com a cena usando o mouse 
#e o teclado.
