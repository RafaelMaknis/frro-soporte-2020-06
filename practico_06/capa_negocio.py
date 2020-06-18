# Implementar los metodos de la capa de negocio de socios.

from ..practico_05.ejercicio_01 import Socio
from ..practico_05.ejercicio_02 import DatosSocio
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class DniRepetido(Exception):
    print("".format(Exception+"  - El DNI ya se encuentra ingresado para otro cliente, verifique."))
    return None


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        socio = datos.buscar(id_socio)
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return socio

    def buscar_dni(self, dni_socio):
        socio = datos.buscar_dni(dni_socio)
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return socio

    def todos(self):
        socios_lista = datos.todos()
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return socios_lista

    def alta(self, socio):
        if not regla_1(socio):
            return False
        if not regla_2(socio):
            return False
        if not regla_3(socio):
            return False

        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return False

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        return False

    def regla_1(self, socio):
        dni = socio.dni
        try:
            socio = datos.buscar_dni(dni)
            if socio is not None:
                raise DniRepetido(e)
                return False

        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        return False

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        return False
