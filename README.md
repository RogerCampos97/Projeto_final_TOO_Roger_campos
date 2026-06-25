# Projeto_final_TOO_Roger_campos
Trabalho final disciplina Técnologia de Orienteção a objetos

## Descrição do tema e objetivo do projeto

    O tema do trabalho é: Sistema de Gerenciamento de Biblioteca Pessoal
    O objetivo é criar um sistema para gerenciar midias de vários tipos que um usuario pode controlar, atualizar, deletar, etc.


## Diagrama de classes (inserido como imagem ou link)

    - local do diagrama de classes: doc\classes UML.pdf

## Descrição de cada classe e pilar da POO utilizado

    - Factory: src\models\factory_midia.py
    - State: src\models\estado_midia.py
    - singleton: src\controllers\controller_categorias.py

## Explicação dos padrões de projeto aplicados (Factory e o adicional)
- State: aplicado na classe midia para mudar o estado atravez do estado_contexto sem precisar de uma implementacao de estado em midia
- Factoty: aplicado com uma classe abstrata de factory e uma concreta de cada tipo de midia, além de um metodo adicional para receber os dados para cada midia.
- Singleton:  para garantir que só exista uma instancia ativa do controlador das categorias de mídia, foi usado o padrão singleton que impede que outros controladores que por ventura sejam criados sejam o mesmo controlador.

## Instruções para execução e testes do sistema.
* O sistema pode ser testado usando o pytest (ver arquivo testagem em doc)
* Também pode ser testado só rodando os arquivos 
* Para rodar o sistema basta rodara o arquivo run.py na pasta raiz ou ir para o arquivo em src\views\menu_principal.py
## Detalhamento de Aprendizado
* Dataclasses como uma alternativa para dados mais rápida
* estruturas do projeto e testagem com pytest
* uso do venv
* uso de dicionarios para criar objetos ou definir algo especifico sem precisar de muitos ifs
### Dificuldades Encontradas: 
* dificuldades na implementação do Padrão State
    - Como resolvi: pesquisei termos que vi no site refactoring guru no google e gemini até eu conseguir compreender como poderia fazer as trocas de estado de forma correta e sem precisar importar a midia, usando o padrão state.
* problemas nos imports, onde usando o isinstance mesmo sendo o mensmo tipo acusava diferente
    - Como resolvi: mudando todos os imports para iguais (pela importação relativa o python cria objetos diferentes se o estilo do import for diferente (relativo vs absoluto))

### Principal Aprendizado:
* A estruturação do projeto acho que é o que foi mais importante

## Declaração de Uso de IA

(Prática comum de transparência acadêmica e profissional no GitHub)

[ ] Nenhuma IA foi utilizada na elaboração deste código.

[X] Utilizei IA como ferramenta de apoio.

Ferramenta(s): gemini pro, Duck ai
Finalidade: 

* ajuda na idealização inicial das classes (apenas auxilio inicial)
* ajuda na criação do padrão state (retirada de duvidas baseado no site [padrão state e class context](https://refactoring.guru/design-patterns/state/python/example))
* ajuda na criacão do menu.py em src\views\menu.py com o menu sendo gerado inicialmente e adaptado para simplifcar / permitir outros detalhes
* ajuda na retirada de erros pontuais onde não conseguiria resolver em tempo hábil

Validação: Declaro que todo o código gerado foi lido, testado e e ajustado conforme as necessidades específicas do projeto e da disciplina. A responsabilidade pela arquitetura, decisões de design e correção do código é de minha total responsabilidade.