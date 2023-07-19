"""
Realizado por Sofia Arce y Miguel Valdez
"""
#2 Graficar Señales y Graficar la Transformada de Fourier de un señal DTMF
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Definir los tonos DTMF
tonos = {'1':(697,1209),
         '2':(697,1336),
         '3':(697,1477),
         '4':(770,1209),
         '5':(770,1336),
         '6':(770,1477),
         '7':(852,1209),
         '8':(852,1336),
         '9':(852,1477),
         '*':(941,1209),
         '0':(941,1336),
         '#':(941,1477)}

# Pedir al usuario que ingrese un número
numero = input("Ingresa un número: ")

# Verificar si el número ingresado está en la lista de tonos DTMF
if numero in tonos:
    # Obtener las frecuencias correspondientes al número
    frecuencia1, frecuencia2 = tonos[numero]

    # Generar la señal sinusoidal para cada frecuencia
    
    tiempo = np.arange(0,1, 1/44100)
    senal1 = np.sin(2*np.pi*frecuencia1*tiempo)
    senal2 = np.sin(2*np.pi*frecuencia2*tiempo)
    

    # Sumar las señales sinusoidales para crear la señal DTMF
    senal_DTMF = senal1 + senal2

    # graficar señal1
    plt.plot(tiempo,senal1)
    plt.xlim(0,0.005)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Señal 1')
    plt.show()
    # greficar señal2
    plt.plot(tiempo,senal2)
    plt.xlim(0,0.005)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Señal 2')
    plt.show()
    #Graficar la señal DTMF en el tiempo
    plt.plot(tiempo, senal_DTMF)
    plt.xlim(0,0.05)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title(f'Señal DTMF para el número {numero}')
    plt.show()

    # Calcular la Transformada de fourier de la señal DTMF
    frecuencias = np.fft.fftfreq(len(senal_DTMF), d=1/44100)
    transformada = np.fft.fft(senal_DTMF)

    # Graficar la Transformada de fourier de la señal DTMF
    plt.plot(frecuencias, abs(transformada))
    plt.xlim(0, 2000)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    plt.title(f'Transformada de Fourier para el número {numero}')
    plt.show()

    # Identificar las dos frecuencias presentes en la señal DTMF
    amplitudes = abs(transformada)
    frecuencia1_idx = np.argmax(amplitudes[:len(amplitudes)//2])
    frecuencia2_idx = np.argmax(amplitudes[len(amplitudes)//2:]) + len(amplitudes)//2
