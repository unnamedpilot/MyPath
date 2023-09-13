document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.getElementById('mi-formulario');

    formulario.addEventListener('submit', function (event) {
        event.preventDefault();

        const textarea = document.getElementById('texto-a-enviar');
        const contenido = textarea.value;

        const data = { contenido: contenido };

        fetch('/api/chat-gpt/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),  
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(respuestaDeChatGPT => {
            const respuestaDiv = document.getElementById('respuesta-de-chat');
            respuestaDiv.innerHTML = respuestaDeChatGPT.respuesta;
        })
        .catch(error => {
            console.error('Error al enviar solicitud a la API de ChatGPT', error);
        });
    });
});




