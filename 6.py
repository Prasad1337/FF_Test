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

        # Event handler for OptionMenu
        def picker_update(*args):
            for x in city_info:
                if city_picker_variable.get() == x['name']:
                    county_value.delete(0, END)
                    latitude_value.delete(0, END)
                    longitude_value.delete(0, END)
                    county_value.insert(0, x['full_county_name'])
                    latitude_value.insert(0, x['primary_latitude'])
                    longitude_value.insert(0, x['primary_longitude'])
                    break

        city_picker_variable = StringVar(master)
        city_picker_variable.set("")  # default value
        city_picker = apply(OptionMenu, (master, city_picker_variable) + tuple(options))
        city_picker_variable.trace('w', picker_update)

        master.wm_title("City Information")
        city_label = Label(master, text="City")
        county_label = Label(master, text="County")
        latitude_label = Label(master, text="Latitude")
        longitude_label = Label(master, text="Longitude")
        county_value = Entry(master, width=40)
        latitude_value = Entry(master, width=40)
        longitude_value = Entry(master, width=40)

        city_label.grid(row=0, column=0, sticky=W)
        county_label.grid(row=1, column=0, sticky=W)
        latitude_label.grid(row=2, column=0, sticky=W)
        longitude_label.grid(row=3, column=0, sticky=W)
        city_picker.grid(row=0, column=1, sticky=EW)
        county_value.grid(row=1, column=1)
        latitude_value.grid(row=2, column=1)
        longitude_value.grid(row=3, column=1)


root = Tk()
ci = CityInformation(root, "ca.json")
root.mainloop()
