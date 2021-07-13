from core.models import AbstractModel


class Restaurante(AbstractModel):
    def __str__(self) -> str:
        return super().__str__(self.nome)
