import numpy as np
import matplotlib.pyplot as plt

def main():
    # Parámetros iniciales
    contaminacion_inicial = 100  # Nivel inicial de contaminación en ppm
    k = 0.1  # Constante de efectividad de las políticas
    tiempo = np.linspace(0, 10, 100)  # Tiempo en años

    # Diferentes niveles de políticas implementadas (de 0 a 1)
    niveles_politicas = [0, 0.3, 0.5, 0.8, 1]

    # Graficar
    plt.figure(figsize=(10, 6))
    for p in niveles_politicas:
        contaminacion = contaminacion_inicial * np.exp(-k * p * tiempo)
        plt.plot(tiempo, contaminacion, label=f'Políticas = {p}')

    # Configuración del gráfico
    plt.xlabel("Tiempo (años)")
    plt.ylabel("Nivel de Contaminación (ppm)")
    plt.title("Reducción de Contaminación con la Implementación de Políticas Ambientales")
    plt.legend()
    plt.grid()
    
    # En lugar de plt.show(), guardamos la figura
    plt.savefig('grafico_contaminacion.png')
    plt.close()

if __name__ == "__main__":
    main()