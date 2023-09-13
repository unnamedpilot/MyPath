document.addEventListener('DOMContentLoaded', function () {
    const ubicacionUsuario = document.getElementById('ubicacion-usuario');

    if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            const latitud = position.coords.latitude;
            const longitud = position.coords.longitude;

            ubicacionUsuario.textContent = `Latitud: ${latitud}, Longitud: ${longitud}`;

        }, function (error) {
            console.error('Error al obtener la ubicación:', error);
            ubicacionUsuario.textContent = 'No se pudo obtener la ubicación.';
        });
    } else {
        ubicacionUsuario.textContent = 'La geolocalización no está disponible en este navegador.';
    }
});
