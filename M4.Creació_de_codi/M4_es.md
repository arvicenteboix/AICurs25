---
# Información general del documento
title: 4. Creación de código
lang: es
page-background: img/bg.png
linkcolor: blue

# Portada
titlepage: true
titlepage-rule-height: 3
titlepage-rule-color: eeeee4
titlepage-text-color: eeeee4
titlepage-background: img/U4c.png

# Tabla de contenidos
toc: true
toc-own-page: true
toc-title: Contenidos

# Cabeceras y pies
header-left: Creación de código. 
header-right: Curso 2024-2025
footer-left: CEFIRE FP
footer-right: \thepage/\pageref{LastPage}

# Imágenes
float-placement-figuro: H
caption-justification: centering

# Listados de código
listings-no-page-break: true
listings-disable-line-numbers: false

header-includes:
- |
  ```{=latex}
  \usepackage{lastpage}
  \usepackage{awesomebox}
  \usepackage{caption}
  \usepackage{array}
  \usepackage{tabularx}
  \usepackage{ragged2e}
  \usepackage{multirow}
  \usepackage{xcolor}
  \setkeys{Gin}{width=\maxwidth,height=\maxheight,keepaspectratio}

  ```
pandoc-latex-environment:
  noteblock: [note]
  tipblock: [tip]
  warningblock: [warning]
  cautionblock: [caution]
  importantblock: [important]
...

<!-- \awesomebox[violet]{2pt}{\faRocket}{violet}{Lorem ipsum…} -->

<!-- \awesomebox[violet]{2pt}{\faRobot}{violet}{Lorem ipsum…} -->

<!-- IMATGE ![Pregunta inicial](./img/proxi/5b.png){ width=70% } -->

<!-- \textbf{greatest} -->

<!-- \awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{greatest}\hfill \break} -->

\vspace*{\fill}

![](img/cc.png){ height=50px }

Este documento está sujeto a una licencia creative commons que permite su difusión y uso comercial reconociendo siempre la autoría de su creador. Este documento se encuentra para ser modificado en el siguiente repositorio de github:
<!-- CANVIAR L'ENLLAÇ -->
[https://github.com/arvicenteboix/AICurs25](https://github.com/arvicenteboix/AICurs25)
\newpage


# Introducción

En esta unidad, lo primero que vamos a pedirles es que no se pongan nerviosos ni se desesperen, pero cuando hablamos de inteligencia artificial, tenemos que hablar de una de sus principales funciones y que verdaderamente está revolucionando muchos aspectos de la vida profesional de muchos trabajadores.

Estamos hablando de la creación de código. En este módulo vamos a utilizar diferentes lenguajes de programación, tocaremos python, html, xml y javascript, ya que son lenguajes muy conocidos y pueden facilitarnos la tarea de crear código.

# Utilizando modelos libres

## Objetivo

Nuestro objetivo va a ser crear una aplicación que active la cámara web de nuestro ordenador y detecte si estamos sonriendo o estamos tristes.

Para realizar esta aplicación, tenemos que conocer en qué sistema operativo vamos a crearla, ya que no solo nos hará falta el código, sino también cómo ejecutarlo. Para este fin, utilizaremos únicamente Copilot, ya que es la que, en principio, funciona mejor para programar. No es necesario que repliquen esta tarea concretamente, ya que en Windows y Mac es complicado crear el entorno para que funcione. Tienen que descargar los modelos y compilarlos. GNU/Linux es mucho más sencillo.

:::important
Es necesario decir que no obtendremos un resultado que se ajuste al 100% de lo que esperamos. Siempre debemos realizar una comprobación del código y modificar los aspectos que queremos adaptar. Si no sabemos programar, debemos conformarnos con lo que nos dé o, es un buen punto para aprender a programar, ya que la mejor manera de aprender es a base de ejemplos que nos irá proporcionando la IA.
:::

:::tip
Existe una opción de pago (gratuita para docentes) llamada GitHub Copilot, que nos permite modificar código específico sobre el editor de texto Visual Studio Code. En muchas de las formaciones que se están ofreciendo, se explica esta opción. Pero está pensada más para programadores.
:::

## Realización

Para crear un programa con python, tenemos que pegar el código en un archivo de texto (.txt, no sirve ni .doc ni .odt) y guardarlo con extensión .py.

Plantearemos un prompt como este:

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Eres un programador experimentado que le gusta documentar su código y trabaja con linux. Nuestra vida depende de realizar un programa con python que abrirá una ventana que nos mostrará lo que hay en la cámara web de nuestro ordenador. Este programa detectará cuando nuestra cara sonríe y cuando está triste, y mostrará un mensaje en la pantalla que se refrescará cada segundo mostrando el texto "triste" o "alegre"}}

Copiamos y pegamos lo que nos dice exactamente, ya que se trata de una respuesta bastante larga:

Hola! Como quieres hacer un programa que detecte emociones a través de la cámara web de tu ordenador, te recomiendo que utilices la librería **OpenCV** para Python. Esta librería es una herramienta de código abierto que se puede utilizar para la visión por computadora y el procesamiento de imágenes. Para la detección de emociones, puedes utilizar el reconocimiento facial en tiempo real con **OpenCV**. Esto implica la detección de caras y la identificación de las emociones a través de las expresiones faciales.

Para la detección de emociones, te recomiendo que utilices el modelo **FER+** (Face Expression Recognition Plus), que es un modelo de red neuronal que se puede entrenar para la detección de emociones a través de las expresiones faciales. Este modelo se puede utilizar con **OpenCV** para la detección de emociones en tiempo real.

A continuación, te proporciono un ejemplo de código que utiliza **OpenCV** y **FER+** para la detección de emociones a través de la cámara web de tu ordenador:


```python
import cv2
import numpy as np
from fer import FER

cap = cv2.VideoCapture(0)
detector = FER(mtcnn=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect faces in the frame
    faces = detector.detect_emotions(frame)

    # Draw bounding boxes and labels of detected faces
    for face in faces:
        x, y, w, h = face["box"]
        emotions = face["emotions"]
        emotion = max(emotions, key=emotions.get)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Emotion Detection", frame)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture and destroy the window
cap.release()
cv2.destroyAllWindows()
```

Este código abre la cámara web de tu ordenador y detecta las caras en tiempo real. A continuación, utiliza el modelo **FER+** para la detección de emociones a través de las expresiones faciales. El código dibuja cuadros delimitadores y etiquetas de las caras detectadas y muestra el texto "alegre" o "triste" en la pantalla, dependiendo de la emoción detectada.

¡Espero que esto te ayude a empezar a desarrollar tu programa! Si tienes alguna otra pregunta, no dudes en preguntarme.

Nosotros solo queremos el código, así que lo copiamos y pegamos en un archivo de texto llamado camera.py y ejecutamos en la terminal:

```
python camera.py
```

Pero nos da un error y no funciona. Así que recurrimos a Bing Copilot para ver qué nos dice:

![Respuesta de Copilot](img/0.png){ width=70% }

Así, ejecutamos lo que nos dice la IA y volvemos a ejecutar:

```python
python camera.py
```
Y este es el resultado:

![Aplicación](img/1.png){ width=70% }

![Aplicación](img/2.png){ width=70% }

![Aplicación](img/3.png){ width=70% }

![Aplicación](img/4.png){ width=70% }

:::note
En nuestro caso, hemos utilizado un Sistema Operativo basado en linux como LliureX, pero cada sistema operativo tendrá su complejidad. LliureX destaca porque simplifica mucho las tareas de configuración.
:::

:::caution
Este es un ejemplo de lo que se puede hacer, pero no se os pide en ningún momento que realicéis este ejemplo. Podéis probar y despertar vuestra curiosidad para trabajar con código. Pero no es necesario que lo hagáis.
Programar puede acabar resultando una tarea verdaderamente estresante.
:::

# Creación de un juego con Python

Crear un juego no es una tarea sencilla y vamos a utilizar una biblioteca de python llamada *Pygame* que es muy sencilla de utilizar. Personalmente no la he utilizado nunca. Pero podremos ver que no solo hay que realizar un comando para realizar el juego, sino que habrá que ir dándole instrucciones para que vaya cambiando las cosas que no entiende de lo que nosotros queremos.

:::caution
La creación de un videojuego lleva muchas veces años, y juegos sencillos quizá no años, pero meses dedicados en exclusiva. Así que no esperemos sacar una maravilla de juego en un día, aun así, los resultados son bastante sorprendentes.
:::

Puede parecer una tarea sencilla tal y como voy a plantearles, pero el prompt que he creado para que la IA me cree el videojuego lo he tenido que modificar un poco (y después he modificado un poco el código) para que me funcione correctamente. Además, como hemos comentado, siempre es importante conocer un poco (aunque sea muy poco) de qué estamos tratando con la IA para poder perfilar mejor el prompt.

La plataforma que hemos utilizado es Copilot y el prompt planteado ha sido el siguiente:

\awesomebox[violet]{2pt}{\faRobot}{violet}{Crea un juego con la biblioteca Pygame para python que tenga una pantalla estática con una plataforma del 20 por ciento del total de la ventana que pueda desplazarse a la izquierda o la derecha con el teclado de manera suave y rápida. La velocidad de la bola será constante de 1 y se actualizará la función que mueve la bola cada 0.3 segundos y cuando la bola choque con los extremos de la pantalla rebotará con un ángulo de 45 grados en la dirección que lleva, si la bola choca contra la plataforma rebotará, si rebota en la mitad derecha de la plataforma se irá hacia la derecha con un ángulo de 45 grados hacia arriba y si rebota en la mitad izquierda de la plataforma se irá hacia la izquierda con un ángulo de 45 grados hacia arriba. Al principio habrá una bola encima de la tabla sin moverse y cuando se pulse la tecla espacio, la bola comenzará a moverse hacia arriba. Escribe solo el código, sin comentarios y de la manera más resumida posible.\newline No quiero que me escribas ninguna explicación, solo quiero el código y sin comentarios.}

La respuesta tal cual ha sido:

![Respuesta de Copilot](img/8.png){ width=70% }

Les transcribimos el código aquí


```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ball = pygame.Rect(400, 570, 10, 10)
paddle = pygame.Rect(350, 580, 100, 10)
ball_speed = [3, -3]
paddle_speed = 10
moving = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                moving = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < 800:
        paddle.move_ip(paddle_speed, 0)

    if moving:
        ball.move_ip(ball_speed[0], ball_speed[1])

        if ball.left <= 0 or ball.right >= 800:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball.colliderect(paddle):
            if ball.centerx < paddle.centerx:
                ball_speed = [-3, -3]
            else:
                ball_speed = [3, -3]

        if ball.bottom >= 600:
            ball.topleft = (400, 570)
            moving = False

    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.display.flip()
    clock.tick(60)
```

Este es el código generado y el resultado ha sido el siguiente:

![Juego planteado](img/7.png){ width=70% }

:::important
Debéis eliminar el texto que añade la IA al final del código, ya que no son parte del código y pueden generar errores. En este caso, la última línea donde pone CITATION.
:::

:::tip
El problema que hemos detectado es que la bola iba muy lentamente, así que le pedimos que la velocidad fuera mayor. Le preguntamos a Copilot y nos arregló el código.
:::

## Explicación del prompt

Vamos a hacer una pequeña explicación del prompt. Como pueden ver, los prompts no suelen ser "Hazme un juego tipo *Arkanoid*", es necesario detallar claramente lo que queremos. Esta explicación del prompt sirve para cualquier otro tipo de materia.

:::nota
Es posible que ahora ya haya una respuesta para el prompt de crear un juego tipo Arkanoid, ya que está relacionado con el prompt que pregunté después y ya lo haya asociado. A vosotros podría funcionaros. La IA también va aprendiendo de lo que nosotros le "enseñamos".
:::

El prompt que planteamos es:

>Crea un juego con la biblioteca Pygame para python que tenga una pantalla estática con una plataforma del 20% del total de la ventana que pueda desplazarse a la izquierda o la derecha con el teclado de manera suave y rápida. La velocidad de la bola será constante de 1 y se actualizará la función que mueve la bola cada 0.3 segundos y cuando la bola choque con los extremos de la pantalla rebotará con un ángulo de 45º en la dirección que lleva, si la bola choca contra la plataforma rebotará, si rebota en la mitad derecha de la plataforma se irá hacia la derecha con un ángulo de 45º hacia arriba y si rebota en la mitad izquierda de la plataforma se irá hacia la izquierda con un ángulo de 45º hacia arriba. Al principio habrá una bola encima de la tabla sin moverse y cuando se pulse la tecla espacio, la bola comenzará a moverse hacia arriba. Escribe solo el código, sin comentarios y de la manera más resumida posible. No quiero que me escribas ninguna explicación, solo quiero el código y sin comentarios.

> Crea un juego con la biblioteca Pygame para python

Debemos detallar la tecnología que queremos utilizar, aquí estamos planteando un contexto en nuestro prompt.

> que tenga una pantalla estática con una plataforma del 20% del total de la ventana

En este caso continuamos detallando el contexto, podríamos haber pedido una pantalla más pequeña, pero supuso una pantalla de 800x600, indicamos que la ventana tenga un tamaño determinado y queremos una plataforma donde rebotarán las bolas. Vean que le doy ya un valor, como no le he dado un valor a la pantalla le hablo en porcentajes.

> que pueda desplazarse a la izquierda o la derecha con el teclado de manera suave y rápida

Le dejamos claro que queremos manejar la plataforma con el teclado y no con el ratón, especificamos suave y rápida para que entienda que si mantenemos pulsada la tecla queremos que continúe, en este caso me funcionó pero con otros modelos GPT no entiende *suave y rápida*.

> La velocidad de la bola será constante de 1 y se actualizará la función que mueve la bola cada 0.3 segundos

Esta parte puede costar entender un poco más, el FPS es la velocidad con la que quiero que se refresque la pantalla y le dije en segundos que la IA interpretó como 60 fps, y la velocidad 1 porque pygame solo permite valores mayores de 1.

> y cuando la bola choque con los extremos de la pantalla rebotará con un ángulo de 45º en la dirección que lleva

Es importante delimitar cómo rebota, aquí es cuando damos ejemplos a la IA para que entienda que debe rebotar en una dirección diferente, si no podría quedarse rebotando de un lado a otro sin cambiar. Hay que pensar en la dinámica del juego.

> si la bola choca contra la plataforma rebotará, si rebota en la mitad derecha de la plataforma se irá hacia la derecha con un ángulo de 45º hacia arriba y si rebota en la mitad izquierda de la plataforma se irá hacia la izquierda con un ángulo de 45º hacia arriba

Continuamos con los ejemplos que ayudan a entender lo que deseamos.

> Al principio habrá una bola encima de la tabla sin moverse y cuando se pulse la tecla espacio, la bola comenzará a moverse hacia arriba

Es importante definir una situación inicial ya que, como ya hemos comentado, la IA no presupone como un humano. Si no especificamos algo, se lo inventará y podría ser que no fuera lo que deseamos. Las presunciones que hace no son humanas.

> Escribe solo el código, sin comentarios y de la manera más resumida posible. No quiero que me escribas ninguna explicación, solo quiero el código y sin comentarios.

Por último, insistimos en que solo queremos el código sin ningún tipo de explicación y sin ningún tipo de comentario en el código. Los comentarios pueden ayudarnos a entender mejor el código, pero la plataforma tiene limitado el número de caracteres que nos da como respuesta. De esta manera, ahorramos cantidad de caracteres que queremos que nos dé.



:::important
Insistimos en que la plataforma tiene limitado el número de caracteres que nos da como respuesta, por eso insistimos en que no nos dé comentarios adicionales, para que se centre únicamente en el código, que es lo que queremos.
:::

:::warning
Al crear este prompt, en una de las pruebas, la IA me contestó:

![La IA haciendo amigos](img/10.png){ width=70% }

Así que no siempre obtendremos los resultados esperados y será necesario ir modificando variables hasta que nos dé el resultado esperado.
:::

No piensen que este prompt surgió mágicamente de mi cabeza, es necesario ir analizando las respuestas que va dando para ir creando el prompt. Son varios intentos modificando el orden de las frases del prompt y preguntando por separado para analizar las respuestas y poder perfilar mejor el resultado.


# Replit

[Replit](https://replit.com) es una plataforma que nos permite crear código de manera sencilla y rápida. Podemos crear código en diferentes lenguajes de programación y nos permite compartirlo con otras personas. Además, nos permite ejecutar el código en línea y ver el resultado en tiempo real. De manera que no vamos a pedirles que ejecuten el código en su ordenador, en cambio podemos hacerlo en esta plataforma. El principal problema es que solo nos deja crear 3 proyectos en la versión gratuita. Pero nos da bastantes herramientas para poder probarlo y utilizarlo para ir aprendiendo sin necesidad de configurar nada en nuestro ordenador.

![Replit](img/21.png){ width=70% }

Replit es una plataforma muy potente y muy utilizada. En este caso, cuando nos logueamos y le decimos a todo que sí, aparecerá una pantalla como esta:

![Replit](img/22.png){ width=70% }

Si ya tienen algún proyecto comenzado, pueden hacer lo siguiente:

![Replit](img/23.png){ width=70% }

Y hacemos clic en create Repl:

![Create Repl](img/59.png){ width=70% }

Luego se nos abrirá este agente que no podemos utilizar para crear nuestro prompt, ya que tenemos que suscribirnos a la versión de pago. Vamos a Choose template:

![Choose template](img/60.png){ width=70% }

Y elegimos Python y le damos un nombre:

![Elegimos Python](img/61.png){ width=70% }

![Nombre](img/62.png){ width=70% }

Y ahora ya podemos escribir directamente en el asistente de código. Podemos escribir el prompt que hemos creado para el juego:

![Prompt](img/63.png){ width=70% }

En la parte superior podemos ver que nos aparece la tecla insert para poder insertar el código en maon.py:

![Insert](img/64.png){ width=70% }

Una vez insertado, hacemos clic en Run. Y ya tenemos nuestro juego funcionando:

![Juego](img/65.png){ width=70% }

:::warning
El código generado por Copilot ha funcionado mucho mejor. En Replit hemos cambiado los siguientes valores para que funcionara mucho más rápidamente. Pero podemos copiar el código de Copilot y pegarlo aquí para que funcione correctamente.
ball_speed = 20
platform_speed = 20
time.sleep(0.1)
:::

Replit es una plataforma muy potente y puede servirnos para introducir a los alumnos a la programación comenzando con cosas mucho más sencillas como:

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Crea un programa que abra una ventana y me pregunte mi nombre, luego cierre esa ventana y abra otra ventana que diga Hola + mi nombre y espere hasta que yo cierre esa ventana.}}

![Programa](img/29.png){ width=70% }

Pueden ver el resultado [aquí](https://replit.com/join/ovvzfszftt-alviboigva)

:::tip
No es necesario saber programar para utilizar la plataforma, sino saber escribir prompts correctamente. Podemos pensar que esta plataforma sirve solo para programadores, pero no es así. Ya que fíjense en la estructura del prompt, es necesario saber explicar bien lo que queremos. Y eso ayuda a desarrollar el pensamiento computacional.
:::

\awesomebox[black]{2pt}{\faCode}{black}{Como docentes, podemos hacer uso de GitHub Copilot, que deberán solicitar en la plataforma de GitHub y que les permitirá modificar código en tiempo real y se integra muy bien dentro del editor Visual Studio Code.}



# PartyRock

[PartyRock](https://partyrock.aws/) es una plataforma creada por AWS que nos permite combinar diferentes modelos y aprovechar preguntas y respuestas creadas por diferentes IA para crear un prototipo de una aplicación. Se trata de una aplicación muy potente a la cual le dedicamos un curso de 10 horas para poder practicar con ella.

![PartyRock](img/79.png){ width=70% }

Cuando entramos podemos ir a "generate APP":

![Generate APP](img/80.png){ width=70% }

Y podemos escribir un prompt para que nos cree un prototipo de una aplicación.

![Prompt](img/81.png){ width=70% }

Pero para poder crear un prompt es importante que sepamos cómo funciona, por eso iré a "Build manually".

![Build manually](img/82.png){ width=70% }

La aplicación tiene un lienzo donde podemos añadir widgets. Si hacemos clic en el botón "Add widget" podemos ver que nos aparecen diferentes widgets que podemos añadir a nuestra aplicación. Hay 3 widgets potenciados con IA y 3 para hacer una entrada. Los widgets que nos podemos encontrar son:

![Widgets](img/83.png){ width=70% }

| Widget | Descripción |
|--------|-------------|
| User Input | Entrada de texto |
| Static Text | Explicación o un texto en concreto. También podemos utilizarlo como una entrada estática |
| Document | Para subir un documento |
| Text generation | Alimentado con IA. Crea una entrada del prompt |
| Image generation | Alimentado con IA. Crea una imagen |
| Chatbot | Un chat para formular cuestiones |

En cada uno de los widgets hay que poner un prompt para que la IA nos dé una respuesta. Si queremos referenciar a otros widgets, tenemos que poner una @ y el nombre del widget. Aquí os pondríamos un ejemplo extremadamente sencillo de cómo hacerlo:

![Ejemplo](img/84.png){ width=70% }

Y este sería el resultado:

![Resultado](img/85.png){ width=70% }

Obviamente, este ejemplo es muy sencillo, pero podemos hacer cosas mucho más complejas.

:::note
En Aules os hemos dejado un tutorial de ejemplo de una aplicación.
:::



# Creamos una unidad en Aules

En este apartado vamos a crear una unidad desde cero, ya os hemos comentado que siempre es importante tener unas nociones básicas sobre lo que se está preguntando. Vamos a hacer nuestra prueba en nuestro [Aules docente](https://aules.edu.gva.es/docent/my/).

:::tip
Tenéis opciones gratuitas de moodle como [milaulas](https://www.milaulas.com/)
para poder hacer pruebas si no queréis utilizar el Aules docente.
:::


## Diseño estético

Existen páginas como [Colorhunt](https://colorhunt.co/) para poder utilizar colores que combinen entre sí. Nosotros hemos tomado [esta paleta de colores](https://colorhunt.co/palette/4c4b16898121e6c767f87a53) para poder hacer nuestra unidad.

El diseño que vamos a utilizar es más o menos el que hemos utilizado en este mismo curso, aunque cambiaremos algunas cosas ya que hemos usado herramientas como [pandoc](https://pandoc.org/) para poder crear este documento.

En primer lugar, creamos nuestro curso:

![Curso](img/30.png){ width=70% }

![Nombre del curso](img/31.png){ width=70% }

:::caution
El curso tarda un poco en crearse, así que no se preocupen.
:::

![Entramos en modo edición](img/32.png){ width=70% }

Y añadimos una sección.

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Crea una división en html con un título que diga La célula y la fuente sea de color blanco, que tenga un fondo con los bordes redondeados que ocupe el 100 \% de su sección y el fondo sea de varias franjas alternas inclinadas 45 grados con los colores 4C4B16 y un color un poco más oscuro. Es importante que el estilo esté todo contenido dentro de la misma división. Quiero que muestres solo el contenido del body.}}

El resultado ha sido el siguiente:

```html
<body>
    <div style="background: repeating-linear-gradient(45deg, #4C4B16, #4C4B16 10px, #6C6B29 10px, #6C6B29 20px); border-radius: 15px; width: 100%; padding: 20px; text-align: center; color: white;">
        <h1 style="color: white;">La célula</h1>
    </div>
</body>
```

En Añadir una actividad o recurso buscamos "Área de texto y multimedia" y copiamos el código sin la parte del body y aparecerá así:

![Código](img/33.png){ width=90% }

:::caution
Debemos copiarlo haciendo clic en el botón de código (en rojo en la imagen).
:::

El resultado se vería de esta manera:

![Resultado](img/34.png){ width=90% }

Podemos crear títulos más pequeños modificando un poco el prompt:

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Crea una división en html con un título pequeño que diga "Contenidos" y esté alineado a la izquierda. La fuente del título sea de color blanco y tenga un fondo con los bordes redondeados que ocupe el 100\% de su sección y el fondo sea de varias franjas alternas inclinadas 45 grados con los colores \#898121 y un color un poco más oscuro. La altura de todo el contenido no debe ser muy grande. Es importante que el estilo esté todo contenido dentro de la misma división. Quiero que muestres solo el contenido del body.}}

El resultado ha sido el siguiente:

```html
<div style="font-family: 'Verdana', sans-serif; color: #fff; text-align: left; font-size: 1.2em; padding: 20px; width: 100%; height: auto; background: repeating-linear-gradient(45deg, #898121, #898121 10px, #6d6b16 10px, #6d6b16 20px); border-radius: 15px; margin: auto;">
    <h2 style="color: #fff; margin: 0;">Contenidos</h2>
</div>
```

Creo que recordarán que creamos un curso sobre la célula en el módulo 3, así que vamos a aprovecharlo. Añadimos una actividad o recurso URL que quedaría de la siguiente manera:

![URL](img/35.png){ width=70% }

Lo movemos a la derecha para darle un buen formato:

![A la derecha](img/36.png){ width=40% }

Y así se abrirá como en una ventana emergente el contenido:

![Contenido](img/37.png){ width=90% }

## Actividades

Vamos a crear una actividad de tipo cuestionario. Pero vamos a hacer uso de las herramientas que hemos aprendido a utilizar.

Iremos a [magischool](https://app.magicschool.ai/tools) y crearemos un cuestionario. En este caso, haremos un cuestionario de 5 preguntas sobre la célula.

![Magischool](img/38.png){ width=70% }

Creamos el cuestionario:

![Cuestionario](img/39.png){ width=70% }

Y el resultado que tenemos es el siguiente:

![Cuestionario](img/40.png){ width=70% }

:::caution
En este caso no podemos subir la web que hemos creado con mindsmith debido a las características de la plataforma, pero podemos subir nuestras propias notas.
:::

Pero a nosotros nos interesa que estas preguntas estén en Aules... Así que copiaremos el resultado y utilizaremos Copilot:

\awesomebox[violet]{2pt}{\faRobot}{violet}{Crea un código xml para poder importar como cuestionario de moodle utilizando las siguientes preguntas:\newline 
La célula y sus partes\newline
1. ¿Cuál es la función principal del núcleo celular?\newline
a. Controlar las actividades celulares  \newline
b. Proporcionar energía a la célula  \newline
c. Sintetizar proteínas  \newline
d. Almacenar lípidos  \newline
2. ¿Qué estructura celular está involucrada principalmente en la producción de energía?  \newline
a. Núcleo  \newline
b. Mitocondria  \newline
c. Ribosoma  \newline
d. Retículo endoplasmático  \newline
3. ¿Qué parte de la célula contiene enzimas que ayudan a la digestión de material celular?  \newline
a. Aparato de Golgi  \newline
b. Lisosoma  \newline
c. Cloroplasto  \newline
d. Centriolo  \newline
4. ¿Cuál es el papel principal de la membrana plasmática?  \newline
a. Sintetizar lípidos  \newline
b. Mantener el equilibrio osmótico  \newline
c. Controlar lo que entra y sale de la célula  \newline
d. Producir glucosa  \newline
5. ¿Qué orgánulo es responsable de la síntesis de proteínas?  \newline
a. Núcleo  \newline
b. Ribosoma  \newline
c. Lisosoma  \newline
d. Vacuola  \newline
Answer Key (Always review AI generated answers for accuracy - Math is more likely to be inaccurate)

a  
b  
b  
c  
b  }

Y el resultado ha sido el siguiente:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="multichoice">
    <name>
      <text>¿Cuál es la función principal del núcleo celular?</text>
    </name>
    <questiontext format="html">
      <text><![CDATA[<p>¿Cuál es la función principal del núcleo celular?</p>]]></text>
    </questiontext>
    <answer fraction="100">
      <text>Controlar las actividades celulares</text>
    </answer>
    <answer fraction="0">
      <text>Proporcionar energía a la célula</text>
    </answer>
    <answer fraction="0">
      <text>Sintetizar proteínas</text>
    </answer>
    <answer fraction="0">
      <text>Almacenar lípidos</text>
    </answer>
  </question>
  
  <question type="multichoice">
    <name>
      <text>¿Qué estructura celular está involucrada principalmente en la producción de energía?</text>
    </name>
    <questiontext format="html">
      <text><![CDATA[<p>¿Qué estructura celular está involucrada principalmente en la producción de energía?</p>]]></text>
    </questiontext>
    <answer fraction="0">
      <text>Núcleo</text>
    </answer>
    <answer fraction="100">
      <text>Mitocondria</text>
    </answer>
    <answer fraction="0">
      <text>Ribosoma</text>
    </answer>
    <answer fraction="0">
      <text>Retículo endoplasmático</text>
    </answer>
  </question>
  etc...
```

Este texto lo copiamos en un archivo (creado con el bloc de notas de Windows) y lo guardamos como **questions.xml**.

En nuestro Aules añadiremos un Cuestionario en "Añadir una actividad o recurso":

![Cuestionario de Aules](img/41.png){ width=90% }

No hay que modificar nada más, simplemente hacemos clic en "Guardar cambios y volver al curso" y ya tendremos nuestro cuestionario creado.

Entramos en nuestro cuestionario y vamos a Banco de preguntas:

![Banco de preguntas](img/42.png){ width=90% }

Una vez aquí, hacemos clic en "Importar":

![Importar](img/43.png){ width=90% }

Debemos seleccionar las siguientes opciones:

* Formato XML de Moodle
* Arrastrar y soltar el archivo o navegar para subirlo

![Opciones](img/44.png){ width=90% }

Ahora podremos ver las preguntas que hemos creado:

![Preguntas](img/45.png){ width=90% }

:::tip
A partir de ahora, os recomiendo estos pasos para tener las preguntas un poco más organizadas en su curso.
:::

Seleccionamos todas las preguntas y desplegamos el menú de abajo y hacemos clic en "Mover a...":

![Mover a](img/46.png){ width=90% }

Si está en Cuestionario 1, elegimos por defecto en Cuestionario 1 y hacemos clic en "Mover a":

![Mover a](img/47.png){ width=90% }

Una vez hemos hecho esto, tenemos nuestras preguntas en nuestro banco de preguntas, pero esto no significa que estén en el cuestionario. Para ponerlas en el cuestionario, debemos hacer lo siguiente:

1. Vamos a nuestro cuestionario y hacemos clic en "Añadir una pregunta":

![Cuestionario](img/48.png){ width=90% }

2. Luego vamos al menú Añadir y seleccionamos del Banco de preguntas:
  
![Añadir pregunta](img/49.png){ width=90% }

Finalmente, seleccionamos la opción "Por defecto en Cuestionario 1" y hacemos clic en Aplicar Filtros:

![Filtros](img/50.png){ width=90% }

Cuando aplicamos filtros, seleccionamos todas las preguntas y hacemos clic en "Añadir las preguntas seleccionadas al cuestionario":

![Añadir preguntas](img/51.png){ width=90% }

Y ya tendremos nuestras preguntas añadidas al cuestionario:

![Preguntas](img/52.png){ width=90% }

:::tip
Hemos hecho este proceso muy detalladamente porque mucha gente se confunde con los cuestionarios de Moodle. Para muchos de ustedes será una tarea sencilla. También es cierto que estamos hablando de 5 preguntas, pero si queremos hacer un cuestionario de 20 preguntas, puede ahorrarnos mucho trabajo.
:::

También podemos añadir:

\awesomebox[violet]{2pt}{\faRobot}{violet}{Crea un feedback del siguiente cuestionario de moodle:
(Aquí añadimos el código de las preguntas)}

Y la respuesta será esta con un feedback de cada pregunta:

Fíjense cómo nos ha añadido este campo:

```xml
      <feedback>
      <text>Correcto! El núcleo celular es el centro de control de la célula. </text>
      </feedback>
```

Aquí tendríamos la respuesta, pero tiene un problema:



```xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="multichoice">
    <name>
      <text>¿Cuál es la función principal del núcleo celular?</text>
    </name>
    <questiontext format="html">
      <text><![CDATA[<p>¿Cuál es la función principal del núcleo celular?</p>]]></text>
    </questiontext>
    <answer fraction="100">
      <text>Controlar las actividades celulares</text>
      <feedback>
        <text>¡Correcto! El núcleo celular es el centro de control de la célula.</text>
      </feedback>
    </answer>
    <answer fraction="0">
      <text>Proporcionar energía a la célula</text>
      <feedback>
        <text>No es correcto. La principal función del núcleo celular es controlar las actividades celulares.</text>
      </feedback>
    </answer>
    <answer fraction="0">
      <text>Sintetizar proteínas</text>
      <feedback>
        <text>Incorrecto. El núcleo controla las actividades celulares, no sintetiza proteínas directamente.</text>
      </feedback>
    </answer>
    <answer fraction="0">
      <text>Almacenar lípidos</text>
      <feedback>
        <text>No, el núcleo celular no almacena lípidos, controla las actividades celulares.</text>
      </feedback>
    </answer>
  </question>
  
  <question type="multichoice">
    <name>
      <text>¿Qué estructura celular está involucrada principalmente en la producción de energía?</text>
    </name>
    <questiontext format="html">
      <text><![CDATA[<p>¿Qué estructura celular está involucrada principalmente en la producción de energía?</p>]]></text>
    </questiontext>
    <answer fraction="0">
      <text>Núcleo</text>
      <feedback>
        <text>No es correcto. El núcleo no está involucrado principalmente en la producción de energía.</text>
      </feedback>
    </answer>
    <answer fraction="100">
      <text>Mitocondria</text>
      <feedback>
        <text>¡Correcto! La mitocondria es la fuente principal de producción de energía en la célula.</text>
      </feedback>
    </answer>
    <answer fraction="0">
      <text>Ribosoma</text>
      <feedback>
        <text>Incorrecto. Los ribosomas son responsables de la síntesis de proteínas, no de la producción de energía.</text>
      </feedback>
    </answer>
    <answer fraction="0">
      <text>Retículo endoplasmático</text>
      <feedback>
        <text>No, el retículo endoplasmático no es principalmente responsable de la producción de energía.</text>
      </feedback>
    </answer>
  </question>
  
  <question type="multichoice">
    <name>
      <text>¿Qué parte de la célula contiene enzimas que ayudan a la digestión de material celular?</text>
    </name>
    <questiontext format="html">
      <text><![CDATA[<p>¿Qué parte de la célula contiene enzimas que ayudan a la digestión de material celular?</p>]]></text>
    </questiontext>
    <answer fraction="0">
      <text>Aparato de Golgi</text>
      <feedback>
        <text>No es correcto. El Aparato de Golgi no contiene enzimas de digestión de material celular.</text>
      </feedback>
    </answer>
    <answer fraction="100">
      <text>Lisosoma</text>
      <feedback>
        <text>¡Correcto! Los lisosomas contienen enzimas que ayudan a la digestión de material celular.</text>
      </feedback>
    </answer>
    <answer fraction="0">
      <text>Cloroplasto</text>
      <feedback>
        <text>Incorrecto. Los cloroplastos no contienen enzimas de digestión de material celular.</text>
      </feedback>
    </answer>
    <answer fraction="0">
      <text>Centriolo</text>
      <feedback>
        <text>No, los centriolos no están involucrados en la digestión de material celular.</text>
      </feedback>
    </answer>
  </question>
  
  <question type="multichoice">
    <name>
      <text>¿Cuál es el papel principal de la membrana plasmática?</text>
    </name>
    <questiontext format="html">
      <text><![CDATA[<p>¿Cuál es el papel principal de la membrana plasmática?</p>]]></text>
    </questiontext>
    <answer fraction="0">
      <text>Sintetizar lípidos</text>
      <feedback>
        <text>Incorrecto. La membrana plasmática no es responsable de sintetizar lípidos.</text>
      </feedback>
    </answer>
    <answer fraction="0">
      <text>Mantener el equilibrio osmótico</text>
      <feedback>
        <text>No es correcto. La principal función de la membrana plasmática no es mantener el equilibrio osmótico.</text>
      </feedback>
    </answer>
    <answer fraction="100">
      <text>Controlar lo que entra y sale de la célula</text>
      <feedback>
        <text>¡Correcto! La función principal de la membrana plasmática es controlar lo que entra y sale de la célula.</text>
      </feedback>
    </answer>
    ...
```

En este caso, Copilot tiene un límite de tamaño de respuesta. Si quisiéramos hacer feedback de todas las preguntas, deberíamos hacerlo de dos en dos o de tres en tres, dependiendo de la longitud de las preguntas.

:::warning
En ningún momento he revisado que las respuestas sean correctas, perfectamente podrían ser incorrectas. Así que es importante revisarlas.
:::

Finalmente, para darle un último toque a nuestro curso, crearíamos un video.

## Vídeo

Para crear un vídeo podríamos utilizar la herramienta https://simpleshow.com/ que nos permite crear vídeos de manera sencilla y rápida. En este caso haremos un vídeo sobre la célula.

![Simpleshow](img/53.png){ width=90% }

Debemos dar un título a la historia y crear nuestro guion del vídeo:

![Guion](img/56.png){ width=90% }

:::tip
Para hacer el guion hemos utilizado Copilot, ya que el resultado era mucho mejor.
:::

Finalmente, puedes editar el vídeo y cambiar las imágenes que utiliza, lo cual es muy recomendable en este caso, ya que su banco de imágenes no es muy grande. Pero podemos comprobar el resultado aquí:

[https://videos.simpleshow.com/jeqomMgovT](https://videos.simpleshow.com/jeqomMgovT)

Podríamos añadir el vídeo a nuestro curso y ya tendríamos la unidad completada.

![Vídeo](img/58.png){ width=90% }

# Ayudando a los compañeros

En esta unidad hemos creado aplicaciones muy sencillas, pero podemos crear aplicaciones mucho más complejas y que pueden llevar mucho más tiempo en ser creadas. Como ejemplo, hemos creado una aplicación muy sencilla y otra más compleja que pueden facilitaros las tareas de Aules. No vamos a detallar el proceso ya que es muy largo y complejo. Y se requieren conocimientos de programación. Vamos a crear un taller para explicar cómo hemos creado esta aplicación. Estas aplicaciones os las subiremos a Aules.

## Diseñador de títulos

Se trata de una página donde podéis crear títulos para vuestras unidades. Esta aplicación permite crear títulos de manera sencilla y rápida. Podéis elegir entre diferentes tipos de letra, colores y efectos para personalizar vuestro título.

![Diseñador de títulos](img/66.png){ width=90% }

# Contestar foro de Aules con IA

Se trata de un botón que pondremos en Aules que una vez hagamos clic contestará todas las preguntas de un foro que no tengan respuesta.

Para realizar esta aplicación necesitaréis una API Key de Google AI Studio[^1]. Google AI Studio nos permite acceder a un modelo de manera gratuita e integrarlo en nuestras aplicaciones. Para conseguir

[^1]: Una API Key es un código que nos permite acceder a un servicio web de manera segura. En este caso, necesitamos una API Key de Google AI Studio para poder utilizar el modelo de lenguaje natural de Google.

![Google AI Studio](img/67.png){ width=90% }

Nos registramos con un correo de gmail. Aceptamos los términos:

![Aceptamos](img/68.png){ width=90% }

Hacemos clic en create API Key:

![Create API Key](img/69.png){ width=90% }

Y nos dará una cadena de caracteres que será nuestra API Key. Esta cadena la guardamos en lugar seguro:

![API Key](img/70.png){ width=90% }

## Crear página para contestar foros

Hemos creado una página que os generará la aplicación. Si hacéis clic en la página que hemos creado veréis lo siguiente:

![Página](img/71.png){ width=90% }

Donde pone API Key pondremos nuestra API Key que hemos creado antes. Donde pone prompt es el prompt que crearemos para contestar las preguntas del foro. Y donde pone Id del foro e Id del curso es el identificador del foro y el curso, que podemos encontrar en la URL del foro:

![Id del foro](img/72.png){ width=90% }

![Id del curso](img/73.png){ width=90% }

Debes tratar de generar un prompt genérico que conteste a las preguntas del foro. Por ejemplo:

> Responde a las preguntas de manera clara y concisa. Si la pregunta está relacionada con cuestionarios, funcionamiento del curso o calificaciones, remite a la guía didáctica del curso para obtener más información detallada. Por ejemplo: ¡Hola! Gracias por tu pregunta. Para más información sobre este tema, consulta la guía didáctica del curso. Si tienes alguna otra pregunta o alguna duda concreta, plantea un nuevo tema. La pregunta es:

Esta página la subiremos a Aules en un tema oculto pero con la página disponible:

![Subir a Aules](img/74.png){ width=90% }

Después cambiaremos la apariencia para que se abra en ventana emergente:

![Ventana emergente](img/75.png){ width=90% }

Y haremos clic sobre la página y veremos que no hace nada. Se queda colgada en esta posición:

![Colgada](img/76.png){ width=90% }

Pero copiamos la url. En nuestro caso sería algo así:

```
https://aules.edu.gva.es/docent/pluginfile.php/4450754/mod_resource/content/1/pagina_generada.html
```

Luego creamos un Área de texto y multimedia como esta. Que hará que nos aparezca un botón:

```html
<p dir="ltr" style="text-align: left;">
    <button onclick="window.open(`[TU URL PEGADA AQUÍ]?sesskey=${encodeURIComponent(M.cfg.sesskey)}&amp;cookie=${encodeURIComponent(document.cookie)}`, 'newwindow', 'width=800,height=600')">Responder foro</button>
</p>
```

En nuestro caso quedaría así:

```html
<p dir="ltr" style="text-align: left;">
    <button onclick="window.open(`https://aules.edu.gva.es/docent/pluginfile.php/4450754/mod_resource/content/1/pagina_generada.html?sesskey=${encodeURIComponent(M.cfg.sesskey)}&amp;cookie=${encodeURIComponent(document.cookie)}`, 'newwindow', 'width=800,height=600')">Responder foro</button>
</p>
```

Recuerda que debes tener este código en html, por lo tanto, debes pulsar el botón **</>**:

![Botón](img/77.png){ width=90% }

Finalmente, ya nos contestará las preguntas del foro.

![Respondiendo](img/78.png){ width=90% }

## Conclusión

La inteligencia artificial no nos proporciona todo el trabajo hecho, sino que actúa como una herramienta poderosa para facilitar y agilizar nuestras tareas. Nos permite automatizar procesos repetitivos, generar contenido de manera eficiente y ofrecer soluciones rápidas a problemas complejos. No obstante, es esencial que los usuarios mantengamos un papel activo en la supervisión y validación de los resultados generados por la IA. Así, podemos asegurarnos de que las soluciones propuestas se ajusten a nuestras necesidades específicas y mantengan un alto nivel de calidad. En resumen, la IA es una aliada que nos ayuda a ser más productivos y creativos, pero nuestra intervención y criterio siguen siendo fundamentales para obtener los mejores resultados.
