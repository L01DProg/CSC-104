import tkinter as tk

def toggle_light():
    
    if light_state.get() == "on":
        light_state.set("off")
        root.configure(bg="gray")
        button_text.set("Lights On") 
    else:
        light_state.set("on")
        root.configure(bg="yellow")
        button_text.set("Lights Off") 

root = tk.Tk()
root.title("Light Switch Control")
root.geometry("400x300")

light_state = tk.StringVar(value="off") 
button_text = tk.StringVar(value="Lights On")



light1 = tk.Button(root, textvariable=button_text, command=toggle_light)
light1.pack(pady=20)

light2 = tk.Button(root, textvariable=button_text, command=toggle_light)
light2.pack(pady=20)


light3 = tk.Button(root, textvariable=button_text, command=toggle_light)
light3.pack(pady=20)

root.mainloop()