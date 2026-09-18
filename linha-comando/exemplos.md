# Executando python via linah de comando

Usando `python3 -c` para executar código Python diretamente no terminal, sem criar um arquivo `.py`.

 Aqui vão alguns exemplos:

 ### 1\. Variáveis

```
python3 -c "nome='João'; print(f'Olá, {nome}!')"
```

 ### 2\. Soma

```
python3 -c "print(10 + 20)"
```

 ### 3\. Multiplicação

```
python3 -c "print(7 * 8)"
```

 ### 4\. Data e hora

```
python3 -c "from datetime import datetime; print(datetime.now())"
```

 ### 5\. Loop `for`

```
python3 -c "for i in range(5): print(i)"
```

 ### 6\. Lista

```
python3 -c "frutas=['maçã','banana','laranja']; print(frutas)"
```

 ### 7\. Filtrar números pares

```
python3 -c "print([x for x in range(20) if x % 2 == 0])"
```

 ### 8\. Ler um argumento do terminal

```
python3 -c "import sys; print('Olá,', sys.argv[1])" Maria
```

 Resultado:

```
Olá, Maria
```

 ### 9\. Criar várias linhas de código

 Você pode usar `;` para separar instruções:

```
python3 -c "nome='Carlos'; idade=25; print(nome); print(idade)"
```

 Ou usar `\n`:

```
python3 -c $'nome="Carlos"\nidade=25\nprint(nome, idade)'
```

 ### 10\. Executar uma função

```
python3 -c "def saudacao(nome): return f'Olá, {nome}!'; print(saudacao('Ana'))"
```

 ### 11\. Trabalhar com JSON

```
python3 -c "import json; dados={'nome':'Ana','idade':30}; print(json.dumps(dados, indent=2))"
```

 ### 12\. Fazer uma requisição HTTP

 Com a biblioteca padrão, por exemplo:

```
python3 -c "from urllib.request import urlopen; print(urlopen('https://example.com').status)"
```

 A ideia geral é:

```
python3 -c "CÓDIGO_PYTHON"
```

 Por exemplo, o seu:

```
python3 -c "print('Hello World!')"
```

 é equivalente a criar um arquivo `hello.py` contendo:

```
print("Hello World!")
```

 e depois executar:

```
python3 hello.py
```

Claro — aqui está uma sequência de **20 exemplos de `python3 -c`**, começando do básico e avançando para automação no Linux.

 ## Básico

 ### 1\. Hello World

```
python3 -c "print('Hello World!')"
```

 ### 2\. Variáveis

```
python3 -c "nome='Maria'; idade=25; print(nome, idade)"
```

 ### 3\. Operações matemáticas

```
python3 -c "print(10 + 5); print(10 - 5); print(10 * 5); print(10 / 5)"
```

 ### 4\. F-string

```
python3 -c "nome='João'; idade=30; print(f'{nome} tem {idade} anos')"
```

 ### 5\. Condicional

```
python3 -c "idade=20; print('Maior de idade' if idade >= 18 else 'Menor de idade')"
```

 ## Listas e loops

 ### 6\. Criar uma lista

```
python3 -c "frutas=['maçã','banana','laranja']; print(frutas)"
```

 ### 7\. Percorrer uma lista

```
python3 -c "for fruta in ['maçã','banana','laranja']: print(fruta)"
```

 ### 8\. Números de 1 a 10

```
python3 -c "for i in range(1,11): print(i)"
```

 ### 9\. Números pares

```
python3 -c "print([i for i in range(1,21) if i % 2 == 0])"
```

 ### 10\. Somar uma lista

```
python3 -c "numeros=[10,20,30,40]; print(sum(numeros))"
```

 ## Arquivos

 ### 11\. Ler um arquivo

```
python3 -c "print(open('arquivo.txt').read())"
```

 ### 12. Contar linhas de um arquivo

```
python3 -c "print(len(open('arquivo.txt').readlines()))"
```

 ### 13\. Escrever em um arquivo

```
python3 -c "open('saida.txt','w').write('Olá do Python!\n')"
```

 ### 14\. Procurar uma palavra

```
python3 -c "texto=open('arquivo.txt').read(); print('Python' in texto)"
```

 ## JSON

 ### 15\. Criar JSON

```
python3 -c "import json; dados={'nome':'Carlos','idade':35}; print(json.dumps(dados, indent=2))"
```

 ### 16\. Ler um JSON

 Supondo `dados.json`:

```
{"nome": "Carlos", "idade": 35}
```

 Execute:

```
python3 -c "import json; d=json.load(open('dados.json')); print(d['nome'])"
```

 ## Argumentos do terminal

 ### 17\. Receber um argumento

```
python3 -c "import sys; print(f'Olá, {sys.argv[1]}!')" Maria
```

 Resultado:

```
Olá, Maria!
```

 Você também pode passar vários:

```
python3 -c "import sys; print(sys.argv[1:])" um dois três
```

 Resultado:

```
['um', 'dois', 'três']
```

 ## Sistema operacional

 ### 18\. Listar arquivos do diretório

```
python3 -c "import os; print('\n'.join(os.listdir('.')))"
```

 ### 19\. Executar um comando do Linux

```
python3 -c "import subprocess; subprocess.run(['ls','-lah'])"
```

 Aqui o Python executa o `ls -lah` como um processo externo.

 ### 20. Executar um comando e capturar o resultado

```
python3 -c "import subprocess; r=subprocess.run(['uname','-a'], capture_output=True, text=True); print(r.stdout)"
```

 ## Bônus: exemplos mais interessantes

 ### Obter o IP do computador

```
python3 -c "import socket; print(socket.gethostbyname(socket.gethostname()))"
```

 ### Ver a versão do Python

```
python3 -c "import sys; print(sys.version)"
```

 ### Gerar números aleatórios

```
python3 -c "import random; print(random.randint(1,100))"
```

 ### Calcular SHA-256

```
python3 -c "import hashlib; print(hashlib.sha256(b'Hello World').hexdigest())"
```

 ### Fazer uma requisição HTTP

```
python3 -c "from urllib.request import urlopen; r=urlopen('https://example.com'); print(r.status); print(r.read(200).decode())"
```

 ### Encontrar arquivos `.txt`

```
python3 -c "import glob; print('\n'.join(glob.glob('*.txt')))"
```

 ### Compreender a estrutura

 A maioria desses comandos segue este padrão:

```
python3 -c "importação; código; código; código"
```

 Por exemplo:

```
python3 -c "import math; x=16; print(math.sqrt(x))"
```

 pode ser entendido como:

```
import math
x = 16
print(math.sqrt(x))
```

 A grande vantagem é poder transformar **pequenos scripts Python em comandos de uma única linha**, algo bastante útil em shell scripts, administração Linux e automação.

 Claro — abaixo está uma versão pensada para LinkedIn, com tom técnico, didático e acessível, usando os exemplos como uma introdução prática ao `python3 -c`.

 Python no terminal: 20 exemplos com python3 -c

# 🐍 Python no terminal: 20 exemplos com `python3 -c`

 Você sabia que pode executar código Python diretamente pelo terminal, sem precisar criar um arquivo `.py`?

 Basta usar:

```
python3 -c "print('Hello World!')"
```

 O parâmetro `-c` permite passar um trecho de código Python diretamente para o interpretador.

 Isso pode ser extremamente útil para **automação, administração Linux, scripts, testes rápidos e manipulação de arquivos**.

 A seguir, alguns exemplos que vão do básico ao mais avançado.

 ### 1️⃣ Variáveis

```
python3 -c "nome='Maria'; idade=25; print(nome, idade)"
```

 ### 2️⃣ Operações matemáticas

```
python3 -c "print(10 + 5); print(10 * 5); print(10 / 5)"
```

 ### 3️⃣ F-strings

```
python3 -c "nome='João'; idade=30; print(f'{nome} tem {idade} anos')"
```

 ### 4️⃣ Condicional

```
python3 -c "idade=20; print('Maior de idade' if idade >= 18 else 'Menor de idade')"
```

 ### 5️⃣ Trabalhando com listas

```
python3 -c "frutas=['maçã','banana','laranja']; print(frutas)"
```

 ### 6️⃣ Loop `for`

```
python3 -c "for fruta in ['maçã','banana','laranja']: print(fruta)"
```

 ### 7️⃣ Gerando números

```
python3 -c "for i in range(1,11): print(i)"
```

 ### 8️⃣ Filtrando números pares

```
python3 -c "print([i for i in range(1,21) if i % 2 == 0])"
```

 ### 9️⃣ Somando valores

```
python3 -c "print(sum([10,20,30,40]))"
```

 ### 🔟 Lendo um arquivo

```
python3 -c "print(open('arquivo.txt').read())"
```

 A partir daqui, o `python3 -c` começa a ficar especialmente interessante para automação.

 ### 1️⃣1️⃣ Contando linhas

```
python3 -c "print(len(open('arquivo.txt').readlines()))"
```

 ### 1️⃣2️⃣ Criando um arquivo

```
python3 -c "open('saida.txt','w').write('Olá do Python!\n')"
```

 ### 1️⃣3️⃣ Procurando uma palavra

```
python3 -c "texto=open('arquivo.txt').read(); print('Python' in texto)"
```

 ### 1️⃣4️⃣ Trabalhando com JSON

```
python3 -c "import json; dados={'nome':'Carlos','idade':35}; print(json.dumps(dados, indent=2))"
```

 ### 1️⃣5️⃣ Lendo um JSON

```
python3 -c "import json; d=json.load(open('dados.json')); print(d['nome'])"
```

 ### 1️⃣6️⃣ Recebendo argumentos do terminal

```
python3 -c "import sys; print(f'Olá, {sys.argv[1]}!')" Maria
```

 Resultado:

```
Olá, Maria!
```

 ### 1️⃣7️⃣ Listando arquivos

```
python3 -c "import os; print('\n'.join(os.listdir('.')))"
```

 ### 1️⃣8️⃣ Executando comandos do sistema

```
python3 -c "import subprocess; subprocess.run(['ls','-lah'])"
```

 Aqui, Python pode atuar como uma ponte para executar comandos do sistema operacional.

 ### 1️⃣9️⃣ Capturando a saída de um comando

```
python3 -c "import subprocess; r=subprocess.run(['uname','-a'], capture_output=True, text=True); print(r.stdout)"
```

 ### 2️⃣0️⃣ Gerando um hash SHA-256

```
python3 -c "import hashlib; print(hashlib.sha256(b'Hello World').hexdigest())"
```

 ## 🚀 Por que usar `python3 -c`?

 Não é uma substituição para scripts Python tradicionais.

 A ideia é outra: resolver tarefas pequenas de forma rápida.

 Por exemplo, imagine que você está trabalhando em um servidor Linux e precisa:

 - verificar rapidamente uma informação;
- manipular um arquivo;
- processar JSON;
- fazer uma pequena conversão;
- testar uma expressão Python;
- executar uma operação matemática;
- automatizar uma tarefa simples;
- integrar Python com comandos do shell.

 Em vez de criar:

```
script.py
```

 você pode executar diretamente:

```
python3 -c "seu código aqui"
```

 ## 💡 Uma dica importante

 Quando o comando começa a ficar muito grande ou complexo, provavelmente é hora de criar um arquivo `.py`.

 O `python3 -c` é excelente para **comandos rápidos**.

 Para lógica complexa, reutilização, testes e manutenção, um script tradicional tende a ser muito mais legível.

 ### Em resumo

 O `python3 -c` transforma o Python em uma ferramenta extremamente prática para o terminal.

 É uma pequena funcionalidade, mas pode ser muito útil para quem trabalha com:

 🐍 Python\
 🐧 Linux\
 ⚙️ DevOps\
 ☁️ Cloud\
 🔧 Automação\
 💻 Desenvolvimento\
 📊 Processamento de dados

 Se você trabalha com terminal diariamente, vale a pena experimentar.

 **Qual desses exemplos você mais usaria no seu dia a dia?**

 #Python #Linux #DevOps #Automação #Programação #Cloud #Desenvolvimento #Terminal #Tecnologia

 Se quiser, posso também transformar esse conteúdo em uma versão **mais “viral” para LinkedIn**, com um título mais forte, storytelling e um gancho inicial para aumentar a retenção.