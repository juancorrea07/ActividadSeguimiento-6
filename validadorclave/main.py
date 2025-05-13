

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
            raise ErrorValidacionGanimedes("La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise ErrorValidacionGanimedes("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise ErrorValidacionGanimedes("La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise ErrorValidacionGanimedes("La clave debe contener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise ErrorValidacionGanimedes("La clave debe contener al menos un carácter especial (@, _, #, $ o %)")
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave):
        clave_lower = clave.lower()
        if "calisto" not in clave_lower:
            return False

        # Extraer la parte que contiene "calisto" para validarla
        index = clave_lower.find("calisto")
        palabra_original = clave[index:index + 7]

        mayus = sum(1 for c in palabra_original if c.isupper())
        if mayus >= 2 and mayus < 7:
            return True
        return False

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise ErrorValidacionCalisto("La clave debe tener una longitud de más de 6 caracteres")
        if not self._contiene_numero(clave):
            raise ErrorValidacionCalisto("La clave debe contener al menos un número")
        if not self.contiene_calisto(clave):
            raise ErrorValidacionCalisto("La palabra calisto debe estar escrita con al menos dos letras en mayúscula")
        return True


class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
