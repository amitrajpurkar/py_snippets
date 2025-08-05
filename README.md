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


### using UV instead of Poetry
* UV is another package manager for python
* UV is becoming a norm these days (@July-2025)
* on my mac, i added UV using HomeBrew
* understand usage of UV
* get handle to a proper project-structure for python.. Flask-Application offers one
* project structure must include:
  * which files stay in the root-location of project
  * how is src/main and src/test organized
  * what are the standard subfolders under src/main
  * how to tell UV or Vercel or the build file which one is the "bootstrap.py" the main script that starts the application
  * things like that, etc.


### steps for regular usage
* for day to day project usage here are some activities/ tasks that are commonly done
* add / remove dependencies
* add/update dependencies for specific group.
* add new python project less frequently
