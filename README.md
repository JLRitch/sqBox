## sqBox
This is a basic Python package layout implementing possibly rectangular squares and a slew of other misnomers.
Use it for a basic package template or to introduce newer Python programmers to packages and classes.

## Install Instructions
```
python -m pip install git+https://github.com/JLRitch/sqBox.git@master
```

## Update and Modification
Modify any code contained in this package and use setuptools/wheel to rebuild distributions

```
# install the latest versions of these packages
python3 -m pip install --user --upgrade setuptools wheel

# run this command to build the dist files
python3 setup.py sdist bdist_wheel
```