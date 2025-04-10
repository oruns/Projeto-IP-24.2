# Projeto-IP-24.2

Grupo 9
Anderson Lima - avll
Julio cesar de lima - jcbl2
Renata Alves  - rgaw
Felipe de Lima -  flo
Edenn Weslley - ewss


Descrição do jogo:

Snake duo é um jogo da cobrinha multiplayer versus desenvolvido no pygame ,onde quem faz mais pontuação ou pega a quantidade necessária de coroas é o vencedor, você tem as habilidades necessárias para vencer os seus adversários?

Controles:

Jogador 1: WASD .
Jogador 2: SETAS.

Mecânicas:
Fruta: Aumenta o corpo da cobra e sua pontuação aumenta em 10 pontos.
Bomba: Diminui o corpo da cobra e sua pontuação vai cair em 10 pontos.
Coroas: Ao coletar 3 coroas o jogador ganha automaticamente.
Bater nas paredes perde 5 pontos
Ganha o jogo quem alcançar 100 pontos ou coletar 3 coroas

Iniciando o jogo:
clone o repositório do github ou faça o download do arquivo zip,
e execute o menu.py.

Sistema funcionando
![image](https://github.com/user-attachments/assets/bee96601-f53e-42d8-bf7f-962503aacdcc)
![image](https://github.com/user-attachments/assets/e1843fab-df14-4409-bf17-48434b33379d)
![image](https://github.com/user-attachments/assets/d579d6c8-b20a-4359-9ee7-99ffe42965cb)







Ferramentas:
As ferramentas, bibliotecas, frameworks utilizados com as respectivas justificativas para o uso;
Discord: amplamente utilizado como meio de comunicação entre os membros do grupo, e inicialmente foi usado para enviar as partes do código. 
Visual Studio Code: um dos principais meios utilizados pela equipe para desenvolver o código do jogo.
GitHub: meio principal de compartilhamento do código entre os membros da equipe. Utilizado para organizar e modularizar as partes desenvolvidas
Bibliotecas:
Pygame: biblioteca principal, utilizada como alicerce para construção e desenvolvimento do jogo 2d Snake Duo.
Random: biblioteca cujo propósito no código foi de acrescentar aleatoriedade ao aparecimento dos coletáveis. As coroas, bombas e maçãs aparecem pelo mapa de maneira aleatória de forma a criar uma dificuldade e competitividade no jogo.
OS: biblioteca para trabalhar com diretórios, especialmente para trocar de pasta antes de carregar imagens
SYS: biblioteca para sair completamente do programa, por exemplo, nos créditos

Frameworks:
A equipe não utilizou frameworks.  

Divisão de trabalho
Anderson Lima - avll:  Parte gráfica e organização da equipe e das tarefas.
Renata Alves  - rgaw: Classes/objetos, colisões e movimentação.
Julio Cesar de lima - jcbl2: Refatoração e debug.
 Felipe de Lima -  flo:  Mapas e lógica do código
Edenn Weslley - ewss:  Modularização e menu.

Conceitos
Os conceitos que foram apresentados durante a disciplina e utilizados no projeto (indicando onde foram usados);
Condicionais(if - elif - else): esse conceito aparece no momento de definir a movimentação de cada jogador, ajudar a definir as colisões, aumento ou diminuição do tamanho de cada player, visibilidade da coroa.
Laços de repetição(for - while): conceito fundamental que propicia o funcionamento do jogo, pois o mesmo é rodado no laço de repetição running. Além disso, tal conceito é utilizado para manter os coletáveis aparecendo no mapa (desenhar os coletáveis no mapa acontece por meio de laços de repetição), a própria ação de reposicionar das cobrinhas ocorre por meio desse conceito.
Funções: esse conceito foi amplamente utilizado para definir desde ações dentro das classes de objetos até usos específicos da biblioteca pygame, como as funções de desenho dos objetos coletáveis e jogadores.
Listas: esse conceito esteve presente no desenvolvimento do código para guardar a quantidade desejada de maçãs e bombinhas.
Tuplas: esse conceito foi usado majoritariamente para definição de coordenadas e uso das cores na biblioteca pygame. 
Programação orientada a objetos(opp): esse conceito foi usado para criar as classes de jogador e coletáveis dentro do jogo(maçãs, bombinhas e coroas).

Desafios
Os desafios e erros enfrentados no decorrer do projeto e as lições aprendidas. Para tanto, respondam às seguintes perguntas:
Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
A criação das colisões foi um dos momentos que geraram mais falhas. Foi preciso um trabalho constante de acertos e erros até conseguirmos chegar ao resultado final. Para lidar com isso, foi preciso tirar um tempo de estudo mais aprofundado sobre como implementar os conceitos vistos em aula junto ao uso das bibliotecas utilizadas.
Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
Um dos maiores desafios foi a comunicação entre os membros, o projeto foi proposto num momento em que nós alunos estávamos realizando outros trabalhos e provas das demais disciplinas. Por conta disso, a equipe demorou a estabelecer uma comunicação viável. Isso só foi resolvido quando esse período terminou.  
Quais as lições aprendidas durante o projeto?
Uma das lições mais importantes que pudemos aprender foi a importância e a realização de um trabalho em equipe, no qual todas as partes foram igualmente importantes no desenvolvimento e organização do projeto.

Documentação
Como os arquivos se comunicam: Arquivos principais: main.py, menu.py Execucao comeca em menu.py, que chama main.py, e os dois pegam o material necessário a partir dos módulos no mesmo diretório, em cada módulo os arquivos internos se comunicam entre si.
Descrição hierárquica dos diretórios:
assets: arquivos de conteúdo para o jogo (músicas).
config: configurações/dados usados.
Cores, dados de entidades e tela.
imgs: imagens usadas pelo jogo.
src: código fonte do jogo.
Pacotes (feitos por nós):
config: carregamento as configurações/dados.
entidades: entidades que serão carregadas (jogador, itens, etc).
gerenciamento: código de inicialização e controle.
imgs: importação das imagens dentro do python.
mapa: código relativo ao mapa.
menu: menu para entrar no jogo.
tela: código para desenhar a tela.
main: iniciar o jogo.
menu: iniciar o menu do jogo.
tela créditos : uma tela de créditos com o nome de cada aluno

