from tkinter import *
import pandas as pd
import numpy as np
from tkinter import filedialog as fd
from datetime import datetime

class Janela():
    """
    Classe utilizada para criar uma interface gráfica para a entrada de dados.
    O objetivo principal desta classe é retornar o nome completo de um arquivo .xlsx
    OBS: Para que a interface seja fechada, é obrigatório escolher um arquivo.
    """
    def __init__(self):
        #Cria uma instância de Tk para que a janela seja criada.
        self.root = Tk()
        self.root.title('Simulação Planetária')
        self.mainWindow()
        self.root.mainloop()

    def mainWindow(self):
        """Método para criar a janela principal da interface."""
        #Retirando widgets anteriores
        self.deleteWidgets()

        #Widgets da tela principal
        self.t_entry = Label(self.root,text="Simulação Planetária")
        self.b_new = Button(self.root,text="Novo arquivo",width=15,command=self.secondWindow)
        self.b_select = Button(self.root,text="Selecionar arquivo",width=15,command=self.selectFile)

        #Colocando as Widgets na tela principal
        self.t_entry.grid(row=0,column=0,columnspan=2)
        self.b_new.grid(row=1,column=0)
        self.b_select.grid(row=2,column=0)

    def selectFile(self):
        """Método para selecionar o arquivo com os dados para a continuidade do programa principal (main.py)."""
        #Uma janela será aberta para a seleção de arquivo.
        self.file = fd.askopenfilename(title = "Selecione o arquivo", filetypes = (("Txt files",'*.txt'),("Excel files","*.xls*"),("All files","*.*")))

        #Checando se o arquivo é txt para transforma-lo em xlsx.
        if self.file[-4:] == '.txt':
            self.path = self.file
            self.txtToXlsx()
            self.file = self.path
        #Para o continuamento do programa, a janela deve ser fechada.
        if self.file != '':
            self.root.destroy()

    def secondWindow(self):
        """Método para criar uma janela para a entrada dos parâmetros gerais e de tempo."""
        #Criando um dicionário para guardar os parâmetros.
        self.parameters = {}

        #Retirando as Widgets da tela principal.
        self.deleteWidgets()

        #Widgets da segunda tela.
        self.t_path = Label(self.root,text='Nome do arquivo:',width=30,anchor=E)
        self.e_path = Entry(self.root)
        self.t_planets = Label(self.root,text="Número de planetas:",width=30,anchor=E)
        self.e_planets = Entry(self.root)
        self.t_collision = Label(self.root,text='Quantidade de modelos de colisão:',width=30,anchor=E)
        self.e_collision = Entry(self.root)
        self.t_integrator = Label(self.root,text="Tipo de integrador (Newton ou Verlet):",width=30,anchor=E)
        self.e_integrator = Entry(self.root)
        self.t_time = Label(self.root,text="Parâmetros de tempo",width=30,anchor=W)
        self.t_timedx = Label(self.root,text="Passo do tempo (x):",width=30,anchor=E)
        self.e_timedx = Entry(self.root)
        self.t_timefinal = Label(self.root,text="Tempo final:",width=30,anchor=E)
        self.e_timefinal = Entry(self.root)
        self.t_timen = Label(self.root,text="Número de passos para impressão:",width=30,anchor=E)
        self.e_timen = Entry(self.root)
        self.b_ready = Button(self.root,text="Pronto",width=8,command=self.thirdWindow)

        #Colocando as widgets na segunda tela.
        self.t_path.grid(row=0,column=0)
        self.e_path.grid(row=0,column=1)
        self.t_planets.grid(row=1,column=0)
        self.e_planets.grid(row=1,column=1)
        self.t_collision.grid(row=2,column=0)
        self.e_collision.grid(row=2,column=1)
        self.t_integrator.grid(row=3,column=0)
        self.e_integrator.grid(row=3,column=1)
        self.t_time.grid(row=4,column=0)
        self.t_timedx.grid(row=5,column=0)
        self.e_timedx.grid(row=5,column=1)
        self.t_timefinal.grid(row=6,column=0)
        self.e_timefinal.grid(row=6,column=1)
        self.t_timen.grid(row=7,column=0)
        self.e_timen.grid(row=7,column=1)
        self.b_ready.grid(row=8,column=1)

        #Nome default do arquivo.
        self.e_path.insert(0,'data_'+datetime.now().strftime("%d-%m-%Y_%H-%M"))

    def thirdWindow(self):
        """Método para criar uma janela para a entrada de dados dos planetas"""
        #Guardando os parâmetros
        self.path = self.e_path.get()+'.xlsx'
        self.n_planets = int(self.e_planets.get())
        self.n_collision = int(self.e_collision.get())
        self.parameters['Integrador'] = self.e_integrator.get()
        self.parameters['Passo'] = float(self.e_timedx.get())
        self.parameters['Tempo final'] = float(self.e_timefinal.get())
        self.parameters['N impressões'] = int(self.e_timen.get())
        self.df1 = pd.DataFrame([self.parameters])

        #Retirando as widgets da segunda tela.
        self.deleteWidgets()

        #Criando widgets para a terceira tela.
        self.t_nplanet = Label(self.root,text='Planeta 1')
        self.t_x0 = Label(self.root,text='x0:')
        self.e_x0 = Entry(self.root)
        self.t_y0 = Label(self.root,text='y0:')
        self.e_y0 = Entry(self.root)
        self.t_z0 = Label(self.root,text='z0:')
        self.e_z0 = Entry(self.root)
        self.t_v0x = Label(self.root,text='v0x:')
        self.e_v0x = Entry(self.root)
        self.t_v0y = Label(self.root,text='v0y:')
        self.e_v0y = Entry(self.root)
        self.t_v0z = Label(self.root,text='v0z:')
        self.e_v0z = Entry(self.root)
        self.t_radius = Label(self.root,text='Raio:')
        self.e_radius = Entry(self.root)
        self.t_mass = Label(self.root,text='Massa:')
        self.e_mass = Entry(self.root)
        self.b_addPlanet = Button(self.root,text='Adicionar',command=self.addPlanets)

        #Posicionando as widgets na terceira tela.
        self.t_nplanet.grid(row=0,column=0,columnspan=6)
        self.t_x0.grid(row=1,column=0)
        self.e_x0.grid(row=1,column=1)
        self.t_y0.grid(row=1,column=2)
        self.e_y0.grid(row=1,column=3)
        self.t_z0.grid(row=1,column=4)
        self.e_z0.grid(row=1,column=5)
        self.t_v0x.grid(row=2,column=0)
        self.e_v0x.grid(row=2,column=1)
        self.t_v0y.grid(row=2,column=2)
        self.e_v0y.grid(row=2,column=3)
        self.t_v0z.grid(row=2,column=4)
        self.e_v0z.grid(row=2,column=5)
        self.t_radius.grid(row=3,column=0)
        self.e_radius.grid(row=3,column=1)
        self.t_mass.grid(row=3,column=2)
        self.e_mass.grid(row=3,column=3)
        self.b_addPlanet.grid(row=4,column=5)

        #Criando listas para as características dos planetas.
        self.x0 = []
        self.y0 = []
        self.z0 = []
        self.v0x = []
        self.v0y = []
        self.v0z = []
        self.radius = []
        self.mass = []

        #Criando variável de controle para a função addUser.
        self.i = 1

    def addPlanets(self):
        """Método para coletar os dados dos planetas."""
        #Se uma Entry widget estiver vazia, seu valor será 0.
        for widget in self.root.grid_slaves():
            if isinstance(widget, Entry):
                if widget.get() == '':
                    widget.insert(0,'0')

        #Adicionando os dados para suas respectivas listas.
        self.x0.append(float(self.e_x0.get()))
        self.y0.append(float(self.e_y0.get()))
        self.z0.append(float(self.e_z0.get()))
        self.v0x.append(float(self.e_v0x.get()))
        self.v0y.append(float(self.e_v0y.get()))
        self.v0z.append(float(self.e_v0z.get()))
        self.radius.append(float(self.e_radius.get()))
        self.mass.append(float(self.e_mass.get()))

        #Após adicionar, os conteúdos das Entry widgets serão apagados.
        for widget in self.root.grid_slaves():
            if isinstance(widget, Entry):
                widget.delete(0,END)

        #Checando se todos os planetas receberam seus dados.
        if self.i == self.n_planets:
            self.forthWindow()

        #Incremetando a variável de controle e mudando a Label para o planeta atual.
        self.i+=1
        self.t_nplanet['text'] = f'Planeta {self.i}'

    def forthWindow(self):
        """Método para criar uma janela para a entrada dos modelos de colisão."""
        #Retirando todas as widgets da terceira tela.
        self.deleteWidgets()

        #Criando um dataframe para os dados dos planetas.
        self.df2 = pd.DataFrame({'x0':self.x0,'y0':self.y0,'z0':self.z0,
                                 'v0x':self.v0x,'v0y':self.v0y,'v0z':self.v0z,
                                 'Raio':self.radius,'Massa':self.mass})

        #Criando widgets para a quarta tela.
        self.t_nmodel = Label(self.root,text='Modelo 1')
        self.t_K = Label(self.root,text='K:')
        self.e_K = Entry(self.root)
        self.b_addModel = Button(self.root,text='Adicionar',command=self.addModel)

        #Posicionando as widgets na quarta tela.
        self.t_nmodel.grid(row=0,column=0,columnspan=2)
        self.t_K.grid(row=1,column=0)
        self.e_K.grid(row=1,column=1)
        self.b_addModel.grid(row=2,column=1)

        #Criando uma lista para os modelos de colisão.
        self.models = []

        #Criando variável de controle para a função addModel.
        self.j = 1

    def addModel(self):
        """Método para coletar os modelos de colisão."""
        #Coletando o modelo de colisão.
        self.models.append([self.j,int(self.e_K.get())])

        #Após adicionar, os conteúdos da Entry widget será apagada.
        self.e_K.delete(0,END)

        #Checando se todos os modelos foram coletados.
        if self.j== self.n_collision:
            self.lastWindow()

        #Incremetando a variável de controle e mudando a Label para o modelo atual.
        self.j+=1
        self.t_nmodel['text'] = f'Modelo {self.j}'

    def lastWindow(self):
        """Método para criar uma janela para a entrada dos elementos da matriz de colisão."""
        #Retirando as widgets da quarta tela.
        self.deleteWidgets()

        #Criando widgets para a última tela.
        self.t_pmodel = Label(self.root,text='Colisão entre os planetas 1 e 2:')
        self.e_collision_ij = Entry(self.root)
        self.b_collision_ij = Button(self.root,text='Adicionar',command=self.addCollision)

        #Posicionando as widgets na última tela.
        self.t_pmodel.grid(row=0,column=0,columnspan=2)
        self.e_collision_ij.grid(row=1,column=0,columnspan=2)
        self.b_collision_ij.grid(row=2,column=1)

        #Criando uma matriz com ordem de acordo com a quantidade de planetas.
        self.collision = np.ones((self.n_planets,self.n_planets))

        #Criando variáveis de controle para a função addCollision.
        self.k=0
        self.l=1

    def addCollision(self):
        """Método para coletar os elementos da matriz de colisão."""
        #Coletando o elemento.
        self.collision[self.k,self.l] = int(self.e_collision_ij.get())

        #Após adicionar, os conteúdos da Entry widget será apagada.
        self.e_collision_ij.delete(0,END)

        #Checando se todos os elementos foram coletados ou se há apenas 2 planetas.
        if (self.k == self.n_planets - 2 and self.l == self.n_planets - 1) or self.n_planets == 2:
            #Se todos os elementos foram coletados, dataframes para os modelos de colisão e a matriz de colisão.
            df3 = pd.DataFrame(np.array(self.models))
            df3.set_index(df3[0],inplace=True)
            df4 = pd.DataFrame(self.collision)

            self.exportToFile(self.df1,self.df2,df3,df4)

        #Incremetando as variáveis de controle e mudando a Label para o elemento atual.
        if self.l != self.n_planets - 1:
            self.l += 1
        else:
            self.k += 1
        self.t_pmodel['text'] = f'Colisão entre os planetas {self.k+1} e {self.l+1}:'


    def exportToFile(self,df1,df2,df3,df4):
        """Função para exportar os dataframes para um arquivo .xlsx"""
        #Criação de um dicionário com todos os dataframes.
        dfs = {'Parâmetros':df1,'Planetas':df2,'Modelos de colisão':df3,'Matriz colisão':df4}

        #Exportando os dataframes com sua worksheet associada.
        with pd.ExcelWriter(self.path, engine='xlsxwriter') as writer:
            for sheet in dfs.keys():
                dfs[sheet].to_excel(writer,sheet_name=sheet)

        self.mainWindow()

    def deleteWidgets(self):
        """Retira todas as widgets presentes na tela atual."""
        #Iteração em uma lista de todos os widgets na janela atual.
        for widget in self.root.grid_slaves():
            widget.grid_forget()

    def txtToXlsx(self):
        """Método para converter um arquivo .txt para um arquivo .xlsx com o formato adequado."""
        with open(self.file,'r') as f:
            #Lendo todo o arquivo .txt e colocando numa lista.
            content = f.readlines()

            for string in content:
                #Retirando '\n' de todas as strings e transformando-as em lista.
                if string != '\n':
                    line = string[-len(string):-1].split()

                #Substituindo as linhas.
                if len(line) > 1:
                    content[content.index(string)] = line
                elif len(line) == 1:
                    content[content.index(string)] = line[0]

        #Realizando a troca de extensão do arquivo.
        self.path = self.path[-len(self.path):-4]+'.xlsx'

        #Coletando o integrador.
        k = content.index("#INTEGRADOR")
        integrator = content[k+1]

        #Coletando os parâmetros de tempo.
        k = content.index("#PARAMETROS_TEMPO")
        dt = float(content[k+1][0])
        final_time = float(content[k+1][1])
        n_impressions = int(content[k+1][2])

        #Criando um dataframe para parâmetros.
        df1 = pd.DataFrame([{'Integrador':integrator,'Passo':dt,
                             'Tempo final':final_time,'N impressões':n_impressions}])

        #Criando listas para as características dos planetas.
        x0 = []
        y0 = []
        z0 = []
        v0x = []
        v0y = []
        v0z = []
        radius = []
        mass = []

        #Adicionando os dados para suas respectivas listas
        for i in range(int(content[1])):
            x0.append(float(content[i+2][0]))
            y0.append(float(content[i+2][1]))
            z0.append(float(content[i+2][2]))
            v0x.append(float(content[i+2][3]))
            v0y.append(float(content[i+2][4]))
            v0z.append(float(content[i+2][5]))
            radius.append(int(content[i+2][6]))
            mass.append(int(content[i+2][7]))

        #Criando um dataframe para os dados dos planetas.
        df2 = pd.DataFrame({'x0':x0,'y0':y0,'z0':z0,
                            'v0x':v0x,'v0y':v0y,'v0z':v0z,
                            'Raio':radius,'Massa':mass})

        #Coletando os modelos de colisão.
        k = content.index("#CONTATO_DEM")
        collision_model = [[int(j) for j in content[k+i+2]] for i in range(int(content[k+1]))]

        #Coletando matrizes de contato.
        k = content.index("#CONTATO_INTERACAO")
        collision_matrix = [[int(j) for j in content[k+i+1]] for i in range(int(content[1]))]

        #Criando dataframes para os modelos de colisão e a matriz de colisão dos planetas.
        df3 = pd.DataFrame(np.array(collision_model))
        df3.set_index(df3[0],inplace=True)
        df4 = pd.DataFrame(np.array(collision_matrix))

        self.exportToFile(df1,df2,df3,df4)
