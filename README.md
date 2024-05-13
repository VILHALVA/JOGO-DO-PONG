# JOGO DO PONG
🎮JOGO DO PONG COM INTERFACE GRAFICA.

<img src="FOTO.png" align="center" width="400"> <br>

## DESCRIÇÃO:
Este programa utiliza a biblioteca Pygame e OpenGL para criar um jogo simples de Pong, um jogo de arcade clássico de dois jogadores. Aqui estão as principais funcionalidades do código:

- Define as dimensões da janela do jogo (640x480 pixels).
- Inicializa as variáveis relacionadas à posição e velocidade da bola, bem como à posição dos jogadores.
- Implementa funções para calcular as coordenadas X dos jogadores e as dimensões dos jogadores.
- Atualiza a lógica do jogo, movendo a bola, verificando colisões com os jogadores e as bordas da tela, e atualizando as posições dos jogadores com base nas teclas pressionadas.
- Implementa funções para desenhar retângulos coloridos na tela, representando a bola e os jogadores.
- Configura o ambiente OpenGL e a matriz de projeção para renderizar os elementos na tela.
- Utiliza um loop principal para continuamente atualizar e desenhar o estado do jogo.

O jogo é controlado pelos seguintes comandos do teclado:
- Jogador 1 (vermelho): Teclas "W" para cima e "S" para baixo.
- Jogador 2 (azul): Teclas de seta para cima e para baixo.

O jogo continua indefinidamente no loop principal, sendo atualizado e renderizado a cada iteração.

## EXECUTANDO O JOGO:
1. Certifique-se de ter o Pygame e o PyOpenGL instalados. Você pode instalá-los usando pip:
    ```bash
    pip install pygame PyOpenGL
    ```
2. Execute o arquivo Python.
3. O jogo da Pong será iniciado em uma janela.
4. Use as teclas 'W' e 'S' para mover o jogador 1 para cima e para baixo, respectivamente.
5. Use as teclas de seta para cima e para baixo para mover o jogador 2 para cima e para baixo, respectivamente.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
- Este arquivo executável está disponível apenas para `Windows X64`. Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

### 2. GERANDO:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -F CODIGO.py
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)





