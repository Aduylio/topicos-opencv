# Tópicos Especiais

## O que é OpenCV

OpenCV (Open source computer vision) é uma biblioteca de funções para visão computacional em tempo real. É escrita em C++ e sua interface principal é em C++, com uma pequena parte em C. Possui mapeamentos para utilização em Python, Java, JavaScript, entre outras linguagens. A documentação oficial para a versão mais recente encontra-se em https://docs.opencv.org/4.1.1/.

## Instalação

Para usar a versão mais recente da biblioteca OpenCV, é necessário que a sua versão de Python seja 3.4 ou maior (3.4, 3.5, 3.6 ou 3.7, no momento - agosto de 2019). Python 2.7 somente é suportado nas versões 2.x do OpenCV.

A forma mais fácil de instalar a biblioteca é usando o PIP (o sistema de gerenciamento de pacotes de Python - similar ao NPM).

Verifique se você tem o PIP instalado, executando o comando `python -m pip -V`. Este comando verifica a versão do PIP instalada. Caso você veja a mensagem que python não é reconhecido como um comando interno, precisará adicionar o caminho para o executável às variáveis de ambiente.

Após verificar que o PIP está funcionando, execute `python -m pip install opencv-python` para instalar a OpenCV para Python.

### Gerenciando múltiplas versões de Python

Quando já existe uma versão de Python já instalada no seu computador, ou você precisar manter múltiplas versões, será necessário usar um ambiente virtual. Um ambiente virtual permite que você mantenha versões e pacotes de Python para tais versões separados, para que não haja conflito. Em resumo, um ambiente virtual é útil quando você precisa alternadamente executar uma versão de Python ou outra.

Você utilizará o **virtualenv** para gerenciar múltiplas versões. Caso não tenha instalado, você também precisará instalá-lo com o PIP. Nesse caso, usaremos uma forma diferente da que fizemos para instalar o OpenCV.

Antes de continuar, encontre o diretório de instalação das suas versões de Python, como exemplo, vamos supor que os diretórios para as minhas instalações são:

* **Python 2.7**: C:\Python27
* **Python 3.7**: C:\Users\antonio\AppData\Local\Programs\Python3.7

Nesse curso, você precisará de Python 3.7, então criaremos o ambiente virtual somente para esta versão. Repita os passos a seguir para criar um ambiente virtual para qualquer outra versão.

#### 1. Instalando o `virtualenv``

Supondo que o diretório de instalação de Python é `C:\Users\antonio\AppData\Local\Programs\Python3.7`, no terminal do windows, execute:

```
C:\Users\antonio\AppData\Local\Programs\Python3.7\Scripts\pip.exe install virtualenv
```

Se a instalação terminou sem problemas, você terá instalado o `virtualenv`.

#### 2. Criando o ambiente virtual

Primeiramente, crie um diretório `topicos-opencv` no local de sua preferência onde salvaremos o código criado nessa disciplina e onde você criará o ambiente virtual, para facilitar o seu uso.

Considerando o mesmo diretório de instalação de Python usado na etapa 1, você executará o `virtualenv` da forma a seguir, onde `env3` é o nome do diretório onde ficará o ambiente virtual de Python 3.7 (o nome foi escolhido por mim).

```
C:\Users\antonio\AppData\Local\Programs\Python3.7\Scripts\virtualenv.exe env3
```

#### 3. Ativando o ambiente virtual

No terminal, agora considere que você está no diretório `topicos-opencv` criado na etapa 2 e que neste diretório você criou o ambiente virtual dentro do diretório `env3`.

Para ativar o ambiente virtual de Python3.7, digite no terminal:

```
env3\Scripts\activate.bat
```

No início da linha atual do terminal, você verá "(env3)", indicando que o ambiente virtual está ativado e tudo que você executar será com Python 3.7.

#### 4. Testando o ambiente virtual

Para certificar-se que a versão de Python usada no ambiente virtual é a 3.7, como o esperado, execute Python, chamando `python`. Veja se o número da versão que aparece no topo do cabeçalho emitido por Python é 3.7.

## Tópicos

## 1. Trabalhando com imagens

Código desenvolvido neste tópico disponível [aqui](https://github.com/antoniojnr/topicos-opencv/tree/master/1-imagens).

Conteúdo abordado:

* Carregar imagem
* Obter informações do tamanho da imagem
* Exibir imagem
* Salvar imagem

## 2. Operações em imagens

Código desenvolvido neste tópico disponível [aqui](https://github.com/antoniojnr/topicos-opencv/tree/master/2-ops-imagens).


