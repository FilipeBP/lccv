pip install: openpyxl, xlsxwriter, vpython, numpy, pandas, matplotlib.

O projeto � constitu�do de 4 m�dulos e 1 programa principal.
Os m�dulos s�o: interface, entrada, analise e visualizacao.

O m�dulo interface tem 3 funcionalidades: criar uma interface simples para a entrada de dados, e export�-los para um arquivo .xlsx;
escolher o arquivo em que ir� conter todos os dados necess�rios; caso o arquivo escolhido seja .txt, e com o modelo padr�o, converte-lo
em um arquivo .xlsx.

O m�dulo entrada consiste em duas classes, a classe Planeta, para que os dados iniciais de cada planeta seja atruibuido a esta classe,
e a classe Entrada cuja fun��o � ler o arquivo passado e associar os dados do arquivo � vari�veis, ou � dataframes, utilizando o m�dulo
pandas.

O m�dulo analise ir� calcular, utilizando m�todos de integra��o, as posi��es, velocidades e acelera��es dos planetas ao decorrer do tempo,
e para finalizar, exportar as posi��es e velocidades para o mesmo arquivo .xlsx.

Por fim, o m�todo visualizacao tem como fun��o mostrar as posi��es dos planetas, em rela��o ao tempo, em 2D, 3D e sua trajet�ria, com
o vetor da for�a de cada planeta.
---------------------------------
TUTORIAL:
Para rodar o projeto, � necess�rio executar o programa principal, o main.py. Ao executar o programa, ir� aparecer uma interface com 2
op��es: 'Novo arquivo' e 'Selecionar arquivo'. Se j� existir um arquivo .txt com o modelo padr�o, clica em 'Selecionar arquivo', e 
aparecer� uma janela para selecionar o arquivo, com uma lista de op��es no canto inferior direito. Se for necess�rio criar um arquivo, clica no
bot�o 'Novo arquivo', e ir� aparecer vari�s interfaces, uma de cada vez, para a entrada de dados. Por�m, para a continuidade do programa
� OBRIGAT�RIO selecionar um arquivo. Ap�s selecionar, o programa ir� calcular com os dados fornecidos, e ao fim, ir� aparecer, em sequ�ncia,
um gr�fico em 2D, um gr�fico em 3D, e uma anima��o com a trajet�ria dos planetas e seus vetores.
OBS: Se for necess�rio mudar a constante G para os dados em uma escala adequada, seu valor poder� ser modificado na linha 19 do m�dulo an�lise.