from .filmes import filmes
from .animes import Animes
from .jogos import Jogos
from .livros import Livros
from .mangas import Mangas
from .seriados import Seriados

# Only export the concrete classes users should instantiate
__all__ = ["filmes", "Animes", "Jogos", "Livros", "Mangas", "Seriados"]