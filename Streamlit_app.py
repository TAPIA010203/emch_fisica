import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    velocidad = random.randint(5, 20)  # velocidad en m/s
    tiempo = random.randint(1, 10)      # tiempo en segundos
    distancia = velocidad * tiempo
    return velocidad, tiempo, distancia

# Función principal de la app
def main():
    st.title("Ejercicios de Cinemática")
    st.write("Generador de ejercicios de cinemática")

    # Generar un nuevo ejercicio
    velocidad, tiempo, distancia = generar_ejercicio()
    st.write(f"Un objeto se mueve a una velocidad de **{velocidad} m/s** durante **{tiempo} segundos**.")
    st.write("¿Cuál es la distancia recorrida?")

    # Entrada del usuario
    respuesta_usuario = st.number_input("Ingresa tu respuesta (en metros):", min_value=0)

    # Botón para verificar la respuesta
    if st.button("Verificar respuesta"):
        if respuesta_usuario == distancia:
            st.success("¡Correcto! La distancia recorrida es de **{} metros**.".format(distancia))
        else:
            st.error("Incorrecto. La distancia recorrida es de **{} metros**.".format(distancia))

if __name__ == "__main__":
    main()
