Instalação:
curl -LsSf https://astral.sh/uv/install.sh | sh

Ambiente:
source $HOME/.cargo/env

Criar projeto do zero:
uv init example

Rodar aplicativos python sem precisar instalar:
uvx pycowsay hello

Instalar ferramentas dentro do uv para poder ser usada em qualquer ambiente:
uv tool install flake8
Roda a ferramenta instalada no UV na aplicação local:
uv run flake8 hello.py 

Instala nova versão do python dentro do uv:
uv python install 3.10

Cria ambiente virtual com o python selecionado:
uv venv --python 3.10

Adiciona bibliotecas:
uv add pandas

Ajusta as bibliotecas a partir de um arquivo requirements.txt
uv pip install -r requirements.txt

Compila um arquivo de requirements.
uv pip compile requirements.txt


Roda um script que possui dependências sem precisar de um requirements.txt, de ter um venv, container ou de instalar no python local
uv run --with rich script.py

Adiciona bibliotecas no corpo do script para ser executada com uv run
uv add --script script.py "dynaconf" "rich"
Para rodar use run, que ele instala temporariamente as dependências necessárias que foram inseridas no arquivo .py
uv run script.py
