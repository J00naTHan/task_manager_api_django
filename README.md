# API RESTful em Django para Gerenciamento de Tarefas

## Tutorial para Trabalhar Localmente no Projeto

Para participar no desenvolvimento desse projeto, comece usando o comando `git clone https://github.com/J00naTHan/task_manager_api_django.git` pelo *Git* no seu terminal de preferência. Caso o projeto já esteja clonado em seu computador, você pode atualizar seu código para a versão atual com o código `git pull origin <branch de destino>`.

Em seguida, você deve ter instalado em seu PC o *Python* e o *PIP* (instalador de pacotes oficial da linguagem). Você deve executar o comando `python -m venv <nome-do-ambiente-virtual>` para criar um ambiente virtual com nome de sua escolha usando a biblioteca nativa do *Python* para criação e manipulação de ambientes virtuais. Após criar seu ambiente virtual, você pode usar o comando `venv\Scripts\activate` no terminal de sua preferência para iniciar o ambiente virtual na pasta raiz do seu projeto.

O ambiente virtual facilita a instalação das dependências do projeto, como o *framework Django*, entre outros. Para fazer essa instalação, você pode usar o comando `pip install -r requirements.txt` para instalar automaticamente as dependências (lembre-se de fazer isso estando com o ambiente virtual ativado, para que essas dependências não ocupem memória do seu computador).

Algumas informações importantes do projeto são sensíveis e não podem estar disponíveis para a visualização de qualquer pessoa (*secrets*), essas informações estarão em um arquivo **.env**, que pode ser disponibilizado individual e manualmente.
