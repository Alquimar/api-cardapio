from core.models import AbstractModel


class Estabelecimento(AbstractModel):
    def __str__(self) -> str:
        return super().nome
