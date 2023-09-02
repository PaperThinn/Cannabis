from tkinter import Tk, Label, Menu, messagebox, Toplevel, Entry, Button
from PIL import ImageTk, Image
from tkinter import ttk
import csv
import tkinter as tk
import calendar
import datetime
import json
import os
import tkinter

# Create the main window
root = Tk()
root.title("GrowSense")


# Function to show the about information
def show_about():
    about_text = """
    GrowSense
    Created by Jordan Smith
    Version 1.1
    
    This program is designed to automate and monitor the growth of cannabis plants. It provides real-time data on temperature, humidity, light intensity, and pH level. Additionally, it offers features such as strain selection, data logging, and predictive harvest estimation.
    """
    messagebox.showinfo("About", about_text)


# Function to show the system settings
def show_settings():
    # Create a new window for the settings
    settings_window = Tk()
    settings_window.title("System Settings")

    # Function to save the settings
    def save_settings():
        settings = {
            "temperature_units": temperature_units_var.get(),
            "light_schedule": light_schedule_var.get(),
            "pH_threshold": float(pH_threshold_var.get())
        }

        with open("settings.json", "w") as file:
            json.dump(settings, file)

        messagebox.showinfo("Settings", "Settings saved successfully!")
        settings_window.destroy()

    # Function to cancel and close the settings window
    def cancel_settings():
        settings_window.destroy()

    # Load the settings from the JSON file, if it exists
    try:
        with open("settings.json") as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {}

    # Create the settings form
    label_temperature_units = Label(settings_window, text="Temperature Units:")
    label_temperature_units.grid(row=0, column=0, padx=5, pady=5)

    temperature_units_var = ttk.Combobox(settings_window, state="readonly")
    temperature_units_var["values"] = ["Celsius", "Fahrenheit"]
    temperature_units_var.grid(row=0, column=1, padx=5, pady=5)
    temperature_units_var.set(settings.get("temperature_units", "Celsius"))

    label_light_schedule = Label(settings_window, text="Light Schedule:")
    label_light_schedule.grid(row=1, column=0, padx=5, pady=5)

    light_schedule_var = ttk.Combobox(settings_window, state="readonly")
    light_schedule_var["values"] = ["12/12", "24/0", "18/6"]
    light_schedule_var.grid(row=1, column=1, padx=5, pady=5)
    light_schedule_var.set(settings.get("light_schedule", "12/12"))

    label_pH_threshold = Label(settings_window, text="pH Threshold:")
    label_pH_threshold.grid(row=2, column=0, padx=5, pady=5)

    pH_threshold_var = ttk.Entry(settings_window)
    pH_threshold_var.grid(row=2, column=1, padx=5, pady=5)
    pH_threshold_var.insert(0, settings.get("pH_threshold", "7.0"))

    button_save = ttk.Button(settings_window, text="Save", command=save_settings)
    button_save.grid(row=3, column=0, padx=5, pady=5)

    button_cancel = ttk.Button(settings_window, text="Cancel", command=cancel_settings)
    button_cancel.grid(row=3, column=1, padx=5, pady=5)


# Create the menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create the File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)

# Create the Settings menu
settings_menu = Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="System Settings", command=show_settings)

# Define your default parameters dictionary
default_parameters = {
    'temperature': 72,
    'humidity': 50,
    'light_intensity': 80,
    'nutrients': {
        'nitrogen': 10,
        'phosphorus': 5,
        'potassium': 7,
        'calcium': 3,
        'magnesium': 2,
        'sulfur': 1
    },
    'growing_medium': 'Soil' # Default growing medium is set to Soil
}

# Function to open the parameters window
def open_parameters_window():
    # Create a new window for the parameters
    parameters_window = Toplevel()
    parameters_window.title("Default Parameters")
    
    # Create and configure the input fields for each parameter
    temperature_label = Label(parameters_window, text="Temperature (°F):")
    temperature_entry = Entry(parameters_window)
    temperature_label.pack()
    temperature_entry.pack()
    
    humidity_label = Label(parameters_window, text="Humidity (%):")
    humidity_entry = Entry(parameters_window)
    humidity_label.pack()
    humidity_entry.pack()
    
    light_intensity_label = Label(parameters_window, text="Light Intensity (%):")
    light_intensity_entry = Entry(parameters_window)
    light_intensity_label.pack()
    light_intensity_entry.pack()
    
    nitrogen_label = Label(parameters_window, text="Nitrogen Level:")
    nitrogen_entry = Entry(parameters_window)
    nitrogen_label.pack()
    nitrogen_entry.pack()
    
    phosphorus_label = Label(parameters_window, text="Phosphorus Level:")
    phosphorus_entry = Entry(parameters_window)
    phosphorus_label.pack()
    phosphorus_entry.pack()
    
    potassium_label = Label(parameters_window, text="Potassium Level:")
    potassium_entry = Entry(parameters_window)
    potassium_label.pack()
    potassium_entry.pack()
    
    calcium_label = Label(parameters_window, text="Calcium Level:")
    calcium_entry = Entry(parameters_window)
    calcium_label.pack()
    calcium_entry.pack()
    
    magnesium_label = Label(parameters_window, text="Magnesium Level:")
    magnesium_entry = Entry(parameters_window)
    magnesium_label.pack()
    magnesium_entry.pack()
    
    sulfur_label = Label(parameters_window, text="Sulfur Level:")
    sulfur_entry = Entry(parameters_window)
    sulfur_label.pack()
    sulfur_entry.pack()

    growing_medium_label = tkinter.Label(parameters_window, text="Growing Medium:")
    growing_medium_var = tkinter.StringVar(parameters_window)
    growing_medium_var.set("Soil") # Set default value to Soil
    growing_medium_dropdown = tkinter.OptionMenu(parameters_window, growing_medium_var, "Soil", "Hydroponics")
    growing_medium_label.pack()
    growing_medium_dropdown.pack()
    
    # Populate the input fields with default parameter values
    temperature_entry.insert(tkinter.END, str(default_parameters['temperature']))
    humidity_entry.insert(tkinter.END, str(default_parameters['humidity']))
    light_intensity_entry.insert(tkinter.END, str(default_parameters['light_intensity']))
    nitrogen_entry.insert(tkinter.END, str(default_parameters['nutrients']['nitrogen']))
    phosphorus_entry.insert(tkinter.END, str(default_parameters['nutrients']['phosphorus']))
    potassium_entry.insert(tkinter.END, str(default_parameters['nutrients']['potassium']))
    calcium_entry.insert(tkinter.END, str(default_parameters['nutrients']['calcium']))
    magnesium_entry.insert(tkinter.END, str(default_parameters['nutrients']['magnesium']))
    sulfur_entry.insert(tkinter.END, str(default_parameters['nutrients']['sulfur']))
    
    # Save button event handler
    def save_parameters():
        # Retrieve user-modified parameter values from input fields
        new_temperature = float(temperature_entry.get())
        new_humidity = float(humidity_entry.get())
        new_light_intensity = float(light_intensity_entry.get())
        new_nitrogen = float(nitrogen_entry.get())
        new_phosphorus = float(phosphorus_entry.get())
        new_potassium = float(potassium_entry.get())
        new_calcium = float(calcium_entry.get())
        new_magnesium = float(magnesium_entry.get())
        new_sulfur = float(sulfur_entry.get())
        new_growing_medium = growing_medium_var.get()
        
        # Update the default parameter values in your code or configuration file
        default_parameters['temperature'] = new_temperature
        default_parameters['humidity'] = new_humidity
        default_parameters['light_intensity'] = new_light_intensity
        default_parameters['nutrients']['nitrogen'] = new_nitrogen
        default_parameters['nutrients']['phosphorus'] = new_phosphorus
        default_parameters['nutrients']['potassium'] = new_potassium
        default_parameters['nutrients']['calcium'] = new_calcium
        default_parameters['nutrients']['magnesium'] = new_magnesium
        default_parameters['nutrients']['sulfur'] = new_sulfur
        default_parameters["growing_medium"] = new_growing_medium
        
        # Close the parameters window
        parameters_window.destroy()
    
    # Save button
    save_button = Button(parameters_window, text="Save", command=save_parameters)
    save_button.pack()

# Parameters Submenu
parameters_submenu = Menu(settings_menu, tearoff=0)
settings_menu.add_cascade(label="Parameters", menu=parameters_submenu)
parameters_submenu.add_command(label="Default Parameters", command=open_parameters_window)

# Create the Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)

# Add the menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)


# Add your trademark to the menu bar
label_trademark = Label(root, text="GrowSense®", anchor="e")
label_trademark.pack(side="top", fill="y")


# Add elements to the dashboard
label_temperature = Label(root, text="Temperature: 72.3 ")
label_temperature.pack()

label_humidity = Label(root, text="Humidity: 61.5 ")
label_humidity.pack()

label_light = Label(root, text="Light Intensity: 1080 ")
label_light.pack()

label_ph = Label(root, text="pH Level: 6.43 ")
label_ph.pack()


# Load and display an image
image = Image.open("/home/jordan/Desktop/Cannabis.png")
image = image.resize((100, 100))
photo = ImageTk.PhotoImage(image)
label_image = Label(root, image=photo)
label_image.pack()


# Create a tab control
tab_control = ttk.Notebook(root)
tab_control.pack(fill='both', expand=True)


# Create a label to display the week and day
label_planting_info = ttk.Label(root, text="")
label_planting_info.pack(anchor='ne', padx=5, pady=5)


# Create an entry field for the manual date input
date_entry_label = ttk.Label(root, text="Enter Planting Date (MM/DD/YYYY):")
date_entry_label.pack()

date_entry_var = tk.StringVar()
date_entry = ttk.Entry(root, textvariable=date_entry_var)
date_entry.pack()


# Create a function to update the week and day display based on the manual date input
def update_week_and_day():
    date_str = date_entry_var.get()

    try:
        planting_date = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
        today = datetime.date.today()

        if planting_date > today:
            label_planting_info.config(text="Invalid Date: Future Date")
        else:
            days_passed = (today - planting_date).days
            weeks_passed = days_passed // 7 + 1
            planting_day = calendar.day_name[planting_date.weekday()]
            label_planting_info.config(text=f"Week: {weeks_passed} | Day: {planting_day}")
    except ValueError:
        label_planting_info.config(text="Invalid Date: Please use the format MM/DD/YYYY")


# Create a button to trigger the manual date update
update_button = ttk.Button(root, text="Update", command=update_week_and_day)
update_button.pack()


# Create the main dashboard tab
dashboard_frame = ttk.Frame(tab_control)
tab_control.add(dashboard_frame, text='Dashboard')


# Create string variables to hold the sensor data
temperature_var = tk.StringVar()
humidity_var = tk.StringVar()
light_intensity_var = tk.StringVar()
light_schedule_var = tk.StringVar()  # Define the light schedule variable


# Create A label and dropdown for the light schedule
label_light_schedule = ttk.Label(dashboard_frame, text="Light Schedule:")
label_light_schedule.pack()

dropdown_light_schedule = ttk.Combobox(dashboard_frame, textvariable=light_schedule_var)
dropdown_light_schedule['values'] = ['12/12', '24/0', '18/6']
dropdown_light_schedule.pack()


# Create data tab
data_frame = ttk.Frame(tab_control)
tab_control.add(data_frame, text='Data')


# Add a button to save the data
def save_data():
    # Get the data from the sensors
    temperature = 73.3
    humidity = 61.8
    light_intensity = 1080

    # Define the file path and open the CSV file in append mode
    file_path = 'sensor_data.csv'
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)

        # Write data to the CSV file
        writer.writerow([temperature, humidity, light_intensity])

    # Provide feedback to the user (optional)
    print("Data saved successfully!")


save_button = ttk.Button(data_frame, text='Save Data', command=save_data)
save_button.pack()


# Create the strains tab
strains_frame = ttk.Frame(tab_control)
tab_control.add(strains_frame, text='Strains')

# Create a dictionary to hold the strain data
strain_data = {}
strain_names = []

# Load strain data from JSON file
def load_strain_data():
    file_path = 'strains.json'
    if os.path.exists(file_path):
        with open(file_path) as file:
            data = json.load(file)
            # Populate the strain_data dictionary with strain information
            for strain in data:
                strain_name = strain.get('name')
                strain_data[strain_name] = strain
                strain_names.append(strain_name)
        return data  # Return the loaded data
    return []  # Return an empty list if the file doesn't exist

# Call the function to load strain data and store the returned data
data = load_strain_data()

# Function to update strain information
def update_strain_info(strain_info):
    label_strain_name.config(text=f"Strain Name: {strain_info.get('name', '')}")
    label_type.config(text=f"Type: {strain_info.get('type', '')}")
    label_thc.config(text=f"THC Level: {strain_info.get('thc_level', 'N/A')}")
    label_terpene.config(text=f"Common Terpene: {strain_info.get('most_common_terpene', 'N/A')}")

# Function to display strain information when selected from the dropdown
def display_strain_info(event):
    selected = dropdown_strains.get()
    if selected:
        strain_info = strain_data.get(selected)
        if strain_info:
            update_strain_info(strain_info)
        else:
            clear_strain_info()
    else:
        clear_strain_info()

# Function to clear strain information labels
def clear_strain_info():
    label_strain_name.config(text="Strain Name:")
    label_type.config(text="Type:")
    label_thc.config(text="THC Level:")
    label_terpene.config(text="Common Terpene:")

# Create a label for the strain dropdown
label_strain = ttk.Label(strains_frame, text="Select Strain:")
label_strain.grid(row=0, column=0, padx=10, pady=10)

# Create a StringVar to store the selected strain
selected_strain = tk.StringVar()

# Create the dropdown box
dropdown_strains = ttk.Combobox(strains_frame, textvariable=selected_strain)
dropdown_strains['values'] = [strain.get('name') for strain in data]
dropdown_strains.grid(row=0, column=0, padx=10, pady=10)

# Bind the function to the dropdown selection event
dropdown_strains.bind("<<ComboboxSelected>>", display_strain_info)

# Create labels to display the strain information
label_strain_name = ttk.Label(strains_frame, text="Strain Name:")
label_strain_name.grid(row=1, column=0, padx=10, pady=5)

label_type = ttk.Label(strains_frame, text="Type:")
label_type.grid(row=2, column=0, padx=10, pady=5)

label_thc = ttk.Label(strains_frame, text="THC Level:")
label_thc.grid(row=3, column=0, padx=10, pady=5)

label_terpene = ttk.Label(strains_frame, text="Common Terpene:")
label_terpene.grid(row=4, column=0, padx=10, pady=5)

# Create a frame to hold the search functionality
search_frame = ttk.Frame(strains_frame)
search_frame.grid(row=0, column=1, padx=10, pady=10)

# Create a label and entry for the search box
label_search = ttk.Label(search_frame, text="Search Strain:")
label_search.grid(row=0, column=0, padx=5, pady=5)

entry_search = ttk.Entry(search_frame)
entry_search.grid(row=0, column=1, padx=5, pady=5)

# Function to search for strains
def search_strain():
    search_text = entry_search.get().lower()
    matching_strains = [strain for strain in data if search_text in strain['name'].lower()]
    dropdown_strains['values'] = [strain.get('name') for strain in matching_strains]
    if matching_strains:
        dropdown_strains.current(0)  # Select the first matching strain
    else:
        clear_strain_info()

# Create a button to search for strains
btn_search = ttk.Button(search_frame, text="Search", command=search_strain)
btn_search.grid(row=0, column=2, padx=5, pady=5)

# Function to add a new strain
def add_strain():
    # Create a new window for adding strain details
    add_window = tk.Toplevel(root)
    add_window.title("Add New Strain")
    
    # Create labels and entry fields for strain details
    label_name = ttk.Label(add_window, text="Strain Name:")
    label_name.grid(row=0, column=0, padx=10, pady=5)
    entry_name = ttk.Entry(add_window)
    entry_name.grid(row=0, column=1, padx=10, pady=5)
    
    label_type = ttk.Label(add_window, text="Type:")
    label_type.grid(row=1, column=0, padx=10, pady=5)
    entry_type = ttk.Entry(add_window)
    entry_type.grid(row=1, column=1, padx=10, pady=5)
    
    label_thc = ttk.Label(add_window, text="THC Level:")
    label_thc.grid(row=2, column=0, padx=10, pady=5)
    entry_thc = ttk.Entry(add_window)
    entry_thc.grid(row=2, column=1, padx=10, pady=5)
    
    label_terpene = ttk.Label(add_window, text="Common Terpene:")
    label_terpene.grid(row=3, column=0, padx=10, pady=5)
    entry_terpene = ttk.Entry(add_window)
    entry_terpene.grid(row=3, column=1, padx=10, pady=5)
    
    # Function to save the new strain data
    def save_strain():
        strain_name = entry_name.get()
        strain_type = entry_type.get()
        strain_thc = entry_thc.get()
        strain_terpene = entry_terpene.get()
        
        # Create a dictionary with the strain data
        new_strain = {
            'name': strain_name,
            'type': strain_type,
            'thc_level': strain_thc,
            'most_common_terpene': strain_terpene
        }
        
        # Add the new strain to the data dictionary and strain_names list
        strain_data[strain_name] = new_strain
        strain_names.append(strain_name)
        
        # Update the dropdown values and select the new strain
        dropdown_strains['values'] = strain_names
        dropdown_strains.set(strain_name)
        
        # Update the strain information labels
        update_strain_info(new_strain)
        
        # Save the updated strain data to the JSON file
        with open('strains.json', 'w') as file:
            json.dump(list(strain_data.values()), file, indent=4)
        
        # Close the add window
        add_window.destroy()
    
    # Create a button to save the new strain
    btn_save = ttk.Button(add_window, text="Save", command=save_strain)
    btn_save.grid(row=4, column=1, padx=10, pady=10)

# Create a button to add a new strain
btn_add_strain = ttk.Button(strains_frame, text="Add New Strain", command=add_strain)
btn_add_strain.grid(row=5, column=0, padx=10, pady=10)



# Create the predictive harvest tab
predictive_harvest_frame = ttk.Frame(tab_control)
tab_control.add(predictive_harvest_frame, text='Predictive Harvest')


# Create a dropdown menu to select the type of strain
strain_type_var = tk.StringVar()
strain_type_dropdown = ttk.Combobox(predictive_harvest_frame, textvariable=strain_type_var)
strain_type_dropdown['values'] = ["Photo Period", "Auto Flower"]
strain_type_dropdown.grid(row=0, column=1, sticky="w")

# Add a date picker for inputting the start of flowering
flowering_date_label = ttk.Label(predictive_harvest_frame, text="Start of Flowering:")
flowering_date_label.grid(row=0, column=2, padx=5, sticky="w")

day_var = tk.StringVar()
day_dropdown = ttk.Combobox(predictive_harvest_frame, textvariable=day_var, width=2)
day_dropdown['values'] = [str(day) for day in range(1, 32)]
day_dropdown.grid(row=0, column=3, padx=5)

month_var = tk.StringVar()
month_dropdown = ttk.Combobox(predictive_harvest_frame, textvariable=month_var, width=4)
month_dropdown['values'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                            'August', 'September', 'October', 'November', 'December']
month_dropdown.grid(row=0, column=4, padx=5)


# Create a label to display the predictive harvest date
label_predictive_harvest = ttk.Label(predictive_harvest_frame, text="")
label_predictive_harvest.grid(row=1, column=1, columnspan=4, pady=5)


# Create a function to calculate the predictive harvest date
def calculate_predictive_harvest():
    start_of_flowering_day = int(day_var.get())
    start_of_flowering_month = month_dropdown.current() + 1  # Adjust for zero-based index
    strain_type = strain_type_var.get()

    if strain_type == "Photo Period":
        average_flowering_time = 63  # Average flowering time in days for photo period strains
    elif strain_type == "Auto Flower":
        average_flowering_time = 49  # Average flowering time in days for auto flower strains

    # Create a datetime object for the start of flowering
    start_of_flowering = datetime.date(datetime.date.today().year, start_of_flowering_month, start_of_flowering_day)

    # Calculate the harvest date by adding the average flowering time
    harvest_date = start_of_flowering + datetime.timedelta(days=average_flowering_time)

    # Display the predictive harvest date
    label_predictive_harvest.config(text=f"Predictive Harvest: {harvest_date.strftime('%m-%d-%Y')}")


# Add a button to calculate the predictive harvest date
calculate_button = ttk.Button(predictive_harvest_frame, text="Calculate", command=calculate_predictive_harvest)
calculate_button.grid(row=2, column=1, pady=5)


# Add a label to display the data file path
data_file_path = ttk.Label(data_frame, text="Data File Path: sensor_data.csv")
data_file_path.pack()


# Run the main event loop
root.mainloop()