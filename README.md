# Requerimento do Projeto:

**A modelagem 3D deve conter no mínimo:**

Navegação usando o teclado/mouse permitindo ao usuário visualizar a parte externa e interna do Laboratório;
5 objetos diferentes do laboratório;
Janelas: a janela deverá ser aberta e fechada usando o teclado;
1 Porta: A porta deverá ser aberta ou fechada (baixa rotação) através da ação de um botão do teclado.
2 ventiladores de teto rotacionando em baixa velocidade;
Construção de um ambiente compilável para o programa:
Para rodar nosso código que possue as bibliotecas "OpenGL.GL", "OpenGL.GLUT", "OpenGL.GLU", "pyrender", "pyrr" e "pywavefront", você precisa instalar os seguintes pacotes na ordem a seguir:

- "numpy": pode ser instalado pelo pip, com o comando "pip install numpy".

- "PyOpenGL": pode ser instalado pelo pip, com o comando "pip install PyOpenGL".

- "PyOpenGL-accelerate": pode ser instalado pelo pip, com o comando "pip install PyOpenGL- accelerate".

- "PyWavefront": pode ser instalado pelo pip, com o comando "pip install PyWavefront".

- "pyrender": pode ser instalado pelo pip, com o comando "pip install pyrender".

- "pyrr": pode ser instalado pelo pip, com o comando "pip install pyrr".

_Lembrando que é importante ter um ambiente Python configurado corretamente, com a versão compatível com as bibliotecas que serão utilizadas._

# Sobre o funcionamento e interação do código:

Este programa cria uma cena 3D usando a biblioteca pyrender e permite que o usuário navegue pela cena usando as teclas W, A, S e D para mover a câmera e o mouse para girar a câmera.

A cena consiste em cinco modelos carregados a partir de arquivos .obj, posicionados e orientados na cena usando matrizes de transformação 4x4.

O programa cria uma instância da classe **pyrender.Scene** e adiciona a câmera e a luz à cena usando as funções **set_camera()** e **add()**, respectivamente. Em seguida, os modelos são carregados a partir dos arquivos **.obj** usando a classe **pywavefront.Wavefront**. Cada modelo é posicionado e orientado na cena usando matrizes de transformação e adicionado à cena usando a função **add()**.

Finalmente, o programa cria uma instância da classe pyrender.Viewer e inicia o loop de eventos usando a função **glutMainLoop()**. A classe **pyrender.Viewer** permite que o usuário visualize e interaja com a cena usando o mouse e o teclado.
