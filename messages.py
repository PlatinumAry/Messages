import tkinter as tk # Imports the library for the program

# Create the main window
root = tk.Tk()
root.title("Message Storage Software") # Program title


def save_message(): # Function
    message = message_entry.get() # Tkinter "erntry widget, let's you input", the "get" method retrieves the text content currently present in the entry field
    if message: # Checks if the vairable "message" has any text 
        with open("stored_messages.txt", "a") as file: # Opens a file with the same name
            file.write(message + "\n") # Writes the message to the new line
        message_entry.delete(0, tk.END) # Clears the text entry



# Message Entry Field
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=10)

# Save Button
save_button = tk.Button(root, text="Save Message", command=save_message)
save_button.pack()

# Text Area to Display Stored Messages
text_area = tk.Text(root, width=60, height=20)
text_area.pack(pady=10)



def load_messages(): # Function
    try: 
        with open("stored_messages.txt", "r") as file: # Opens file in read mode
            messages = file.readlines() # Reads the lines and stores them
            text_area.delete(1.0, tk.END) # Clears so previous content is removed
            for message in messages: # Iterates over each message in the messages list obtained from the file.
                text_area.insert(tk.END, message)
    except FileNotFoundError:
        pass



# Load Button

load_button = tk.Button(root, text="Load Message", command=load_messages)
load_button.pack()

text_area = tk.Text(root, width=60, height=20)
text_area.pack(pady=10)

root.mainloop()
