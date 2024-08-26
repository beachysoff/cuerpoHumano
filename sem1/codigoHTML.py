# Código para crear un archivo HTML

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>El Fascinante Mundo del Cuerpo Humano</title>
</head>
<body>
  <header>
    <h1>El Fascinante Mundo del Cuerpo Humano</h1>
  </header>

  <section>
    <p>Bienvenido a mi sitio web dedicado a explorar y comprender el cuerpo humano.
    Aquí encontrarás información detallada sobre cómo funciona nuestro cuerpo, sus sistemas, órganos y procesos fundamentales.
    Este sitio está diseñado para todos aquellos que desean conocer más sobre la biología y la anatomía humana.</p>
    <p>El cuerpo humano es una de las estructuras más fascinantes y complejas que existen en la naturaleza.
    Desde el momento en que un óvulo es fertilizado, se comienza a formar un ser humano que, tras un proceso de desarrollo de unos nueve meses,
    se convertirá en un individuo capaz de interactuar con el mundo. En este sitio encontrarás infromación sobre la anatomía,
    fisiología, el funcionamiento y el papel del cuerpo humano a lo largo de la vida, así como su relación con la salud y el bienestar.</p>
  </section>

  <section>
    <h3>Temas Principales</h3>
    <ul>
    <li>Sistemas del cuerpo humano</li>
    <li>Tejidos del cuerpo humano</li>
    <li>Órganos vitales</li>
    <li>Fisiología del cuerpo humano</li>
    <li>Contacto</li>
    </ul>
  </section>

  <section>
    <img src="david.jpg" alt="David de Miguel Ángel">
    <p>David de Miguel Ángel</p>
  </section>

  <footer>
    <p>Desarrollado por: Sofía Rico</p>
    <p>Contacto: 3233197546 | Correo: <a href="mailto:ricozaratesofia@gmail.com">ricozaratesofia@gmail.com</a></p>
    <p>Institución: Skolmi</p>
  </footer>
</body>
</html>

"""

# Crear el archivo HTML
with open("cuerpo_humano.html", "w") as file:
    file.write(html_content)

print("Archivo HTML
 'cuerpo_humano.html' creado exitosamente.")
