import os
import json
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) 

openai.api_key  = os.environ['OPENAI_API_KEY']

delimiter = "####"

base_system_message = f"""Eres un sistema que da recomendaciones de lugares en función de los gustos de los usuarios. \
Se te proporcionarán comentarios con los gustos de la persona que quiere viajar o simplemente visitar lugares. \
Los comentarios del usuario estarán en delimitados con 4 hashtags, por ejemplo, {delimiter}. \

Sigue los siguientes pasos para responder al usuario:

Paso 1:#### Revisa que el comentario del usuario cumpla con los dos requisitos:
    a. Realmente se enfoque en los gustos de una persona cuando se trata de turistear, pasear en una ciudad o pueblo, o saber sobre de forma turística lugares para comer.
    b. El comentario menciona el lugar el cuál quiere visitar.
Si el mensaje no cumple con estos requisitos de forma explícita y directamente entonces solamente devuelve un [] y no pases al siguiente paso.

Paso 2:#### Teniendo en cuenta los comentarios del usuario, devuelve una lista en formato JSON de al menos 6 diccionarios de python donde \
cada objeto tenga nombre y descripción:
  'name': <Nombre del lugar>,
  'description': <Descripción del lugar como si hablara un guía turístico>,

Cada objeto debe tener nombre y descripción. Cada descripción debe ser de al menos 90 palabras.

Paso 3:#### Al final de la lista pon un diccionario que tenga el siguiente dato en el siguiente formato:
  'settlement' : <Nombre del pueblo, ciudad o localidad en la que se encuentran los lugares>
  
Paso 4:#### Asegurate de que no haya ningún salto de línea, la lista como tal debe de poder ser leida en forma de JSON.
"""

categories_list = ["restaurante", "museo", "parque", "monumento", "hotel", "playa", "montaña", "mercado", "tienda", "bar", "cafetería", "zoo", "acuario", "galería de arte", "teatro", "cine", "estadio", "centro cultural", "biblioteca", "iglesia"]

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=3000):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"] # type: ignore

def read_string_to_list(input_string):
    if input_string is None:
        return None

    try:
        input_string = input_string.replace("'", "\"")  # Replace single quotes with double quotes for valid JSON
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None

    
def messages_list_maker(user_message, system_message = base_system_message):
    messages = [{'role': 'system', 'content': system_message}, {'role':'user', 'content': f"{delimiter}{user_message}{delimiter}"}]
    return messages

    
def get_completion_in_list(messages):
    string = get_completion_from_messages(messages)
    return read_string_to_list(string)

def get_completion_automatic_format(message):
    messages = messages_list_maker(message)
    return get_completion_in_list(messages)

