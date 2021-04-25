# translator-linux
A simple translator that allows you to translate any text you copy in linux.

# Dependency Steps
Due to the [keyboard](https://pypi.org/project/keyboard/) library, you need to run the python script with sudo privilege, run `sudo -i` for the package installation and then install the following packages.

`pip3 install googletrans==3.1.0a0`

`pip3 install keyboard`

`apt install gxmessage`

`apt install xsel`

# Installation Steps
The script takes 2 parameters. Source language and destination language. In the example below, source language is English and destination language is Turkish. ([See other languages](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages))

`python3 translate.py en tr &`

Do not forget to run script with sudo privilege.

# Usage
After copying any text on your computer, you can get the translation result by pressing the `q` button.

If you want to use a button other than q, change the part below in translate.py.
```python
keyboard.wait('q')
```

Check out the [keyboard](https://pypi.org/project/keyboard/) library for buttons.
