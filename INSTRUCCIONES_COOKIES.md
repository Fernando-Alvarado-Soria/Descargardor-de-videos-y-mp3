# 🍪 Cómo Solucionar Error de Autenticación de YouTube

Si recibes un error que dice "Sign in to confirm you're not a bot", necesitas exportar las cookies de tu navegador.

## 📋 Método Recomendado: Extensión de Chrome

### Paso 1: Instalar la extensión
1. Abre **Google Chrome**
2. Ve a Chrome Web Store y busca: **"Get cookies.txt LOCALLY"**
   - O usa este link: https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc
3. Haz clic en **"Agregar a Chrome"**

### Paso 2: Exportar las cookies
1. Ve a **https://www.youtube.com**
2. Asegúrate de estar **con sesión iniciada**
3. Haz clic en el ícono de **extensiones** (🧩) en la barra superior
4. Selecciona **"Get cookies.txt LOCALLY"**
5. Se descargará automáticamente un archivo `.txt`

### Paso 3: Configurar el archivo
1. **Renombra** el archivo descargado a: `youtube_cookies.txt`
2. **Mueve** el archivo a la carpeta del proyecto:
   ```
   D:\Github\Descargardor-de-videos-y-mp3\youtube_cookies.txt
   ```

### Paso 4: ¡Listo!
Ahora ejecuta el descargador normalmente. Detectará automáticamente el archivo de cookies y podrás descargar videos sin problemas.

---

## 🔄 Actualizar Cookies

Las cookies pueden caducar después de unos días/semanas. Si vuelves a tener el error:
1. Elimina el archivo `youtube_cookies.txt` anterior
2. Repite los pasos 2-3 para exportar cookies nuevas

---

## ⚠️ Solución de Problemas

### "Could not copy Chrome cookie database"
Este error ocurre cuando intentas exportar cookies con Chrome abierto.
**Solución**: Usa la extensión en lugar del exportador automático.

### "No supported JavaScript runtime"
Necesitas tener Node.js instalado.
**Solución**: Descarga e instala Node.js desde https://nodejs.org/

### El video aún no se descarga
- Verifica que el archivo se llame exactamente `youtube_cookies.txt`
- Asegúrate de que esté en la carpeta correcta del proyecto
- Verifica que tengas sesión iniciada en YouTube cuando exportes las cookies
- Intenta exportar cookies nuevamente

---

## 📝 Notas
- Solo necesitas hacer esto **una vez** (o cuando las cookies caduquen)
- Las cookies son específicas de tu cuenta de YouTube
- El archivo de cookies NO debe compartirse (contiene información de tu sesión)
