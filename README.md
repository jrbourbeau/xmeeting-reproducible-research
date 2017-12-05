# Reproducible Research with Python

Repository for "Reproducible Research with Python" X-meeting talk at WIPAC. Slides can be found [here](slides.pdf).

## Installation

It's recommended to install the dependencies for this project into a virtual Python environment. Virtual environments can be created with two different methods, depending on which version of Python you're using.

1. Using the Python 3 `venv` module
    ```bash
    $ python3 -m venv ~/.venvs/xmeeting-reproducible-research
    $ source ~/.venvs/xmeeting-reproducible-research/bin/activate
    (xmeeting-reproducible-research) $
    ```

2. Using the `virtualenv` package (for Python 2)
    ```bash
    $ pip install virtualenv
    $ virtualenv ~/.venvs/xmeeting-reproducible-research
    $ source ~/.venvs/xmeeting-reproducible-research/bin/activate
    (xmeeting-reproducible-research) $
    ```

To install the example Python package, `expackage`, run

```bash
pip install expackage
```

from inside the `xmeeting-reproducible-research` repository.


## Additional resources

- David Beazley's "Modules and Packages:
Live and Let Die!" talk @ PyCon 2015 [[youtube](https://www.youtube.com/watch?v=0oTh1CXRaQ0)] [[slides](http://www.dabeaz.com/modulepackage/ModulePackage.pdf)]

- David Baumgold's "Get Started With Git" talk @ PyCon 2016 [[youtube](https://www.youtube.com/watch?v=RrdECLvHW6g)] [[slides](https://speakerdeck.com/singingwolfboy/get-started-with-git)]

- How To Package Your Python Code tutorial http://python-packaging.readthedocs.io
