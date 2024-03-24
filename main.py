#
# author : Meryem Afife Keskin / rgwO9w
# 

from simple_term_menu import TerminalMenu


print("Select your chef")

chefs_dict = {"Old Turkish Woman Chef":"Old_Turkish_Woman_Chef.py","Bartender":"Bartender.py","Italian Pizza Chef":"Italian_Pizza_Chef.py"}
options = list(chefs_dict.keys())

terminal_menu = TerminalMenu(options)
menu_entry_index = terminal_menu.show()


with open(chefs_dict[options[menu_entry_index]]) as file:
    exec(file.read())

