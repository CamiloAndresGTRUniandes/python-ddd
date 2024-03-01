


from dataclasses import dataclass

from seedwork.domain.factory import Factory
from seedwork.domain.repositories import Repository
from modules.property.domain.repositories import PropertyRepository


@dataclass
class ReposirotyFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == PropertyRepository.__class__:
            return RepositorioPropiedadesPostgresSQL()
        else:
            raise ExcepcionFabrica(f"Fallo {obj}")