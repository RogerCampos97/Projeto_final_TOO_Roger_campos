from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Info_data:
    data_concluido: datetime | None = field(default= None)
    data_inclusao: datetime = field(default=datetime.now())
    data_atualizado: datetime = field(default=datetime.now())
        
    def atualizar_data(self):
        self.data_atualizado = datetime.now()
    def concluir(self):
        self.data_concluido = datetime.now()