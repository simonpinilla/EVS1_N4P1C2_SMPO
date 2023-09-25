from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    html = """
    <style>
        /* Estilo del banner */
        .banner {
            background-color: #0074E4;
            color: white;
            text-align: center;
            padding: 20px;
        }

        /* Estilo de la fuente */
        .fuente-especial {
            font-family: 'Courier New', Courier, monospace;
            font-size: 24px;
        }
    </style>
    <div class="banner">
        <h1 class="fuente-especial">
            Bienvenido a  Smpo_app1!
        </h1>
    </div>
    """
    return HttpResponse(html)

def vista2(request):
    html = """
    <style>
        /* Estilo del banner */
        .banner {
            background-color: #4FD11A;
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
            ¡Vista 2 app1!
        </h1>
        <p class="mensaje">
            Esta es la vista número  en nuestra aplicación.
        </p>
    </div>
    """
    return HttpResponse(html)

