import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import random as np
from vpython import *

class Plotting():
    """
    Classe para plotar as posições, em 2D e 3D, dos planetas ao decorrer do tempo, e também, sua trajetória.
    """
    def __init__(self,path):
        #Abrindo o arquivo excel.
        file = pd.ExcelFile(path)
        self.planets = []

        #Para cada sheet de planeta no arquivo haverá um dataframe.
        for i in range(len(file.sheet_names)-4):
            planet = file.parse(f'Planeta {i+1}')
            self.planets.append(planet)

    def getRadius(self,radius):
        self.radius = radius

    def plot2d(self):
        """Função para plotar as posições dos planetas em 2 dimensões."""
        fig2d = plt.figure()
        ax2d = fig2d.add_subplot(111)

        for i in range(len(self.planets)):
            ax2d.scatter(self.planets[i]['x'],self.planets[i]['y'],label=f'Planeta {i+1}',s=7)

            #Colocando o tempo em cada posição (x,y), se houver menos de 100 passos.
            if len(self.planets[i]['x']) > 100:
                pass
            else:
                for j, t in enumerate(self.planets[i]['t']):
                    #Checando se não a posições com sobreposição.
                    if j > 0:
                        coord_actual = self.planets[i].loc[j,'x'],self.planets[i].loc[j,'y']
                        coord_previous = self.planets[i].loc[j-1,'x'],self.planets[i].loc[j-1,'y']

                    if j == 0 or coord_actual != coord_previous:
                        ax2d.annotate(t,xy=(self.planets[i].loc[j,'x'],self.planets[i].loc[j,'y']),**{'fontsize':'small'})

        plt.xlabel('eixo X')
        plt.ylabel('eixo Y')
        plt.legend()
        plt.show()

    def plot3d(self):
        """Função para plotar as posições dos planetas em 3 dimensões."""
        fig3d = plt.figure()
        ax3d = fig3d.add_subplot(111, projection='3d')

        for i in range(len(self.planets)):
            ax3d.scatter(self.planets[i]['x'],self.planets[i]['y'],self.planets[i]['z'],label=f'Planeta {i+1}',s=7)

            if len(self.planets[i]['x']) > 100:
                pass
            else:
                for j, t in enumerate(self.planets[i]['t']):
                    if j > 0:
                        coord_actual = self.planets[i].loc[j,'x'],self.planets[i].loc[j,'y'],self.planets[i].loc[j,'z']
                        coord_previous = self.planets[i].loc[j-1,'x'],self.planets[i].loc[j-1,'y'],self.planets[i].loc[j-1,'z']

                    if j == 0 or coord_actual != coord_previous:
                        ax3d.text(self.planets[i].loc[j,'x'],self.planets[i].loc[j,'y'],self.planets[i].loc[j,'z'],f'{t}',**{'fontsize':'xx-small'})

        ax3d.set_xlabel('eixo X')
        ax3d.set_ylabel('eixo Y')
        ax3d.set_zlabel('eixo Z')

        plt.legend()
        plt.show()

    def trajectory(self,fps=60):
        """Função para plotar as trajetórias dos planetas e seus vetores."""
        objects = []

        #Adicionando os modelos dos planetas e seus vetores à lista objects.
        for i in range(len(self.planets)):
            #Posição dos planetas.
            sphere_pos = vector(self.planets[i].loc[0,'x'],self.planets[i].loc[0,'y'],self.planets[i].loc[0,'z'])
            #Posição dos vetores.
            arrow_axis = vector(self.planets[i].loc[0,'vx'],self.planets[i].loc[0,'vx'],self.planets[i].loc[0,'vz'])
            #Criação de uma cor aleatória para diferenciar os planetas.
            color = vector(np.rand(1),np.rand(1),np.rand(1))

            #Criação do planeta.
            ball = sphere(pos=sphere_pos,make_trail=True,radius=self.radius[i],color=color)
            #Criação do vetor.
            vetor = arrow(pos=sphere_pos,axis=arrow_axis)

            objects.append([ball,vetor])

        #Atualização das posições dos planetas, das posições dos vetores e seus tamanhos.
        for i in range(1,self.planets[0].shape[0]):
            #Limitando os quadros por segundo de acordo com a variável fps.
            rate(fps)
            for j in range(len(self.planets)):
                objects[j][0].pos = vector(self.planets[j].loc[i,'x'],self.planets[j].loc[i,'y'],self.planets[j].loc[i,'z'])
                objects[j][1].pos = vector(self.planets[j].loc[i,'x'],self.planets[j].loc[i,'y'],self.planets[j].loc[i,'z'])
                objects[j][1].axis = vector(self.planets[j].loc[i,'vx']+self.radius[j],self.planets[j].loc[i,'vy']+self.radius[j],self.planets[j].loc[i,'vz']+self.radius[j]) #Tamanho do vetor.
