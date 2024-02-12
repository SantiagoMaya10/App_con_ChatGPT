import streamlit as st

def temperatura():
    opciones = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    conversion = st.selectbox("Seleccione el tipo de conversión de temperatura:", opciones)
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if conversion == "Celsius a Fahrenheit":
        resultado = valor * 9/5 + 32
        st.write(f"{valor} grados Celsius son {resultado} grados Fahrenheit.")
    elif conversion == "Fahrenheit a Celsius":
        resultado = (valor - 32) * 5/9
        st.write(f"{valor} grados Fahrenheit son {resultado} grados Celsius.")
    elif conversion == "Celsius a Kelvin":
        resultado = valor + 273.15
        st.write(f"{valor} grados Celsius son {resultado} grados Kelvin.")
    elif conversion == "Kelvin a Celsius":
        resultado = valor - 273.15
        st.write(f"{valor} grados Kelvin son {resultado} grados Celsius.")

def longitud():
    opciones = ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"]
    conversion = st.selectbox("Seleccione el tipo de conversión de longitud:", opciones)
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if conversion == "Pies a metros":
        resultado = valor * 0.3048
        st.write(f"{valor} pies son {resultado} metros.")
    elif conversion == "Metros a pies":
        resultado = valor / 0.3048
        st.write(f"{valor} metros son {resultado} pies.")
    elif conversion == "Pulgadas a centímetros":
        resultado = valor * 2.54
        st.write(f"{valor} pulgadas son {resultado} centímetros.")
    elif conversion == "Centímetros a pulgadas":
        resultado = valor / 2.54
        st.write(f"{valor} centímetros son {resultado} pulgadas.")

def peso_masa():
    opciones = ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"]
    conversion = st.selectbox("Seleccione el tipo de conversión de peso/masa:", opciones)
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if conversion == "Libras a kilogramos":
        resultado = valor * 0.453592
        st.write(f"{valor} libras son {resultado} kilogramos.")
    elif conversion == "Kilogramos a libras":
        resultado = valor / 0.453592
        st.write(f"{valor} kilogramos son {resultado} libras.")
    elif conversion == "Onzas a gramos":
        resultado = valor * 28.3495
        st.write(f"{valor} onzas son {resultado} gramos.")
    elif conversion == "Gramos a onzas":
        resultado = valor / 28.3495
        st.write(f"{valor} gramos son {resultado} onzas.")

def volumen():
    opciones = ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"]
    conversion = st.selectbox("Seleccione el tipo de conversión de volumen:", opciones)
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if conversion == "Galones a litros":
        resultado = valor * 3.78541
        st.write(f"{valor} galones son {resultado} litros.")
    elif conversion == "Litros a galones":
        resultado = valor / 3.78541
        st.write(f"{valor} litros son {resultado} galones.")
    elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
        resultado = valor * 16.3871
        st.write(f"{valor} pulgadas cúbicas son {resultado} centímetros cúbicos.")
    elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
        resultado = valor / 16.3871
        st.write(f"{valor} centímetros cúbicos son {resultado} pulgadas cúbicas.")

def tiempo():
    opciones = ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"]
    conversion = st.selectbox("Seleccione el tipo de conversión de tiempo:", opciones)
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if conversion == "Horas a minutos":
        resultado = valor * 60
        st.write(f"{valor} horas son {resultado} minutos.")
    elif conversion == "Minutos a segundos":
        resultado = valor * 60
        st.write(f"{valor} minutos son {resultado} segundos.")
    elif conversion == "Días a horas":
        resultado = valor * 24
        st.write(f"{valor} días son {resultado} horas.")
    elif conversion == "Semanas a días":
        resultado = valor * 7
        st.write(f"{valor} semanas son {resultado} días.")

def velocidad():
    opciones = ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"]
    conversion = st.selectbox("Seleccione el tipo de conversión de velocidad:", opciones)
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if conversion == "Millas por hora a kilómetros por hora":
        resultado = valor * 1.60934
        st.write(f"{valor} millas por hora son {resultado} kilómetros por hora.")
    elif conversion == "Kilómetros por hora a metros por segundo":
        resultado = valor * 0.277778
        st.write(f"{valor} kilómetros por hora son {resultado} metros por segundo.")
    elif conversion == "Nudos a millas por hora":
        resultado = valor * 1.15078
        st.write(f"{valor} nudos son {resultado} millas por hora.")
    elif conversion == "Metros por segundo a pies por segundo":
        resultado = valor * 3.28084
        st.write(f"{valor} metros por segundo son {resultado} pies por segundo.")

def area():
    opciones = ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"]
    conversion = st.selectbox("Seleccione el tipo de conversión de área:", opciones)
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if conversion == "Metros cuadrados a pies cuadrados
