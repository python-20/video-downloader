# youtube-video-downloader

# Getting started with PyQt5
## How to use qt designer
https://www.youtube.com/watch?v=FVpho_UiDAY&t=398s

## Useful stuff for PyQt5
- https://data-flair.training/blogs/python-pyqt5-tutorial/

- [Python GUI Development With PyQt5 Introduction & Creating Window #1](https://youtu.be/yD0iu3n-e_s?list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa)

- [PyQt5 Tutorial](https://www.youtube.com/watch?v=_bi0SqW_4L0&list=PLS1QulWo1RIZTkXbVkjr5Z3m-uMs05u7V)

- https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/

# Getting started with PyTube

[Pytube Quickstart](https://python-pytube.readthedocs.io/en/latest/user/quickstart.html)

[Pytube github repository](https://github.com/nficano/pytube)

# Current Bug and fix
### (KeyError: 'url_encoded_fmt_stream_map')

[Fix](https://github.com/nficano/pytube/pull/537/files/bceb929e143caadd874955fa422f8a58955bafaf)

[Issue] (https://github.com/python-20/video-downloader/issues/7)

# Setting up Virtual Environment
## Install the virtualenv package
```
pip install virtualenv
```
## Create the virtual environment
```
virtualenv env
```
where env is the name/directory of the virtual environemnt

## Activate the virtual environment

- Mac OS / Linux

```
source env/bin/activate
```

- Windows
```
env\Scripts\activate
```

## Deactivate the virtual environment
```
deactivate
```

## Installing project dependencies
```
pip install requirements.txt
```

## Add project depenencies
```
pip freeze > requirements.txt.
```