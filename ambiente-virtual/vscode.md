# Criando um ambiente virtual Python no VS Code

Um ambiente virtual (`venv`) permite instalar e gerenciar as dependências de um projeto Python de forma isolada, evitando conflitos com outros projetos ou com a instalação global do Python.

## 1\. Crie ou abra a pasta do projeto

Crie uma pasta para o seu projeto e abra essa pasta no **VS Code**.

## 2\. Abra a Paleta de Comandos

No VS Code, pressione:

```
Ctrl + Shift + P
```

Isso abrirá a **Paleta de Comandos**.

## 3\. Crie o ambiente virtual

Na Paleta de Comandos, digite:

```
Python: Create Environment
```

Selecione a opção **Python: Create Environment**.

Em seguida:

1. Selecione **Venv** como o tipo de ambiente.
2. Selecione a versão do **Python** que deseja utilizar.

O VS Code criará automaticamente uma pasta chamada:

```
.venv
```

Essa pasta conterá o ambiente virtual do seu projeto.

## 4\. Verifique se o ambiente está ativo

Abra um novo terminal no VS Code:

**Terminal → New Terminal**

Se o ambiente virtual estiver ativo, você verá `(.venv)` antes do caminho da pasta, por exemplo:

```
(.venv) C:\projetos\meu-projeto>
```

Isso indica que o ambiente virtual está ativo.

## 5\. Ative manualmente, se necessário

Caso o VS Code não ative o ambiente automaticamente, utilize o comando correspondente ao seu sistema operacional.

### Windows — CMD

```
.venv\Scripts\activate.bat
```

### Windows — PowerShell

```
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```
source .venv/bin/activate
```

Após a ativação, o terminal deverá apresentar `(.venv)` antes do caminho do projeto.

## 6\. Instale as bibliotecas

Com o ambiente virtual ativo, você pode instalar as bibliotecas necessárias para o projeto normalmente:

```
pip install nome-da-biblioteca
```

Por exemplo:

```
pip install requests
```

 As bibliotecas serão instaladas dentro do ambiente virtual, mantendo as dependências do projeto isoladas.

 ## Pronto! 🎉

 Seu projeto agora possui um ambiente virtual Python próprio.

 Essa abordagem ajuda a manter as dependências **organizadas, isoladas e controladas**, evitando conflitos entre diferentes projetos Python.

