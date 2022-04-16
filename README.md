

# New Version - CaveScape

**Número da Lista**: 5 <br>
**Conteúdo da Disciplina**: Programação Dinâmica

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0164357  |  Ugor Brandão |
| 17/0161897 | Eduarda Servidio |

## Sobre  
Você está dentro de uma caverna e precisa escapar dela! Você tem acesso a um mapa onde mostra todos os postos dentro da caverna, porém percebe que ele está desatualizado! No mapa que você tem, todos os postos estão conectados entre si, e algumas conexões não existem mais. O seu objetivo é sair da caverna testando se existem caminhos ou não entre os postos. <br>

NOVIDADE!!! <br>

Mas agora, há desafios! Você terá que carregar moedas com você até a saída! É preciso que você defina nos postos qual
o maior valor de moedas que consegue levar a partir do máximo de Kg dados!

## Screenshots
![image](https://user-images.githubusercontent.com/52542729/163654706-2fae760d-81ec-402a-9019-c8cea27e037d.png)
Figura 1: Tela inicial.

![image](https://user-images.githubusercontent.com/52542729/163659615-113a53a2-1acd-4eb8-b6cf-41310b17add8.png)
Figura 2: Tela de quando há caminho entre os postos.

![image](https://user-images.githubusercontent.com/52542729/163654735-66860ab7-0dda-4566-b9bc-e63750a633a7.png)
Figura 3: Tela de quando não há caminho entre os postos. Mensagem de Erro (GameOver).

![image](https://user-images.githubusercontent.com/52542729/163654800-736f455c-ac44-41d0-b412-d65aa7dfb77e.png)
Figura 4: Tela de quando encontra a saída. Mensagem de Vitória.

![image](https://user-images.githubusercontent.com/52542729/163659641-294c6bd4-5bfc-40ed-881f-ffb109c90cfe.png)
Figura 5: Tela de quando acerta o maior valor. Mensagem de Acerto.

![image](https://user-images.githubusercontent.com/52542729/163659660-dd77ea83-d402-478c-b392-0fe214ed0076.png)
Figura 6: Tela de quando não acerta o maior valor. Mensagem de Erro.

## Instalação 
**Linguagem**: Python, HTML e CSS. <br>
**Pré-requisitos**: ter o Python e o Flask instalados na máquina, abrir e executar os arquivos de preferência no VSCode.
Ao executar o arquivo no VSCode, um localhost será criado, dando acesso ao jogo.

## Uso 
Os caminhos que existem entre os postos (nós) são os seguintes:

| Posto | Acesso a |
| -- | -- |
| 1  | 2,7,8 |
| 2  | 7,1,8 |
| 3  | 7 |
| 4  | 6,8 |
| 5  | 5,10 |
| 6  | 4,5 |
| 7  | 1,3,4 |
| 8  | 1,4,9 |
| 9  | 8 |
| 10  | 5 |

* Para uma rápida avaliação do jogo, a resposta com o maior valor das moedas de cada posto está rotacionada embaixo da tabela de valores. <br>

* Ao acertar o valor máximo, aparecerá uma mensagem de acerto e você terá que ir para outro posto. <br>

* Ao errar, uma mensagem de erro aparecerá e você deverá tentar novamente.

* Ao chegar no posto 10, uma mensagem de "Você encontrou a saída" aparecerá. <br> 

* Ao tentar acessar um posto que não tem caminho, uma mensagem de "Voce errou" irá surgir, onde o jogador deve voltar a página inicial e tentar encontrar a saída novamente.
