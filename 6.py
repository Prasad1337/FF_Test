import Tkinter
import json


# UI Class
class CityInformation:
    # Constructor
    def __init__(self, master):
        city_info_file = open("ca.json", "r")
        

        master.wm_title("City Information")
        left_frame = Tkinter.Frame(master)
        right_frame = Tkinter.Frame(master)
        left_frame.pack(side=Tkinter.LEFT)
        right_frame.pack(side=Tkinter.RIGHT)

        variable = Tkinter.StringVar(master)
        variable.set("")  # default value

        city_label = Tkinter.Label(left_frame, text="City", anchor="w", width=10)
        county_label = Tkinter.Label(left_frame, text="County", anchor="w", width=10)
        latitude_label = Tkinter.Label(left_frame, text="Latitude", anchor="w", width=10)
        longitude_label = Tkinter.Label(left_frame, text="Longitude", anchor="w", width=10)

        city_picker = Tkinter.OptionMenu(right_frame, variable, "one", "two", "three")
        county_entry = Tkinter.Entry(right_frame, width=40)
        latitude_entry = Tkinter.Entry(right_frame, width=40)
        longitude_entry = Tkinter.Entry(right_frame, width=40)

        city_label.pack()
        county_label.pack()
        latitude_label.pack()
        longitude_label.pack()
        city_picker.pack()
        county_entry.pack()
        latitude_entry.pack()
        longitude_entry.pack()


root = Tkinter.Tk()
ci = CityInformation(root)
root.mainloop()
