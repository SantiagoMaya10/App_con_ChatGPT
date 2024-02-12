import streamlit as st

def temperatura():
    conversiones = {
        "Celsius a Fahrenheit": lambda c: c * 9/5 + 32,
        "Fahrenheit a Celsius": lambda f: (f - 32) * 5/9,
        "Celsius a Kelvin": lambda c: c + 273.15,
        "Kelvin a Celsius": lambda k: k - 273.15
    }

    conversion = st.selectbox("Seleccione el tipo de conversión de temperatura:", list(conversiones.keys()))
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if st.button("Convertir"):
        resultado = conversiones[conversion](valor)
        st.write(f"{valor} {conversion.split(' a ')[0]} son {resultado:.2f} {conversion.split(' a ')[1]}.")

def longitud():
    conversiones = {
        "Pies a metros": lambda p: p * 0.3048,
        "Metros a pies": lambda m: m / 0.3048,
        "Pulgadas a centímetros": lambda p: p * 2.54,
        "Centímetros a pulgadas": lambda c: c / 2.54
    }

    conversion = st.selectbox("Seleccione el tipo de conversión de longitud:", list(conversiones.keys()))
    valor = st.number_input("Ingrese el valor a convertir:")
    
    if st.button("Convertir"):
        resultado = conversiones[conversion](valor)
        st.write(f"{valor} {conversion.split(' a ')[0]} son {resultado:.2f} {conversion.split(' a ')[1]}.")

if __name__ == "__main__":
    temperatura()
    longitud()
