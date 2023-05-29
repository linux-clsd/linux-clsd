import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox

def listar_archivos_directorios(ruta):
    contenido = os.listdir(ruta)
    resultado = ""

    for item in contenido:
        ruta_completa = os.path.join(ruta, item)

        if os.path.isfile(ruta_completa):
            informacion = os.stat(ruta_completa)
            nombre = item
            tamaño = informacion.st_size
            fecha_modificacion = time.ctime(informacion.st_mtime)
            permisos = oct(informacion.st_mode)[-3:]

            resultado += f"Archivo: {nombre} - Tamaño: {tamaño} bytes - Modificado: {fecha_modificacion} - Permisos: {permisos}\n"
        elif os.path.isdir(ruta_completa):
            resultado += f"Directorio: {item}\n"
        else:
            resultado += f"Otro: {item}\n"

    return resultado

def filtrar_por_extension(ruta, extension):
    contenido = os.listdir(ruta)
    resultado = ""

    for item in contenido:
        ruta_completa = os.path.join(ruta, item)

        if os.path.isfile(ruta_completa) and item.endswith(extension):
            informacion = os.stat(ruta_completa)
            nombre = item
            tamaño = informacion.st_size
            fecha_modificacion = time.ctime(informacion.st_mtime)
            permisos = oct(informacion.st_mode)[-3:]

            resultado += f"Archivo: {nombre} - Tamaño: {tamaño} bytes - Modificado: {fecha_modificacion} - Permisos: {permisos}\n"

    return resultado

def ordenar_lista(ruta, criterio='nombre'):
    contenido = os.listdir(ruta)

    if criterio == 'nombre':
        contenido.sort()
    elif criterio == 'tamaño':
        contenido.sort(key=lambda x: os.path.getsize(os.path.join(ruta, x)))
    elif criterio == 'fecha':
        contenido.sort(key=lambda x: os.path.getmtime(os.path.join(ruta, x)))

    resultado = ""

    for item in contenido:
        ruta_completa = os.path.join(ruta, item)

        if os.path.isfile(ruta_completa):
            informacion = os.stat(ruta_completa)
            nombre = item
            tamaño = informacion.st_size
            fecha_modificacion = time.ctime(informacion.st_mtime)
            permisos = oct(informacion.st_mode)[-3:]

            resultado += f"Archivo: {nombre} - Tamaño: {tamaño} bytes - Modificado: {fecha_modificacion} - Permisos: {permisos}\n"
        elif os.path.isdir(ruta_completa):
            resultado += f"Directorio: {item}\n"

    return resultado

def abrir_dialogo_seleccionar_carpeta():
    carpeta_seleccionada = filedialog.askdirectory()
    if carpeta_seleccionada:
        texto_ruta.delete("1.0", tk.END)
        texto_ruta.insert(tk.END, carpeta_seleccionada)

def mostrar_resultado():
    ruta = texto_ruta.get("1.0", tk.END).strip()

    if not ruta:
        messagebox.showerror("Error", "Debe seleccionar una carpeta.")
        return

    resultado = ""

    if seleccion.get() == 1:
        resultado = listar_archivos_directorios(ruta)
    elif seleccion.get() == 2:
        extension = entrada_extension.get().strip()
        if not extension:
            messagebox.showerror("Error", "Debe ingresar una extensión.")
            return
        resultado = filtrar_por_extension(ruta, extension)
    elif seleccion.get() == 3:
        seleccion_indices = lista_ordenamiento.curselection()
        if not seleccion_indices:
            messagebox.showerror("Error", "Debe seleccionar un criterio de ordenamiento.")
            return
        indice_seleccionado = seleccion_indices[0]
        criterio = lista_ordenamiento.get(indice_seleccionado)
        resultado = ordenar_lista(ruta, criterio)

    ventana_resultado = tk.Toplevel(ventana_principal)
    ventana_resultado.title("Resultado")

    etiqueta_resultado = tk.Label(ventana_resultado, text=resultado, justify=tk.LEFT)
    etiqueta_resultado.pack(padx=10, pady=10)

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Explorador de archivos")

# Crear controles de la interfaz gráfica
etiqueta_ruta = tk.Label(ventana_principal, text="Ruta:")
etiqueta_ruta.pack(pady=10)

texto_ruta = tk.Text(ventana_principal, height=1, width=30)
texto_ruta.pack()

boton_seleccionar_carpeta = tk.Button(ventana_principal, text="Seleccionar carpeta", command=abrir_dialogo_seleccionar_carpeta)
boton_seleccionar_carpeta.pack(pady=10)

seleccion = tk.IntVar()
seleccion.set(1)

radiobutton_lista = tk.Radiobutton(ventana_principal, text="Listar archivos y directorios", variable=seleccion, value=1)
radiobutton_lista.pack(anchor=tk.W)

radiobutton_filtro = tk.Radiobutton(ventana_principal, text="Filtrar por extensión", variable=seleccion, value=2)
radiobutton_filtro.pack(anchor=tk.W)

entrada_extension = tk.Entry(ventana_principal)
entrada_extension.pack(pady=5)

radiobutton_ordenamiento = tk.Radiobutton(ventana_principal, text="Ordenar la lista", variable=seleccion, value=3)
radiobutton_ordenamiento.pack(anchor=tk.W)

lista_ordenamiento = tk.Listbox(ventana_principal)
lista_ordenamiento.insert(tk.END, "nombre")
lista_ordenamiento.insert(tk.END, "tamaño")
lista_ordenamiento.insert(tk.END, "fecha")
lista_ordenamiento.pack()

boton_mostrar_resultado = tk.Button(ventana_principal, text="Mostrar resultado", command=mostrar_resultado)
boton_mostrar_resultado.pack(pady=10)

ventana_principal.mainloop()
