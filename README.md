# 🐍 Projetos em Python

Repositório com diversos projetos desenvolvidos em Python.

Na pasta `jupyter-notebook` estão os projetos que podem ser executador diretamente no VSCode.

---

## ⚙️ Configuração do ambiente local

### 1. Instalar suporte a ambientes virtuais

```bash
sudo apt install python3.10-venv
```

### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Gerenciamento de dependências

### Salvar dependências no arquivo `requirements.txt`

```bash
pip freeze > requirements.txt
```

### Instalar dependências a partir do arquivo

```bash
pip install -r requirements.txt
```

---

## 🔄 Atualização de dependências

Para atualizar os pacotes listados no `requirements.txt`:

```bash
pip install upgrade-requirements
upgrade-requirements
pip freeze > requirements.txt
```

---

## 🚪 Desativar o ambiente virtual

```bash
deactivate
```

---

## 💡 Dicas

* Sempre ative o ambiente virtual antes de instalar novas dependências.
* Evite instalar pacotes globalmente para não causar conflitos entre projetos.
* Mantenha o `requirements.txt` atualizado para garantir reprodutibilidade.

---
