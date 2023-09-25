from django.shortcuts import render
from django.http import HttpResponse

def vista1(request):
    html = """
    <style>
        /* Estilo del banner */
        .banner {
            background-color: #0B3780;
            color: white;
            text-align: center;
            padding: 40px;
        }

        /* Estilo de la fuente */
        .fuente-especial {
            font-family: 'Arial', sans-serif;
            font-size: 36px;
            font-weight: bold;
        }

        /* Estilo del párrafo */
        .mensaje {
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <div class="banner">
        <h1 class="fuente-especial">
            ¡Bienvenido a la App2!
        </h1>
        <p class="mensaje">
            Esperamos que disfrutes de tu experiencia en nuestra aplicación.
        </p>
    </div>
    """
    return HttpResponse(html)

def vista2(request):
    html = """
    <style>
        /* Estilo del banner */
        .banner {
            background-color: #009688;
            color: white;
            text-align: center;
            padding: 40px;
        }

        /* Estilo de la fuente */
        .fuente-especial {
            font-family: 'Verdana', sans-serif;
            font-size: 36px;
            font-weight: bold;
        }

        /* Estilo del párrafo */
        .mensaje {
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <div class="banner">
        <h1 class="fuente-especial">
            ¡Esta es la vista 2!
        </h1>
        <p class="mensaje">
            Esta es la vista número 2 en nuestra aplicación.
        </p>
    </div>
    """
    return HttpResponse(html)
