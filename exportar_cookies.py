"""
Script para exportar cookies de Chrome/Edge a un archivo compatible con yt-dlp
Ejecutar este script cuando Chrome/Edge esté CERRADO
"""
import subprocess
import os
import sys

def exportar_cookies():
    print("=" * 60)
    print("EXPORTADOR DE COOKIES PARA YOUTUBE")
    print("=" * 60)
    print()
    
    # Pregunta al usuario qué navegador usar
    print("Selecciona tu navegador:")
    print("1. Chrome")
    print("2. Edge")
    print("3. Firefox")
    
    while True:
        opcion = input("\nIngresa el número (1, 2 o 3): ").strip()
        if opcion in ['1', '2', '3']:
            break
        print("Opción inválida. Intenta de nuevo.")
    
    navegadores = {
        '1': 'chrome',
        '2': 'edge', 
        '3': 'firefox'
    }
    
    navegador = navegadores[opcion]
    archivo_salida = 'youtube_cookies.txt'
    
    print(f"\n⚠️  IMPORTANTE: Cierra TODAS las ventanas de {navegador.upper()} antes de continuar.")
    input("Presiona ENTER cuando hayas cerrado el navegador...")
    
    print(f"\nExportando cookies de {navegador.upper()}...")
    
    try:
        # Usar yt-dlp para exportar las cookies
        comando = [
            sys.executable, '-m', 'yt_dlp',
            '--cookies-from-browser', navegador,
            '--cookies', archivo_salida,
            '--skip-download',
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Video de prueba
        ]
        
        resultado = subprocess.run(comando, capture_output=True, text=True)
        
        if os.path.exists(archivo_salida):
            print(f"\n✅ ¡Éxito! Cookies exportadas a: {archivo_salida}")
            print("\nAhora puedes cerrar esta ventana y volver a usar el descargador.")
            print("Las cookies se usarán automáticamente.")
        else:
            print("\n❌ Error al exportar cookies.")
            print("\nMétodo alternativo:")
            print("1. Abre Chrome e instala la extensión 'Get cookies.txt LOCALLY'")
            print("2. Ve a youtube.com y haz clic en el ícono de la extensión")
            print("3. Descarga el archivo cookies.txt")
            print(f"4. Renómbralo a 'youtube_cookies.txt' y colócalo en: {os.getcwd()}")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMétodo alternativo manual:")
        print("1. Instala la extensión de Chrome: 'Get cookies.txt LOCALLY'")
        print("   URL: https://chrome.google.com/webstore/detail/get-cookiestxt-locally/")
        print("2. Ve a https://www.youtube.com")
        print("3. Haz clic en el ícono de la extensión")
        print("4. Descarga el archivo cookies.txt")
        print(f"5. Renómbralo a 'youtube_cookies.txt' y guárdalo en: {os.getcwd()}")
    
    print("\n" + "=" * 60)
    input("\nPresiona ENTER para salir...")

if __name__ == "__main__":
    exportar_cookies()
