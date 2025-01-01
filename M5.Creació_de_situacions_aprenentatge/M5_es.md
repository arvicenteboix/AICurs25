---
# Información general del documento
title: 5. Creación de situaciones de aprendizaje
lang: can
page-background: img/bg.png
linkcolor: blue


# Portada
titlepage: true
titlepage-rule-height: 2
titlepage-rule-color: AA0000
titlepage-texto-color: AA0000
titlepage-background: U5.png

# Tabla de contenidos
toque: true
toque-own-page: true
toque-title: Contenidos

# Cabeceras y pies
header-left: 5. Creación de situaciones de aprendizaje
header-right: Curso 2023-2024
footer-left: CEFIRE Valencia
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

<!-- IMATGE ![Pregunta inicial](./img/proxi/5b.png) -->

<!-- \textbf{greatest} -->

<!-- \awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{greatest}} -->

\vspace{\fill}


![](img/cc.png){ height=50px }

Este documento está sujeto a una licencia creative commons que permite su difusión y uso comercial reconociendo siempre la autoría de su creador. Este documento se encuentra para ser modificado en el siguiente repositorio de github:
<!-- CANVIAR L'ENLLAÇ -->
[https://github.com/arvicenteboix/aicurscefire](https://github.com/arvicenteboix/aicurscefire)
\newpage

# SA con IA

En este bloque vamos a explicar cómo diseñar una Situación de aprendizaje (SA) utilizando Inteligencia Artificial (IA). La idea es la de ir rellenando la plantilla de SA que nos proporciona Conselleria con unos pocos prompts. Puede que la primera vez que lo hagas te cueste un poco, pero verás que, con la práctica, en unos minutos puedes crear una situación de aprendizaje en pocos pasos. Obviamente, el papel fundamental de la IA es ofrecerte inspiración para que tú selecciones y modifiques los resultados que te dé. No recomendamos volcar los resultados que nos ofrezca la IA tal cual, sino que, mediante el diálogo con ella, obtengamos resultados cada vez más precisos y coherentes.

Antes de empezar necesitamos tener a mano dos documentos:

-   La plantilla de situación de aprendizaje. Descárgala aquí: [Plantilla SA](https://portal.edu.gva.es/formaciodelprofessorat/es/2-situaciones-de-aprendizaje-en-marcha/).

-   El currículo oficial del que extraeremos las competencias específicas, los criterios de evaluación y saberes básicos. Lo puedes encontrar fácilmente en [noucurrículum.es](https://portal.edu.gva.es/noucurriculum/)

A continuación, explicaremos paso a paso el proceso de creación de una SA mediante IA:

##  Asignar un rol a la IA:

Es fundamental crear buenos prompts (instrucciones) para obtener los mejores resultados posibles. Pero igual de importante es pedirle a la IA que adopte un rol determinado desde el que nos pueda dar la mejor información posible. Por ello lo primero que haremos es pedirle que se convierta en una experta en el diseño de SA. Te ofrecemos un ejemplo de prompt para asignar el rol, en el que sólo tendrás que cambiar lo que esté subrayado para adaptarlo a tus necesidades:

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Actúa como una experta en el diseño de Situaciones de Aprendizaje (LOMLOE) para el primer curso de Educación Secundaria Obligatoria. Tienes un amplio conocimiento en Metodologías innovadoras, Aprendizaje Basado en Proyectos e inclusión, y estás familiarizada con una gran variedad de bibliografía al respecto que utilizas para brindar asesoramiento a otros profesores. Si tienes alguna pregunta o inquietud relacionada con el tema que te planteo, te animo a compartirla conmigo. Si hay algún tema del cual no tengas conocimiento, prefiero que evites improvisar; sé honesta y notifícame si no has comprendido algo. Me gustaría que utilices un lenguaje claro y formal, y que tus ideas sean creativas y apropiadas para la situación educativa que te solicitaré a continuación. ¿Me he explicado correctamente?}}

##  Seguir la plantilla de SA:



Para poder crear un buen prompt, que nos ofrezca una respuesta lo más personalizada posible, hay apartados de la plantilla que debemos rellenar nosotros mismos. Se trata de toda la primera fila de la tabla. También debemos rellenar la información de contexto: Dónde está ubicado el centro, nivel socioeconómico de las familias del alumnado, del entorno incluyendo las características del alumnado, necesidades específicas, problemática concreta, etc. Finalmente, debemos indicar en la plantilla, el mismo prompt qué competencias específicas, criterios de evaluación y saberes básicos queremos trabajar. Para esto debemos ayudarnos del currículo oficial, cortando y pegando. Aquí tienes un ejemplo en el que debes sustituir el texto subrayado por el tuyo personalizado.

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Crea la estructura de una Situación de Aprendizaje para la materia de Geografía e historia, de 1.º de ESO, que se desarrollará en el siguiente contexto: \_\_.}}

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Tiene que trabajar estas competencias básicas: \_\_.}}

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Tiene que trabajar estos criterios de evaluación: \_\_.}}

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Tiene que trabajar estos saberes básicos: \_\_.}}

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Indícame el título de la Situación de Aprendizaje, la descripción, la justificación y el producto final que deberá elaborar el alumnado en grupos para resolver el desafío planteado. Intenta que sea muy atractivo para el alumnado y que esté muy vinculado a la resolución de un problema real, cercano y útil.}}

A partir de aquí pega donde corresponda la respuesta de la IA. Si no te parece correcta o mejorable indícaselo: “Genera una respuesta nueva”, “Repítelo dando más importancia al contexto que te he indicado”.

##  Prompt secuencia didáctica:

A continuación podemos pedirle a la IA que genere las actividades y la temporalización de las mismas.

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Desarrolla las actividades que compondrán la Situación de Aprendizaje. Indica el número de sesiones de la situación de aprendizaje, el número de actividades por sesión y la descripción de la actividad. Ten en cuenta  que cada sesión es de 55 minutos. Finalmente indica la fecha de fin, sabiendo que quiero empezar \_\_ y que dedico \_\_ sesiones en la semana.}}

Si en la secuencia didáctica no aparecen desarrolladas las actividades, pídele que lo haga si así lo deseas:

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Desarrolla Sesión 1/Actividad 1 e indica en forma de cronograma como se desarrollaría.}}

##  Prompt de evaluación:

Llegados a este punto podemos intentar que la IA nos haga una propuesta en relación a la evaluación. Podemos pedirle que nos indique qué instrumentos de evaluación propone para registrar cada criterio.

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Crea una tabla con dos columnas: criterio de evaluación e instrumento de evaluación (observación directa, lista de cotejo, rúbrica, diana de evaluación,  exit ticket\...). Rellénala con los criterios de evaluación que te indiqué y el instrumento de evaluación que consideras más apropiado en cada caso.}}

Puedes pedirle incluso que desarrolle o creo esos instrumentos de evaluación:

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Desarrolla la lista de cotejo que has propuesto para evaluar el criterio \_\_\_ en la actividad \_\_\_.}}

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Desarrolla la rúbrica de la tarea \_\_\_ en forma de tabla de doble  entrada en la cual cada fila es un item en el cual se relaciona el criterio de evaluación con los saberes básicos y cada columna el grado de consecución de cada item.}}

Si en este apartado, los resultados que te ofrece la IA no te convencen te proponemos otra forma de utilizarla para facilitar el proceso de evaluación. Como en una situación de aprendizaje, de lo que se trata es de evaluar el progreso en el grado de adquisición de las competencias específicas, tomando como referente los criterios de evaluación, te ayudamos a mostrarlo en forma de rúbrica. 

Crea una tabla similar a esta, en la que sustituyas la competencia específica, y sus respectivos criterios de evaluación, por los que a ti te interese:

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{CE 1. Describir y contextualizar en el tiempo y el espacio los acontecimientos y los procesos más relevantes de la historia propia y universal, identificando referentes de la evolución hacia la sociedad actual y valorando la diversidad.}}

![Plantilla](./img/1.png)

Ahora pídele a la IA que muestre en progresión los diferentes grados de adquisición  de cada criterio:

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Desglosa el siguiente criterio: “Construir un relato cronológicamente ordenado y coherente sobre hechos y personajes relevantes del pasado y sobre su relación con el presente”, en cinco niveles de desempeño.}}

##  Prompt atención a la diversidad:

Finalmente, puedes pedirle a la IA que haga una propuesta sobre las medidas de respuesta para la inclusión. Aunque quizás en este apartado es donde el factor humano es más importante, por tanto, tras la respuesta de la IA, aplica el sentido común y tus conocimientos sobre el DUA-A, que puedes ampliar a través de estos recursos: [DUA-a](https://portal.edu.gva.es/cefireinclusiva/es/dua-a-2/)

\awesomebox[violet]{2pt}{\faRobot}{violet}{\textbf{Desarrolla las Medidas de respuesta para la inclusión (DUA), metodologías inclusivas, Organización de espacios de aprendizaje, Recursos y Materiales, teniendo en cuenta al alumnado que tiene las siguientes necesidades especiales.}}

Esperamos que esta guía te haya resultado útil, y que te haya servido de ayuda en el diseño de tus situaciones de aprendizaje. No olvides que la ayuda viene de las ideas inspiradoras que aporta, pero que conviene filtrar y seleccionar, en función de nuestros conocimientos e intereses. 