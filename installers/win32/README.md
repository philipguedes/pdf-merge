# Usage
## Pynsist
Run this command from project root folder
```zsh
$ python -m nsist win32installer.cfg
```


Official docs for **pynsist** module can be found [here](http://pynsist.readthedocs.io/en/latest/index.html)

## Notes
Currently, the **pynsist** module has few problems to create a *working* windows installer for **tkinter** applications.

The workaround described here may work in regular cases. 

If you have any trouble, please refer to [pynsist issue page](https://github.com/takluyver/pynsist/issues/)

## Workaround
> The original post can be found [here](https://github.com/takluyver/pynsist/issues/124)

First of all, find your python main dir. Let's call it `${PYTHON_MAIN_DIR}`.
1. These files need to be placed into the `installers/win32` folder:

    ``tcl86t.dll`` 
    
    ``tk86t.dll``

    They can be found under at `${PYTHON_MAIN_DIR}/DLLs`
2.  Copy all the contents of `${PYTHON_MAIN_DIR}/tcl/` into `installers/win32/lib/`
