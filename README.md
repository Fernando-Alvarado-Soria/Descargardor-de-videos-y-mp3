# 🎬 Descargador de Videos y MP3 de YouTube

Aplicación de escritorio con interfaz gráfica para descargar videos y audios de YouTube.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey.svg)

## ⚡ Inicio Rápido (TL;DR)

```bash
# 1. Clona e instala
git clone https://github.com/Fernando-Alvarado-Soria/Descargardor-de-videos-y-mp3.git
cd Descargardor-de-videos-y-mp3
python -m venv venv
venv\Scripts\activate  # Windows | source venv/bin/activate en Linux/Mac
pip install -r requirements.txt  # Usa versiones fijas probadas

# 2. Instala Deno (REQUERIDO para YouTube)
# Windows PowerShell:
irm https://deno.land/install.ps1 | iex
# Linux/Mac:
curl -fsSL https://deno.land/x/install/install.sh | sh

# 3. Instala FFmpeg (para MP3)
winget install --id=Gyan.FFmpeg -e  # Windows

# 4. Exporta cookies de YouTube (evita bloqueos)
# Instala extensión "Get cookies.txt LOCALLY" en Chrome
# Exporta cookies.txt desde youtube.com

# 5. Ejecuta
python convertidor.py
```

---

## 🚀 Características

- ✅ Descarga videos en formato MP4 (1080p, 720p, 480p)
- ✅ Descarga audios en formato MP3 (320kbps, 192kbps, 128kbps)
- ✅ Interfaz gráfica intuitiva
- ✅ Barra de progreso en tiempo real
- ✅ Sistema de descarga con doble método (pytubefix + yt-dlp)
- ✅ Limpieza automática de URLs con parámetros de playlist

## 📋 Requisitos

- Python 3.7+
- **Deno** (JavaScript runtime - **REQUERIDO** para YouTube)
- FFmpeg (para conversión a MP3)

## 🔧 Instalación

### 1️⃣ Clona el repositorio
```bash
git clone https://github.com/Fernando-Alvarado-Soria/Descargardor-de-videos-y-mp3.git
cd Descargardor-de-videos-y-mp3
```

### 2️⃣ Crea y activa un entorno virtual
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instala las dependencias de Python

**⚠️ IMPORTANTE:** Este proyecto usa versiones fijas de dependencias para garantizar estabilidad.

```bash
# Instala las dependencias con versiones exactas
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene versiones específicas que se sabe que funcionan correctamente juntas. Esto incluye:
- `yt-dlp==2026.3.17` - Versión probada del descargador
- `yt-dlp-ejs==0.8.0` - Soporte para JavaScript de YouTube
- Y todas las demás dependencias

**Si en el futuro algo deja de funcionar** (YouTube cambia su estructura):

```bash
# Actualiza solo yt-dlp a la última versión
pip install -U "yt-dlp[default]"

# Si funciona, congela las nuevas versiones
pip freeze > requirements.txt
```

### 4️⃣ Instala Deno (JavaScript Runtime)

**Deno es OBLIGATORIO** para que yt-dlp pueda descargar de YouTube (resuelve desafíos de JavaScript).

#### **Windows:**

**Opción A - Con instalador (recomendado):**
```powershell
irm https://deno.land/install.ps1 | iex
```

**Opción B - Manual:**
1. Descarga `deno-x86_64-pc-windows-msvc.zip` desde: https://github.com/denoland/deno/releases/latest
2. Descomprímelo → obtendrás `deno.exe`
3. Mueve `deno.exe` a una carpeta en tu PATH, por ejemplo:
   - `C:\Windows\System32\`
   - O crea una carpeta `C:\deno\` y agrégala al PATH

**Opción C - Con Scoop:**
```powershell
scoop install deno
```

#### **Linux/Mac:**
```bash
curl -fsSL https://deno.land/x/install/install.sh | sh
```

#### **Verifica la instalación:**
```bash
deno --version
```

Deberías ver algo como:
```
deno 1.x.x
v8 12.x.x.x
typescript 5.x.x
```

### 5️⃣ Instala FFmpeg (para conversión a MP3)

**Windows:**
```bash
winget install --id=Gyan.FFmpeg -e
```

**Linux:**
```bash
sudo apt install ffmpeg
```

**Mac:**
```bash
brew install ffmpeg
```

**Verifica la instalación:**
```bash
ffmpeg -version
```

## 💻 Uso

### Inicio Rápido

1. **Ejecuta la aplicación:**
   ```bash
   python convertidor.py
   ```

2. **Interfaz Gráfica:**
   - Pega la URL del video de YouTube
   - Selecciona el formato (Video MP4 o Audio MP3)
   - Elige la calidad deseada
   - Selecciona la carpeta de destino (opcional)

3. **Configuración de Cookies** (MUY importante para evitar bloqueos):
   
   YouTube bloquea descargas detectadas como bots. **Necesitas autenticarte con cookies**.

   **Método 1 - Archivo cookies.txt (RECOMENDADO):**
   - Instala la extensión ["Get cookies.txt LOCALLY"](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) en Chrome/Firefox
   - Ve a https://www.youtube.com con sesión iniciada
   - Haz clic en la extensión y descarga el archivo
   - En la aplicación, usa el botón "Cargar cookies.txt" y selecciona el archivo

   **Método 2 - Desde navegador directamente:**
   - **⚠️ IMPORTANTE: Cierra COMPLETAMENTE Chrome/Firefox antes de descargar**
   - En la aplicación, selecciona tu navegador (chrome, firefox, edge, etc.)
   - Si el navegador está abierto, verás el error "Could not copy cookie database"

4. **Haz clic en "Descargar"**

### 🧪 Prueba desde la Terminal

Para verificar que todo funciona correctamente:

```bash
# Con archivo de cookies (recomendado)
yt-dlp --cookies youtube_cookies.txt "https://www.youtube.com/watch?v=sm2v1wRCFLE"

# Sin cookies (puede fallar en algunos videos)
yt-dlp "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Si este comando funciona, la aplicación también funcionará.

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

### ⚠️ "No supported JavaScript runtime" o "EJS challenge solving failed"

**Causa:** Deno no está instalado o no está en el PATH.

**Solución:**
```bash
# Verifica si Deno está instalado
deno --version

# Si no funciona, instálalo:
# Windows (PowerShell como administrador):
irm https://deno.land/install.ps1 | iex

# O descarga manual desde:
# https://github.com/denoland/deno/releases/latest
```

Después de instalar, **reinicia la terminal** y verifica nuevamente.

---

### 🔴 "Sign in to confirm you're not a bot"

**Causa:** YouTube está bloqueando la descarga porque no detecta autenticación.

**Solución:** Configura las cookies (ver sección de Uso arriba).

---

### 🔴 "Could not copy Chrome cookie database"

**Causa:** Chrome (o el navegador seleccionado) está abierto y tiene el archivo de cookies bloqueado.

**Solución:**
1. **Cierra COMPLETAMENTE Chrome** (verifica en el Administrador de Tareas que no haya procesos)
2. Intenta de nuevo

**Alternativa (sin cerrar el navegador):**
1. Usa el **Método 1** (archivo cookies.txt) en lugar del Método 2
2. Exporta las cookies con la extensión "Get cookies.txt LOCALLY"
3. Carga el archivo en la aplicación
4. Cambia el navegador a "ninguno"

---

### 🟡 "WARNING: Skipping client android since it does not support cookies"

Este es solo un warning. Si tienes las cookies configuradas correctamente, puedes ignorarlo.

---

### ❌ "Requested format is not available"

**Posibles causas:**
- El video tiene restricciones geográficas
- El video requiere membresía premium
- El video es un Short o contenido especial

**Solución:**
1. Prueba con "Mejor disponible" en la calidad
2. Verifica que la URL sea de un video normal (no un Short, playlist, o post)
3. Asegúrate de tener las cookies configuradas

---

### 🔧 Actualizar yt-dlp

YouTube cambia frecuentemente su estructura. Si algo deja de funcionar:

```bash
# Actualiza yt-dlp a la última versión
pip install -U "yt-dlp[default]"

# Prueba que funcione
yt-dlp --cookies youtube_cookies.txt "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Si funciona correctamente, congela las nuevas versiones
pip freeze > requirements.txt

# Haz commit de las nuevas versiones
git add requirements.txt
git commit -m "Actualizar dependencias - yt-dlp [versión]"
```

**¿Por qué usar versiones fijas?**
- ✅ Evita que actualizaciones automáticas rompan la funcionalidad
- ✅ Garantiza que todos los usuarios tengan las mismas versiones probadas
- ✅ Facilita la resolución de problemas
- ✅ Permite actualizar de forma controlada solo cuando sea necesario

---

### ✅ Verificación completa del sistema

```bash
# Python
python --version

# yt-dlp
yt-dlp --version

# Deno (REQUERIDO)
deno --version

# FFmpeg
ffmpeg -version

# Prueba de descarga
yt-dlp --cookies youtube_cookies.txt "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Si todos estos comandos funcionan, la aplicación debería funcionar perfectamente.

## 📚 Librerías y Herramientas

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Descargador principal de YouTube
- **[Deno](https://deno.com)** - JavaScript runtime (para resolver desafíos de YouTube)
- **[FFmpeg](https://ffmpeg.org)** - Conversión de audio/video
- **[tkinter](https://docs.python.org/3/library/tkinter.html)** - Interfaz gráfica

## 🎨 Características Técnicas

- ✅ Interfaz moderna con tema oscuro (estilo Catppuccin)
- ✅ Doble método de autenticación (archivo + navegador)
- ✅ Limpieza automática de URLs (elimina parámetros de playlist)
- ✅ Barra de progreso en tiempo real
- ✅ Selección de calidad flexible
- ✅ Manejo robusto de errores con mensajes informativos
- ✅ Soporte para múltiples navegadores (Chrome, Firefox, Edge, Brave, Opera)

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
