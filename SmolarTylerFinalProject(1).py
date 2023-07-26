import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Main class for the Bakery Order Application
class BakeryOrder:
    def __init__(self, master):  # Initializer method, it takes the master/root widget as input
        self.master = master  # Main root widget
        master.title("T&N Bakery")  # Set title for application
        master.configure(bg='pink')  # Set the background color of the application

        # Load and display the first image
        right_image = Image.open("C:\\Users\\tyler\\pictures\\py1\\cupcake.png")  # Load the cupcake image
        self.right_image = ImageTk.PhotoImage(right_image)  # Convert image for tkinter
        self.right_label = tk.Label(master, image=self.right_image)  # Create label to display the cupcake image
        self.right_label.grid(row=0, column=1, rowspan=10)  # Place the label in the grid

        # Add text under the first image
        self.right_text = tk.Label(master, text="This is one of our cupcakes!", bg='pink', fg='black')  # Label for cupcake text
        self.right_text.grid(row=10, column=1)  # Place the text under the cupcake image

        # Load and display the second image
        bottom_image = Image.open("C:\\Users\\tyler\\pictures\\py1\\brownie.png")  # Load the brownie image
        self.bottom_image = ImageTk.PhotoImage(bottom_image)  # Convert image for tkinter
        self.bottom_label = tk.Label(master, image=self.bottom_image)  # Create label to display the brownie image
        self.bottom_label.grid(row=11, column=1, rowspan=10)  # Place the label in the grid

        # Add text under the second image
        self.bottom_text = tk.Label(master, text="This is one of our brownies!", bg='pink', fg='black')  # Label for brownie text
        self.bottom_text.grid(row=21, column=1)  # Place the text under the brownie image

        # Create input labels and entry boxes
        # Each item has a label and an entry box for user to input the quantity they want to order
        # The label displays the name and the price of the item
        # The entry box captures the user input
        # Each item follows the similar pattern
        self.cupcake_lbl = tk.Label(master, text="Cupcake ($7.99)", fg="black", bg="pink",
                                    font=("Helvetica", 10, "bold"))
        self.cupcake_lbl.grid(row=0, column=0)
        self.cupcake_ent = tk.Entry(master, fg="black", bg="pink")  # Entry field for cupcake quantity
        self.cupcake_ent.grid(row=1, column=0)

        self.cookie_lbl = tk.Label(master, text="Cookie ($3.99)", fg="black", bg="pink", font=("Helvetica", 10, "bold"))
        self.cookie_lbl.grid(row=2, column=0)
        self.cookie_ent = tk.Entry(master, fg="black", bg="pink")  # Entry field for cookie quantity
        self.cookie_ent.grid(row=3, column=0)

        self.cake_lbl = tk.Label(master, text="Cake ($17.99)", fg="black", bg="pink", font=("Helvetica", 10, "bold"))
        self.cake_lbl.grid(row=4, column=0)
        self.cake_ent = tk.Entry(master, fg="black", bg="pink")  # Entry field for cake quantity
        self.cake_ent.grid(row=5, column=0)

        self.cake_pop_lbl = tk.Label(master, text="Cake Pop ($1.99)", fg="black", bg="pink",
                                     font=("Helvetica", 10, "bold"))
        self.cake_pop_lbl.grid(row=6, column=0)
        self.cake_pop_ent = tk.Entry(master, fg="black", bg="pink")  # Entry field for cake pop quantity
        self.cake_pop_ent.grid(row=7, column=0)

        self.brownie_lbl = tk.Label(master, text="Brownie ($5.99)", fg="black", bg="pink",
                                    font=("Helvetica", 10, "bold"))
        self.brownie_lbl.grid(row=8, column=0)
        self.brownie_ent = tk.Entry(master, fg="black", bg="pink")  # Entry field for brownie quantity
        self.brownie_ent.grid(row=9, column=0)

        self.brookie_lbl = tk.Label(master, text="Brookie ($6.99)", fg="black", bg="pink",
                                    font=("Helvetica", 10, "bold"))
        self.brookie_lbl.grid(row=10, column=0)
        self.brookie_ent = tk.Entry(master, fg="black", bg="pink")  # Entry field for brookie quantity
        self.brookie_ent.grid(row=11, column=0)

        # Create order button, which will calculate total cost when clicked
        self.order_btn = tk.Button(master, text="Place Order", command=self.calculate_total, fg="black", bg="pink",
                                   font=("Helvetica", 10, "bold"))
        self.order_btn.grid(row=12, column=0)

        # Create exit button, which will close the application when clicked
        self.exit_btn = tk.Button(master, text="Exit", command=master.quit, fg="black", bg="pink",
                                  font=("Helvetica", 10, "bold"))
        self.exit_btn.grid(row=13, column=0)

    # Method to calculate total cost of the order based on user inputs and show the total cost in a messagebox
    def calculate_total(self):
        try:
            # Get the quantity for each item from corresponding Entry fields
            cupcake = int(self.cupcake_ent.get())
            cookie = int(self.cookie_ent.get())
            cake = int(self.cake_ent.get())
            cake_pop = int(self.cake_pop_ent.get())
            brownie = int(self.brownie_ent.get())
            brookie = int(self.brookie_ent.get())

            # Calculate the total cost for each item by multiplying quantity with the price of each item
            total_price = (cupcake * 7.99) + (cookie * 3.99) + (cake * 17.99) + (cake_pop * 1.99) + (brownie * 5.99) + (
                        brookie * 6.99)
            total_price *= 1.07  # Add 7% sales tax to the total price

            # Display the total cost in a messagebox
            messagebox.showinfo("Total Price", f"Your total bill is ${total_price:.2f}")
        except ValueError:
            # Display an error message if the user input is not valid (not a number)
            messagebox.showerror("Invalid Input", "Please enter a valid integer for each item.")


# Main Application start here
root = tk.Tk()  # Create the main window

order_form = BakeryOrder(root)

# Run main loop
root.mainloop()
