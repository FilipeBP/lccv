import pandas as pd
import numpy as np

class Planeta():
    """
    Classe para atribuir as variáveis iniciais de cada planeta.
    """
    def __init__(self,x0,y0,z0,v0x,v0y,v0z,raio,massa):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.v0x = v0x
        self.v0y = v0y
        self.v0z = v0z
        self.radius = raio
        self.mass = massa

class Entrada():
    """
    Classe para coletar os parâmetros, as variáveis de colisão e os dados iniciais dos planetas.
    """
    def __init__(self, file):
        #Criando dataframes a partir do arquivo coletado.
        self.parameters = pd.read_excel(file, sheet_name = 'Parâmetros')
        self.data = pd.read_excel(file, sheet_name = 'Planetas')
        self.models = np.array(pd.read_excel(file, sheet_name = 'Modelos de colisão', usecols='B:BB'))
        self.collision_matrix = np.array(pd.read_excel(file, sheet_name = 'Matriz colisão', usecols='B:BB'))

        self.generalParameters()

    def generalParameters(self):
        #Coletando os parametros.
        self.integrator = str(self.parameters['Integrador'])
        self.dt = float(self.parameters['Passo'])
        self.t_final = float(self.parameters['Tempo final'])
        self.n_impressions = int(self.parameters['N impressões'])

    def planetsAtributes(self):
        planets = []
        self.radius = []

        for i in range(self.data.shape[0]):
            #Atribuindo atributos para a instância
            x0 = self.data.loc[i,'x0']
            y0 = self.data.loc[i,'y0']
            z0 = self.data.loc[i,'z0']
            v0x = self.data.loc[i,'v0x']
            v0y = self.data.loc[i,'v0y']
            v0z = self.data.loc[i,'v0z']
            radius = self.data.loc[i,'Raio']
            mass = self.data.loc[i,'Massa']

            self.radius.append(radius)

            #Criando uma instância de planeta
            planet = Planeta(x0,y0,z0,v0x,v0y,v0z,radius,mass)

            #Adicionando a instância para a lista que será retornada.
            planets.append(planet)

        return planets
