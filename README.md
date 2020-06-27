# template-pyqt5
template for pyqt5 apps


## Prepare develop environment with anaconda

Create and active environment.

`conda create -n env_name python=3.7`

`conda activate env_name`

Install PyQt5

`conda install -c anaconda pyqt`


## Mandatory folders and files

- .ui: ui files generated with qt designer
- .icons/icons.qrc: resource file with all icons, generated with qt designer
- .app: your code
- ./devtool-convert_ui_files.sh - script to prepare our project:
    - Convert ui files to python code and copy into 'app/ui'
    - generate translation files and copy into 'app/i18n' (prepared to use with linguist)
    - convert icons.qrc file to python code and copy into app folder
