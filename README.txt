pip install: openpyxl, xlsxwriter, vpython, numpy, pandas, matplotlib.

O projeto é constituído de 4 módulos e 1 programa principal.
Os módulos são: interface, entrada, analise e visualizacao.

O módulo interface tem 3 funcionalidades: criar uma interface simples para a entrada de dados, e exportá-los para um arquivo .xlsx;
escolher o arquivo em que irá conter todos os dados necessários; caso o arquivo escolhido seja .txt, e com o modelo padrão, converte-lo
em um arquivo .xlsx.

O módulo entrada consiste em duas classes, a classe Planeta, para que os dados iniciais de cada planeta seja atruibuido a esta classe,
e a classe Entrada cuja função é ler o arquivo passado e associar os dados do arquivo à variáveis, ou à dataframes, utilizando o módulo
pandas.

O módulo analise irá calcular, utilizando métodos de integração, as posições, velocidades e acelerações dos planetas ao decorrer do tempo,
e para finalizar, exportar as posições e velocidades para o mesmo arquivo .xlsx.

Por fim, o método visualizacao tem como função mostrar as posições dos planetas, em relação ao tempo, em 2D, 3D e sua trajetória, com
o vetor da força de cada planeta.
---------------------------------
TUTORIAL:
Para rodar o projeto, é necessário executar o programa principal, o main.py. Ao executar o programa, irá aparecer uma interface com 2
opções: 'Novo arquivo' e 'Selecionar arquivo'. Se já existir um arquivo .txt com o modelo padrão, clica em 'Selecionar arquivo', e 
aparecerá uma janela para selecionar o arquivo, com uma lista de opções no canto inferior direito. Se for necessário criar um arquivo, clica no
botão 'Novo arquivo', e irá aparecer variás interfaces, uma de cada vez, para a entrada de dados. Porém, para a continuidade do programa
é OBRIGATÓRIO selecionar um arquivo. Após selecionar, o programa irá calcular com os dados fornecidos, e ao fim, irá aparecer, em sequência,
um gráfico em 2D, um gráfico em 3D, e uma animação com a trajetória dos planetas e seus vetores.
OBS: Se for necessário mudar a constante G para os dados em uma escala adequada, seu valor poderá ser modificado na linha 19 do módulo análise.