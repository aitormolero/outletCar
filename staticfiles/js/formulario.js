document.addEventListener('DOMContentLoaded', function () {
    const marcaSelect = document.querySelector('select[name="marca"]');
    const categoriaSelect = document.querySelector('select[name="categoria"]');
    const modeloSelect = document.querySelector('select[name="modelo"]');

    categoriaSelect.innerHTML = '<option value="">Selecciona la marca</option>';
    modeloSelect.innerHTML = '<option value="">Selecciona la marca</option>';

    marcaSelect.addEventListener('change', function () {
        const marcaId = this.value;

        if (!marcaId) {
            categoriaSelect.innerHTML = '<option value="">Selecciona la marca</option>';
            modeloSelect.innerHTML = '<option value="">Selecciona la marca</option>';
            return;
        }

        categoriaSelect.innerHTML = '<option value="">Cargando categorías...</option>';
        modeloSelect.innerHTML = '<option value="">Selecciona la categoría</option>';

        fetch(`/api/categorias/${marcaId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    categoriaSelect.innerHTML = '<option value="">Sin categorías disponibles</option>';
                } else {
                    categoriaSelect.innerHTML = '<option value="">----</option>';
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

        if (!marcaId) {
            modeloSelect.innerHTML = '<option value="">Selecciona la marca</option>';
            return;
        }

        if (!categoriaId) {
            modeloSelect.innerHTML = '<option value="">Selecciona la categoría</option>';
            return;
        }

        modeloSelect.innerHTML = '<option value="">Cargando modelos...</option>';

        fetch(`/api/coches/${marcaId}/${categoriaId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    modeloSelect.innerHTML = '<option value="">Sin modelos disponibles</option>';
                } else {
                    modeloSelect.innerHTML = '<option value="">----</option>';
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
