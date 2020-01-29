# Video Downloader [![Python 3.7x](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-376/)

Video downloader is a desktop application made with Python. The GUI is built using [PyQT5](https://pypi.org/project/PyQt5/). It allows downloading of Youtube Videos and Playlists to the user's system.

## Future Plans
- [ ] download playlists
- [ ] download from from different 
media sources, such as Reddit, Imgur, GifyCat, and more.

## IMPORTANT ! 
As the original pytube is not being maintained we have made the decision to switch to [pytube3](https://github.com/hbmartin/pytube3)

If you're already using the original pytube, please upgrade using.  

```
pip install pytube3 --upgrade
```

or  

```
pip uninstall pytube
pip install pytube3
```
*_If its a new installation of the project, please ignore this session_*

## Prerequisites
- [Python 3.7x](https://www.python.org/downloads/release/python-376/)

## Contributors
* [**Cheryl M / cherylli**](https://github.com/cherylli) - *Project Lead #1*
* [**Jon M / chonix**](https://github.com/chonix) - *Co-Project Lead #1*
* [**Ryan Samman**](https://github.com/RyanSamman) - *Expert beginner*

Please feel free to contact us if you would like to contribute. We also have a discord server for various projects including this.

## Dependencies
- **PyQt5==5.14.1**
- **PyQt5-sip==12.7.0** `extension module provides support for the PyQt5 package`
- [**pytube3**](https://github.com/hbmartin/pytube3) `A lightweight, Pythonic, dependency-free, library for downloading YouTube Videos` - hbmartin forked version from [original pytube](https://github.com/nficano/pytube/tree/master/pytube)

## Dev environment setup:
### Setting up Virtual Environment
#### Install the virtualenv package
```
pip install virtualenv
```
#### Create the virtual environment
```
virtualenv env
```
where <i>env</i> is the name/directory of the virtual environemnt

### Activate the virtual environment

- Mac OS / Linux
```
source env/bin/activate
```

- Windows
```
env\Scripts\activate
```

### Deactivate the virtual environment
```
deactivate
```

### Installing project dependencies
```
pip install requirements.txt
```

### Add project depenencies
```
pip freeze > requirements.txt
```

# Useful guides:
## Getting started with PyQt5
### How to use qt designer
https://www.youtube.com/watch?v=FVpho_UiDAY&t=398s

### Useful stuff for PyQt5
- [https://data-flair.training/blogs/python-pyqt5-tutorial/](https://data-flair.training/blogs/python-pyqt5-tutorial/)

- [Python GUI Development With PyQt5 Introduction & Creating Window #1](https://youtu.be/yD0iu3n-e_s?list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa)

- [PyQt5 Tutorial](https://www.youtube.com/watch?v=_bi0SqW_4L0&list=PLS1QulWo1RIZTkXbVkjr5Z3m-uMs05u7V)

- [https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/](https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/)

## Getting started with PyTube

[Pytube Quickstart](https://python-pytube.readthedocs.io/en/latest/user/quickstart.html)


## License
GNU General Public License v3.0 - 
[https://www.gnu.org/licenses/gpl-3.0.en.html]
