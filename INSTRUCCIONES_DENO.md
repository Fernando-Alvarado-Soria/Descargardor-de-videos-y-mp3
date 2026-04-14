# 🦕 Instalación de Deno - Guía Detallada

Deno es un **JavaScript runtime** necesario para que yt-dlp pueda resolver los desafíos de JavaScript que YouTube usa para prevenir bots.

## ⚠️ ¿Por qué es necesario Deno?

Sin Deno verás estos errores:
- `No supported JavaScript runtime could be found`
- `Signature solving failed`
- `n challenge solving failed`
- `WARNING: Only images are available for download`

## 📥 Instalación

### Windows

#### **Método 1: PowerShell (Recomendado)**

1. Abre **PowerShell como administrador**
2. Ejecuta:
   ```powershell
   irm https://deno.land/install.ps1 | iex
   ```
3. Reinicia la terminal
4. Verifica:
   ```powershell
   deno --version
   ```

#### **Método 2: Instalación Manual**

1. Ve a https://github.com/denoland/deno/releases/latest
2. Descarga `deno-x86_64-pc-windows-msvc.zip`
3. Descomprime el archivo → obtendrás `deno.exe`
4. Opción A - Sistema:
   - Mueve `deno.exe` a `C:\Windows\System32\`
5. Opción B - Usuario (recomendado):
   - Crea la carpeta `C:\deno\`
   - Mueve `deno.exe` ahí
   - Agrega `C:\deno` al PATH:
     1. Presiona `Win + X` → Sistema
     2. Configuración avanzada del sistema
     3. Variables de entorno
     4. En "Variables del sistema", selecciona `Path` → Editar
     5. Nuevo → `C:\deno`
     6. Aceptar todo
6. Abre una **terminal NUEVA**
7. Verifica:
   ```powershell
   deno --version
   ```

#### **Método 3: Con Scoop**

```powershell
# Instala Scoop primero (si no lo tienes)
irm get.scoop.sh | iex

# Instala Deno
scoop install deno

# Verifica
deno --version
```

#### **Método 4: Con Chocolatey**

```powershell
# Instala Chocolatey primero (si no lo tienes)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instala Deno
choco install deno

# Verifica
deno --version
```

---

### Linux

```bash
# Instalación automática
curl -fsSL https://deno.land/x/install/install.sh | sh

# Agregar al PATH (agregar al final de ~/.bashrc o ~/.zshrc)
echo 'export DENO_INSTALL="$HOME/.deno"' >> ~/.bashrc
echo 'export PATH="$DENO_INSTALL/bin:$PATH"' >> ~/.bashrc

# Recargar configuración
source ~/.bashrc

# Verificar
deno --version
```

---

### macOS

```bash
# Con Homebrew
brew install deno

# O instalación manual
curl -fsSL https://deno.land/x/install/install.sh | sh

# Agregar al PATH (si usas bash)
echo 'export DENO_INSTALL="$HOME/.deno"' >> ~/.bash_profile
echo 'export PATH="$DENO_INSTALL/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile

# Si usas zsh (por defecto en macOS Catalina+)
echo 'export DENO_INSTALL="$HOME/.deno"' >> ~/.zshrc
echo 'export PATH="$DENO_INSTALL/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Verificar
deno --version
```

---

## ✅ Verificación

Después de instalar, deberías poder ejecutar:

```bash
deno --version
```

**Salida esperada:**
```
deno 1.41.0 (release, x86_64-pc-windows-msvc)
v8 12.1.285.6
typescript 5.3.3
```

(Los números de versión pueden variar)

---

## 🧪 Prueba con yt-dlp

Una vez instalado Deno, prueba si yt-dlp funciona:

```bash
# Con cookies (recomendado)
yt-dlp --cookies youtube_cookies.txt "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Sin cookies (puede fallar)
yt-dlp "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Si ves que descarga correctamente sin errores de JavaScript, ¡Deno está funcionando!

---

## 🔧 Solución de Problemas

### "deno: command not found" (después de instalar)

**Windows:**
1. Cierra y abre una nueva terminal/PowerShell
2. Si persiste, verifica que `C:\deno` (o donde instalaste) esté en el PATH
3. Ejecuta `refreshenv` (si usas Chocolatey) o reinicia el sistema

**Linux/Mac:**
1. Recarga la configuración del shell: `source ~/.bashrc` o `source ~/.zshrc`
2. Verifica que las líneas de exportación estén en tu archivo de configuración
3. Cierra y abre una nueva terminal

### "Permission denied" al instalar en Linux/Mac

```bash
# Asegúrate de que el directorio tenga permisos
chmod +x ~/.deno/bin/deno
```

### Deno instalado pero yt-dlp sigue fallando

1. Verifica la versión:
   ```bash
   deno --version
   yt-dlp --version
   ```

2. Actualiza yt-dlp:
   ```bash
   pip install -U "yt-dlp[default]"
   ```

3. Prueba un video simple:
   ```bash
   yt-dlp --verbose "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   ```

4. Revisa los logs en busca de errores específicos

---

## 📚 Más Información

- **Sitio oficial de Deno:** https://deno.com
- **Documentación de instalación:** https://docs.deno.com/runtime/manual/getting_started/installation
- **GitHub de Deno:** https://github.com/denoland/deno
- **Wiki de yt-dlp sobre EJS:** https://github.com/yt-dlp/yt-dlp/wiki/EJS

---

## ❓ ¿Por qué Deno y no Node.js?

Aunque yt-dlp también soporta Node.js, **Deno es la opción recomendada** porque:

- ✅ Más fácil de instalar (un solo ejecutable)
- ✅ No requiere configuración adicional
- ✅ Mejor rendimiento para este caso de uso
- ✅ Habilitado por defecto en yt-dlp

---

Si después de seguir esta guía aún tienes problemas, abre un [issue en GitHub](https://github.com/Fernando-Alvarado-Soria/Descargardor-de-videos-y-mp3/issues) con:
- Tu sistema operativo
- Versión de Deno (`deno --version`)
- Versión de yt-dlp (`yt-dlp --version`)
- El error completo que recibes
