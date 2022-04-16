

# New Version - CaveScape

**Número da Lista**: 5 <br>
**Conteúdo da Disciplina**: Programação Dinâmica

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0164357  |  Ugor Brandão |
| 17/0161897 | Eduarda Servidio |

## Sobre  
Você está dentro de uma caverna e precisa escapar dela! Você tem acesso a um mapa onde mostra todos os postos dentro da caverna, porém percebe que ele está desatualizado! No mapa que você tem, todos os postos estão conectados entre si, e algumas conexões não existem mais. O seu objetivo é sair da caverna testando se existem caminhos ou não entre os postos.
Mas agora, há desafios! Você terá que carregar itens com você até a saída! É preciso que você defina nos postos qual
o maior valor de itens que consegue levar a partir do máximo de Kg dados!

## Screenshots
![image](https://user-images.githubusercontent.com/52542729/152828799-4331f393-4844-427b-b8d2-a9ac5e86f17f.png)
Figura 1: Tela inicial.

![image](https://user-images.githubusercontent.com/52542729/152828897-3e5b8100-7fd7-4b01-8303-e2df8e3e13e4.png)
Figura 2: Tela de quando há caminho entre os postos.

![image](https://user-images.githubusercontent.com/52542729/152828973-291a6a34-b4f1-4ab0-8ed4-f441491685a1.png)
Figura 3: Tela de quando não há caminho entre os postos. Mensagem de Erro (GameOver).

![image](https://user-images.githubusercontent.com/52542729/152829049-8edab551-e090-46b2-a39b-daf529c63a82.png)
Figura 4: Tela de quando encontra a saída. Mensagem de Vitória.

Figura 5: Tela de quando acerta o maior valor. Mensagem de Acerto.

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

A resposta com o maior valor de cada posto está embaixo rotacionada para uma rápida avaliação do jogo. <br>
Ao acertar o valor máximo, aparecerá uma mensagem de acerto e você terá que ir para outro posto. <br>
Ao errar, uma mensagem de erro aparecerá e você deverá tentar novamente.

Ao chegar no posto 10, uma mensagem de "Você encontrou a saída" aparecerá. <br> 
Ao tentar acessar um posto que não tem caminho, uma mensagem de "Voce errou" irá surgir, onde o jogador deve voltar a página inicial e tentar encontrar a saída novamente.
