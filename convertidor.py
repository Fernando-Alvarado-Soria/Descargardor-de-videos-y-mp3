import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import os
import yt_dlp

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("650x660")
        self.root.resizable(True, True)
        self.root.configure(bg="#1e1e2e")

        self.url_var          = tk.StringVar()
        self.format_var       = tk.StringVar(value="mp4")
        self.quality_var      = tk.StringVar(value="1080p (Full HD)")
        self.cookies_path_var = tk.StringVar(value="")
        self.download_path    = os.path.expanduser("~/Downloads")

        self._setup_styles()
        self._setup_ui()

    # ────────────────────────────────────────────────────────────
    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        BG      = "#1e1e2e"
        SURFACE = "#2a2a3e"
        ACCENT  = "#89b4fa"
        TEXT    = "#cdd6f4"
        MUTED   = "#a6adc8"
        SUCCESS = "#a6e3a1"
        ERROR   = "#f38ba8"
        WARN    = "#fab387"

        style.configure(".",           background=BG, foreground=TEXT, font=("Segoe UI", 10))
        style.configure("TFrame",      background=BG)
        style.configure("TLabel",      background=BG, foreground=TEXT)
        style.configure("TLabelframe", background=BG, foreground=ACCENT, relief="flat")
        style.configure("TLabelframe.Label", background=BG, foreground=ACCENT,
                        font=("Segoe UI", 10, "bold"))
        style.configure("TEntry",      fieldbackground=SURFACE, foreground=TEXT,
                        insertcolor=TEXT, relief="flat")
        style.configure("TCombobox",   fieldbackground=SURFACE, foreground=TEXT,
                        selectbackground=SURFACE)
        style.map("TCombobox", fieldbackground=[("readonly", SURFACE)])
        style.configure("TRadiobutton", background=BG, foreground=TEXT, indicatorcolor=ACCENT)
        style.map("TRadiobutton", background=[("active", BG)])
        style.configure("TButton",     background=ACCENT, foreground="#1e1e2e",
                        font=("Segoe UI", 11, "bold"), relief="flat", padding=6)
        style.map("TButton",
            background=[("active", "#74c7ec"), ("disabled", SURFACE)],
            foreground=[("disabled", MUTED)])
        style.configure("Secondary.TButton", background=SURFACE, foreground=ACCENT,
                        font=("Segoe UI", 9), relief="flat", padding=4)
        style.map("Secondary.TButton", background=[("active", "#313244")])
        style.configure("Danger.TButton", background="#f38ba8", foreground="#1e1e2e",
                        font=("Segoe UI", 9), relief="flat", padding=4)
        style.map("Danger.TButton", background=[("active", "#eb6f92")])
        style.configure("Horizontal.TProgressbar",
            troughcolor=SURFACE, background=ACCENT, thickness=8)
        style.configure("Status.TLabel",  background=BG, foreground=SUCCESS, font=("Segoe UI", 10))
        style.configure("Error.TLabel",   background=BG, foreground=ERROR,   font=("Segoe UI", 10))
        style.configure("Muted.TLabel",   background=BG, foreground=MUTED,   font=("Segoe UI", 9))
        style.configure("Warn.TLabel",    background=BG, foreground=WARN,    font=("Segoe UI", 9))
        style.configure("Title.TLabel",   background=BG, foreground=ACCENT,  font=("Segoe UI", 18, "bold"))

        self._colors = dict(BG=BG, SURFACE=SURFACE, ACCENT=ACCENT,
                            TEXT=TEXT, MUTED=MUTED, SUCCESS=SUCCESS,
                            ERROR=ERROR, WARN=WARN)

    # ────────────────────────────────────────────────────────────
    def _setup_ui(self):
        main = ttk.Frame(self.root, padding="20")
        main.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main, text="  YouTube Downloader", style="Title.TLabel").pack(pady=(0, 16))

        # ── URL ─────────────────────────────────────────────────
        url_frame = ttk.LabelFrame(main, text=" URL de YouTube ", padding="10")
        url_frame.pack(fill=tk.X, pady=(0, 10))
        self.url_entry = ttk.Entry(url_frame, textvariable=self.url_var, font=("Segoe UI", 10))
        self.url_entry.pack(fill=tk.X)

        # ── COOKIES ─────────────────────────────────────────────
        ck_frame = ttk.LabelFrame(main, text=" Autenticacion con Cookies ", padding="10")
        ck_frame.pack(fill=tk.X, pady=(0, 10))

        # Metodo 1: archivo (PRIORIDAD ALTA)
        ttk.Label(ck_frame,
                  text="Metodo 1 — Archivo cookies.txt  (RECOMENDADO, tiene prioridad)",
                  style="Warn.TLabel").pack(anchor=tk.W)
        ttk.Label(ck_frame,
                  text="Exporta las cookies con la extension 'Get cookies.txt LOCALLY'\n"
                       "en Chrome/Firefox mientras tienes YouTube abierto y sesion iniciada.",
                  style="Muted.TLabel", justify=tk.LEFT).pack(anchor=tk.W, pady=(2, 6))

        file_row = ttk.Frame(ck_frame)
        file_row.pack(fill=tk.X, pady=(0, 10))
        self.ck_label = ttk.Label(file_row, text="Sin archivo cargado", style="Muted.TLabel")
        self.ck_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(file_row, text="Cargar cookies.txt",
                   style="Secondary.TButton",
                   command=self._select_cookies).pack(side=tk.RIGHT, padx=(4, 0))
        ttk.Button(file_row, text="X Quitar",
                   style="Danger.TButton",
                   command=self._clear_cookies).pack(side=tk.RIGHT)

        # Separador
        sep_label = ttk.Label(ck_frame,
            text="─" * 60,
            style="Muted.TLabel")
        sep_label.pack(fill=tk.X)

        # Metodo 2: navegador (requiere que Chrome este CERRADO)
        ttk.Label(ck_frame,
                  text="Metodo 2 — Desde navegador  (Chrome debe estar CERRADO)",
                  style="Warn.TLabel").pack(anchor=tk.W, pady=(6, 0))
        ttk.Label(ck_frame,
                  text="yt-dlp lee la base de datos del navegador. Si Chrome esta abierto,\n"
                       "el archivo estara bloqueado y fallara con el error 'Could not copy'.",
                  style="Muted.TLabel", justify=tk.LEFT).pack(anchor=tk.W, pady=(2, 6))

        browser_row = ttk.Frame(ck_frame)
        browser_row.pack(fill=tk.X)
        ttk.Label(browser_row, text="Navegador:", style="Muted.TLabel").pack(side=tk.LEFT)
        self.browser_var = tk.StringVar(value="ninguno")
        browsers = ["ninguno", "chrome", "firefox", "edge", "brave", "opera", "chromium"]
        self.browser_combo = ttk.Combobox(browser_row, textvariable=self.browser_var,
                                          values=browsers, state="readonly", width=11)
        self.browser_combo.pack(side=tk.LEFT, padx=(6, 0))
        self.browser_status = ttk.Label(browser_row,
            text="  (ignorado si hay archivo cookies.txt cargado)", style="Muted.TLabel")
        self.browser_status.pack(side=tk.LEFT)
        self.browser_var.trace_add("write", self._on_browser_change)
        self.cookies_path_var.trace_add("write", self._update_browser_status)

        # ── FORMATO ─────────────────────────────────────────────
        fmt_frame = ttk.LabelFrame(main, text=" Formato ", padding="10")
        fmt_frame.pack(fill=tk.X, pady=(0, 10))
        row = ttk.Frame(fmt_frame)
        row.pack(fill=tk.X)
        ttk.Radiobutton(row, text="Video (MP4)", variable=self.format_var,
                        value="mp4", command=self._update_quality).pack(side=tk.LEFT, padx=20)
        ttk.Radiobutton(row, text="Audio (MP3)", variable=self.format_var,
                        value="mp3", command=self._update_quality).pack(side=tk.LEFT, padx=20)

        # ── CALIDAD ─────────────────────────────────────────────
        q_frame = ttk.LabelFrame(main, text=" Calidad ", padding="10")
        q_frame.pack(fill=tk.X, pady=(0, 10))
        self.quality_combo = ttk.Combobox(q_frame, textvariable=self.quality_var,
                                          state="readonly", font=("Segoe UI", 10))
        self.quality_combo.pack(fill=tk.X)
        self._update_quality()

        # ── DESTINO ─────────────────────────────────────────────
        dest_frame = ttk.LabelFrame(main, text=" Carpeta de Destino ", padding="10")
        dest_frame.pack(fill=tk.X, pady=(0, 10))
        dest_row = ttk.Frame(dest_frame)
        dest_row.pack(fill=tk.X)
        self.path_label = ttk.Label(dest_row, text=self.download_path, style="Muted.TLabel")
        self.path_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(dest_row, text="Cambiar...", style="Secondary.TButton",
                   command=self._select_path).pack(side=tk.RIGHT)

        # ── PROGRESO ────────────────────────────────────────────
        self.progress_var = tk.DoubleVar()
        ttk.Progressbar(main, variable=self.progress_var, maximum=100, mode="determinate",
                        style="Horizontal.TProgressbar").pack(fill=tk.X, pady=(0, 6))

        self.status_label = ttk.Label(main, text="Listo para descargar", style="Status.TLabel")
        self.status_label.pack(pady=(0, 10))

        self.download_button = ttk.Button(main, text="  Descargar", command=self._start)
        self.download_button.pack(fill=tk.X, ipady=8)

    # ────────────────────────────────────────────────────────────
    # Helpers UI
    # ────────────────────────────────────────────────────────────
    def _update_quality(self):
        if self.format_var.get() == "mp4":
            opts = ["1080p (Full HD)", "720p (HD)", "480p (SD)", "Mejor disponible"]
            self.quality_var.set("1080p (Full HD)")
        else:
            opts = ["320 kbps (Maxima)", "192 kbps (Alta)", "128 kbps (Estandar)"]
            self.quality_var.set("320 kbps (Maxima)")
        self.quality_combo["values"] = opts

    def _select_path(self):
        folder = filedialog.askdirectory(initialdir=self.download_path)
        if folder:
            self.download_path = folder
            self.path_label.config(text=folder)

    def _select_cookies(self):
        path = filedialog.askopenfilename(
            title="Selecciona cookies.txt",
            filetypes=[("Archivo de cookies", "*.txt"), ("Todos", "*.*")])
        if path:
            self.cookies_path_var.set(path)
            self.ck_label.config(text=os.path.basename(path))
            self._update_browser_status()

    def _clear_cookies(self):
        self.cookies_path_var.set("")
        self.ck_label.config(text="Sin archivo cargado")
        self._update_browser_status()

    def _on_browser_change(self, *_):
        self._update_browser_status()

    def _update_browser_status(self, *_):
        ck_file = self.cookies_path_var.get()
        browser = self.browser_var.get()
        if ck_file and os.path.isfile(ck_file):
            self.browser_status.config(
                text="  (ignorado — se usara el archivo cookies.txt)")
        elif browser and browser != "ninguno":
            self.browser_status.config(
                text="  IMPORTANTE: cierra Chrome/navegador antes de descargar")
        else:
            self.browser_status.config(
                text="  (ignorado si hay archivo cookies.txt cargado)")

    def _set_status(self, text, ok=True):
        self.status_label.config(
            text=text,
            style="Status.TLabel" if ok else "Error.TLabel")

    # ────────────────────────────────────────────────────────────
    # Progreso yt-dlp
    # ────────────────────────────────────────────────────────────
    def _progress_hook(self, d):
        if d["status"] == "downloading":
            pct_str = d.get("_percent_str", "0%").strip().replace("%", "")
            try:
                pct = float(pct_str)
                self.root.after(0, lambda p=pct: self.progress_var.set(p))
                self.root.after(0, lambda p=pct: self._set_status(f"Descargando... {p:.1f}%"))
            except ValueError:
                pass
        elif d["status"] == "finished":
            self.root.after(0, lambda: self.progress_var.set(100))
            self.root.after(0, lambda: self._set_status("Procesando archivo..."))

    # ────────────────────────────────────────────────────────────
    # Opciones yt-dlp
    # ────────────────────────────────────────────────────────────
    def _build_ydl_opts(self):
        fmt  = self.format_var.get()
        qual = self.quality_var.get()

        if fmt == "mp4":
            qmap = {
                "1080p (Full HD)":  "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=1080]+bestaudio/best[height<=1080]/best",
                "720p (HD)":        "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=720]+bestaudio/best[height<=720]/best",
                "480p (SD)":        "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=480]+bestaudio/best[height<=480]/best",
                "Mejor disponible": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            }
            opts = {
                "format":               qmap.get(qual, "best[ext=mp4]/best"),
                "merge_output_format":  "mp4",
                "outtmpl":              os.path.join(self.download_path, "%(title)s.%(ext)s"),
                "progress_hooks":       [self._progress_hook],
                "quiet":                False,
            }
        else:
            bmap = {
                "320 kbps (Maxima)":   "320",
                "192 kbps (Alta)":     "192",
                "128 kbps (Estandar)": "128",
            }
            opts = {
                "format":          "bestaudio/best",
                "outtmpl":         os.path.join(self.download_path, "%(title)s.%(ext)s"),
                "progress_hooks":  [self._progress_hook],
                "postprocessors":  [{
                    "key":              "FFmpegExtractAudio",
                    "preferredcodec":   "mp3",
                    "preferredquality": bmap.get(qual, "320"),
                }],
                "quiet": False,
            }

        # ── Autenticacion: archivo tiene PRIORIDAD sobre navegador ──
        ck_file = self.cookies_path_var.get()
        browser = self.browser_var.get()

        if ck_file and os.path.isfile(ck_file):
            # Metodo 1: archivo cookies.txt (siempre preferido)
            opts["cookiefile"] = ck_file
        elif browser and browser != "ninguno":
            # Metodo 2: navegador (solo si el navegador esta CERRADO)
            opts["cookiesfrombrowser"] = (browser,)

        return opts

    # ────────────────────────────────────────────────────────────
    # Descarga
    # ────────────────────────────────────────────────────────────
    def _clean_url(self, url):
        import re
        for pat in [
            r"youtube\.com/watch\?(?:.*&)?v=([A-Za-z0-9_-]{11})",
            r"youtu\.be/([A-Za-z0-9_-]{11})",
            r"youtube\.com/embed/([A-Za-z0-9_-]{11})",
        ]:
            m = re.search(pat, url)
            if m:
                return f"https://www.youtube.com/watch?v={m.group(1)}"
        return url

    def _download_thread(self):
        url = self.url_var.get().strip()
        if not url:
            self.root.after(0, lambda: messagebox.showerror(
                "Error", "Por favor ingresa una URL de YouTube"))
            self.root.after(0, lambda: self.download_button.config(state="normal"))
            return

        url     = self._clean_url(url)
        ck_file = self.cookies_path_var.get()
        browser = self.browser_var.get()

        # Validacion previa
        if not ck_file and (not browser or browser == "ninguno"):
            resp = messagebox.askyesno(
                "Sin autenticacion",
                "No hay cookies configuradas.\n\n"
                "YouTube probablemente bloqueara la descarga.\n"
                "¿Intentar de todas formas?")
            if not resp:
                self.root.after(0, lambda: self.download_button.config(state="normal"))
                return

        try:
            opts = self._build_ydl_opts()
            self.root.after(0, lambda: self._set_status("Conectando con YouTube..."))

            with yt_dlp.YoutubeDL(opts) as ydl:
                info     = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                if self.format_var.get() == "mp3":
                    base, _ = os.path.splitext(filename)
                    filename = base + ".mp3"

            self.root.after(0, lambda: self.progress_var.set(100))
            self.root.after(0, lambda: self._set_status("Descarga completada!"))
            self.root.after(0, lambda f=filename: messagebox.showinfo(
                "Exito", f"Archivo descargado correctamente:\n\n{f}"))

        except Exception as e:
            err = str(e)
            print(f"ERROR: {err}")

            if "Could not copy" in err or "cookie database" in err.lower() or "locked" in err.lower():
                msg = (
                    "Error al leer las cookies del navegador.\n\n"
                    "Causa: Chrome (u otro navegador) esta ABIERTO y tiene\n"
                    "el archivo de cookies bloqueado.\n\n"
                    "Solucion inmediata:\n"
                    "  1. Cierra COMPLETAMENTE Chrome (o el navegador seleccionado).\n"
                    "  2. Vuelve a intentar la descarga.\n\n"
                    "Solucion alternativa (sin cerrar el navegador):\n"
                    "  1. En Chrome/Firefox, instala 'Get cookies.txt LOCALLY'.\n"
                    "  2. Ve a youtube.com con sesion iniciada.\n"
                    "  3. Exporta el archivo cookies.txt.\n"
                    "  4. Cargalo con el boton 'Cargar cookies.txt'.\n"
                    "  5. Cambia el navegador a 'ninguno'."
                )
                self.root.after(0, lambda: messagebox.showerror("Navegador bloqueando cookies", msg))
            elif "Sign in to confirm" in err or "bot" in err.lower():
                msg = (
                    "YouTube detecto la descarga como bot.\n\n"
                    "Soluciones:\n"
                    "1. Carga un archivo cookies.txt exportado desde el navegador\n"
                    "   (extension 'Get cookies.txt LOCALLY').\n\n"
                    "2. O cierra Chrome y selecciona 'chrome' en navegador."
                )
                self.root.after(0, lambda: messagebox.showerror("Error de autenticacion", msg))
            else:
                self.root.after(0, lambda e=err: messagebox.showerror("Error de descarga", e))

            self.root.after(0, lambda: self._set_status("Error en la descarga", ok=False))
            self.root.after(0, lambda: self.progress_var.set(0))

        finally:
            self.root.after(0, lambda: self.download_button.config(state="normal"))

    def _start(self):
        self.download_button.config(state="disabled")
        self._set_status("Iniciando descarga...")
        self.progress_var.set(0)
        threading.Thread(target=self._download_thread, daemon=True).start()


def main():
    root = tk.Tk()
    YouTubeDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()