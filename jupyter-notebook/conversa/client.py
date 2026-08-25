import socket
import threading
from colorama import Fore, Style, init

init(autoreset=True)

HOST = "127.0.0.1"
PORT = 9473


def receber_mensagens(client):
    while True:
        try:
            mensagem = client.recv(1024)

            if not mensagem:
                print("\nServidor desconectou.")
                break

            mensagem = mensagem.decode("utf-8")
            print(f"\n{Fore.BLUE}{Style.BRIGHT}Servidor:{Style.RESET_ALL} {mensagem}")
            print("Cliente: ", end="", flush=True)

        except (ConnectionResetError, ConnectionAbortedError):
            print("\nConexão encerrada pelo servidor.")
            break

        except OSError as erro:
            print(f"\nErro na conexão: {erro}")
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"Conectado ao servidor {HOST}:{PORT}")

        thread = threading.Thread(
            target=receber_mensagens,
            args=(client,),
            daemon=True
        )
        thread.start()

        while True:
            mensagem = input("Cliente: ")

            if mensagem.lower() == "sair":
                break

            client.sendall(mensagem.encode("utf-8"))

    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor.")

    except OSError as erro:
        print(f"Erro: {erro}")

    finally:
        client.close()
        print("Cliente encerrado.")


if __name__ == "__main__":
    main()