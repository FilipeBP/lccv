from interface import Janela
import entrada
from analise import Integral
from visualizacao import Plotting
import pandas as pd

def main():
    window = Janela()
    arquivo = window.file

    arquivo_excel = pd.ExcelFile(arquivo)

    parametros = entrada.Entrada(arquivo)
    planetas = parametros.planetsAtributes()

    if len(arquivo_excel.sheet_names) == 4:
        integrador = str(parametros.integrator[5:11]).lower()

        tf = parametros.t_final
        dt = parametros.dt
        passos = parametros.n_impressions

        calculo = Integral(planetas,tf,dt)
        calculo.getCollision(parametros.models,parametros.collision_matrix)

        if integrador == 'newton':
            data = calculo.newton()
        elif integrador == 'verlet':
            data = calculo.verlet()
        else:
            print('Integrador inválido.')
            return

        calculo.exportToFile(arquivo,passos)
    else:
        pass

    grafico = Plotting(arquivo)
    grafico.getRadius(parametros.radius)
    grafico.plot2d()
    grafico.plot3d()
    grafico.trajectory(4)

if __name__ == '__main__':
    main()
