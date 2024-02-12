import streamlit as st

def convertir_temperatura(valor, conversion):
    conversiones = {
        "Celsius a Fahrenheit": lambda c: c * 9/5 + 32,
        "Fahrenheit a Celsius": lambda f: (f - 32) * 5/9,
        "Celsius a Kelvin": lambda c: c + 273.15,
        "Kelvin a Celsius": lambda k: k - 273.15
    }

    if st.button(f"Convertir {conversion}"):
        resultado = conversiones[conversion](valor)
        st.write(f"{valor} {conversion.split(' a ')[0]} son {resultado:.2f} {conversion.split(' a ')[1]}.")

def convertir_longitud(valor, conversion):
    conversiones = {
        "Pies a metros": lambda p: p * 0.3048,
        "Metros a pies": lambda m: m / 0.3048,
        "Pulgadas a centímetros": lambda p: p * 2.54,
        "Centímetros a pulgadas": lambda c: c / 2.54
    }

    if st.button(f"Convertir {conversion}"):
        resultado = conversiones[conversion](valor)
        st.write(f"{valor} {conversion.split(' a ')[0]} son {resultado:.2f} {conversion.split(' a ')[1]}.")

def convertir_peso_masa(valor, conversion):
    conversiones = {
        "Libras a kilogramos": lambda l: l * 0.453592,
        "Kilogramos a libras": lambda k: k / 0.453592,
        "Onzas a gramos": lambda o: o * 28.3495,
        "Gramos a onzas": lambda g: g / 28.3495
    }

    if st.button(f"Convertir {conversion}"):
        resultado = conversiones[conversion](valor)
        st.write(f"{valor} {conversion.split(' a ')[0]} son {resultado:.2f} {conversion.split(' a ')[1]}.")

if __name__ == "__main__":
    st.header("Conversor Universal")
    
    st.subheader("Conversión de Temperatura")
    valor_temp = st.number_input("Ingrese el valor a convertir:", key="temperatura")
    conversion_temp = st.selectbox("Seleccione el tipo de conversión de temperatura:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"])
    convertir_temperatura(valor_temp, conversion_temp)

    st.subheader("Conversión de Longitud")
    valor_long = st.number_input("Ingrese el valor a convertir:", key="longitud")
    conversion_long = st.selectbox("Seleccione el tipo de conversión de longitud:", ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"])
    convertir_longitud(valor_long, conversion_long)

    st.subheader("Conversión de Peso/Masa")
    valor_peso = st.number_input("Ingrese el valor a convertir:", key="peso_masa")
    conversion_peso = st.selectbox("Seleccione el tipo de conversión de peso/masa:", ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"])
    convertir_peso_masa(valor_peso, conversion_peso)
