"""Página de Quipu: se lee bien en el celular, suma la descarga para Android y la política de privacidad.
Se puede correr más de una vez sin duplicar nada."""
from pathlib import Path

RESPALDOS = Path("respaldos")


def editar(ruta, reemplazos, marca):
    ruta = Path(ruta)
    texto = ruta.read_text(encoding="utf-8-sig")
    if marca in texto:
        print(f"  {ruta}: ya estaba, no lo toqué")
        return
    original = texto
    for viejo, nuevo in reemplazos:
        if viejo not in texto:
            raise SystemExit(f"  ERROR en {ruta}: no encontré este pedazo:\n{viejo}")
        texto = texto.replace(viejo, nuevo, 1)
    RESPALDOS.mkdir(exist_ok=True)
    (RESPALDOS / (ruta.name + ".antes")).write_text(original, encoding="utf-8")
    ruta.write_text(texto, encoding="utf-8")
    print(f"  {ruta}: actualizado (copia en respaldos)")


APK = "https://github.com/quipu-app/quipu-celular/releases/latest/download/Quipu.apk"

# ---------- index.html ----------
CSS_INDEX = """
  /* Descarga para Android */
  #asistente .foto, .sobre img { min-width: 0; }
  .boton-claro { background: var(--crema); box-shadow: 0 4px 0 #bfb59c; }
  .boton-claro:active { box-shadow: 0 1px 0 #bfb59c; }
  .instalar { background: var(--tarjeta); border-radius: 14px; padding: 4px 18px; }
  .instalar summary { cursor: pointer; padding: 12px 0; font-weight: 600; color: var(--oro); }
  .instalar ol { margin: 0 0 14px; padding-left: 22px; display: flex; flex-direction: column; gap: 8px;
                 font-size: 16px; line-height: 1.5; color: var(--texto); }
  .instalar p { margin: 0 0 14px; font-size: 15px; line-height: 1.5; color: var(--apagado); }
  footer .derecha { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 22px; }

  /* Pantallas chicas (celulares) */
  @media (max-width: 700px) {
    nav { padding: 8px 16px; gap: 8px 12px; }
    nav .logo img { height: 32px; }
    nav .boton { margin-left: auto; padding: 8px 14px; font-size: 14px; }
    nav .links { order: 3; flex: 1 1 100%; flex-wrap: nowrap; overflow-x: auto; gap: 18px; font-size: 15px;
                 padding-bottom: 2px; scrollbar-width: none; }
    nav .links::-webkit-scrollbar { display: none; }
    nav .links a { white-space: nowrap; }
    .retro { font-size: 22px; }
    .ancho { padding: 0 18px; }
    #inicio { padding: 48px 18px 44px; gap: 16px; }
    #inicio p, .por-que p, .sobre p { font-size: 17px; }
    .por-que, .sobre { padding: 52px 18px; gap: 24px; }
    .por-que h2 { font-size: 30px; }
    #asistente { padding: 56px 18px; gap: 32px; }
    .info > p { font-size: 17px; }
    .descarga .boton { flex: 1 1 100%; text-align: center; font-size: 18px; padding: 14px 20px; }
    #personajes { padding: 56px 18px; }
    .personaje img { height: 170px; }
    .apps { padding-bottom: 56px; }
    #comentarios { padding: 56px 18px; }
    footer .ancho { padding: 24px 18px; }
  }
</style>"""

editar("index.html", [
    ("\n</style>", CSS_INDEX),
    ('      <p>Nació de una necesidad propia: las herramientas que uso a diario ya existían, pero estaban repartidas en distintos programas. El asistente las reúne en una sola consola.</p>\n',
     '      <p>Nació de una necesidad propia: las herramientas que uso a diario ya existían, pero estaban repartidas en distintos programas. El asistente las reúne en una sola consola.</p>\n'
     '      <p>Y también va en tu celu: si conectás tu Google Drive, tus notas y tu agenda te siguen de un aparato al otro.</p>\n'),
    ('            <div class="descarga">\n'
     '        <a class="boton" id="descargar" href="https://apps.microsoft.com/detail/9MW60L67MV8W">Descargar desde Microsoft Store</a>\n'
     '        <small>Gratis · Windows 10 y 11 · Se actualiza solo</small>\n'
     '      </div>\n',
     '      <div class="descarga">\n'
     '        <a class="boton" id="descargar" href="https://apps.microsoft.com/detail/9MW60L67MV8W">Descargar para Windows</a>\n'
     f'        <a class="boton boton-claro" id="descargar-android" href="{APK}">Descargar para Android</a>\n'
     '        <small>Gratis · Windows 10 y 11 desde la Microsoft Store · Android 7 o más nuevo</small>\n'
     '      </div>\n'
     '      <details class="instalar">\n'
     '        <summary>¿Cómo instalo la app en Android?</summary>\n'
     '        <ol>\n'
     '          <li>Desde el celu, tocá <b>Descargar para Android</b> y abrí el archivo <b>Quipu.apk</b> cuando termine.</li>\n'
     '          <li>Si Android avisa que no puede instalar apps de esa fuente, tocá <b>Configuración</b>, activá <b>Permitir de esta fuente</b> y volvé atrás.</li>\n'
     '          <li>Tocá <b>Instalar</b>. Si aparece Play Protect con “App no reconocida”, tocá <b>Más detalles</b> y después <b>Instalar de todas formas</b>.</li>\n'
     '          <li>Abrí Quipu y, si querés tener tus datos de la compu, andá a <b>Ajustes → Google Drive → Conectar</b>.</li>\n'
     '        </ol>\n'
     '        <p>Esos avisos aparecen porque la app no viene de Google Play. Es la misma versión que uso yo todos los días, firmada siempre con la misma llave.</p>\n'
     '      </details>\n'),
    ('      <div><span class="retro" style="color:var(--apagado)">PRONTO</span><b>Quipu para celular</b><span>El asistente en tu Android, con tus mismos datos.</span></div>\n',
     '      <div class="lista"><span class="retro">DISPONIBLE</span><b>Quipu para celular</b><span>Para Android, con tus mismos datos por Google Drive.</span></div>\n'),
    ('      <span>@quipu_app</span>\n    </a>\n    <small>© 2026 Quipu · Hecho en Argentina</small>\n',
     '      <span>@quipu_app</span>\n    </a>\n    <div class="derecha">\n      <a href="privacidad.html">Privacidad</a>\n'
     '      <small>© 2026 Quipu · Hecho en Argentina</small>\n    </div>\n'),
], marca="descargar-android")

# ---------- descargables.html ----------
CSS_DESC = """
  /* Pantallas chicas (celulares) */
  @media (max-width: 700px) {
    nav { padding: 8px 16px; gap: 8px 12px; }
    nav img { height: 32px; }
    nav .boton { margin-left: auto; padding: 8px 14px; font-size: 14px; }
    nav .links { order: 3; flex: 1 1 100%; flex-wrap: nowrap; overflow-x: auto; gap: 18px; font-size: 15px;
                 padding-bottom: 2px; scrollbar-width: none; }
    nav .links::-webkit-scrollbar { display: none; }
    nav .links a { white-space: nowrap; }
    main { padding: 32px 16px 60px; }
    .retro { font-size: 22px; }
    .intro { font-size: 17px; }
    .indice a { padding: 6px 12px; font-size: 15px; }
    section { padding-top: 36px; scroll-margin-top: 110px; }
    .galeria { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
    .tarjeta { padding: 8px; border-radius: 12px; }
    .tarjeta b { font-size: 13px; overflow-wrap: anywhere; }
    .tarjeta span { font-size: 13px; padding: 5px 10px; }
  }
</style>"""

editar("descargables.html", [
    ("\n</style>", CSS_DESC),
    ("  </nav>\n  </nav>\n", "  </nav>\n"),
], marca="Pantallas chicas")

# ---------- privacidad.html ----------
privacidad = Path("privacidad.html")
if privacidad.exists():
    print("  privacidad.html: ya estaba, no lo toqué")
else:
    privacidad.write_text("""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quipu · Política de privacidad</title>
<link rel="icon" href="img/favicon.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=VT323&display=swap">
<style>
  :root { --fondo: #0d1730; --fondo2: #0a1226; --tarjeta: #16254a; --crema: #f5eedc; --texto: #c9d2e8;
          --apagado: #9fb0d6; --oro: #f4b83a; --azul: #2f5fb3; }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--fondo); color: var(--crema); font-family: 'Fredoka', 'Trebuchet MS', sans-serif; }
  header { background: var(--fondo2); border-bottom: 3px solid var(--azul); }
  nav { display: flex; align-items: center; gap: 16px; padding: 10px 20px; max-width: 900px; margin: 0 auto; }
  nav img { height: 40px; width: auto; display: block; }
  nav a.volver { margin-left: auto; color: var(--crema); text-decoration: none; font-size: 16px; }
  main { max-width: 800px; margin: 0 auto; padding: 48px 20px 80px; }
  .retro { font-family: 'VT323', monospace; font-size: 24px; color: var(--oro); letter-spacing: 2px; }
  h1 { margin: 6px 0 8px; font-size: clamp(30px, 5vw, 44px); line-height: 1.1; }
  h2 { margin: 36px 0 10px; font-size: 24px; color: var(--oro); }
  p, li { font-size: 17px; line-height: 1.6; color: var(--texto); }
  ul { padding-left: 22px; }
  b { color: var(--crema); }
  a { color: var(--oro); }
  .fecha { color: var(--apagado); font-size: 15px; }
</style>
</head>
<body>
<header>
  <nav>
    <a href="index.html" aria-label="Quipu, ir al inicio"><img src="img/placa.png" alt="Quipu"></a>
    <a class="volver" href="index.html">‹ Volver a la página</a>
  </nav>
</header>
<main>
  <span class="retro">PRIVACIDAD</span>
  <h1>Política de privacidad de Quipu</h1>
  <p class="fecha">Última actualización: 12 de noviembre de 2026</p>

  <p>Quipu es un asistente para Windows y Android hecho por Eric (Quipu Estudio), en Argentina. Esta página explica, en palabras simples, qué datos usa Quipu, dónde se guardan y qué podés hacer con ellos.</p>

  <h2>Lo que guardás en Quipu queda en tu aparato</h2>
  <p>Tus notas, carpetas, eventos de la agenda, respuestas, tu nombre y tus ajustes se guardan en tu propia compu o en tu propio celu. En la compu, dentro de la carpeta de datos de Quipu de tu usuario de Windows; en el celu, dentro de la app. Quipu no tiene un servidor propio que reciba esos datos.</p>

  <h2>Google Drive (solo si lo conectás)</h2>
  <p>Si tocás <b>Conectar</b> en Ajustes, Quipu te pide permiso para usar su <b>carpeta privada de la app</b> dentro de tu Google Drive (el permiso <b>drive.appdata</b>). Ahí guarda una copia de tus notas, carpetas, agenda y tu nombre, para que la compu y el celu tengan lo mismo.</p>
  <ul>
    <li>Ese permiso solo deja a Quipu ver y escribir sus propios archivos. <b>No puede ver ni tocar el resto de tu Drive.</b></li>
    <li>Los datos viajan directo entre tu aparato y tu cuenta de Google. Nadie más los recibe ni los ve, tampoco quien hace Quipu.</li>
    <li>Podés desconectarte cuando quieras desde <b>Ajustes → Google Drive → Desconectar</b>.</li>
    <li>Para borrar la copia que quedó en tu Drive: en Google Drive, entrá a <b>Configuración → Administrar apps</b>, buscá Quipu y elegí <b>Borrar datos ocultos de la app</b>.</li>
  </ul>
  <p>El uso que hace Quipu de la información recibida de las APIs de Google cumple con la <a href="https://developers.google.com/terms/api-services-user-data-policy">Política de Datos del Usuario de los Servicios de API de Google</a>, incluidos los requisitos de Uso Limitado.</p>

  <h2>Notas compartidas</h2>
  <p>Si compartís una nota con un código, el contenido de esa nota se guarda en Firebase (un servicio de Google) para que la otra persona pueda abrirla con ese código. Solo se sube la nota que elegís compartir.</p>

  <h2>El tiempo</h2>
  <p>Para mostrarte el clima, Quipu consulta el servicio gratuito <a href="https://open-meteo.com/">Open-Meteo</a> con la ciudad que elegís en la función Tiempo. Quipu no usa el GPS ni tu ubicación exacta.</p>

  <h2>Actualizaciones</h2>
  <p>La versión de compu consulta GitHub para saber si hay una versión nueva de Quipu. Esa consulta no incluye tus datos.</p>

  <h2>Comentarios en esta página</h2>
  <p>Si dejás un comentario en la página, el nombre y el texto que escribís se publican y se guardan en Firebase. No pongas ahí datos que no quieras que se vean.</p>

  <h2>Lo que Quipu no hace</h2>
  <ul>
    <li>No vende ni comparte tus datos.</li>
    <li>No muestra publicidad.</li>
    <li>No usa herramientas de seguimiento ni de análisis de uso.</li>
  </ul>

  <h2>Contacto</h2>
  <p>Si tenés dudas sobre tus datos, escribime por Instagram a <a href="https://instagram.com/quipu_app">@quipu_app</a> o dejá un mensaje en la sección de <a href="index.html#comentarios">comentarios</a>.</p>

  <h2>Cambios en esta política</h2>
  <p>Si esta política cambia, la vas a encontrar actualizada en esta misma página, con la fecha nueva arriba.</p>
</main>
</body>
</html>
""", encoding="utf-8")
    print("  privacidad.html: creada")

print("\nListo.")