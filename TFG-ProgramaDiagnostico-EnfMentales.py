#!/usr/bin/env python
# coding: utf-8

# In[ ]:


################################################################################################################################
################################################################################################################################

#####TRABAJO DE FIN DE GRADO 2024

##### Estudio y Desarrollo de una Herramienta de Diagnóstico para Trastornos Mentales en Clínica

##### Grado de Biomedicina
##### Universidad Alfonso X El Sabio (UAX)

##### Desarrollado por Megan Trayling Jiménez 

##### Tutora: Irene del Hierro García
##### Co-tutora: Alejandra Gutiérrez González

################################################################################################################################

##### Este trabajo ha sido desarrollado en Python 3.12.3v, empleando Jupyter Notebook (https://www.anaconda.com/).
##### El script está disponible tanto en formato .py
##### REPOSITORIO DEL CÓDIGO: https://github.com/Bioinf-Biomedicina-IDHG/TFG

##### Ejecución (Windows 10 v o superior):
##### 1.- Descargar la carpeta comprimida
##### 2.- Descomprimir la carpeta (7zpi, WinRAR o similares)
##### 3.- Instalar python 3.0 o superior (si no lo tiene ya instalado)
##### 4.- Situarse en el interior de la carpeta
##### 5.- Botón derecho -> Abrir Terminal 
##### 6.- Escribir el siguiente comando:
#####         python TFG-ProgramaDiagnostico-EnfMentales.py

################################################################################################################################
################################################################################################################################


#### MODULOS A CARGAR
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk


##### APERTURA DEL FORMUALRIO DE ENTRADA 

# Función que inicializa la ejecución
def mostrar_formulario():
    
    #### CONFIGURACIÓN VENTANA DEL FORMULARIO
    ventana_formulario = Tk() 
    ventana_formulario.title("FORMULARIO DE DIAGNOSTICO")   
    ventana_formulario.configure(bg="white") 
    ventana_formulario.iconbitmap("iconos/Pantallas.ico")
    
    # Centramos y ponemos el tamaño de forma proporcional (igual que en la ventan de inicio)
    ancho_ventana_formulario = 1000
    alto_ventana_formulario = 500
    x_formulario = ventana_formulario.winfo_screenwidth() // 2 - ancho_ventana_formulario // 2
    y_formulario = ventana_formulario.winfo_screenheight() // 2 - alto_ventana_formulario // 2
    posicion_formulario =str(ancho_ventana_formulario) + "x" + str(alto_ventana_formulario) + "+" + str(x_formulario) + "+" + str(y_formulario)
    ventana_formulario.geometry(posicion_formulario)
    ventana_formulario.resizable(0,0)
    
    # Expansión a pantalla completa
    ventana_formulario.state('zoomed')
    
    # Protocolo de cierre de seguridad de la ventana del formulario
    def cerrar_formulario():
        close = askyesno("Confirmar cierre","¿Está seguro de que quiere cerrar la aplicación?")
        if close:
            ventana_formulario.destroy()
            
    
        
    #### CAMPOS DEL FORMULARIO 
    
    
    # ENTRADA DEL NOMBRE Y VALIDACIÓN
    def validar_nombre(input): #validación de solo caracteres alfabéticos y/o espacios (nombres compuestos)
        if all(letra.isalpha() or letra.isspace() for letra in input): return input
        else:
            showwarning("Warning", "El nombre introducido tiene caracteres no admitidos")
            
    etiqueta_nombre = Label(ventana_formulario, text="Nombre: ",bg="white").grid(row=0, column=0, padx=10, pady=5,sticky='w')
    entrada_nombre = Entry(ventana_formulario, bg ="aquamarine")
    entrada_nombre.grid(row=0, column=1, padx=10, pady=5,sticky='w')
    
    
    # ENTRADA DE LOS APELLIDOS Y VALIDACIÓN
    def validar_apellidos(input):
        if all(letra.isalpha() or letra.isspace() for letra in input): return input #validación de solo caracteres alfabéticos y/o espacios (dos apellidos o compuestos)
        else:
            showwarning("Warning", "Los apellidos introducidos tienen caracteres no admitidos")
    
    etiqueta_apellidos = Label(ventana_formulario, text="Apellidos: ",bg="white").grid(row=1, column=0, padx=10, pady=5,sticky='w')
    entrada_apellidos = Entry(ventana_formulario,bg="aquamarine")
    entrada_apellidos.grid(row=1, column=1, padx=10, pady=5,sticky='w')
    

    # ENTRADA DE LA EDAD Y VALIDACIÓN
    def validar_edad(input):
        if input.isdigit() and 0 <= int(input) <= 150: return input #validación solo números enteros entre un rango determinado
        else:
            showwarning("Warning", "La edad introducida no es correcta")

    etiqueta_edad = Label(ventana_formulario, text="Edad: ",bg="white").grid(row=2, column=0, padx=10, pady=5,sticky='w')
    entrada_edad = Entry(ventana_formulario,bg="aquamarine")
    entrada_edad.grid(row=2, column=1, padx=10, pady=5,sticky='w')
    
    
    # ENTRADA DEL SEXO BIOLÓGICO Y VALIDACIÓN
    def validar_sexo(sexo): #validación dos tipos de posibilidades
        if sexo in ["Masculino", "Femenino"]:
            return sexo
        else: 
            showwarning('Warning',"Seleccione un sexo biológico")
    
    etiqueta_sexo = Label(ventana_formulario, text="Sexo Biológico: ",bg="white")
    etiqueta_sexo.grid(row=0, column=2, padx=10, pady=5,sticky='w')
    seleccion_sexo = StringVar(ventana_formulario) 
    opciones_sexo = ["Masculino", "Femenino"]
    menu_sexo = OptionMenu(ventana_formulario, seleccion_sexo, *opciones_sexo)
    menu_sexo.grid(row=0, column=3, padx=10, pady=5,sticky='w')
    menu_sexo.configure(bg="aquamarine")
    
    # Inclusión de celdas en blanco
    etiqueta_blanco1=Label(ventana_formulario,text="",bg="white").grid(row=1,column=2,padx=10,pady=5)
    etiqueta_blanco2=Label(ventana_formulario,text="",bg="white").grid(row=1,column=3,padx=10,pady=5)
    
    
    # ENTRADA DEL GÉNERO Y VALIDACIÓN
    def validar_genero(genero):
        if genero in ["Mujer", "Hombre", "No Binario", "Otro", "No contesta"]:
            return genero
        else:
            showwarning('Warning', "Seleccione un género válido")

    etiqueta_genero = Label(ventana_formulario, text="Género: ", bg="white")
    etiqueta_genero.grid(row=2, column=2, padx=10, pady=5, sticky='w')
    seleccion_genero = StringVar(ventana_formulario)
    opciones_genero = ["Mujer", "Hombre", "No Binario", "Otro", "No contesta"]
    menu_genero = OptionMenu(ventana_formulario, seleccion_genero, *opciones_genero)
    menu_genero.grid(row=2, column=3, padx=10, pady=5,sticky='w')
    menu_genero.configure(bg="aquamarine")
    
    
    #### ENTRADA DE POSIBLES CONDICIONANTES PREVIOS
    etiqueta_enf_previas = Label(ventana_formulario, text="CONDICIONANTES PREVIOS", bg="white").grid(row=0, column=4, padx=10, pady=5, sticky='w')

    global lista_enf   # declaración de variable global para poder pasarla entre las ventanas
    lista_enf = ""   # la incializamos vacía
    
    # Aquí creamos una entrada para guardar el resultado (si hay)
    resultado_enf_previas = Entry(ventana_formulario,width=22,bg="aquamarine", fg="dark blue") 
    resultado_enf_previas.grid(row=1, column=5, padx=10, pady=5)
    
    # Función para actualizar el valor de la entrada de enfermedades previas
    def actualizar_enf_previas(valor):
        resultado_enf_previas.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_enf_previas.insert(0, valor)  # inserta el nuevo valor
        return valor
    
    # Función para crear la ventana una vez que se clica en el botón
    def mostrar_ventana_enf_previas():
        ventana_enf_previas = Toplevel() 
        ventana_enf_previas.title("Lista de Condicionantes Previos")    
        ventana_enf_previas.geometry(posicion_formulario)
        ventana_enf_previas.configure(bg="white")
        ventana_enf_previas.iconbitmap("iconos/Pantallas.ico")
        ventana_enf_previas.state('zoomed')

        # Creación de una barra de scroll lateral vertical
        frame_enf_previas = Frame(ventana_enf_previas,bg="white") # Primero se crea un frame
        frame_enf_previas.grid(row=0,column=0,sticky="nsew")
        canvas_enf_previas=Canvas(frame_enf_previas,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_enf_previas = Scrollbar(frame_enf_previas,orient="vertical",command=canvas_enf_previas.yview)
        canvas_enf_previas.configure(yscrollcomman=scrollbar_enf_previas.set)
        content_frame_enf_previas = Frame(canvas_enf_previas,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_enf_previas.bind("<Configure>",lambda e: canvas_enf_previas.configure(scrollregion=canvas_enf_previas.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_enf_previas.columnconfigure(0,weight=1)
        ventana_enf_previas.rowconfigure(0,weight=1)
        frame_enf_previas.columnconfigure(0,weight=1)
        frame_enf_previas.rowconfigure(0,weight=1)
        
        # Lista de enfermedades
        lista_enfermedades = ['Alzhéimer','Bebé Prematuro','Cáncer','Diabetes','Enfermedad Autoinmunitaria','Enfermedad Coronaria',
                              'EPOC','Esclerosis múltiple','Esclerosis Tuberosa','Hipertiroidismo','Hipotiroidismo',
                              'Párkinson','Síndrome del cromosoma X frágil','Síndrome de Rett','VIH/SIDA']
        
        # Creamos los botones (checkboxes)
        check_vars = [BooleanVar() for _ in lista_enfermedades]
        for i, enf in enumerate(lista_enfermedades):
            chk=Checkbutton(content_frame_enf_previas,text=enf,variable=check_vars[i],bg="white")
            chk.grid(row=i,column=0,padx=10,pady=5,sticky="w")
            
        # Función para guardar los checkboxes seleccionados
        def guardar_enfermedades():
            enf_seleccionados = [lista_enfermedades[i] for i, var in enumerate(check_vars) if var.get()]
            resultado_enf_previas = ", ".join(enf_seleccionados)
            actualizar_enf_previas(resultado_enf_previas)
            ventana_enf_previas.destroy() # destruimos la ventana

        # Botón para ejecutar el guardado de las enfermedades seleccionadas
        boton_guardar = Button(content_frame_enf_previas, text="Guardar", command=guardar_enfermedades, bg="aquamarine")
        boton_guardar.grid(row=len(lista_enfermedades)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_enf_previas.create_window((0,0),window=content_frame_enf_previas,anchor="nw")
        canvas_enf_previas.grid(row=0,column=0,sticky="nsew")
        scrollbar_enf_previas.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_enf_previas.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_enf_previas.bind_all("<MouseWheel>",_on_mousewheel)
        
    # Botón para mostrar las enfermedades previas
    boton_enf_previas = Button(ventana_formulario, text="Lista de condicionantes", command=mostrar_ventana_enf_previas, bg="aquamarine")
    boton_enf_previas.grid(row=0, column=5, padx=10, pady=5,sticky='w')
    
    # Inclusión de celdas vacías por estética en la ventana del formulario
    etiqueta_blanco3=Label(ventana_formulario,text="",bg="white").grid(row=3,column=0,padx=10,pady=5)
    etiqueta_blanco4=Label(ventana_formulario,text="",bg="white").grid(row=3,column=1,padx=10,pady=5)
    etiqueta_blanco5=Label(ventana_formulario,text="",bg="white").grid(row=3,column=2,padx=10,pady=5)
    etiqueta_blanco6=Label(ventana_formulario,text="",bg="white").grid(row=3,column=3,padx=10,pady=5)
    etiqueta_blanco7=Label(ventana_formulario,text="",bg="white").grid(row=3,column=4,padx=10,pady=5)
    
    
    ##### ENTRADA ANALISIS PSICOLOGICO
    
    etiqueta_analisis_psicologico = Label(ventana_formulario, text="ANALISIS PSICOLOGICO", bg="white").grid(row=4, column=0, padx=10, pady=5, sticky='w')

    
    # DEPRESION
    global resultado_depresion   # declaración de variable global para poder pasarla entre las ventanas
    resultado_depresion = 0      # la incializamos en cero
    
    resultado_D = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_D.grid(row=5, column=1, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_rd(valor):
        resultado_D.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_D.insert(0, str(valor))  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test de depresión
    def mostrar_ventana_depresion():
        ventana_depresion = Toplevel() # las ventanas nuevas se crean mejor con Toplevel
        ventana_depresion.title("Test Diagnóstico del Trastorno Depresivo Mayor según el DSM-V")    
        ventana_depresion.geometry(posicion_formulario)
        ventana_depresion.configure(bg="white")
        ventana_depresion.iconbitmap("iconos/Pantallas.ico")
        ventana_depresion.state('zoomed')

        # Creación de una barra de scroll lateral vertical
        frame_depresion = Frame(ventana_depresion,bg="white") # Primero se crea un frame
        frame_depresion.grid(row=0,column=0,sticky="nsew")
        canvas_depresion=Canvas(frame_depresion,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_depresion = Scrollbar(frame_depresion,orient="vertical",command=canvas_depresion.yview)
        canvas_depresion.configure(yscrollcomman=scrollbar_depresion.set)
        content_frame_depresion = Frame(canvas_depresion,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_depresion.bind("<Configure>",lambda e: canvas_depresion.configure(scrollregion=canvas_depresion.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_depresion.columnconfigure(0,weight=1)
        ventana_depresion.rowconfigure(0,weight=1)
        frame_depresion.columnconfigure(0,weight=1)
        frame_depresion.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        criterios_dsmv = [
            "Estado de ánimo deprimido la mayor parte del día, casi todos los días.",
            "Disminución importante del interés o el placer por todas o casi todas las actividades.",
            "Pérdida importante de peso sin hacer dieta o aumento de peso, o disminución o aumento del apetito.",
            "Insomnio o hipersomnia casi todos los días.",
            "Agitación o enlentecimiento psicomotor casi todos los días.",
            "Fatiga o pérdida de energía casi todos los días.",
            "Sentimiento de inutilidad o culpabilidad excesiva o inapropiada.",
            "Disminución de la capacidad para pensar o concentrarse, o para tomar decisiones.",
            "Pensamientos de muerte recurrentes, ideas suicidas recurrentes sin un plan determinado, intento de suicidio o un plan específico para llevarlo a cabo.",
            "Los síntomas causan malestar clínicamente significativo o deterioro en lo social, laboral u otras áreas importantes del funcionamiento.",
            "El episodio no se puede atribuir a los efectos fisiológicos de una sustancia o de otra afección médica.",
            "Nunca ha habido un episodio maníaco o hipomaníaco."
        ]

        check_vars = [BooleanVar() for _ in criterios_dsmv]
        for i, criterio in enumerate(criterios_dsmv):
            chk = Checkbutton(content_frame_depresion, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_depresion():
            total_seleccionados = sum(var.get() for var in check_vars)
            actualizar_rd(total_seleccionados)
            ventana_depresion.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_depresion, text="Calcular", command=calcular_depresion, bg="aquamarine")
        boton_calcular.grid(row=len(criterios_dsmv) + 1, column=1, padx=10, pady=10)

        # Empaquetamos todo el contenido en nuestra ventana
        canvas_depresion.create_window((0,0),window=content_frame_depresion,anchor="nw")
        canvas_depresion.grid(row=0,column=0,sticky="nsew")
        scrollbar_depresion.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_depresion.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_depresion.bind_all("<MouseWheel>",_on_mousewheel)
        
    # Botón para mostrar el test de depresión
    boton_depresion = Button(ventana_formulario, text="Trastorno Depresivo Mayor (TDM)", command=mostrar_ventana_depresion, bg="aquamarine")
    boton_depresion.grid(row=5, column=0, padx=10, pady=5,sticky='w')
    

    # ESQUIZOFRENIA
    global resultado_esquizofrenia   # declaración de variable global para poder pasarla entre las ventanas
    resultado_esquizofrenia = 0      # la incializamos en cero
    
    resultado_E = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_E.grid(row=6, column=1, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_re(valor):
        resultado_E.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_E.insert(0, str(valor))  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test de esquizofrenia
    def mostrar_ventana_esquizofrenia():
        ventana_esquizofrenia = Toplevel() 
        ventana_esquizofrenia.title("Test Diagnóstico de la Esquizofrenia según el DSM-V")    
        ventana_esquizofrenia.geometry(posicion_formulario)
        ventana_esquizofrenia.configure(bg="white")
        ventana_esquizofrenia.iconbitmap("iconos/Pantallas.ico")
        ventana_esquizofrenia.state('zoomed')
        
        # Creación de una barra de scroll lateral vertical
        frame_esquizofrenia = Frame(ventana_esquizofrenia,bg="white") # Primero se crea un frame
        frame_esquizofrenia.grid(row=0,column=0,sticky="nsew")
        canvas_esquizofrenia=Canvas(frame_esquizofrenia,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_esquizofrenia = Scrollbar(frame_esquizofrenia,orient="vertical",command=canvas_esquizofrenia.yview)
        canvas_esquizofrenia.configure(yscrollcomman=scrollbar_esquizofrenia.set)
        content_frame_esquizofrenia = Frame(canvas_esquizofrenia,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_esquizofrenia.bind("<Configure>",lambda e: canvas_esquizofrenia.configure(scrollregion=canvas_esquizofrenia.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_esquizofrenia.columnconfigure(0,weight=1)
        ventana_esquizofrenia.rowconfigure(0,weight=1)
        frame_esquizofrenia.columnconfigure(0,weight=1)
        frame_esquizofrenia.rowconfigure(0,weight=1)

        # Entrada de las preguntas y la respuesta
        criterios_esquizofrenia = [
            "Delirios",
            "Alucinaciones",
            "Habla desorganizada",
            "Comportamiento extremadamente desorganizado o catatónico",
            "Síntomas negativos (p. ej., disminución de la motivación y disminución de la expresividad)",
            "Disminución significativa del nivel de funcionamiento en una o más áreas principales (trabajo, relaciones interpersonales, autocuidado).",
            "Signos continuos de la alteración persisten durante un periodo de al menos 6 meses",
            "La alteración no es atribuible a los efectos fisiológicos de una sustancia u otra afección médica",
            "Antecedentes de trastorno del espectro autista o un trastorno de comunicación de inicio en la infancia con delirios o alucinaciones prominentes."
        ]

        check_vars = [BooleanVar() for _ in criterios_esquizofrenia]
        for i, criterio in enumerate(criterios_esquizofrenia):
            chk = Checkbutton(content_frame_esquizofrenia, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_esquizofrenia():
            total_seleccionados = sum(var.get() for var in check_vars)
            actualizar_re(total_seleccionados)
            ventana_esquizofrenia.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_esquizofrenia, text="Calcular", command=calcular_esquizofrenia, bg="aquamarine")
        boton_calcular.grid(row=len(criterios_esquizofrenia)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_esquizofrenia.create_window((0,0),window=content_frame_esquizofrenia,anchor="nw")
        canvas_esquizofrenia.grid(row=0,column=0,sticky="nsew")
        scrollbar_esquizofrenia.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_esquizofrenia.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_esquizofrenia.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test de esquizofrenia
    boton_esquizofrenia = Button(ventana_formulario, text="Esquizofrenia", command=mostrar_ventana_esquizofrenia, bg="aquamarine")
    boton_esquizofrenia.grid(row=6, column=0, padx=10, pady=5,sticky='w')
    

    # BIPOLARIDAD
    global resultado_bipolaridad_maniaco   # declaración de variable global para poder pasarla entre las ventanas
    global resultado_bipolaridad_depresivo
    resultado_bipolaridad_maniaco = 0      # la incializamos en cero
    resultado_bipolaridad_depresivo = 0
    
    etiqueta_B_maniaco = Label(ventana_formulario, text="Episodio Maníaco", bg="white").grid(row=8, column=1, padx=10, pady=5, sticky='w')
    resultado_B_maniaco = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_B_maniaco.grid(row=8, column=2, padx=10, pady=5)

    etiqueta_B_depresivo = Label(ventana_formulario, text="Episodio Depresivo", bg="white").grid(row=8, column=3, padx=10, pady=5, sticky='w')
    resultado_B_depresivo = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_B_depresivo.grid(row=8, column=4, padx=10, pady=5)


    # Función para actualizar el valor de la entrada
    def actualizar_rb_maniaco(valor):
        resultado_B_maniaco.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_B_maniaco.insert(0, str(valor))  # inserta el nuevo valor
        return valor
    
    # Función para actualizar el valor de la entrada
    def actualizar_rb_depresivo(valor):
        resultado_B_depresivo.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_B_depresivo.insert(0, str(valor))  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test de bipolaridad
    def mostrar_ventana_bipolaridad():
        ventana_bipolaridad = Toplevel() 
        ventana_bipolaridad.title("Test Diagnóstico del Trastorno de Bipolaridad según el DSM-V")    
        ventana_bipolaridad.geometry(posicion_formulario)
        ventana_bipolaridad.configure(bg="white")
        ventana_bipolaridad.iconbitmap("iconos/Pantallas.ico")
        ventana_bipolaridad.state('zoomed')

        # Creación de una barra de scroll lateral vertical
        frame_bipolaridad = Frame(ventana_bipolaridad,bg="white") # Primero se crea un frame
        frame_bipolaridad.grid(row=0,column=0,sticky="nsew")
        canvas_bipolaridad=Canvas(frame_bipolaridad,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_bipolaridad = Scrollbar(frame_bipolaridad,orient="vertical",command=canvas_bipolaridad.yview)
        canvas_bipolaridad.configure(yscrollcomman=scrollbar_bipolaridad.set)
        content_frame_bipolaridad = Frame(canvas_bipolaridad,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_bipolaridad.bind("<Configure>",lambda e: canvas_bipolaridad.configure(scrollregion=canvas_bipolaridad.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_bipolaridad.columnconfigure(0,weight=1)
        ventana_bipolaridad.rowconfigure(0,weight=1)
        frame_bipolaridad.columnconfigure(0,weight=1)
        frame_bipolaridad.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        criterios_bipolaridad_maniaco = [
        "Estado de ánimo anormalmente elevado o irritable.",
        "Aumento significativo de la actividad o energía.",
        "Aumento de la autoestima o sentimiento de grandeza.",
        "Disminución de la necesidad de dormir.",
        "Participación excesiva en actividades de alto riesgo.",
        "El episodio debe causar un deterioro significativo en el funcionamiento social o laboral.",
        "El episodio no se puede contribuir a los efectos fisiológicos de una sustancia o de otra afección médica.",
        ]
        
        criterios_bipolaridad_depresivo = [
        "Estado de ánimo deprimido la mayor parte del día.",
        "Tristeza profunda.",
        "Disminución importante del interés o placer por todas o casi todas las actividades.",
        "Pérdida de peso sin hacer dieta o aumento de peso.",
        "Insomnio o hipersomnia.",
        "Agitación o retraso psicomotor.",
        "Fatiga o pérdida de la energía.",
        "Sentimientos de inutilidad o de culpabilidad excesiva o inapropiada.",
        "Disminución de la capacidad para pensar, concentrarse, o tomar decisiones.",
        "Pensamientos de muerte recurrentes.",
        "El episodio debe causar un deterioro significativo en el funcionamiento social o laboral.",
        ]
        
        entrada_maniaco = Label(content_frame_bipolaridad,text="Episodio Maníaco",bg="white").grid(row=0,column=0,padx=10,pady=5,sticky='w')
        entrada_depresivo = Label(content_frame_bipolaridad,text="Episodio Depresivo",bg="white").grid(row=0,column=1,padx=10,pady=5,sticky='w')

        check_vars_maniaco = [BooleanVar() for _ in criterios_bipolaridad_maniaco]
        for i, criterio in enumerate(criterios_bipolaridad_maniaco):
            chk = Checkbutton(content_frame_bipolaridad, text=criterio, variable=check_vars_maniaco[i], bg="white")
            chk.grid(row=i+1, column=0, padx=10, pady=5, sticky='w')
            
        check_vars_depresivo = [BooleanVar() for _ in criterios_bipolaridad_depresivo]
        for i, criterio in enumerate(criterios_bipolaridad_depresivo):
            chk = Checkbutton(content_frame_bipolaridad, text=criterio, variable=check_vars_depresivo[i], bg="white")
            chk.grid(row=i+1, column=1, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_bipolaridad():
            total_seleccionados_maniaco = sum(var.get() for var in check_vars_maniaco)
            total_seleccionados_depresivo = sum(var.get() for var in check_vars_depresivo)
            actualizar_rb_maniaco(total_seleccionados_maniaco)
            actualizar_rb_depresivo(total_seleccionados_depresivo)
            ventana_bipolaridad.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_bipolaridad, text="Calcular", command=calcular_bipolaridad, bg="aquamarine")
        boton_calcular.grid(row=len(criterios_bipolaridad_depresivo)+1, column=2, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_bipolaridad.create_window((0,0),window=content_frame_bipolaridad,anchor="nw")
        canvas_bipolaridad.grid(row=0,column=0,sticky="nsew")
        scrollbar_bipolaridad.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_bipolaridad.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_bipolaridad.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test de bipolaridad
    boton_bipolaridad = Button(ventana_formulario, text="Trastorno de Bipolaridad (TB)", command=mostrar_ventana_bipolaridad, bg="aquamarine")
    boton_bipolaridad.grid(row=8, column=0, padx=10, pady=5,sticky='w')
    
    # ESPECTRO AUTISTA
    global resultado_autismo   # declaración de variable global para poder pasarla entre las ventanas
    resultado_autismo = 0      # la incializamos en cero
    
    resultado_AUT = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_AUT.grid(row=7, column=1, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_autismo(valor):
        resultado_AUT.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_AUT.insert(0, str(valor))  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test de bipolaridad
    def mostrar_ventana_autismo():
        ventana_autismo = Toplevel() 
        ventana_autismo.title("Test Diagnóstico del Trastorno del Espectro Autista según el DSM-V")    
        ventana_autismo.geometry(posicion_formulario)
        ventana_autismo.configure(bg="white")
        ventana_autismo.iconbitmap("iconos/Pantallas.ico")
        ventana_autismo.state('zoomed')

        # Creación de una barra de scroll lateral vertical
        frame_autismo = Frame(ventana_autismo,bg="white") # Primero se crea un frame
        frame_autismo.grid(row=0,column=0,sticky="nsew")
        canvas_autismo=Canvas(frame_autismo,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_autismo = Scrollbar(frame_autismo,orient="vertical",command=canvas_autismo.yview)
        canvas_autismo.configure(yscrollcomman=scrollbar_autismo.set)
        content_frame_autismo = Frame(canvas_autismo,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_autismo.bind("<Configure>",lambda e: canvas_autismo.configure(scrollregion=canvas_autismo.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_autismo.columnconfigure(0,weight=1)
        ventana_autismo.rowconfigure(0,weight=1)
        frame_autismo.columnconfigure(0,weight=1)
        frame_autismo.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        criterios_autismo = [
        "Deficiencias persistentes en la comunicación e interacción sociales.",
        "Patrones restrictivos y repetitivos de comportamiento, intereses o actividades.",
        "Síntomas presentes en las primeras fases del desarrollo, que causan un deterioro clínicamente significativo en áreas importantes del funcionamiento habitual.",
        "Estos síntomas no deben explicarse mejor por la discapacidad intelectual o por el retraso global del desarrollo.",
        ]

        check_vars = [BooleanVar() for _ in criterios_autismo]
        for i, criterio in enumerate(criterios_autismo):
            chk = Checkbutton(content_frame_autismo, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_autismo():
            total_seleccionados = sum(var.get() for var in check_vars)
            actualizar_autismo(total_seleccionados)
            ventana_autismo.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_autismo, text="Calcular", command=calcular_autismo, bg="aquamarine")
        boton_calcular.grid(row=len(criterios_autismo)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_autismo.create_window((0,0),window=content_frame_autismo,anchor="nw")
        canvas_autismo.grid(row=0,column=0,sticky="nsew")
        scrollbar_autismo.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_autismo.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_autismo.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test de autismo
    boton_autismo = Button(ventana_formulario, text="Trastorno del Espectro Autista (TEA)", command=mostrar_ventana_autismo, bg="aquamarine")
    boton_autismo.grid(row=7, column=0, padx=10, pady=5,sticky='w')
    
    # TOC
    global resultado_toc   # declaración de variable global para poder pasarla entre las ventanas
    resultado_toc = 0      # la incializamos en cero
    
    resultado_T = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_T.grid(row=9, column=1, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_toc(valor):
        resultado_T.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_T.insert(0, str(valor))  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test de bipolaridad
    def mostrar_ventana_toc():
        ventana_toc = Toplevel() 
        ventana_toc.title("Test Diagnóstico del Trastorno Obsesivo-Compulsivo según el DSM-V")    
        ventana_toc.geometry(posicion_formulario)
        ventana_toc.configure(bg="white")
        ventana_toc.iconbitmap("iconos/Pantallas.ico")
        ventana_toc.state('zoomed')

        # Creación de una barra de scroll lateral vertical
        frame_toc = Frame(ventana_toc,bg="white") # Primero se crea un frame
        frame_toc.grid(row=0,column=0,sticky="nsew")
        canvas_toc =Canvas(frame_toc,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_toc = Scrollbar(frame_toc,orient="vertical",command=canvas_toc.yview)
        canvas_toc.configure(yscrollcomman=scrollbar_toc.set)
        content_frame_toc = Frame(canvas_toc,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_toc.bind("<Configure>",lambda e: canvas_toc.configure(scrollregion=canvas_toc.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_toc.columnconfigure(0,weight=1)
        ventana_toc.rowconfigure(0,weight=1)
        frame_toc.columnconfigure(0,weight=1)
        frame_toc.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        criterios_toc = [
        "Pensamientos, impulsos o imágenes recurrentes y persistentes que causan ansiedad o malestar importante. ",
        "El paciente intenta ignorar o suprimir los pensamientos o neutralizarlos con una compulsión.",
        "Comportamientos o actos mentales repetitivos realizados como respuesta a una obsesión.",
        "Comportamientos realizados para disminuir la ansiedad o malestar, o evitar algún suceso o situación temida.",
        "Los síntomas deben ocupar mucho tiempo, causar malestar significativo o deterioro en diversas áreas de la vida.",
        "No pueden ser atribuidos a sustancias o afecciones médicas.",
        "El sujeto tiene antecedentes de trastornos de tics.",
        ]

        check_vars = [BooleanVar() for _ in criterios_toc]
        for i, criterio in enumerate(criterios_toc):
            chk = Checkbutton(content_frame_toc, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_toc():
            total_seleccionados = sum(var.get() for var in check_vars)
            actualizar_toc(total_seleccionados)
            ventana_toc.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_toc, text="Calcular", command=calcular_toc, bg="aquamarine")
        boton_calcular.grid(row=len(criterios_toc)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_toc.create_window((0,0),window=content_frame_toc,anchor="nw")
        canvas_toc.grid(row=0,column=0,sticky="nsew")
        scrollbar_toc.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_toc.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_toc.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test de toc
    boton_toc = Button(ventana_formulario, text="Trastorno Obsesivo-Compulsivo (TOC)", command=mostrar_ventana_toc, bg="aquamarine")
    boton_toc.grid(row=9, column=0, padx=10, pady=5,sticky='w')

    # ANSIEDAD
    global resultado_aeg   # declaración de variable global para poder pasarla entre las ventanas
    resultado_toc = 0      # la incializamos en cero
    
    resultado_AEG = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_AEG.grid(row=10, column=1, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_aeg(valor):
        resultado_AEG.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_AEG.insert(0, str(valor))  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test de bipolaridad
    def mostrar_ventana_aeg():
        ventana_aeg = Toplevel() 
        ventana_aeg.title("Test Diagnóstico del Trastorno de Ansiedad Generalizada según el DSM-V")    
        ventana_aeg.geometry(posicion_formulario)
        ventana_aeg.configure(bg="white")
        ventana_aeg.iconbitmap("iconos/Pantallas.ico")
        ventana_aeg.state('zoomed')

        # Creación de una barra de scroll lateral vertical
        frame_aeg = Frame(ventana_aeg,bg="white") # Primero se crea un frame
        frame_aeg.grid(row=0,column=0,sticky="nsew")
        canvas_aeg =Canvas(frame_aeg,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_aeg = Scrollbar(frame_aeg,orient="vertical",command=canvas_aeg.yview)
        canvas_aeg.configure(yscrollcomman=scrollbar_aeg.set)
        content_frame_aeg = Frame(canvas_aeg,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_aeg.bind("<Configure>",lambda e: canvas_aeg.configure(scrollregion=canvas_aeg.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_aeg.columnconfigure(0,weight=1)
        ventana_aeg.rowconfigure(0,weight=1)
        frame_aeg.columnconfigure(0,weight=1)
        frame_aeg.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        criterios_aeg = [
        "Ansiedad y preocupación excesiva en relación con diversos sucesos o actividades.",
        "Dificultad para controlar la preocupación.",
        "Inquietud, sensación de estar atrapado o con los nervios de punta.",
        "Facilidad para fatigarse.",
        "Dificultad para concentrarse o quedarse con la mente en blanco.",
        "Irritabilidad.",
        "Tensión muscular.",
        "Problemas de sueño, como dificultad para dormirse o continuar durmiendo.",
        "Malestar clínicamente significativo o deterioro en áreas importantes del funcionamiento.",
        "No está causada por sustancias o condiciones médicas y no es explicable mejor por otro trastorno mental.",
        ]

        check_vars = [BooleanVar() for _ in criterios_aeg]
        for i, criterio in enumerate(criterios_aeg):
            chk = Checkbutton(content_frame_aeg, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_aeg():
            total_seleccionados = sum(var.get() for var in check_vars)
            actualizar_aeg(total_seleccionados)
            ventana_aeg.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_aeg, text="Calcular", command=calcular_aeg, bg="aquamarine")
        boton_calcular.grid(row=len(criterios_aeg)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_aeg.create_window((0,0),window=content_frame_aeg,anchor="nw")
        canvas_aeg.grid(row=0,column=0,sticky="nsew")
        scrollbar_aeg.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_aeg.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_aeg.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test de ansiedad
    boton_aeg = Button(ventana_formulario, text="Trastorno de Ansiedad Generalizada (TAG)", command=mostrar_ventana_aeg, bg="aquamarine")
    boton_aeg.grid(row=10, column=0, padx=10, pady=5,sticky='w')
    
    ###### ENTRADA ANALISIS GENÉTICO
    
    etiqueta_analisis_genetico = Label(ventana_formulario, text="ANALISIS GENÉTICO", bg="white").grid(row=4, column=5, padx=10, pady=5, sticky='w')

    # GENES DEPRESION
    global resultado_genes_d   # declaración de variable global para poder pasarla entre las ventanas
    resultado_genes_d = 0      # la incializamos en cero
    
    resultado_G_d = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_G_d.grid(row=5, column=6, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_rg_d(valor):
        resultado_G_d.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_G_d.insert(0, valor)  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test genético
    def mostrar_ventana_genes_depresion():
        ventana_genes_d = Toplevel() # las ventanas nuevas se crean mejor con Toplevel
        ventana_genes_d.title("Marcadores genéticos para el Trastorno de Depresión Mayor")    
        ventana_genes_d.geometry(posicion_formulario)
        ventana_genes_d.configure(bg="white")
        ventana_genes_d.iconbitmap("iconos/Pantallas.ico")
        ventana_genes_d.state('zoomed')
        
        # Creación de una barra de scroll lateral vertical
        frame_genes_d = Frame(ventana_genes_d,bg="white") # Primero se crea un frame
        frame_genes_d.grid(row=0,column=0,sticky="nsew")
        canvas_genes_d=Canvas(frame_genes_d,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_genes_d = Scrollbar(frame_genes_d,orient="vertical",command=canvas_genes_d.yview)
        canvas_genes_d.configure(yscrollcomman=scrollbar_genes_d.set)
        content_frame_genes_d = Frame(canvas_genes_d,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_genes_d.bind("<Configure>",lambda e: canvas_genes_d.configure(scrollregion=canvas_genes_d.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_genes_d.columnconfigure(0,weight=1)
        ventana_genes_d.rowconfigure(0,weight=1)
        frame_genes_d.columnconfigure(0,weight=1)
        frame_genes_d.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        genes_d = ["SLC6A4","FKBP5","CYP2D6","TPH2","DRD2","HTR2A","GRM5","GRM7","CRHR1","CACNA1C","PCLO"]

        check_vars = [BooleanVar() for _ in genes_d]
        for i, criterio in enumerate(genes_d):
            chk = Checkbutton(content_frame_genes_d, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_genes_d():
            genes_seleccionados_d = [genes_d[i] for i, var in enumerate(check_vars) if var.get()]
            resultado_genes_d = ", ".join(genes_seleccionados_d)
            actualizar_rg_d(resultado_genes_d)
            ventana_genes_d.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_genes_d, text="Guardar", command=calcular_genes_d, bg="aquamarine")
        boton_calcular.grid(row=len(genes_d)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_genes_d.create_window((0,0),window=content_frame_genes_d,anchor="nw")
        canvas_genes_d.grid(row=0,column=0,sticky="nsew")
        scrollbar_genes_d.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_genes_d.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_genes_d.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test de depresión
    boton_genes_d = Button(ventana_formulario, text="Trastorno Depresivo Mayor (TDM)", command=mostrar_ventana_genes_depresion, bg="aquamarine")
    boton_genes_d.grid(row=5, column=5, padx=10, pady=5,sticky='w')

# GENES ESQUIZOFRENIA
    global resultado_genes_e   # declaración de variable global para poder pasarla entre las ventanas
    resultado_genes_e = 0      # la incializamos en cero
    
    resultado_G_e = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_G_e.grid(row=6, column=6, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_rg_e(valor):
        resultado_G_e.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_G_e.insert(0, valor)  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test genético
    def mostrar_ventana_genes_e():
        ventana_genes_e = Toplevel() # las ventanas nuevas se crean mejor con Toplevel
        ventana_genes_e.title("Marcadores genéticos para la Esquizofrenia")    
        ventana_genes_e.geometry(posicion_formulario)
        ventana_genes_e.configure(bg="white")
        ventana_genes_e.iconbitmap("iconos/Pantallas.ico")
        ventana_genes_e.state('zoomed')
        
        # Creación de una barra de scroll lateral vertical
        frame_genes_e = Frame(ventana_genes_e,bg="white") # Primero se crea un frame
        frame_genes_e.grid(row=0,column=0,sticky="nsew")
        canvas_genes_e=Canvas(frame_genes_e,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_genes_e = Scrollbar(frame_genes_e,orient="vertical",command=canvas_genes_e.yview)
        canvas_genes_e.configure(yscrollcomman=scrollbar_genes_e.set)
        content_frame_genes_e = Frame(canvas_genes_e,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_genes_e.bind("<Configure>",lambda e: canvas_genes_e.configure(scrollregion=canvas_genes_e.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_genes_e.columnconfigure(0,weight=1)
        ventana_genes_e.rowconfigure(0,weight=1)
        frame_genes_e.columnconfigure(0,weight=1)
        frame_genes_e.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        genes_e = ["AKT1","ABCB1","ANK3","AVPR1A","BACE1","BECN1","BRD1","CACNA1C","CHI3L1","CHRNA7","COMT","CSMD1","DAOA","DISC1","DISC2","DRD3","FEZ1","FOXP2","GNAS","GRIA1","GRM5","HTR2A","KMO","LRRTM1","MAGI2","MAP2K7","MAP6","MBP","MTHFR","NCAM1","NLGN2","NOS1AP","NOTCH4","NR4A2","NRG1","NRXN1","PPP1R1B","PPP3R1","PRODH","PTGS2","RTN4R","SETD1A","SHANK3","SLC1A1","SRGAP3","SRR","SYNGAP1","TAAR1","TBX1","TCF4","YWHAH","ZDHHC8","ZIC2"]

        check_vars = [BooleanVar() for _ in genes_e]
        for i, criterio in enumerate(genes_e):
            chk = Checkbutton(content_frame_genes_e, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_genes_e():
            genes_seleccionados_e = [genes_e[i] for i, var in enumerate(check_vars) if var.get()]
            resultado_genes_e = ", ".join(genes_seleccionados_e)
            actualizar_rg_e(resultado_genes_e)
            ventana_genes_e.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_genes_e, text="Guardar", command=calcular_genes_e, bg="aquamarine")
        boton_calcular.grid(row=len(genes_e)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_genes_e.create_window((0,0),window=content_frame_genes_e,anchor="nw")
        canvas_genes_e.grid(row=0,column=0,sticky="nsew")
        scrollbar_genes_e.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_genes_e.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_genes_e.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test
    boton_genes_e = Button(ventana_formulario, text="Esquizofrenia", command=mostrar_ventana_genes_e, bg="aquamarine")
    boton_genes_e.grid(row=6, column=5, padx=10, pady=5,sticky='w')

    # GENES BIPOLARIDAD
    global resultado_genes_b   # declaración de variable global para poder pasarla entre las ventanas
    resultado_genes_b = 0      # la incializamos en cero
    
    resultado_G_b = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_G_b.grid(row=8, column=6, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_rg_b(valor):
        resultado_G_b.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_G_b.insert(0, valor)  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test genético
    def mostrar_ventana_genes_b():
        ventana_genes_b = Toplevel() # las ventanas nuevas se crean mejor con Toplevel
        ventana_genes_b.title("Marcadores genéticos para el Trastorno Bipolar")    
        ventana_genes_b.geometry(posicion_formulario)
        ventana_genes_b.configure(bg="white")
        ventana_genes_b.iconbitmap("iconos/Pantallas.ico")
        ventana_genes_b.state('zoomed')
        
        # Creación de una barra de scroll lateral vertical
        frame_genes_b = Frame(ventana_genes_b,bg="white") # Primero se crea un frame
        frame_genes_b.grid(row=0,column=0,sticky="nsew")
        canvas_genes_b=Canvas(frame_genes_b,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_genes_b = Scrollbar(frame_genes_b,orient="vertical",command=canvas_genes_b.yview)
        canvas_genes_b.configure(yscrollcomman=scrollbar_genes_b.set)
        content_frame_genes_b = Frame(canvas_genes_b,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_genes_b.bind("<Configure>",lambda e: canvas_genes_b.configure(scrollregion=canvas_genes_b.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_genes_b.columnconfigure(0,weight=1)
        ventana_genes_b.rowconfigure(0,weight=1)
        frame_genes_b.columnconfigure(0,weight=1)
        frame_genes_b.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        genes_b = ["ANK3","BDNF","CACNA1C","CLOCK","COMT","DGKH","DRD1","GAD1","GRIN2A","GSK3B","HTR2A","INS","MTHFR","NR3C1","NR3C1","NRG1","RELN","S100B","SLC6A4","ZNF804A"]

        check_vars = [BooleanVar() for _ in genes_b]
        for i, criterio in enumerate(genes_b):
            chk = Checkbutton(content_frame_genes_b, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_genes_b():
            genes_seleccionados_b = [genes_b[i] for i, var in enumerate(check_vars) if var.get()]
            resultado_genes_b = ", ".join(genes_seleccionados_b)
            actualizar_rg_b(resultado_genes_b)
            ventana_genes_b.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_genes_b, text="Guardar", command=calcular_genes_b, bg="aquamarine")
        boton_calcular.grid(row=len(genes_b)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_genes_b.create_window((0,0),window=content_frame_genes_b,anchor="nw")
        canvas_genes_b.grid(row=0,column=0,sticky="nsew")
        scrollbar_genes_b.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_genes_b.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_genes_b.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test
    boton_genes_b = Button(ventana_formulario, text="Trastorno Bipolar (TB)", command=mostrar_ventana_genes_b, bg="aquamarine")
    boton_genes_b.grid(row=8, column=5, padx=10, pady=5,sticky='w')

    # GENES AUTISMO
    global resultado_genes_a   # declaración de variable global para poder pasarla entre las ventanas
    resultado_genes_a = 0      # la incializamos en cero
    
    resultado_G_a = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_G_a.grid(row=7, column=6, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_rg_a(valor):
        resultado_G_a.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_G_a.insert(0, valor)  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test genético
    def mostrar_ventana_genes_a():
        ventana_genes_a = Toplevel() # las ventanas nuevas se crean mejor con Toplevel
        ventana_genes_a.title("Marcadores genéticos para el Trastorno del Espectro Autista")    
        ventana_genes_a.geometry(posicion_formulario)
        ventana_genes_a.configure(bg="white")
        ventana_genes_a.iconbitmap("iconos/Pantallas.ico")
        ventana_genes_a.state('zoomed')
        
        # Creación de una barra de scroll lateral vertical
        frame_genes_a = Frame(ventana_genes_a,bg="white") # Primero se crea un frame
        frame_genes_a.grid(row=0,column=0,sticky="nsew")
        canvas_genes_a=Canvas(frame_genes_a,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_genes_a = Scrollbar(frame_genes_a,orient="vertical",command=canvas_genes_a.yview)
        canvas_genes_a.configure(yscrollcomman=scrollbar_genes_a.set)
        content_frame_genes_a = Frame(canvas_genes_a,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_genes_a.bind("<Configure>",lambda e: canvas_genes_a.configure(scrollregion=canvas_genes_a.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_genes_a.columnconfigure(0,weight=1)
        ventana_genes_a.rowconfigure(0,weight=1)
        frame_genes_a.columnconfigure(0,weight=1)
        frame_genes_a.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        genes_a = ["CHD8","CNTNAP2","NLGN3","NRXN1","SCN1A","SHANK3"]

        check_vars = [BooleanVar() for _ in genes_a]
        for i, criterio in enumerate(genes_a):
            chk = Checkbutton(content_frame_genes_a, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_genes_a():
            genes_seleccionados_a = [genes_a[i] for i, var in enumerate(check_vars) if var.get()]
            resultado_genes_a = ", ".join(genes_seleccionados_a)
            actualizar_rg_a(resultado_genes_a)
            ventana_genes_a.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_genes_a, text="Guardar", command=calcular_genes_a, bg="aquamarine")
        boton_calcular.grid(row=len(genes_a)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_genes_a.create_window((0,0),window=content_frame_genes_a,anchor="nw")
        canvas_genes_a.grid(row=0,column=0,sticky="nsew")
        scrollbar_genes_a.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_genes_a.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_genes_a.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test
    boton_genes_a = Button(ventana_formulario, text="Trastorno del Espectro Autista (TEA)", command=mostrar_ventana_genes_a, bg="aquamarine")
    boton_genes_a.grid(row=7, column=5, padx=10, pady=5,sticky='w')
    
    # GENES TOC
    global resultado_genes_t   # declaración de variable global para poder pasarla entre las ventanas
    resultado_genes_t = 0      # la incializamos en cero
    
    resultado_G_t = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_G_t.grid(row=9, column=6, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_rg_t(valor):
        resultado_G_t.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_G_t.insert(0, valor)  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test genético
    def mostrar_ventana_genes_t():
        ventana_genes_t = Toplevel() # las ventanas nuevas se crean mejor con Toplevel
        ventana_genes_t.title("Marcadores genéticos para el Trastorno Obsesivo-Compulsivo")    
        ventana_genes_t.geometry(posicion_formulario)
        ventana_genes_t.configure(bg="white")
        ventana_genes_t.iconbitmap("iconos/Pantallas.ico")
        ventana_genes_t.state('zoomed')
        
        # Creación de una barra de scroll lateral vertical
        frame_genes_t = Frame(ventana_genes_t,bg="white") # Primero se crea un frame
        frame_genes_t.grid(row=0,column=0,sticky="nsew")
        canvas_genes_t=Canvas(frame_genes_t,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_genes_t = Scrollbar(frame_genes_t,orient="vertical",command=canvas_genes_t.yview)
        canvas_genes_t.configure(yscrollcomman=scrollbar_genes_t.set)
        content_frame_genes_t = Frame(canvas_genes_t,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_genes_t.bind("<Configure>",lambda e: canvas_genes_t.configure(scrollregion=canvas_genes_t.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_genes_t.columnconfigure(0,weight=1)
        ventana_genes_t.rowconfigure(0,weight=1)
        frame_genes_t.columnconfigure(0,weight=1)
        frame_genes_t.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        genes_t = ["HTR2A","SLC6A4"]

        check_vars = [BooleanVar() for _ in genes_t]
        for i, criterio in enumerate(genes_t):
            chk = Checkbutton(content_frame_genes_t, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_genes_t():
            genes_seleccionados_t = [genes_t[i] for i, var in enumerate(check_vars) if var.get()]
            resultado_genes_t = ", ".join(genes_seleccionados_t)
            actualizar_rg_t(resultado_genes_t)
            ventana_genes_t.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_genes_t, text="Guardar", command=calcular_genes_t, bg="aquamarine")
        boton_calcular.grid(row=len(genes_t)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_genes_t.create_window((0,0),window=content_frame_genes_t,anchor="nw")
        canvas_genes_t.grid(row=0,column=0,sticky="nsew")
        scrollbar_genes_t.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_genes_t.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_genes_t.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test
    boton_genes_t = Button(ventana_formulario, text="Trastorno Obsesivo-Compulsivo (TOC)", command=mostrar_ventana_genes_t, bg="aquamarine")
    boton_genes_t.grid(row=9, column=5, padx=10, pady=5,sticky='w')

    # GENES AEG
    global resultado_genes_aeg   # declaración de variable global para poder pasarla entre las ventanas
    resultado_genes_aeg = 0      # la incializamos en cero
    
    resultado_G_aeg = Entry(ventana_formulario, width=22, bg="aquamarine", fg="dark blue")   # entrada donde se guarda el resultado del test
    resultado_G_aeg.grid(row=10, column=6, padx=10, pady=5)

    # Función para actualizar el valor de la entrada
    def actualizar_rg_aeg(valor):
        resultado_G_aeg.delete(0, END)  # borra si hay algún contenido previo en la entrada
        resultado_G_aeg.insert(0, valor)  # inserta el nuevo valor
        return valor
    
    # Función para mostrar la ventana del test genético
    def mostrar_ventana_genes_aeg():
        ventana_genes_aeg = Toplevel() # las ventanas nuevas se crean mejor con Toplevel
        ventana_genes_aeg.title("Marcadores genéticos para el Trastorno de Ansiedad Generalizada")    
        ventana_genes_aeg.geometry(posicion_formulario)
        ventana_genes_aeg.configure(bg="white")
        ventana_genes_aeg.iconbitmap("iconos/Pantallas.ico")
        ventana_genes_aeg.state('zoomed')
        
        # Creación de una barra de scroll lateral vertical
        frame_genes_aeg = Frame(ventana_genes_aeg,bg="white") # Primero se crea un frame
        frame_genes_aeg.grid(row=0,column=0,sticky="nsew")
        canvas_genes_aeg=Canvas(frame_genes_aeg,bg="white") # Ahora creamos un canvas y el scrollbar
        scrollbar_genes_aeg = Scrollbar(frame_genes_aeg,orient="vertical",command=canvas_genes_aeg.yview)
        canvas_genes_aeg.configure(yscrollcomman=scrollbar_genes_aeg.set)
        content_frame_genes_aeg = Frame(canvas_genes_aeg,bg="white") # En el content metemos todo
        # Aquí se configura el canvas y el scrollbar dentro del content frame
        content_frame_genes_aeg.bind("<Configure>",lambda e: canvas_genes_aeg.configure(scrollregion=canvas_genes_aeg.bbox("all")))
        # Permitimos que la ventana puede hacerse más grande o más pequeña (el mínimo sería nuestro tamaño original, el máximo fullscreen)
        ventana_genes_aeg.columnconfigure(0,weight=1)
        ventana_genes_aeg.rowconfigure(0,weight=1)
        frame_genes_aeg.columnconfigure(0,weight=1)
        frame_genes_aeg.rowconfigure(0,weight=1)
        
        # Entrada de las preguntas y la respuesta
        genes_aeg = ["SLC6A4"]

        check_vars = [BooleanVar() for _ in genes_aeg]
        for i, criterio in enumerate(genes_aeg):
            chk = Checkbutton(content_frame_genes_aeg, text=criterio, variable=check_vars[i], bg="white")
            chk.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # Función para contar los checkboxes seleccionados y actualizar el resultado
        def calcular_genes_aeg():
            genes_seleccionados_aeg = [genes_aeg[i] for i, var in enumerate(check_vars) if var.get()]
            resultado_genes_aeg = ", ".join(genes_seleccionados_aeg)
            actualizar_rg_aeg(resultado_genes_aeg)
            ventana_genes_aeg.destroy()

        # Botón para calcular el resultado
        boton_calcular = Button(content_frame_genes_aeg, text="Guardar", command=calcular_genes_aeg, bg="aquamarine")
        boton_calcular.grid(row=len(genes_aeg)+1, column=1, padx=10, pady=10)
        
        # Empaquetamos todo el contenido en nuestra ventana
        canvas_genes_aeg.create_window((0,0),window=content_frame_genes_aeg,anchor="nw")
        canvas_genes_aeg.grid(row=0,column=0,sticky="nsew")
        scrollbar_genes_aeg.grid(row=0,column=1,sticky="ns")
        
        # Función para que podamos mover la scrollbar con el ratón
        def _on_mousewheel(event):
            canvas_genes_aeg.yviewscroll(int(-1*(event.delta/120)),"units")
        canvas_genes_aeg.bind_all("<MouseWheel>",_on_mousewheel)

    # Botón para mostrar el test
    boton_genes_aeg = Button(ventana_formulario, text="Trastorno de Ansiedad Generalizada (TAG)", command=mostrar_ventana_genes_aeg, bg="aquamarine")
    boton_genes_aeg.grid(row=10, column=5, padx=10, pady=5,sticky='w')

    
##### ENVIO FORMULARIO

    # Función para enviar el formulario
    def enviar_formulario(nombre,apellidos,edad,sexo,genero):
        if validar_nombre(nombre) and validar_apellidos(apellidos) and validar_sexo(sexo) and validar_genero(genero):
            
            # Aviso de formulario completado correctamente
            showinfo("Diagnóstico","Datos enviados correctamente")
            
            # Obtener informacion enfermedades previas
            enfermedades_previas = resultado_enf_previas.get()
            
            # Obtener información test psicologico
            text_resultado_d = resultado_D.get()  # obtención del resultado de la entrada del test de depresión
            text_resultado_e = resultado_E.get()  # obtención del resultado de la entrada del test de esquizofrenia
            text_resultado_b_maniaco = resultado_B_maniaco.get()  # obtención del resultado de la entrada del test de bipolaridad
            text_resultado_b_depresivo = resultado_B_depresivo.get()  # obtención del resultado de la entrada del test de bipolaridad
            text_resultado_aut = resultado_AUT.get() # obtención del resultado de la entrada del test de espectro autista
            text_resultado_t = resultado_T.get() # obtención del resultado de la entrada del test de toc
            text_resultado_aeg = resultado_AEG.get() # obtención del resultado de la entrada del test de aeg
            
            # Variables para la predicción de pruebas psicológicas (todas inicializadas en False)
            tiene_depresion_psico = False
            tiene_esquizofrenia_psico = False
            tiene_episodio_maniaco = False
            tiene_episodio_depresivo = False
            tiene_bipolaridad_psico = False
            tiene_autismo_psico = False
            tiene_toc_psico = False
            tiene_aeg_psico = False
                        
            # Algoritmo de prediccion test psicologico
            
            # Depresion
            if text_resultado_d == "":
                text_resultado_d_int = 0
            else:
                text_resultado_d_int = int(text_resultado_d)
            
            if text_resultado_d_int >= 5:
                tiene_depresion_psico = True
            
            # Esquizofrenia
            if text_resultado_e == "":
                text_resultado_e_int = 0
            else:
                text_resultado_e_int = int(text_resultado_e)
                
            if text_resultado_e_int >= 2:
                tiene_esquizofrenia_psico = True
                
            # Bipolaridad episodio maniaco
            if text_resultado_b_maniaco == "":
                text_resultado_b_maniaco_int = 0
            else:
                text_resultado_b_maniaco_int = int(text_resultado_b_maniaco)
            
            if text_resultado_b_maniaco_int >= 3:
                tiene_episodio_maniaco = True
                
            # Bipolaridad episodio depresivo
            if text_resultado_b_depresivo == "":
                text_resultado_b_depresivo_int = 0
            else:
                text_resultado_b_depresivo_int = int(text_resultado_b_depresivo)
            
            if text_resultado_b_depresivo_int >= 5:
                tiene_episodio_depresivo = True
                
            # Calculo final de bipolaridad
            if tiene_episodio_depresivo == True and tiene_episodio_maniaco == True:
                tiene_bipolaridad_psico = True
                
            # Autismo
            if text_resultado_aut ==  "":
                text_resultado_aut_int = 0
            else:
                text_resultado_aut_int = int(text_resultado_aut)
                
            if text_resultado_aut_int >= 1:
                tiene_autismo_psico = True
                
            # TOC
            if text_resultado_t ==  "":
                text_resultado_t_int = 0
            else:
                text_resultado_t_int = int(text_resultado_t)
                
            if text_resultado_t_int >= 1:
                tiene_toc_psico = True
            
            # Ansiedad
            if text_resultado_aeg == "":
                text_resultado_aeg_int = True
            else:
                text_resultado_aeg_int = int(text_resultado_aeg)
            
            if text_resultado_aeg_int >= 3:
                tiene_aeg_psico = True
                
            # Genes comunes
            g_comunes_depresion = ["CACNA1C","GRM5","HTR2A","SLC6A4"]
            g_especificos_depresion = ["FKBP5","CYP2D6","TPH2","DRD2","GRM7","CRHR1","PCLO"]

            g_comunes_esquizoide = ["ANK3","CACNA1C","COMT","GRM5","HTR2A","MTHFR","NRG1","NRXN1","SHANK3"]
            g_especificos_esquizoide = ["ABCB1","AKT1","AVPR1A","BACE1","BECN1","BRD1","CHI3L1","CHRNA7","CSMD1","DAOA",
                                        "DISC1","DISC2","DRD3","FEZ1","FOXP2","GNAS","GRIA1","KMO","LRRTM1","MAGI2","MAP2K7",
                                        "MAP6","MBP","NCAM1","NLGN2","NOS1AP","NOTCH4","NR4A2","PPP1R1B","PPP3R1","PRODH",
                                        "PTGS2","RTN4R","SETD1A","SLC1A1","SRGAP3","SRR","SYNGAP1","TAAR1","TBX1","TCF4",
                                        "YWHAH","ZDHHC8","ZIC2"]
            
            g_comunes_bipolar = ["ANK3","COMT","MTHFR","NRG1","SLC6A4","HTR2A","CACNA1C"]
            g_especificos_bipolar = ["BDNF","CACNA1C","CLOCK","DGKH","DRD1","GAD1","GRIN2A","GSK3B",
                                     "INS","NR3C1","RELN","S100B","ZNF804A"]
            
            g_comunes_autismo = ["NRXN1","SHANK3"]
            g_especificos_autismo = ["CHD8","CNTNAP2","NLGN3","SCN1A"]
            
            g_comunes_toc = ["HTR2A","SLC6A4"]
            
            g_comunes_aeg =["SLC6A4"]
                        
            # Inicialización variables test genético
            comun_d = False
            especifico_d = False
            comun_e = False
            especifico_e = False
            comun_b = False
            especifico_b = False
            comun_a = False
            especifico_a = False
            comun_t = False
            comun_aeg = False
            
            # Obtener información test genético
            genes_seleccionados_d = []
            genes_seleccionados_d = resultado_G_d.get()
            
            genes_seleccionados_e = []
            genes_seleccionados_e = resultado_G_e.get()
            
            genes_seleccionados_b = []
            genes_seleccionados_b = resultado_G_b.get()
            
            genes_seleccionados_a = []
            genes_seleccionados_a = resultado_G_a.get()
            
            genes_seleccionados_t = []
            genes_seleccionados_t = resultado_G_t.get()
            
            genes_seleccionados_aeg = []
            genes_seleccionados_aeg = resultado_G_aeg.get()

            # Se crea archivo de salida
            archivo_salida = open("Resultado_formulario_" + nombre[0] + apellidos[0] + ".txt", 'w')
            archivo_salida.write('RESULTADO DEL FORMULARIO\n\n')
            archivo_salida.write('\nNombre: \t' + nombre)
            archivo_salida.write('\nApellidos: \t' + apellidos)
            archivo_salida.write('\nEdad: \t' + edad)
            archivo_salida.write('\nSexo Biológico: \t' + sexo)
            archivo_salida.write('\nGénero: \t' + genero)
            archivo_salida.write('\n\nENFERMEDADES PREVIAS: \t' + enfermedades_previas)
            archivo_salida.write('\n\tCondicionantes enfermedades previas: \n')
            
            # Aquí escribimos los condicionantes para las enfermedades previas
            if "Alzhéimer" in enfermedades_previas:
                archivo_salida.write("\t\tEl Alzhéimer puede desencadenar TDM o TAG.\n")
            if "Bebé Prematuro" in enfermedades_previas:
                archivo_salida.write("\t\tEl nacimiento prematuro puede desencadenar TEA en la infancia.\n")
            if "Cáncer" in enfermedades_previas:
                archivo_salida.write("\t\tEl Cáncer puede desencadenar TDM o TAG.\n") 
            if "Diabetes" in enfermedades_previas:
                archivo_salida.write("\t\tLa Diabetes puede desencadenar TDM o TAG.\n")
            if "Enfermedad Autoinmune" in enfermedades_previas:
                archivo_salida.write("\t\tLas enferemedades autoinmunes pueden desencadenar TDM o TAG.\n") 
            if "Enfermedad Coronaria" in enfermedades_previas:
                archivo_salida.write("\t\tLas enferemedades coronarias pueden desencadenar TDM o TAG.\n") 
            if "EPOC" in enfermedades_previas:
                archivo_salida.write("\t\tLa EPOC puede desencadenar TDM o TAG.\n")
            if "Esclerosis Múltiple" in enfermedades_previas:
                archivo_salida.write("\t\tLa Esclerosis Múltiple puede desencadenar TDM, TAG o trastornos psicóticos.\n")
            if "Esclerosis Tuberosa" in enfermedades_previas:
                archivo_salida.write("\t\tLa Esclerosis Tuberosa puede desencadenar TDM o TAG.\n")
            if "Hipertiroidismo" in enfermedades_previas:
                archivo_salida.write("\t\tEl Hipertiroidismo puede desencadenar TDM o TAG.\n")
            if "Hipotiroidismo" in enfermedades_previas:
                archivo_salida.write("\t\tEl Hipotiroidismo puede desencadenar TDM o TAG.\n")
            if "Parkinson" in enfermedades_previas:
                archivo_salida.write("\t\tEl Párkinson puede desencadenar TDM o TAG.\n")
            if "Síndrome del cromosoma X frágil" in enfermedades_previas:
                archivo_salida.write("\t\tEl Síndrome del cromosoma X frágil puede desencadenar TEA.\n")
            if "Síndrome de Rett" in enfermedades_previas:
                archivo_salida.write("\t\tEl Síndrome de Rett puede desencadenar TEA.\n")
            if "VIH/SIDA" in enfermedades_previas:
                archivo_salida.write("\t\tEl VIH/SIDA puede desencadenar TDM o TAG.\n")
                   
            archivo_salida.write('\n\nTEST PSICOLOGICO\n\n')
            
            archivo_salida.write('Trastorno Depresivo Mayor (TDM): '+ str(tiene_depresion_psico))
            archivo_salida.write('\n\tResultado del test: ' + text_resultado_d)
            
            archivo_salida.write('\nEsquizofrenia: \t' + str(tiene_esquizofrenia_psico))
            archivo_salida.write('\n\tResultado del test:' + text_resultado_e)
            
            archivo_salida.write('\nResultado Bipolaridad (TB):' + str(tiene_bipolaridad_psico))
            archivo_salida.write('\n\tEpisodio Maníaco: \t' + text_resultado_b_maniaco)
            archivo_salida.write('\n\tEpisodio Depresivo: \t' + text_resultado_b_depresivo)
            
            archivo_salida.write('\nTrastorno del Espectro Autista (TEA): ' + str(tiene_autismo_psico))
            archivo_salida.write('\n\tResultado test: ' + text_resultado_aut)
            
            archivo_salida.write('\nTrastorno Obsesivo-Compulsivo (TOC): ' + str(tiene_toc_psico))
            archivo_salida.write('\n\tResultado del test: ' + text_resultado_t)
            
            archivo_salida.write('\nTrastorno de Ansiedad Generalizada (TAG): ' +str(tiene_aeg_psico))
            archivo_salida.write('\n\tResultado del test: ' + text_resultado_aeg)

            archivo_salida.write('\n\n\nTEST GENÉTICO\n\n')
            
            archivo_salida.write('Trastorno Depresivo Mayor (TDM): ' + genes_seleccionados_d)
            
            for i in g_comunes_depresion:
                if i in genes_seleccionados_d:
                    comun_d = True
            for i in g_especificos_depresion:
                if i in genes_seleccionados_d:
                    especifico_d = True
                    
            if comun_d == True and especifico_d == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores comunes y específicos.')
            if comun_d == True and especifico_d == False:
                archivo_salida.write('\n\tCondicionante genético NO DETERMINANTE.\n\tPresencia de marcadores comunes a otros trastornos mentales. ')
            if comun_d == False and especifico_d == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores específicos. Ausencia de marcadores comunes. ')
            
            if "HTR2A" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador HTR2A es común a TDM, Esquizofrenia, TB y TOC.')
            if "SLC6A4" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador SLC6A4 es común a TDM, TB, TOC y TAG.')
            if "CACNA1C" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador CACNA1C es común a TDM, Esquizofrenia y TB.')
            if "GRM5" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador GRM5 es común a TDM y Esquizofrenia.')      
                
            archivo_salida.write('\nEsquizofrenia: ' + genes_seleccionados_e)
            
            for i in g_comunes_esquizoide:
                if i in genes_seleccionados_e:
                    comun_e = True
            for i in g_especificos_esquizoide:
                if i in genes_seleccionados_e:
                    especifico_e = True
                    
            if comun_e == True and especifico_e == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores comunes y específicos.')
            if comun_e == True and especifico_e == False:
                archivo_salida.write('\n\tCondicionante genético NO DETERMINANTE.\n\tPresencia de marcadores comunes a otros trastornos mentales. ')
            if comun_e == False and especifico_e == True:
                archivo_salida.write('\n\tCondicionante genético de DETERMINANTE.\n\tPresencia de marcadores específicos. Ausencia de marcadores comunes. ')
            
            if "HTR2A" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador HTR2A es común a TDM, Esquizofrenia, TB y TOC.')
            if "NRXN1" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador NRXN1 es común a  Esquizofrenia y TEA.')
            if "CACNA1C" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador CACNA1C es común a TDM, Esquizofrenia y TB.')
            if "GRM5" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador GRM5 es común a TDM y Esquizofrenia.')
            if "SHANK3" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador SHANK3 es común a Esquizofrenia y TEA.')
            if "MTHFR" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador MTHFR es común a TB y Esquizofrenia.')  
            if "COMT" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador COMT es común a TB y Esquizofrenia.')
            if "ANK3" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador ANK3 es común a TB y Esquizofrenia.')
            if "NRG1" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador NRG1 es común a TB y Esquizofrenia.')
                
            archivo_salida.write('\nTrastorno Bipolar (TB): ' + genes_seleccionados_b)
            
            for i in g_comunes_bipolar:
                if i in genes_seleccionados_b:
                    comun_d = True
            for i in g_especificos_bipolar:
                if i in genes_seleccionados_b:
                    especifico_b = True
                    
            if comun_b == True and especifico_b == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores comunes y específicos.')
            if comun_b == True and especifico_b == False:
                archivo_salida.write('\n\tCondicionante genético NO DETERMINANTE.\n\tPresencia de marcadores comunes a otros trastornos mentales. ')
            if comun_b == False and especifico_b == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores específicos. Ausencia de marcadores comunes. ')
            
            if "HTR2A" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador HTR2A es común a TDM, Esquizofrenia, TB y TOC.')
            if "SLC6A4" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador SLC6A4 es común a TDM, TB, TOC y TAG.')
            if "CACNA1C" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador CACNA1C es común a TDM, Esquizofrenia y TB.')
            if "MTHFR" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador MTHFR es común a Esquizofrenia y TB.')  
            if "COMT" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador COMT es común a Esquizofrenia y TB.')
            if "ANK3" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador ANK3 es común a Esquizofrenia y TB.')
            if "NRG1" in genes_seleccionados_d:
                archivo_salida.write('\n\t\tEl marcador NRG1 es común a Esquizofrenia y TB.')  
                
            archivo_salida.write('\nTrastorno del Espectro Autista (TEA): ' + genes_seleccionados_a)
            
            for i in g_comunes_autismo:
                if i in genes_seleccionados_a:
                    comun_a = True
            for i in g_especificos_autismo:
                if i in genes_seleccionados_a:
                    especifico_a = True
                    
            if comun_a == True and especifico_a == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores comunes y específicos.')
            if comun_a == True and especifico_a == False:
                archivo_salida.write('\n\tCondicionante genético NO DETERMINANTE.\n\tPresencia de marcadores comunes a otros trastornos mentales.')
            if comun_a == False and especifico_a == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores específicos. Ausencia de marcadores comunes. ')
            
            if "NRXN1" in genes_seleccionados_a:
                archivo_salida.write('\n\t\tEl marcador NRXN1 es común a  Esquizofrenia y TEA.')
            if "SHANK3" in genes_seleccionados_a:
                archivo_salida.write('\n\t\tEl marcador SHANK3 es común a Esquizofrenia y TEA.') 
                
            archivo_salida.write('\nTrastorno Obsesivo-Compulsivo (TOC): ' + genes_seleccionados_t)
            
            for i in g_comunes_toc:
                if i in genes_seleccionados_t:
                    comun_t = True
                    
            if comun_t == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores comunes y ausencia de marcadores específicos hasta la fecha.')
            
            if "SLC6A4" in genes_seleccionados_t:
                archivo_salida.write('\n\t\tEl marcador SLC6A4 es común a TDM, TB, TOC y TAG.')
            if "HTR2A" in genes_seleccionados_t:
                archivo_salida.write('\n\t\tEl marcador HTR2A es común a TDM, Esquizofrenia, TB y TOC.') 
                
            archivo_salida.write('\nTrastorno de Ansiedad Generalizada (TAG): ' + genes_seleccionados_aeg)
            
            for i in g_comunes_aeg:
                if i in genes_seleccionados_aeg:
                    comun_aeg = True
                    
            if comun_aeg == True:
                archivo_salida.write('\n\tCondicionante genético DETERMINANTE.\n\tPresencia de marcadores comunes y ausencia de marcadore específicos hasta la fecha.')
            
            if "SLC6A4" in genes_seleccionados_aeg:
                archivo_salida.write('\n\t\tEl marcador SLC6A4 es común a TDM, TB, TOC y TAG.')
           
            archivo_salida.write('\n\nFin de formulario\n')
            archivo_salida.close()
            
        else:
            showerror('Error', "¡Es obligatorio rellenar nombre, apellidos, edad, sexo biológico y género!")
    
    # Botón de envío y fin del formulario
    boton_enviar = Button(ventana_formulario,text="Enviar",
                          command = lambda: enviar_formulario(entrada_nombre.get(),entrada_apellidos.get(),entrada_edad.get(),
                                                             seleccion_sexo.get(),seleccion_genero.get()),bg="coral",activebackground="white",activeforeground="blue")
    boton_enviar.grid(row=13,column=6,padx=10,pady=5,sticky='w')

    ventana_formulario.protocol("WM_DELETE_WINDOW", cerrar_formulario)
    ventana_formulario.mainloop()
    
    

#### CONFIGURACION VENTANA DE INICIO

ventana_inicio = Tk()
ventana_inicio.title("SISTEMA DE DIAGNOSTICO")  # título
ventana_inicio.configure(bg="white") # color de fondo

# También podemos cambiar el icono de la plumita (SOLO VALE CON IMAGENES .ico). Coge una imagen que quieras y guardatela en una carpeta

# Para que nos salga la ventana siempre centrada y proporcional al tamaño de nuestra pantalla
# Cambia la ruta si la colocas en otro sitio (comentálo si ves que te da fallo)
ventana_inicio.iconbitmap("iconos/Pantallas.ico")

ancho_ventana_inicio = 500 # ancho por defecto de la ventana de inicio
alto_ventana_inicio = 500 #alto por defecto de la ventana de inicio

# Ahora cogemos el ancho y alto de nuestra pantalla y calculamos la posición restando con nuestros valores iniciales
x_ventana = ventana_inicio.winfo_screenwidth() // 2 - ancho_ventana_inicio // 2 
y_ventana = ventana_inicio.winfo_screenheight() // 2 - alto_ventana_inicio // 2

# calculamos la nueva posición y la introducimos en la configuración
posicion_ventana_inicio = str(ancho_ventana_inicio) + "x" + str(alto_ventana_inicio) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana_inicio.geometry(posicion_ventana_inicio) #se introduce el tamaño relativo
ventana_inicio.resizable(0,0)

############# COMIENZO DEL DIAGNOSTICO

# Función que inicia el diagnóstico abriendo la siguiente ventana
def iniciar_diagnostico():
    ventana_inicio.destroy()  #una vez clica el botón cierra la ventana
    mostrar_formulario() #una vez cerrada inicia la siguiente ventana

# Botón que ejecuta la función anterior y que da comienzo al programa
boton_iniciar = Button(ventana_inicio, text="INICIAR DIAGNOSTICO", bg= "aquamarine",activebackground="white",fg="black",activeforeground = "blue",command=iniciar_diagnostico)
boton_iniciar.place(relx=0.5,rely=0.5,anchor=CENTER) # obligamos a centrarlo en todas las direcciones

# Bucle que inicia la ventana de inicio y la mantiene abierta
ventana_inicio.mainloop()
                                      

