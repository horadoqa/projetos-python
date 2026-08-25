# Conversa

Projeto simples de comunicação entre **cliente e servidor utilizando sockets TCP em Python**.

## Estrutura

O projeto é composto por dois arquivos principais:

* `server.py` — inicia o servidor, aguarda conexões e recebe as mensagens enviadas pelo cliente.
* `client.py` — conecta-se ao servidor e envia mensagens.

## Como executar

### 1. Inicie o servidor

Execute primeiro:

```bash
python server.py
```

O servidor ficará aguardando uma conexão na porta `9473`.

### 2. Execute o cliente

Em outro terminal:

```bash
python client.py
```

Digite as mensagens quando solicitado pelo cliente.

## Verificar a porta do servidor

Para verificar se o servidor está escutando na porta `9473`, execute:

```bash
ss -ltn | grep 9473
```

Se estiver funcionando, você verá algo semelhante a:

```text
LISTEN 0 1 127.0.0.1:9473 0.0.0.0:*
```

Isso indica que existe um processo escutando na porta `9473`.

## Fluxo da comunicação

```mermaid
flowchart LR
    C["client.py"] -->|"TCP - mensagens"| S["server.py"]
    S --> R["Recebe e exibe<br/>as mensagens"]
```

## Requisitos

* Python 3
* Biblioteca padrão `socket`

Não é necessário instalar nenhuma biblioteca externa para executar o projeto.

## Observação

O servidor deve ser iniciado **antes do cliente**. Caso contrário, o cliente poderá apresentar:

```text
ConnectionRefusedError: [Errno 111] Connection refused
```

Esse erro normalmente significa que não há nenhum servidor aceitando conexões na porta `9473`.
