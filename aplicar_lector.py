"""Página de Quipu: suma la sección Quipu Lector de PDF y corrige textos de Quipu Estudio.
Se puede correr más de una vez sin duplicar nada."""
from pathlib import Path

# ---- ENLACES DE DESCARGA DEL LECTOR ----
STORE_LECTOR = "https://apps.microsoft.com/detail/9N3MC20N9JCC"
APK_LECTOR = "https://github.com/quipu-app/quipu-lector-pdf/releases/latest/download/Quipu-Lector.apk"
# -----------------------------------------

if not Path("img/lector-pdf.jpg").exists():
    raise SystemExit("Falta la imagen img/lector-pdf.jpg (la placa del lector).")

RESPALDOS = Path("respaldos")
MARCA = 'id="lector-pdf"'

CSS = """
  /* Quipu Lector de PDF */
  #lector-pdf { display: flex; flex-wrap: wrap; gap: 56px; align-items: center; padding: 0 24px 100px; scroll-margin-top: 90px; }
  #lector-pdf .foto { flex: 1 1 380px; max-width: 480px; min-width: 0; margin: 0 auto; border-radius: 24px; }
  #lector-pdf .info { flex: 999 1 460px; display: flex; flex-direction: column; gap: 22px; }
  @media (max-width: 700px) { #lector-pdf { padding: 0 18px 56px; gap: 32px; } }
</style>"""

SECCION = f"""  <section id="lector-pdf" class="ancho">
    <div class="info">
      <span class="retro">QUIPU LECTOR DE PDF</span>
      <h2>Tus apuntes en PDF, con la cartuchera a mano.</h2>
      <p>Un lector de PDF pensado para estudiar: abrís tus apuntes, los marcás y los ordenás en carpetas. Si conectás tu Google Drive, te siguen de la compu a la tableta y al celu.</p>
      <div class="funciones">
        <div><b>Cartuchera</b><span>Anotaciones, marcas y subrayado sobre el PDF, y guardás el PDF con tus cambios.</span></div>
        <div><b>Carpetas</b><span>Organización rápida de tus apuntes.</span></div>
        <div><b>Lectura en voz alta</b><span>Escuchá tus apuntes, con un modo estudio.</span></div>
        <div><b>Google Drive</b><span>Tus apuntes sincronizados en la nube.</span></div>
      </div>
      <div class="descarga">
        <a class="boton" href="{STORE_LECTOR}">Descargar para Windows</a>
        <a class="boton boton-claro" href="{APK_LECTOR}">Descargar para Android</a>
        <small>Gratis · Computadoras con Windows desde la Microsoft Store · Celulares y tabletas Android</small>
      </div>
      <details class="instalar">
        <summary>¿Cómo instalo el lector en Android?</summary>
        <ol>
          <li>Desde el celu o la tableta, tocá <b>Descargar para Android</b> y abrí el archivo cuando termine.</li>
          <li>Si Android avisa que no puede instalar apps de esa fuente, tocá <b>Configuración</b>, activá <b>Permitir de esta fuente</b> y volvé atrás.</li>
          <li>Tocá <b>Instalar</b>. Si aparece Play Protect con “App no reconocida”, tocá <b>Más detalles</b> y después <b>Instalar de todas formas</b>.</li>
        </ol>
      </details>
    </div>
    <img class="foto" src="img/lector-pdf.jpg" alt="Quipu Lector de PDF en la compu, la tableta y el celular">
  </section>

  <section id="personajes" class="ancho">"""

TARJETA = """      <div class="lista"><span class="retro">DISPONIBLE</span><b>Quipu Lector de PDF</b><span>Para Windows y Android: tus apuntes con anotaciones, carpetas y Google Drive.</span></div>
      <div><span class="retro" style="color:var(--apagado)">EN EL TALLER</span>"""

REEMPLAZOS = [
    ("</style>", CSS),
    ('      <a href="#personajes">Personajes</a>',
     '      <a href="#lector-pdf">Lector de PDF</a>\n      <a href="#personajes">Personajes</a>'),
    ('  <section id="personajes" class="ancho">', SECCION),
    ("""      <div><span class="retro" style="color:var(--apagado)">EN EL TALLER</span>""", TARJETA),
    ("Cada app de Quipu parte de una pregunta", "Cada app de Quipu Estudio nace de una pregunta"),
    ("Quipu nace de juntar esos mundos", "Quipu Estudio nace de juntar esos mundos"),
    ('\n        <p style="margin-top:14px">Quipu Estudio es mi sello como desarrollador: todo lo que creo lleva esta marca.</p>', ""),
]

ruta = Path("index.html")
texto = ruta.read_text(encoding="utf-8-sig")
if MARCA in texto:
    raise SystemExit("index.html: ya tenía la sección del lector, no lo toqué")
original = texto
for viejo, nuevo in REEMPLAZOS:
    if viejo not in texto:
        raise SystemExit(f"ERROR: no encontré este pedazo en index.html:\n{viejo}")
    texto = texto.replace(viejo, nuevo, 1)
RESPALDOS.mkdir(exist_ok=True)
(RESPALDOS / "index.html.antes-lector").write_text(original, encoding="utf-8")
ruta.write_text(texto, encoding="utf-8")
print("index.html: actualizado (copia en respaldos/index.html.antes-lector)")