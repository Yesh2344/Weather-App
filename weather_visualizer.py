import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Added comment

# Function to fetch weather data
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to plot weather data
def plot_weather_data(weather_data):
    timestamps = [datetime.fromtimestamp(item['dt']) for item in weather_data['list']]
    temperatures = [item['main']['temp'] for item in weather_data['list']]
# Added comment
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(timestamps, temperatures, marker='o', label='Temperature (°C)', color='b')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('5-Day Temperature Trend')
    ax.legend()
    fig.autofmt_xdate()
    return fig

# Function to handle user input and display results
def fetch_and_display_weather():
# Added comment
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    weather_data = get_weather_data(city, api_key)
    
    if weather_data:
        fig = plot_weather_data(weather_data)
# Added comment
        canvas = FigureCanvasTkAgg(fig, master=frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    else:
        messagebox.showerror("Error", "Failed to fetch weather data. Check the city name or API key.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("800x600")

# Create the input frame
frame_input = tk.Frame(root, pady=10)
frame_input.pack(side=tk.TOP, fill=tk.X)
# Added comment

tk.Label(frame_input, text="Enter City Name:", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
city_entry = tk.Entry(frame_input, width=30, font=("Arial", 12))
city_entry.pack(side=tk.LEFT, padx=10)
fetch_button = tk.Button(frame_input, text="Fetch Weather", command=fetch_and_display_weather, font=("Arial", 12))
fetch_button.pack(side=tk.LEFT, padx=10)

# Create the plot display frame
frame_plot = tk.Frame(root)
frame_plot.pack(fill=tk.BOTH, expand=True, pady=20, padx=20)

# Run the Tkinter event loop
root.mainloop()
