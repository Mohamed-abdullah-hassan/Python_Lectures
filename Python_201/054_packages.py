#Importing colorama and Virtual Enviroment
#From Video #54

#using information from https://pypi.org/ about colorama package
#Then activating Venv to install it locally

from colorama import init
init()


from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')