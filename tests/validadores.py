"""Validadores de dados brasileiros: CPF, CNPJ, e-mail e telefone."""
import re


def _so_digitos(valor) -> str:
    if not isinstance(valor, str):
        return ""
    return re.sub(r"\D", "", valor)


def validar_cpf(cpf) -> bool:
    n = _so_digitos(cpf)
    if len(n) != 11 or n == n[0] * 11:
        return False
    for i in (9, 10):
        soma = sum(int(n[j]) * (i + 1 - j) for j in range(i))
        digito = (soma * 10) % 11 % 10
        if digito != int(n[i]):
            return False
    return True


def validar_cnpj(cnpj) -> bool:
    n = _so_digitos(cnpj)
    if len(n) != 14 or n == n[0] * 14:
        return False
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1
    for pesos, pos in ((pesos1, 12), (pesos2, 13)):
        soma = sum(int(d) * p for d, p in zip(n[:pos], pesos))
        resto = soma % 11
        digito = 0 if resto < 2 else 11 - resto
        if digito != int(n[pos]):
            return False
    return True


def validar_email(email) -> bool:
    if not isinstance(email, str):
        return False
    email = email.strip()
    if ".." in email:
        return False
    return re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", email) is not None


def validar_telefone(telefone) -> bool:
    n = _so_digitos(telefone)
    if len(n) in (12, 13) and n.startswith("55"):
        n = n[2:]
    if len(n) not in (10, 11):
        return False
    if int(n[:2]) < 11:  # DDD válido: 11 a 99
        return False
    if len(n) == 11:  # celular
        return n[2] == "9"
    return n[2] in "2345"  # fixo