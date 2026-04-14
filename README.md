# 🎬 Descargador de Videos y MP3 de YouTube

Aplicación de escritorio con interfaz gráfica para descargar videos y audios de YouTube.

## 🚀 Características

- ✅ Descarga videos en formato MP4 (1080p, 720p, 480p)
- ✅ Descarga audios en formato MP3 (320kbps, 192kbps, 128kbps)
- ✅ Interfaz gráfica intuitiva
- ✅ Barra de progreso en tiempo real
- ✅ Sistema de descarga con doble método (pytubefix + yt-dlp)
- ✅ Limpieza automática de URLs con parámetros de playlist

## 📋 Requisitos

- Python 3.7+
- FFmpeg (para conversión a MP3)
- Node.js (opcional, para ciertos videos)

## 🔧 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Fernando-Alvarado-Soria/Descargardor-de-videos-y-mp3.git
   cd Descargardor-de-videos-y-mp3
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Instala FFmpeg:**
   - Windows: `winget install --id=Gyan.FFmpeg -e`
   - Linux: `sudo apt install ffmpeg`
   - Mac: `brew install ffmpeg`

## 💻 Uso

1. **Ejecuta la aplicación:**
   ```bash
   python convertidor.py
   ```

2. **Pega la URL del video de YouTube**

3. **Selecciona el formato:**
   - Video (MP4) o Audio (MP3)

4. **Elige la calidad**

5. **Selecciona la carpeta de destino** (opcional)

6. **Haz clic en "Descargar"**

## 🔒 Seguridad y Privacidad

### ⚠️ Archivos que NO debes compartir:

- `youtube_cookies.txt` - Contiene información de tu sesión de YouTube
- Cualquier archivo `.cookies` o `.cookie`
- Archivos en la carpeta `venv/`
- Videos y audios descargados (`.mp3`, `.mp4`)

### 🛡️ Protección incluida:

El archivo `.gitignore` está configurado para evitar que subas archivos sensibles accidentalmente.

### 📝 Si necesitas cookies (para videos restringidos):

1. Ejecuta: `python exportar_cookies.py`
2. Sigue las instrucciones en pantalla
3. El archivo `youtube_cookies.txt` se creará localmente
4. **NUNCA** subas este archivo a GitHub

## 🐛 Solución de Problemas

### Error: "Sign in to confirm you're not a bot"
- Sigue las instrucciones en [INSTRUCCIONES_COOKIES.md](INSTRUCCIONES_COOKIES.md)

### Error: "No se pudo descargar con ningún método"
- Verifica que FFmpeg esté instalado: `ffmpeg -version`
- Asegúrate de que la URL sea válida
- Algunos videos pueden estar restringidos geográficamente

### Error: "Could not copy Chrome cookie database"
- Cierra completamente Chrome antes de exportar cookies
- Usa el script `exportar_cookies.py` con el navegador cerrado

## 📚 Librerías Utilizadas

- [pytubefix](https://github.com/JuanBindez/pytubefix) - Descarga principal
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Método alternativo
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Interfaz gráfica
- [FFmpeg](https://ffmpeg.org/) - Conversión de audio/video

## ⚖️ Legal

Esta herramienta es solo para uso personal y educativo. Asegúrate de cumplir con los Términos de Servicio de YouTube y las leyes de derechos de autor de tu país.

- No uses esta herramienta para descargar contenido con derechos de autor sin permiso
- Respeta los derechos de los creadores de contenido
- Usa solo para contenido del que tengas permiso para descargar

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Fernando Alvarado Soria**

- GitHub: [@Fernando-Alvarado-Soria](https://github.com/Fernando-Alvarado-Soria)

## ⭐ Agradecimientos

- A los desarrolladores de pytubefix y yt-dlp
- A la comunidad de Python
- A todos los que contribuyan al proyecto

---

**Nota:** Este proyecto se proporciona "tal cual", sin garantías de ningún tipo. YouTube puede cambiar su estructura en cualquier momento, lo que podría afectar el funcionamiento de esta herramienta.
