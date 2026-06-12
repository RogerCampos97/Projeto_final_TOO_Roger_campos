from .midia import Midia
from .factory_midia import factory_Midia

def nova_midia(titulo: str, tipo: str):
        '''
        aqui logica que define qual tipo de midia vai ser criada
            Args: titulo
            Returns: objeto do tipo midia ou erro caso tipo inválido
        '''
        tipo = tipo.strip().lower()
        match tipo:
            case "anime":
                midia = criar_Anime(titulo).factory_midia(titulo)
            case "jogo":
                midia = criar_Jogo(titulo).factory_midia(titulo)
            case "livro":
                midia = criar_livro(titulo).factory_midia(titulo)
            case "mangá" | "manga":
                midia = criar_Manga(titulo).factory_midia(titulo)
            case "filme":
                midia = criar_filme(titulo).factory_midia(titulo)
            case "seriado" | "seriados":
                midia = criar_seriados(titulo).factory_midia(titulo)
            case _:
                raise Exception("Não foi possivel criar Midia")
        return midia



obj = nova_midia("teste", "anime")
print(obj.get_nome())




#-------------------------------------------------------------- 
#                   Anime
# -------------------------------------------------------------
class criar_Anime(factory_Midia): 
    # classe concreta usada pelo factory para criar o objeto Anime
    def factory_midia(self, titulo) -> Midia:
        return Anime(titulo)
    
class Anime(Midia):
    def __init__(self, titulo: str): 
        # caso não tiver nenhum atributo a mais ou algum codigo 
        # a ser feito na inicialização posso omitir o init, 
        # é usado o da classe abstrata
        super().__init__(titulo)
    def get_nome(self) -> str:
        return "Anime"
    def __eq__(self, outro:object):
        if not isinstance(outro, Anime):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Jogo
# ------------------------------------------------------------- 
class criar_Jogo(factory_Midia): 
    # classe concreta usada pelo factory para criar o objeto Anime
    def factory_midia(self, titulo) -> Midia:
        return Jogo(titulo)

class Jogo(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Jogo"
    def __eq__(self, outro:object):
        if not isinstance(outro, Jogo):
                return False
        return (self.titulo == outro.titulo)
    
#-------------------------------------------------------------- 
#                   Livro
# ------------------------------------------------------------- 
class criar_livro(factory_Midia):
    def factory_midia(self, titulo) -> Midia:
        return Livro(titulo)
    
class Livro(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Livro"
    def __eq__(self, outro:object):
        if not isinstance(outro, Livro):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Mangá
# -------------------------------------------------------------  
class criar_Manga(factory_Midia):
    def factory_midia(self, titulo) -> Midia:
        return Manga(titulo)
    
class Manga(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Mangá"
    def __eq__(self, outro:object):
        if not isinstance(outro, Manga):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Filme
# ------------------------------------------------------------- 
class criar_filme(factory_Midia):
    def factory_midia(self, titulo) -> Midia:
        return filme(titulo)
    
class filme(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Filme"
    def __eq__(self, outro:object):
        if not isinstance(outro, filme):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Sériados
# ------------------------------------------------------------- 
class criar_seriados(factory_Midia):
    def factory_midia(self, titulo) -> Midia:
        return Seriado(titulo)
    
class Seriado(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Seriados"
    def __eq__(self, outro:object):
        if not isinstance(outro, Seriado):
                return False
        return (self.titulo == outro.titulo)
    


#obg  = factory_Midia.nova_midia("teste")