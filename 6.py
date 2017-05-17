import json
from Tkinter import *


# UI Class
class CityInformation:
    # Constructor
    def __init__(self, master, file_name):
        city_info_file = open(file_name, "r")
        city_info = json.loads(city_info_file.read())
        city_info_file.close()

        options = []
        for x in city_info:
            options.append(x['name'])
        options.sort()

        variable = StringVar(master)
        variable.set(options[0])  # default value
        city_picker = apply(OptionMenu, (master, variable) + tuple(options))

        master.wm_title("City Information")
        city_label = Label(master, text="City")
        county_label = Label(master, text="County")
        latitude_label = Label(master, text="Latitude")
        longitude_label = Label(master, text="Longitude")
        county_value = Entry(master, width=40)
        latitude_value = Entry(master, width=40)
        longitude_values = Entry(master, width=40)

        city_label.grid(row=0, column=0, sticky=W)
        county_label.grid(row=1, column=0, sticky=W)
        latitude_label.grid(row=2, column=0, sticky=W)
        longitude_label.grid(row=3, column=0, sticky=W)
        city_picker.grid(row=0, column=1, sticky=EW)
        county_value.grid(row=1, column=1)
        latitude_value.grid(row=2, column=1)
        longitude_values.grid(row=3, column=1)


root = Tk()
ci = CityInformation(root, "ca.json")
root.mainloop()
