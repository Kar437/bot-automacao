

# Automação de Tarefas com Python

Um bot de automação de tarefas desenvolvido com python, utlilizando as bibliotecas PyAutoGUI e Pandas, para preencher um cadastro de produtos com dados provenientes de uma base de dados.

## Como Funciona:

1. Assim que iniciado o bot abre o navegador e realiza automaticamente o login na plataforma fictícia.
2. Ele lê a base de dados (nesse caso, um arquivo CVS).
3. Para cada produtos na base, o bot preenche os campos necessários na página de cadastro.
4. O processo de cadastro é repetido até que todos os produtos sejam cadastrados.

 ### OBS:

- Faça a instalação das bibliotecas utilizando, no terminal o comando ``` pip install pyautogui pandas```
- Execute o arquivo ```bot_automação.py``` no seu editor de prefêrencia.
- Antes de executar o aquivo, verifique se a posição dos cliques com ```pyautogui.click()``` nas linhas 30 e 52 correspondem à posição correta no seu monitor.
-  Para obter a posição exata da área de clique, execute o arquivo ```rastreio_mouse.py```.
