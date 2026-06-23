from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

'''
@dataclass -> classe de dados
'''
@dataclass
class Info_data:
    data_inclusao: datetime = field(default=datetime.now())
    data_atualizado: datetime = field(default=datetime.now())
    data_concluido: Optional[datetime] = field(default= None)

    def atualizar_data(self):
        self.data_atualizado = datetime.now()

    def concluir(self):
        self.data_concluido = datetime.now()
    
    @staticmethod
    def formatar_data(data: datetime):
        return data.strftime("%d/%m/%Y %H:%M:%S")
    
    @staticmethod
    def calcular_intervalo_entre_datas(final: datetime, primeira: datetime):
        intervalo = final - primeira
        total_segundos = int(intervalo.total_seconds())
        dias = total_segundos // 86400
        horas = (total_segundos % 86400) // 3600
        minutos = (total_segundos % 3600) // 60
        segundos = total_segundos % 60
        tempo_completo = f"{dias}d {horas:02d}:{minutos:02d}:{segundos:02d}"
        return(f": {tempo_completo}")
    

    def calcular_inervalo_inclusao(self) -> str:
        return Info_data.calcular_intervalo_entre_datas(datetime.now(), self.data_inclusao)
    
    def calcular_tempo_desde_conclusao(self):
        if self.data_concluido:
            return Info_data.calcular_intervalo_entre_datas(self.data_concluido, self.data_inclusao)
        else:
            return "sem data de conclusão"
        
    def calcular_tempo_desde_ultimo_update(self):
        return Info_data.calcular_intervalo_entre_datas(datetime.now(), self.data_atualizado)
    
    def retorna_todas_datas_formatadas(self):
        return (f"Data Inclusão: {self.formatar_data(self.data_inclusao)}\n"
                f"Data Atualizado: {self.formatar_data(self.data_atualizado)}\n"
                f"Data Concluido: {self.formatar_data(self.data_concluido) if self.data_concluido is not None else "[Incompleto]"}")
