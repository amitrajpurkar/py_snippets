# py_snippets
experimenting with python poetry and vscode


## the discovery journey
needed to draw parallels to the java development world.. 
* how do i setup my operating environment, interpreter, the toolset properly so that i can code like a professional python developer
* just writing code snippets in a single script file is NOT ENOUGH
* bringing in CONSISTENCY TO THE PROCESS is the key "driver"

### references/ links
* [setup PyEnv, Poetry and VSCode](https://youtu.be/547Jr26duHQ?si=VHQ0-bZHvfXWHNB-)
* [PyEnv doco](https://github.com/pyenv/pyenv)
* [Poetry doco](https://python-poetry.org/docs/)
* [VS Code Python config](https://code.visualstudio.com/docs/python/environments)

### setup for machine/ operating system :: for Mac-OS
* what system python installation you have.. installation of python via homebrew
* add "PyEnv" to the machine.. using homebrew 
* add list of python interpreters from PyEnv
* update .rc file for your machine's flavor of shell terminal
* add Poetry using pip install... 
* do not add Poetry via homebrew


### setup for each project
* each python project needs a virtual environment
* python virtual environment is equivalent to gradle build config in Java
* Poetry helps to define/ configure virtual environment
* once you have a project folder, setup git-init
* next setup poetry-init
* add python dependencies using poetry
* get poetry environment path and add it to VS Code python environment
* each python project folder needs a ".vscode" folder having setting.json
* we need to synchronize VS code with Poetry for each project.


### steps for regular usage
* for day to day project usage here are some activities/ tasks that are commonly done
* add / remove dependencies
* add/update dependencies for specific group.
* add new python project less frequently
