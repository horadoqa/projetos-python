from colorama import Fore, Style, init

init(autoreset=True)

# Larguras das colunas
codigo = 8
categoria = 25
descricao = 30

linha = (
    "+"
    + "-" * codigo
    + "+"
    + "-" * categoria
    + "+"
    + "-" * descricao
    + "+"
)

print(Fore.CYAN + "=" * (codigo + categoria + descricao + 4))
print(Fore.CYAN + "                 HTTP STATUS CODES")
print(Fore.CYAN + "=" * (codigo + categoria + descricao + 4))

print(Fore.WHITE + linha)

print(
    Fore.WHITE
    + f"| {'CÓDIGO':<{codigo-1}}"
    + f"| {'CATEGORIA':<{categoria-1}}"
    + f"| {'DESCRIÇÃO':<{descricao-1}}|"
)

print(Fore.WHITE + linha)

# 2xx
print(
    Fore.GREEN
    + f"| {'200':<{codigo-1}}"
    + f"| {'2xx - Sucesso':<{categoria-1}}"
    + f"| {'OK':<{descricao-1}}|"
)

print(
    Fore.GREEN
    + f"| {'201':<{codigo-1}}"
    + f"| {'2xx - Sucesso':<{categoria-1}}"
    + f"| {'Created':<{descricao-1}}|"
)

print(
    Fore.GREEN
    + f"| {'204':<{codigo-1}}"
    + f"| {'2xx - Sucesso':<{categoria-1}}"
    + f"| {'No Content':<{descricao-1}}|"
)

print(Fore.WHITE + linha)

# 3xx
print(
    Fore.YELLOW
    + f"| {'301':<{codigo-1}}"
    + f"| {'3xx - Redirecionamento':<{categoria-1}}"
    + f"| {'Moved Permanently':<{descricao-1}}|"
)

print(
    Fore.YELLOW
    + f"| {'302':<{codigo-1}}"
    + f"| {'3xx - Redirecionamento':<{categoria-1}}"
    + f"| {'Found':<{descricao-1}}|"
)

print(
    Fore.YELLOW
    + f"| {'304':<{codigo-1}}"
    + f"| {'3xx - Redirecionamento':<{categoria-1}}"
    + f"| {'Not Modified':<{descricao-1}}|"
)

print(Fore.WHITE + linha)

# 4xx
print(
    Fore.RED
    + f"| {'400':<{codigo-1}}"
    + f"| {'4xx - Erro do Cliente':<{categoria-1}}"
    + f"| {'Bad Request':<{descricao-1}}|"
)

print(
    Fore.RED
    + f"| {'401':<{codigo-1}}"
    + f"| {'4xx - Erro do Cliente':<{categoria-1}}"
    + f"| {'Unauthorized':<{descricao-1}}|"
)

print(
    Fore.RED
    + f"| {'403':<{codigo-1}}"
    + f"| {'4xx - Erro do Cliente':<{categoria-1}}"
    + f"| {'Forbidden':<{descricao-1}}|"
)

print(
    Fore.RED
    + f"| {'404':<{codigo-1}}"
    + f"| {'4xx - Erro do Cliente':<{categoria-1}}"
    + f"| {'Not Found':<{descricao-1}}|"
)

print(
    Fore.RED
    + f"| {'405':<{codigo-1}}"
    + f"| {'4xx - Erro do Cliente':<{categoria-1}}"
    + f"| {'Method Not Allowed':<{descricao-1}}|"
)

print(
    Fore.RED
    + f"| {'429':<{codigo-1}}"
    + f"| {'4xx - Erro do Cliente':<{categoria-1}}"
    + f"| {'Too Many Requests':<{descricao-1}}|"
)

print(Fore.WHITE + linha)

# 5xx
print(
    Fore.MAGENTA
    + f"| {'500':<{codigo-1}}"
    + f"| {'5xx - Erro do Servidor':<{categoria-1}}"
    + f"| {'Internal Server Error':<{descricao-1}}|"
)

print(
    Fore.MAGENTA
    + f"| {'502':<{codigo-1}}"
    + f"| {'5xx - Erro do Servidor':<{categoria-1}}"
    + f"| {'Bad Gateway':<{descricao-1}}|"
)

print(
    Fore.MAGENTA
    + f"| {'503':<{codigo-1}}"
    + f"| {'5xx - Erro do Servidor':<{categoria-1}}"
    + f"| {'Service Unavailable':<{descricao-1}}|"
)

print(
    Fore.MAGENTA
    + f"| {'504':<{codigo-1}}"
    + f"| {'5xx - Erro do Servidor':<{categoria-1}}"
    + f"| {'Gateway Timeout':<{descricao-1}}|"
)

print(Fore.WHITE + linha)

print(Fore.CYAN + "=" * (codigo + categoria + descricao + 4))
print(Fore.CYAN + "                    FIM")
print(Fore.CYAN + "=" * (codigo + categoria + descricao + 4))