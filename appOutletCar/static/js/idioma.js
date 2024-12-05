document.addEventListener("DOMContentLoaded", function () {
    window.changeLanguage = function (lang) {
        const currentUrl = window.location.pathname;

        // Si el idioma ya está en la URL, no añadirlo de nuevo
        if (lang === 'es' && !currentUrl.startsWith('/es/')) {
            const newUrl = `/es${currentUrl.startsWith('/en') ? currentUrl.slice(3) : currentUrl}`; // Si la URL empieza con /en, se reemplaza por /es
            window.location.pathname = newUrl;
        } else if (lang === 'en' && !currentUrl.startsWith('/en/')) {
            const newUrl = `/en${currentUrl.startsWith('/es') ? currentUrl.slice(3) : currentUrl}`; // Si la URL empieza con /es, se reemplaza por /en
            window.location.pathname = newUrl;
        } else {
            // Manejo con Google Translate
            const iframe = document.querySelector('iframe.goog-te-banner-frame');
            if (iframe) {
                const innerDoc = iframe.contentDocument || iframe.contentWindow.document;
                const select = innerDoc.querySelector('.goog-te-combo');
                if (select) {
                    select.value = lang;
                    select.dispatchEvent(new Event('change'));
                }
            } else {
                console.warn('Google Translate no está disponible.');
            }
        }
    };
});
