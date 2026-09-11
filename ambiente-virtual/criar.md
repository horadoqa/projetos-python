## 1\. Abra a pasta do seu projeto

No VS Code, abra a pasta onde ficará seu projeto.

Depois abra o terminal:

**Terminal → New Terminal**

ou use:

```
Ctrl + `
```

 ## 2\. Crie o ambiente virtual

 No terminal, execute:

```
python -m venv .venv
```

 Isso criará uma pasta chamada `.venv` dentro do projeto:

```
meu-projeto/
├── .venv/
└── ...
```

 Se `python` não funcionar, tente:

```
python3 -m venv .venv
```

 ## 3. Ative o ambiente virtual

 ### Windows — PowerShell

```
.venv\Scripts\Activate.ps1
```

 Se estiver usando o CMD:

```
.venv\Scripts\activate
```

 ### Linux / macOS

```
source .venv/bin/activate
```

 Quando funcionar, você verá algo parecido com:

```
(.venv) C:\meu-projeto>
```

 O `(.venv)` indica que o ambiente está ativo.

 ## 4\. Selecione o Python no VS Code

 O VS Code normalmente detecta o `.venv` automaticamente.

 Se não detectar:

 1. Pressione **Ctrl + Shift + P**
2. Procure por **Python: Select Interpreter**
3. Escolha o Python dentro de `.venv`

 Por exemplo:

```
.venv/Scripts/python.exe
```

 ou, no Linux/macOS:

```
.venv/bin/python
```

 ## 5\. Instale seus pacotes

 Com o ambiente ativado:

```
pip install requests
```

 Por exemplo:

```
pip install pandas numpy
```

 Esses pacotes ficarão instalados **somente nesse ambiente virtual**, sem misturar com os outros projetos.

 ### Dica importante

 É uma boa prática adicionar `.venv` ao `.gitignore`:

```
.venv/
```

 Assim você não envia o ambiente virtual inteiro para o GitHub.

 Se quiser, também posso te mostrar **como configurar um projeto Python completo no VS Code, incluindo `.venv`, `requirements.txt`, `.gitignore` e estrutura de pastas**.