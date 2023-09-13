import openai
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

openai.api_key = ''

def get_completion(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=2000,
        temperature=0,
    )
    return str(response.choices[0].message["content"])

def chat_gpt_api(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido', '')
        lineas = contenido.strip().split('\n')
        ciudad = ""
        intereses = ""
        cantidad_personas = ""

        if len(lineas) >= 1:
            ciudad = lineas[0].strip()
        if len(lineas) >= 2:
            intereses = lineas[1].strip()
        if len(lineas) >= 3:
            cantidad_personas = lineas[2].strip()

        intereseUsuario=""

        messages = [
            {"role": "user", "content": "Hola"},
            {"role": "user", "content": f"La ciudad a la que quiero viajar es {ciudad}"},
            {"role": "user", "content": f"Quiero que me generes una ruta en la que se tengan en que me gusta {intereses}"},
            {"role": "user", "content": f"La cantidad de personas con las que voy a viajar es {cantidad_personas},Divive en una lista cada una de las divisones ya sean dias horas en una lista "},
            {"role": "user", "content": f"Estas son otras caracteristicas de mis carcteristicas que olvidé mencionar{intereseUsuario}, ademas dame una descripcion detallada de cada uno de los sitos que me recomiendas"},
        ]
        if not messages:
            return HttpResponseBadRequest("Por favor, completa al menos uno de los campos antes de consultar.")
        
        respuesta_de_chat_gpt = get_completion(messages)
        return render(request,'path.html',{'respuesta': respuesta_de_chat_gpt})

    return HttpResponseBadRequest("Manda otra cosa")
