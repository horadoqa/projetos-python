# Configuração de Ambiente Python no VS Code

 Este guia apresenta uma configuração básica e organizada para projetos **Python** utilizando o **Visual Studio Code (VS Code)** e ambientes virtuais com `venv`.

 O uso de ambientes virtuais permite manter as dependências de cada projeto isoladas, evitando conflitos entre diferentes versões de bibliotecas.

---

 ## Pré-requisitos

 Antes de começar, certifique-se de ter instalado:

- [Python](<https://www.python.org/>)
- [Visual Studio Code](<https://code.visualstudio.com/>)
- Extensão **Python** para o VS Code

 Para verificar se o Python está instalado, abra o terminal do VS Code e execute:

```
python --version
```

Em alguns sistemas Linux/macOS, pode ser necessário utilizar:

```
python3 --version
```

---

## 📁 1. Crie ou abra o projeto

Crie uma pasta para o seu projeto e abra-a no VS Code.

Uma estrutura inicial pode ser:

```
meu-projeto/
├── .venv/
├── src/
├── .gitignore
├── README.md
└── requirements.txt
```

> A pasta `.venv` será criada automaticamente posteriormente.

---

 ## 2. Crie o ambiente virtual pelo VS Code

 No VS Code, abra a **Paleta de Comandos** utilizando:

```
Ctrl + Shift + P
```

Digite:

```
Python: Create Environment
```

Selecione:

```
Venv
```

Em seguida, selecione a versão do Python que deseja utilizar.

O VS Code criará automaticamente a pasta:

```
.venv/
```

Essa pasta contém o ambiente virtual do projeto.

---

## ⚙️ 3. Selecione o interpretador Python

Caso o VS Code não selecione automaticamente o ambiente criado, abra a Paleta de Comandos:

```
Ctrl + Shift + P
```

Procure por:

```
Python: Select Interpreter
```

Selecione o interpretador localizado dentro da pasta `.venv`.

No Windows:

```
.venv\Scripts\python.exe
```

No Linux/macOS:

```
.venv/bin/python
```

---

## 4. Ative o ambiente virtual

Abra um novo terminal no VS Code:

**Terminal → New Terminal**

O VS Code normalmente ativará o ambiente automaticamente.

Para confirmar, procure por `(.venv)` antes do caminho da pasta:

```
(.venv) C:\projetos\meu-projeto>
```

### Windows — CMD

Caso não esteja ativo:

```
.venv\Scripts\activate.bat
```

### Windows — PowerShell

```
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```
source .venv/bin/activate
```

Quando o ambiente estiver ativo, o terminal deverá apresentar:

```
(.venv)
```

---

# 📦 5. Instale as dependências

Com o ambiente virtual ativado, você pode instalar as bibliotecas necessárias para o projeto.

Por exemplo:

```
pip install requests
```

 Ou:

```
pip install requests pandas
```

As bibliotecas serão instaladas apenas dentro do ambiente virtual.

---

# 📄 6. Crie o `requirements.txt`

O arquivo `requirements.txt` é utilizado para registrar as dependências do projeto.

Depois de instalar todas as bibliotecas necessárias, execute:

```
pip freeze > requirements.txt
```

O arquivo poderá ficar parecido com:

```
certifi==2025.1.31
charset-normalizer==3.4.1
idna==3.10
requests==2.32.3
urllib3==2.3.0
```

Dessa forma, outras pessoas poderão instalar exatamente as dependências utilizadas pelo projeto.

---

# 7. Configure o `.gitignore`

A pasta `.venv` **não deve ser enviada para o GitHub**.

Isso acontece porque o ambiente virtual contém arquivos específicos da máquina e pode ser recriado a partir do projeto.

Crie um arquivo chamado:

```
.gitignore
```

E adicione:

```
# Ambiente virtual
.venv/

# Cache do Python
__pycache__/
*.py[cod]
*$py.class

# Arquivos de configuração local
.env
.env.*

# IDE
.vscode/

# Arquivos do sistema operacional
.DS_Store
Thumbs.db
```

> Se o projeto precisar versionar configurações específicas do VS Code, você pode remover `.vscode/` do `.gitignore`.

---

# 8. Recrie o ambiente em outra máquina

Quando outra pessoa clonar o projeto, **não é necessário enviar a pasta `.venv`**.

Basta clonar o repositório:

```
git clone <URL_DO_REPOSITORIO>
```

 Entrar na pasta:

```
cd meu-projeto
```

E criar um novo ambiente virtual.

### Pelo VS Code

Abra o projeto no VS Code:

```
Ctrl + Shift + P
```

 Depois:

```
Python: Create Environment
```

 Selecione:

```
Venv
```

E escolha a versão do Python.

### Pelo terminal

Também é possível criar o ambiente diretamente pelo terminal:

```
python -m venv .venv
```

 No Linux/macOS, caso necessário:

```
python3 -m venv .venv
```

---

# 9. Instale as dependências do projeto

 Com o novo ambiente virtual criado e ativado, execute:

```
pip install -r requirements.txt
```

O `pip` instalará todas as bibliotecas registradas no arquivo `requirements.txt`.

---

# 10. Execute o projeto

Depois de configurar o ambiente e instalar as dependências, execute o arquivo principal do projeto.

Por exemplo:

```
python main.py
```

 Ou, caso o projeto utilize uma estrutura com `src`:

```
python src/main.py
```

---

# Comandos úteis

### Verificar a versão do Python

```
python --version
```

### Verificar o `pip`

```
pip --version
```

### Verificar o ambiente Python utilizado

Windows:

```
where python
```

Linux/macOS:

```
which python
```

### Listar bibliotecas instaladas

```
pip list
```

### Gerar/atualizar o `requirements.txt`

```
pip freeze > requirements.txt
```

### Instalar dependências

```
pip install -r requirements.txt
```

### Desativar o ambiente virtual

```
deactivate
```

---

# Fluxo recomendado

Em uma máquina nova, o fluxo completo será:

```
# 1. Clonar o projeto
git clone <URL_DO_REPOSITORIO>

# 2. Entrar na pasta
cd meu-projeto

# 3. Criar o ambiente virtual
python -m venv .venv

# 4. Ativar o ambiente
# Windows:
.venv\Scripts\activate

# Linux/macOS:
source .venv/bin/activate

# 5. Instalar as dependências
pip install -r requirements.txt

# 6. Executar o projeto
python main.py
```

---

# Estrutura final recomendada

Ao final, o projeto poderá ter uma estrutura semelhante a:

```
meu-projeto/
│
├── .venv/              # Ambiente virtual (não versionar)
│
├── src/                # Código-fonte
│   └── main.py
│
├── .gitignore          # Arquivos ignorados pelo Git
├── README.md           # Documentação
└── requirements.txt    # Dependências do projeto
```

> **Importante:** a pasta `.venv` deve existir localmente em cada máquina, mas não deve ser versionada no Git. O `requirements.txt` é o responsável por registrar as dependências necessárias para recriar o ambiente.

---

## Resumo

 O fluxo recomendado para projetos Python é:

```
Projeto
  ↓
Criar .venv
  ↓
Selecionar o interpretador no VS Code
  ↓
Ativar ambiente
  ↓
Instalar bibliotecas
  ↓
Gerar requirements.txt
  ↓
Configurar .gitignore
  ↓
Versionar o código no Git
```

 Dessa forma, o projeto fica **isolado, reproduzível e fácil de configurar em qualquer máquina**.