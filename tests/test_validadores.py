import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from validadores import validar_cnpj, validar_cpf, validar_email, validar_telefone


@pytest.mark.parametrize("cpf", ["529.982.247-25", "52998224725"])
def test_cpf_valido(cpf):
    assert validar_cpf(cpf) is True


@pytest.mark.parametrize(
    "cpf",
    ["529.982.247-26", "111.111.111-11", "123", "", "abc.def.ghi-jk", None, 52998224725],
)
def test_cpf_invalido(cpf):
    assert validar_cpf(cpf) is False


@pytest.mark.parametrize("cnpj", ["11.222.333/0001-81", "11222333000181"])
def test_cnpj_valido(cnpj):
    assert validar_cnpj(cnpj) is True


@pytest.mark.parametrize(
    "cnpj", ["11.222.333/0001-82", "00000000000000", "123", "", None]
)
def test_cnpj_invalido(cnpj):
    assert validar_cnpj(cnpj) is False


@pytest.mark.parametrize(
    "email", ["angel@email.com", "a.b+tag@dominio.com.br", "  x@y.co  "]
)
def test_email_valido(email):
    assert validar_email(email) is True


@pytest.mark.parametrize(
    "email", ["", "semarroba.com", "a@b", "a@@b.com", "a..b@c.com", "@c.com", None]
)
def test_email_invalido(email):
    assert validar_email(email) is False


@pytest.mark.parametrize(
    "tel",
    ["(92) 99123-4567", "92991234567", "+55 92 99123-4567", "(92) 3234-5678"],
)
def test_telefone_valido(tel):
    assert validar_telefone(tel) is True


@pytest.mark.parametrize(
    "tel", ["", "12345", "(92) 89123-4567", "(05) 99123-4567", "(92) 1234-5678", None]
)
def test_telefone_invalido(tel):
    assert validar_telefone(tel) is False
    