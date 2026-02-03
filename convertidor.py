import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yt_dlp
import threading
import os

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
    
    def download_video(self):
        """Función que realiza la descarga en un thread separado"""
        url = self.url_var.get().strip()
        
        if not url:
            messagebox.showerror("Error", "Por favor ingresa una URL de YouTube")
            return
        
        try:
            # Configuración según formato
            if self.format_var.get() == "mp4":
                quality_map = {
                    "1080p (Full HD)": "1080",
                    "720p (HD)": "720",
                    "480p (SD)": "480"
                }
                quality = quality_map[self.quality_var.get()]
                
                ydl_opts = {
                    'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]',
                    'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.progress_hook],
                    'merge_output_format': 'mp4'
                }
            else:  # mp3
                quality_map = {
                    "320 kbps (Máxima)": "320",
                    "192 kbps (Alta)": "192",
                    "128 kbps (Estándar)": "128"
                }
                bitrate = quality_map[self.quality_var.get()]
                
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': bitrate,
                    }],
                    'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.progress_hook]
                }
            
            # Descargar
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # Actualizar UI
            self.root.after(0, lambda: self.status_label.config(
                text="✅ Descarga completada!", foreground="green"))
            self.root.after(0, lambda: messagebox.showinfo(
                "Éxito", f"Archivo descargado en:\n{self.download_path}"))
            
        except Exception as e:
            error_msg = str(e)
            self.root.after(0, lambda: self.status_label.config(
                text=f"❌ Error: {error_msg}", foreground="red"))
            self.root.after(0, lambda: messagebox.showerror(
                "Error", f"Error al descargar:\n{error_msg}"))
        finally:
            self.root.after(0, lambda: self.download_button.config(state="normal"))
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