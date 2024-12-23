import tkinter as tk
import math
from time import strftime

# Create the root window
root = tk.Tk()
root.title('Enhanced Analog Clock')

# Set window size
root.geometry('500x500')
root.resizable(False, False)  # Disable resizing

# Create canvas for the clock face
canvas = tk.Canvas(root, width=500, height=500, bg='#f0f0f0')
canvas.pack()

# Clock center coordinates
center_x = 250
center_y = 250
clock_radius = 240

# Draw the clock face (circle)
canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                   center_x + clock_radius, center_y + clock_radius, outline='#000000', width=4)

# Draw the hour marks and numbers (12, 1, 2, ..., 11)
for i in range(12):
    angle = math.radians(i * 30)  # 360 degrees / 12 = 30 degrees for each hour mark
    
    # Coordinates for outer hour mark
    x_outer = center_x + clock_radius * 0.9 * math.sin(angle)
    y_outer = center_y - clock_radius * 0.9 * math.cos(angle)
    
    # Coordinates for inner hour mark
    x_inner = center_x + clock_radius * 0.75 * math.sin(angle)
    y_inner = center_y - clock_radius * 0.75 * math.cos(angle)
    
    # Draw hour mark lines
    canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=4, fill='black')
    
    # Draw numbers for each hour
    number = str(i if i != 0 else 12)  # Clock numbers (0 should display as 12)
    
    # Adjust the text placement for better alignment
    x_text = center_x + clock_radius * 0.65 * math.sin(angle)
    y_text = center_y - clock_radius * 0.65 * math.cos(angle)
    
    canvas.create_text(x_text, y_text, text=number, font=('Helvetica', 20, 'bold'), fill='black')

# Function to update the clock hands
def update_clock():
    canvas.delete('hands')  # Remove previous hands
    
    # Get current time
    current_time = strftime('%I:%M:%S')
    hour, minute, second = map(int, current_time.split(':'))

    # Calculate angles for the hands
    second_angle = math.radians(second * 6)  # 360 degrees / 60 seconds = 6 degrees per second
    minute_angle = math.radians(minute * 6 + second * 0.1)  # Minute hand moves with seconds
    hour_angle = math.radians(hour * 30 + minute * 0.5)  # 360 degrees / 12 hours = 30 degrees per hour

    # Draw second hand (red and thin)
    draw_hand(second_angle, clock_radius * 0.85, '#ff0000', 2)

    # Draw minute hand (black and medium thickness)
    draw_hand(minute_angle, clock_radius * 0.75, '#000000', 4)

    # Draw hour hand (black and thick)
    draw_hand(hour_angle, clock_radius * 0.55, '#000000', 8)

    # Call the update function every 1000ms (1 second)
    root.after(1000, update_clock)

# Function to draw a hand (angle in radians, length of hand, color, width)
def draw_hand(angle, length, color, width):
    x = center_x + length * math.sin(angle)
    y = center_y - length * math.cos(angle)
    canvas.create_line(center_x, center_y, x, y, fill=color, width=width, tags='hands', capstyle=tk.ROUND)

# Initial call to update the clock hands
update_clock()

# Start the Tkinter event loop
root.mainloop()
