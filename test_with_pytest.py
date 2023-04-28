import prvni_pokus
import pytest
from io import StringIO


def test_is_even():
    assert prvni_pokus.is_even(4)
    assert not prvni_pokus.is_even(5)
    assert prvni_pokus.is_even(0)
    assert prvni_pokus.is_even(-4)
    assert not prvni_pokus.is_even(-5)


def test_check_entry():
    assert prvni_pokus.check_entry("1234") == 1234
    with pytest.raises(ValueError, match="Zadaná hodnota není číslo."):
        prvni_pokus.check_entry("cokoliv")


def test_chentry(monkeypatch):
    number_inputs = StringIO('1234\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert prvni_pokus.chentry() == 1234
