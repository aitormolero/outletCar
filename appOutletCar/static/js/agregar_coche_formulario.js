document.addEventListener('DOMContentLoaded', function () {
    const categoriaSelector = document.getElementById('categoria-selector');
    const categoriasSeleccionadasDiv = document.getElementById('categorias-seleccionadas');
    const categoriasInput = document.getElementById('categorias-input');
    let categoriaSeleccionada = null;

    categoriaSelector.addEventListener('change', function () {
        const categoria = this.value;

        if (!categoriaSeleccionada) {
            categoriaSeleccionada = categoria;

            const etiqueta = document.createElement('span');
            etiqueta.className = 'badge text-dark px-3 py-2 m-1';
            etiqueta.textContent = categoria;
            etiqueta.style.cursor = 'pointer';
            etiqueta.style.fontSize = '14px';
            etiqueta.style.backgroundColor = '#f5a623'; 
            etiqueta.style.borderRadius = '20px';

            etiqueta.addEventListener('click', function () {
                categoriaSeleccionada = null;
                categoriasSeleccionadasDiv.removeChild(etiqueta);
                restaurarOpcion(categoria);
                actualizarInput();
                categoriaSelector.disabled = false; 
            });

            categoriasSeleccionadasDiv.appendChild(etiqueta);
            eliminarOpcion(categoria);
            actualizarInput();

            categoriaSelector.disabled = true;
        }

        this.value = '';
    });

    function actualizarInput() {
        categoriasInput.value = categoriaSeleccionada ? categoriaSeleccionada : '';
    }

    function eliminarOpcion(categoria) {
        const option = [...categoriaSelector.options].find(opt => opt.value === categoria);
        if (option) option.remove();
    }

    function restaurarOpcion(categoria) {
        const option = document.createElement('option');
        option.value = categoria;
        option.textContent = categoria;
        categoriaSelector.appendChild(option);
    }
});
