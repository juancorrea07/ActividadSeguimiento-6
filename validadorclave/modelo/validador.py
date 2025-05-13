from abc import ABC, abstractmethod
from .errores import (
    NoCumpleLongitudMinimaError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTieneCaracterEspecialError,
    NoTienePalabraSecretaError
)
class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave):
        return any(c in "@_#$%" for c in clave)

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos un carácter especial (@, _, #, $ o %)")
        return True

