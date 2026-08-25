import socket
import threading
from colorama import Fore, Style, init

init(autoreset=True)

HOST = "127.0.0.1"
PORT = 9473


def receber_mensagens(conn):
    while True:
        try:
            mensagem = conn.recv(1024)

            if not mensagem:
                print("\nCliente desconectou.")
                break

            mensagem = mensagem.decode("utf-8")
            print(f"\n{Fore.GREEN}Cliente:{Style.RESET_ALL} {mensagem}")
            print("Servidor: ", end="", flush=True)

        except (ConnectionResetError, ConnectionAbortedError):
            print("\nConexão encerrada pelo cliente.")
            break

        except OSError as erro:
            print(f"\nErro na conexão: {erro}")
            break

    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reutilizar a porta rapidamente após reiniciar o servidor
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Servidor iniciado em {HOST}:{PORT}")
    print("Aguardando conexão...")

    conn, addr = server.accept()

    print(f"Cliente conectado: {addr[0]}:{addr[1]}")

    thread = threading.Thread(
        target=receber_mensagens,
        args=(conn,),
        daemon=True
    )
    thread.start()

    try:
        while True:
            resposta = input("Servidor: ")

            if resposta.lower() == "sair":
                break

            conn.sendall(resposta.encode("utf-8"))

    except (BrokenPipeError, ConnectionResetError):
        print("\nCliente desconectou.")

    finally:
        conn.close()
        server.close()
        print("Servidor encerrado.")


if __name__ == "__main__":
    main()