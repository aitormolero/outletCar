document.addEventListener("DOMContentLoaded", function () {
    // Obtiene la URL actual
    const currentUrl = window.location.pathname;

    // Cambiar a español
    document.getElementById('lang-es').addEventListener('click', function (event) {
        event.preventDefault(); // Evita el comportamiento por defecto del enlace
        if (!currentUrl.startsWith('/es/')) { // Solo cambiamos si no estamos ya en español
            const newUrl = '/es' + currentUrl; // Añadimos el prefijo /es/
            console.log("Redirigiendo a:", newUrl);
            window.location.pathname = newUrl; // Redirige la página a la nueva URL
        }
    });

    // Cambiar a inglés
    document.getElementById('lang-en').addEventListener('click', function (event) {
        event.preventDefault(); // Evita el comportamiento por defecto del enlace
        if (!currentUrl.startsWith('/en/')) { // Solo cambiamos si no estamos ya en inglés
            const newUrl = '/en' + currentUrl; // Añadimos el prefijo /en/
            console.log("Redirigiendo a:", newUrl);
            window.location.pathname = newUrl; // Redirige la página a la nueva URL
        }
    });
});
