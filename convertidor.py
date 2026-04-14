import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
import yt_dlp

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("600x550")
        self.root.resizable(True, True)
        
        # Variables
        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value="mp4")
        self.quality_var = tk.StringVar(value="1080p")
        self.download_path = os.path.expanduser("~/Downloads")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, text="🎬 YouTube Downloader", 
                                font=("Arial", 18, "bold"))
        title_label.pack(pady=(0, 20))
        
        # URL Frame
        url_frame = ttk.LabelFrame(main_frame, text="URL de YouTube", padding="10")
        url_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.url_entry = ttk.Entry(url_frame, textvariable=self.url_var, 
                                    font=("Arial", 10))
        self.url_entry.pack(fill=tk.X, pady=5)
        
        # Formato Frame
        format_frame = ttk.LabelFrame(main_frame, text="Formato de Descarga", padding="10")
        format_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Radio buttons para formato
        format_buttons_frame = ttk.Frame(format_frame)
        format_buttons_frame.pack(fill=tk.X)
        
        ttk.Radiobutton(format_buttons_frame, text="📹 Video (MP4)", 
                        variable=self.format_var, value="mp4",
                        command=self.update_quality_options).pack(side=tk.LEFT, padx=20)
        ttk.Radiobutton(format_buttons_frame, text="🎵 Audio (MP3)", 
                        variable=self.format_var, value="mp3",
                        command=self.update_quality_options).pack(side=tk.LEFT, padx=20)
        
        # Calidad Frame
        quality_frame = ttk.LabelFrame(main_frame, text="Calidad", padding="10")
        quality_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.quality_combo = ttk.Combobox(quality_frame, textvariable=self.quality_var,
                                          state="readonly", font=("Arial", 10))
        self.quality_combo.pack(fill=tk.X, pady=5)
        self.update_quality_options()
        
        # Carpeta de destino Frame
        destination_frame = ttk.LabelFrame(main_frame, text="Carpeta de Destino", padding="10")
        destination_frame.pack(fill=tk.X, pady=(0, 15))
        
        dest_button_frame = ttk.Frame(destination_frame)
        dest_button_frame.pack(fill=tk.X)
        
        self.path_label = ttk.Label(dest_button_frame, text=self.download_path, 
                                    foreground="gray")
        self.path_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Button(dest_button_frame, text="Cambiar...", 
                   command=self.select_download_path).pack(side=tk.RIGHT, padx=(10, 0))
        
        # Barra de progreso
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var,
                                            maximum=100, mode='determinate')
        self.progress_bar.pack(fill=tk.X, pady=(0, 10))
        
        # Label de estado
        self.status_label = ttk.Label(main_frame, text="Listo para descargar", 
                                      foreground="green")
        self.status_label.pack(pady=(0, 15))
        
        # Botón de descarga
        self.download_button = ttk.Button(main_frame, text="⬇️ Descargar", 
                                          command=self.start_download)
        self.download_button.pack(fill=tk.X, ipady=10)
        
        # Estilo
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 11, "bold"))
        
    def update_quality_options(self):
        """Actualiza las opciones de calidad según el formato seleccionado"""
        if self.format_var.get() == "mp4":
            qualities = ["1080p (Full HD)", "720p (HD)", "480p (SD)"]
            self.quality_var.set("1080p (Full HD)")
        else:
            qualities = ["320 kbps (Máxima)", "192 kbps (Alta)", "128 kbps (Estándar)"]
            self.quality_var.set("320 kbps (Máxima)")
        
        self.quality_combo['values'] = qualities
        
    def select_download_path(self):
        """Permite seleccionar la carpeta de destino"""
        folder = filedialog.askdirectory(initialdir=self.download_path)
        if folder:
            self.download_path = folder
            self.path_label.config(text=folder)
    
    def progress_hook(self, d):
        """Actualiza la barra de progreso durante la descarga"""
        if d['status'] == 'downloading':
            # Extraer porcentaje de descarga
            percent_str = d.get('_percent_str', '0%').strip().replace('%', '')
            try:
                percent = float(percent_str)
                self.progress_var.set(percent)
                self.status_label.config(text=f"Descargando... {percent:.1f}%")
            except:
                pass
        elif d['status'] == 'finished':
            self.progress_var.set(100)
            self.status_label.config(text="Procesando archivo...")
    
    def progress_callback(self, stream, chunk, bytes_remaining):
        """Callback de progreso para pytube"""
        try:
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage = (bytes_downloaded / total_size) * 100
            self.root.after(0, lambda: self.progress_var.set(percentage))
            self.root.after(0, lambda: self.status_label.config(
                text=f"Descargando... {percentage:.1f}%", foreground="blue"))
        except:
            pass
    
    def download_with_pytube(self, url):
        """Método 1: Intentar con pytubefix (más simple y confiable)"""
        try:
            print("\n=== Método 1: Usando pytubefix ===")
            yt = YouTube(url, on_progress_callback=self.progress_callback)
            
            print(f"Título: {yt.title}")
            print(f"Duración: {yt.length}s")
            
            if self.format_var.get() == "mp4":
                # Descargar video
                quality_map = {
                    "1080p (Full HD)": "1080p",
                    "720p (HD)": "720p",
                    "480p (SD)": "480p"
                }
                quality = quality_map[self.quality_var.get()]
                
                print(f"Buscando video en {quality}...")
                
                # Intentar obtener la calidad solicitada, si no está disponible tomar la mejor
                stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=quality).first()
                
                if not stream:
                    print(f"Calidad {quality} no disponible, usando la mejor calidad disponible...")
                    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                
                if not stream:
                    print("No se encontró video progresivo, intentando con adaptativo...")
                    stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=False).order_by('resolution').desc().first()
                
            else:
                # Descargar solo audio
                print("Buscando mejor stream de audio...")
                stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            
            if not stream:
                raise Exception("No se encontró ningún stream disponible")
            
            print(f"Stream seleccionado: {stream}")
            
            # Descargar
            output_file = stream.download(output_path=self.download_path)
            
            # Si es MP3, necesitamos convertir
            if self.format_var.get() == "mp3":
                print("Convirtiendo a MP3...")
                base, ext = os.path.splitext(output_file)
                new_file = base + '.mp3'
                
                # Usar ffmpeg para convertir
                import subprocess
                subprocess.run([
                    'ffmpeg', '-i', output_file,
                    '-vn', '-acodec', 'libmp3lame',
                    '-b:a', '320k', new_file, '-y'
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                # Eliminar archivo original
                if os.path.exists(new_file):
                    os.remove(output_file)
                    output_file = new_file
            
            return True, output_file
            
        except Exception as e:
            print(f"Error con pytubefix: {e}")
            return False, str(e)
    
    def download_with_ytdlp(self, url):
        """Método 2: Intentar con yt-dlp (configuración ultra simple)"""
        try:
            print("\n=== Método 2: Usando yt-dlp ===")
            
            if self.format_var.get() == "mp4":
                ydl_opts = {
                    'format': 'best[ext=mp4]/best',
                    'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.progress_hook],
                    'quiet': True,
                }
            else:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.progress_hook],
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',
                    }],
                    'quiet': True,
                }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                
                # Si es mp3, el archivo tendrá extensión .mp3
                if self.format_var.get() == "mp3":
                    base, _ = os.path.splitext(filename)
                    filename = base + '.mp3'
                
                return True, filename
                
        except Exception as e:
            print(f"Error con yt-dlp: {e}")
            return False, str(e)
    
    def clean_youtube_url(self, url):
        """Limpia la URL de YouTube eliminando parámetros de playlist"""
        import re
        
        # Extraer el video ID
        patterns = [
            r'(?:youtube\.com\/watch\?v=)([^&]+)',
            r'(?:youtu\.be\/)([^?]+)',
            r'(?:youtube\.com\/embed\/)([^?]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                video_id = match.group(1)
                clean_url = f"https://www.youtube.com/watch?v={video_id}"
                if clean_url != url:
                    print(f"URL limpiada: {url} -> {clean_url}")
                return clean_url
        
        return url
    
    def download_video(self):
        """Función que realiza la descarga en un thread separado"""
        url = self.url_var.get().strip()
        
        if not url:
            self.root.after(0, lambda: messagebox.showerror("Error", "Por favor ingresa una URL de YouTube"))
            return
        
        # Limpiar URL (remover parámetros de playlist, etc.)
        url = self.clean_youtube_url(url)
        
        print("\n" + "="*60)
        print(f"Iniciando descarga: {url}")
        print(f"Formato: {self.format_var.get()}")
        print(f"Calidad: {self.quality_var.get()}")
        print("="*60)
        
        # Método 1: Intentar con pytubefix primero (más confiable)
        success, result = self.download_with_pytube(url)
        
        if not success:
            print("\nPytubefix falló, intentando con yt-dlp...")
            # Método 2: Si falla, intentar con yt-dlp
            success, result = self.download_with_ytdlp(url)
        
        if success:
            # Éxito
            self.root.after(0, lambda: self.progress_var.set(100))
            self.root.after(0, lambda: self.status_label.config(
                text="✅ Descarga completada!", foreground="green"))
            self.root.after(0, lambda: messagebox.showinfo(
                "Éxito", f"Archivo descargado exitosamente:\n\n{result}"))
            print(f"\n✅ DESCARGA EXITOSA: {result}\n")
        else:
            # Error en ambos métodos
            error_msg = f"No se pudo descargar el video con ningún método.\n\nError: {result}"
            self.root.after(0, lambda: self.status_label.config(
                text="❌ Error en la descarga", foreground="red"))
            self.root.after(0, lambda: messagebox.showerror("Error", error_msg))
            print(f"\n❌ ERROR: {result}\n")
        
        # Reactivar botón
        self.root.after(0, lambda: self.download_button.config(state="normal"))
        
        if not success:
            self.root.after(0, lambda: self.progress_var.set(0))
    
    def start_download(self):
        """Inicia la descarga en un thread separado"""
        self.download_button.config(state="disabled")
        self.status_label.config(text="Iniciando descarga...", foreground="blue")
        self.progress_var.set(0)
        
        # Ejecutar descarga en thread separado para no bloquear UI
        download_thread = threading.Thread(target=self.download_video, daemon=True)
        download_thread.start()

def main():
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()