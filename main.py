from interface import Janela
import entrada
from analise import Integral
from visualizacao import Plotting
import pandas as pd

def main():
    #Criando uma interface e atribuindo o nome do arquivo a uma variável.
    window = Janela()
    arquivo = window.file

    #Recebendo a workbook para checar se os dados dos planetas já foram calculados.
    arquivo_excel = pd.ExcelFile(arquivo)

    #Recebendos os parâmetros e criando uma lista dos planetas.
    parametros = entrada.Entrada(arquivo)
    planetas = parametros.planetsAtributes()

    #Checando se os dados dos planetas não foram calculados.
    if len(arquivo_excel.sheet_names) == 4:
        #Atribuindo os parâmetros em variáveis.
        integrador = str(parametros.integrator[5:11]).lower()
        tf = parametros.t_final
        dt = parametros.dt
        passos = parametros.n_impressions

        #Calculando os dados dos planetas.
        calculo = Integral(planetas,tf,dt)
        calculo.getCollision(parametros.models,parametros.collision_matrix)

        if integrador == 'newton':
            calculo.newton()
        elif integrador == 'verlet':
            calculo.verlet()
        else:
            print('Integrador inválido.')
            return

        #Exportando os dados para o arquivo inicial.
        calculo.exportToFile(arquivo,passos)
    else:
        pass

    #Plotando os gráficos 2D e 3D e as trajetórias dos planetas.
    grafico = Plotting(arquivo)
    grafico.getRadius(parametros.radius)
    grafico.plot2d()
    grafico.plot3d()
    grafico.trajectory(4)

if __name__ == '__main__':
    main()
