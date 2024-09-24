## UV

- Instalação:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

 - Ambiente:
```sh
source $HOME/.cargo/env
```

- Criar projeto do zero:
```sh
uv init example
```

- Rodar aplicativos python sem precisar instalar:
```sh
uvx pycowsay hello
```

- Instalar ferramentas dentro do uv para poder ser usada em qualquer ambiente:
```sh
uv tool install flake8
```

- Roda a ferramenta instalada no UV na aplicação local:
```sh
uv run flake8 hello.py 
```

- Instala nova versão do python dentro do uv:
```sh
uv python install 3.10
```

- Cria ambiente virtual com o python selecionado:
```
uv venv --python 3.10
```

- Adiciona bibliotecas:
```sh
uv add pandas
```

- Ajusta as bibliotecas a partir de um arquivo requirements.txt
```sh
uv pip install -r requirements.txt
```

- Compila um arquivo de requirements.
```sh
uv pip compile requirements.txt
```

- Roda um script que possui dependências sem precisar de um requirements.txt, de ter um venv, container ou de instalar no python local
```sh
uv run --with rich script.py
```

- Adiciona bibliotecas no corpo do script para ser executada com uv run
```sh
uv add --script script.py "dynaconf" "rich"
```
Para rodar use run, que ele instala temporariamente as dependências necessárias que foram inseridas no arquivo .py

```sh
uv run script.py
```
