# Requirements

  * Python 3.8
  * Sqlalchemy
  * Pandas

> This code makes use of the `f"..."` or [f-string
> syntax](https://www.python.org/dev/peps/pep-0498/). This syntax was
> introduced in Python 3.6.

# The *.env* file
**See the *.env* file after following the next steps**
### The environment variables are:
1. PATH_DATA -- absolute path to directory containing the .csv file
2. FILE_NAME -- name of the .csv file to read

# Sample Execution & Output

You can run the `main.py` file without passing any argument, using

```
python main.py
```

the following packages are required to run this application

```
sqlalchemy==1.4.41
pandas==1.5.0
```

Download this packages by using `pip install <package-name>`
or `conda install <package-name>`
or even better:
1. Make sure *Python 3.8* is installed on your machine;
2. Install [pipenv](https://pypi.org/project/pipenv/): `pip install pipenv`
3. Configure pipenv by following this [tutorial](https://www.pythontutorial.net/python-basics/install-pipenv-windows/);
4. Check if all packages required are described in *Pipfile.lock*;
5. Once with *pipenv* installed:
```
pipenv shell # to enter or create the environment
pipenv install # needed just for the first time you use the pipenv shell
```

!Notice
**Always run the command *pipenv shell* after running the script *py main.py***

*Take care!*
