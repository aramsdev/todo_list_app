import tkinter as tk
from tkinter import messagebox
import json
import os

# Crear la ventana principal
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400") 
root.config(bg="#f5f5f5")

# Colores y estilos personalizados
PRIMARY_COLOR = "#4CAF50"
BUTTON_COLOR = "#eeeeee"
WHITE_COLOR = "#ffffff"
RED_COLOR = "#FF0000"
HOVER_COLOR = "#45a049"
FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 10)

# Ruta del archivo donde se guardan las tareas
data_file = "data/tareas.json"

# Crear la lista de tareas
task_list = []

# Función para cargar tareas desde el archivo
def cargar_tareas():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        with open(data_file, 'w') as file:
            json.dump([], file)
        return []

# Función para guardar las tareas en el archivo
def guardar_tareas():
    with open(data_file, 'w') as file:
        json.dump(task_list, file)

# Función para agregar tarea
def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea != "":
        task_list.append(tarea)
        listbox_tareas.insert(tk.END, tarea)  
        entry_tarea.delete(0, tk.END)  
        guardar_tareas()  
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

# Función para eliminar tarea seleccionada
def eliminar_tarea():
    try:
        selected_task = listbox_tareas.curselection()  # Obtener la tarea seleccionada
        task_list.remove(listbox_tareas.get(selected_task))  # Eliminar de la lista
        listbox_tareas.delete(selected_task)  # Eliminar de la vista
        guardar_tareas()  # Guardar las tareas al archivo
    except:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

# Crear los widgets

# Listbox para mostrar las tareas
listbox_tareas = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE, font=FONT, bg="#ffffff", fg="#333333", selectbackground=PRIMARY_COLOR, bd=0, highlightthickness=0)
listbox_tareas.pack(pady=10)

# Entrada de texto para agregar tareas
entry_tarea = tk.Entry(root, width=40, font=FONT, bd=2, relief="solid", highlightthickness=0)
entry_tarea.pack(pady=10)

# Botón para agregar tarea
button_agregar = tk.Button(root, text="Agregar Tarea", width=15, command=agregar_tarea, font=BUTTON_FONT, fg=PRIMARY_COLOR, bg=BUTTON_COLOR, activebackground=HOVER_COLOR, bd=0, relief="flat")
button_agregar.pack(pady=5)

# Botón para eliminar tarea
button_eliminar = tk.Button(root, text="Eliminar Tarea", width=15, command=eliminar_tarea, font=BUTTON_FONT, fg=WHITE_COLOR, bg=RED_COLOR, activebackground=HOVER_COLOR, bd=0, relief="flat")
button_eliminar.pack(pady=5)

# Cargar las tareas al iniciar la aplicación
task_list = cargar_tareas()
for tarea in task_list:
    listbox_tareas.insert(tk.END, tarea)

# Iniciar la aplicación
root.mainloop()
