document.addEventListener('DOMContentLoaded', function () {
    const marcaSelect = document.querySelector('select[name="marca"]');
    const categoriaSelect = document.querySelector('select[name="categoria"]');
    const modeloSelect = document.querySelector('select[name="modelo"]');

    // Establecer la opción inicial "Selecciona la marca" para las categorías y modelos
    categoriaSelect.innerHTML = '<option value="">Selecciona la marca</option>';
    modeloSelect.innerHTML = '<option value="">Selecciona la marca</option>';

    marcaSelect.addEventListener('change', function () {
        const marcaId = this.value;

        // Si no hay marca seleccionada, se resetean las categorías y los modelos
        if (!marcaId) {
            categoriaSelect.innerHTML = '<option value="">Selecciona la marca</option>';
            modeloSelect.innerHTML = '<option value="">Selecciona la marca</option>';
            return;
        }

        // Mostrar mensaje de carga mientras se obtienen las categorías
        categoriaSelect.innerHTML = '<option value="">Cargando categorías...</option>';
        modeloSelect.innerHTML = '<option value="">Selecciona la categoría</option>';

        fetch(`/api/categorias/${marcaId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    categoriaSelect.innerHTML = '<option value="">Sin categorías disponibles</option>';
                } else {
                    categoriaSelect.innerHTML = '<option value="">-----</option>'; // Establecemos el valor "-----" solo una vez
                    data.forEach(categoria => {
                        const option = document.createElement('option');
                        option.value = categoria.id;
                        option.textContent = categoria.nombre;
                        categoriaSelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                categoriaSelect.innerHTML = '<option value="">Error al cargar categorías</option>';
                console.error('Error al cargar categorías:', error);
            });
    });

    categoriaSelect.addEventListener('change', function () {
        const marcaId = marcaSelect.value;
        const categoriaId = this.value;

        // Si no hay categoría seleccionada, se resetean los modelos
        if (!marcaId) {
            modeloSelect.innerHTML = '<option value="">Selecciona la marca</option>';
            return;
        }

        if (!categoriaId) {
            modeloSelect.innerHTML = '<option value="">Selecciona la categoría</option>';
            return;
        }

        // Mostrar mensaje de carga mientras se obtienen los modelos
        modeloSelect.innerHTML = '<option value="">Cargando modelos...</option>';

        fetch(`/api/coches/${marcaId}/${categoriaId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    modeloSelect.innerHTML = '<option value="">Sin modelos disponibles</option>';
                } else {
                    modeloSelect.innerHTML = '<option value="">-----</option>'; // Establecemos el valor "-----" solo una vez
                    data.forEach(coche => {
                        const option = document.createElement('option');
                        option.value = coche.id;
                        option.textContent = coche.modelo;
                        modeloSelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                modeloSelect.innerHTML = '<option value="">Error al cargar modelos</option>';
                console.error('Error al cargar modelos:', error);
            });
    });
});
