# 📝 Changelog - Descargador de YouTube

## [1.0.0] - 2026-04-13

### ✅ Versiones Probadas y Funcionando

**Dependencias principales:**
- `yt-dlp==2026.3.17` - Descargador de YouTube
- `yt-dlp-ejs==0.8.0` - Soporte JavaScript para resolver desafíos de YouTube
- `aiohttp==3.13.5` - Cliente HTTP asíncrono
- `websockets==16.0` - Comunicación WebSocket
- `pycryptodomex==3.23.0` - Criptografía para descifrado
- `mutagen==1.47.0` - Manejo de metadatos de audio

**Requisitos externos:**
- Deno 1.41+ (JavaScript runtime)
- FFmpeg (conversión de audio/video)

### 🎨 Características

- ✅ Descarga de videos en MP4 (1080p, 720p, 480p, mejor disponible)
- ✅ Descarga de audio en MP3 (320kbps, 192kbps, 128kbps)
- ✅ Interfaz gráfica moderna con tema oscuro (Catppuccin)
- ✅ Doble método de autenticación con cookies:
  - Método 1: Archivo cookies.txt (recomendado, prioridad alta)
  - Método 2: Desde navegador (Chrome, Firefox, Edge, Brave, Opera, Chromium)
- ✅ Limpieza automática de URLs (elimina parámetros de playlist)
- ✅ Barra de progreso en tiempo real
- ✅ Manejo robusto de errores con mensajes informativos
- ✅ Validación de cookies antes de descargar
- ✅ Advertencias específicas cuando Chrome está abierto

### 🐛 Problemas Conocidos y Soluciones

**1. "No supported JavaScript runtime"**
- **Solución:** Instalar Deno (ver INSTRUCCIONES_DENO.md)

**2. "Could not copy Chrome cookie database"**
- **Causa:** Chrome/navegador está abierto
- **Solución:** Cerrar navegador o usar archivo cookies.txt

**3. "Sign in to confirm you're not a bot"**
- **Causa:** Sin autenticación de cookies
- **Solución:** Configurar cookies (archivo o navegador)

### 📋 Notas de Versión

- Esta versión usa **versiones fijas** de dependencias para garantizar estabilidad
- Si YouTube cambia su estructura y algo deja de funcionar:
  1. Actualiza: `pip install -U "yt-dlp[default]"`
  2. Prueba que funcione
  3. Congela: `pip freeze > requirements.txt`
  4. Documenta en este CHANGELOG

### ⚠️ Advertencias

- **NO** subir el archivo `youtube_cookies.txt` a GitHub (contiene datos de sesión)
- Cerrar el navegador antes de usar el Método 2 de cookies
- Las cookies pueden caducar (renovar cada cierto tiempo)
- YouTube puede bloquear descargas excesivas desde una misma IP

---

## Formato de Futuras Versiones

```
## [X.Y.Z] - YYYY-MM-DD

### Cambios
- Descripción del cambio

### Versiones de Dependencias
- yt-dlp==X.Y.Z
- (otras actualizaciones relevantes)

### Problemas Corregidos
- Descripción del problema y solución
```

---

## Versionado

Este proyecto usa [Semantic Versioning](https://semver.org/):
- **MAJOR** (1.x.x): Cambios incompatibles con versiones anteriores
- **MINOR** (x.1.x): Nueva funcionalidad compatible
- **PATCH** (x.x.1): Correcciones de bugs

---

**Última actualización:** 2026-04-13  
**Mantenedor:** Fernando Alvarado Soria
