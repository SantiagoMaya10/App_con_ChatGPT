import streamlit as st

def convert_temperature():
    conversion = st.selectbox("Seleccione el tipo de conversión de temperatura:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"])
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if st.button("Convertir temperatura"):
        if conversion == "Celsius a Fahrenheit":
            resultado = valor * 9/5 + 32
            st.write(f"{valor} grados Celsius son {resultado:.2f} grados Fahrenheit.")
        elif conversion == "Fahrenheit a Celsius":
            resultado = (valor - 32) * 5/9
            st.write(f"{valor} grados Fahrenheit son {resultado:.2f} grados Celsius.")
        elif conversion == "Celsius a Kelvin":
            resultado = valor + 273.15
            st.write(f"{valor} grados Celsius son {resultado:.2f} grados Kelvin.")
        elif conversion == "Kelvin a Celsius":
            resultado = valor - 273.15
            st.write(f"{valor} grados Kelvin son {resultado:.2f} grados Celsius.")

def convert_length():
    conversion = st.selectbox("Seleccione el tipo de conversión de longitud:", ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"])
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if st.button("Convertir longitud"):
        if conversion == "Pies a metros":
            resultado = valor * 0.3048
            st.write(f"{valor} pies son {resultado:.2f} metros.")
        elif conversion == "Metros a pies":
            resultado = valor / 0.3048
            st.write(f"{valor} metros son {resultado:.2f} pies.")
        elif conversion == "Pulgadas a centímetros":
            resultado = valor * 2.54
            st.write(f"{valor} pulgadas son {resultado:.2f} centímetros.")
        elif conversion == "Centímetros a pulgadas":
            resultado = valor / 2.54
            st.write(f"{valor} centímetros son {resultado:.2f} pulgadas.")

def convert_weight_mass():
    conversion = st.selectbox("Seleccione el tipo de conversión de peso/masa:", ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"])
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if st.button("Convertir peso/masa"):
        if conversion == "Libras a kilogramos":
            resultado = valor * 0.453592
            st.write(f"{valor} libras son {resultado:.2f} kilogramos.")
        elif conversion == "Kilogramos a libras":
            resultado = valor / 0.453592
            st.write(f"{valor} kilogramos son {resultado:.2f} libras.")
        elif conversion == "Onzas a gramos":
            resultado = valor * 28.3495
            st.write(f"{valor} onzas son {resultado:.2f} gramos.")
        elif conversion == "Gramos a onzas":
            resultado = valor / 28.3495
            st.write(f"{valor} gramos son {resultado:.2f} onzas.")

if __name__ == "__main__":
    convert_temperature()
    convert_length()
    convert_weight_mass()
