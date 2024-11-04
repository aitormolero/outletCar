from tu_app.models import Coche, Marca, Categoria

def importar_coches():
    coches = [
        {
            'marca': 'BMW',
            'modelo': 'Serie 3',
            'anio': 2020,
            'precio': 35000.00,
            'color': 'Negro',
            'kilometraje': 15000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Trasera',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'Un sedán deportivo con gran rendimiento.',
            'categorias': ['Sedan', 'Deportivo']
        },
        {
            'marca': 'Mercedes',
            'modelo': 'Clase E',
            'anio': 2018,
            'precio': 45000.00,
            'color': 'Gris',
            'kilometraje': 20000,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Delantera',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'Sedán de lujo, ideal para viajes largos.',
            'categorias': ['Sedan', 'Familiar']
        },
        {
            'marca': 'Audi',
            'modelo': 'A4',
            'anio': 2022,
            'precio': 42000.00,
            'color': 'Blanco',
            'kilometraje': 12000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'Una mezcla perfecta de lujo y rendimiento.',
            'categorias': ['Sedan']
        },
        {
            'marca': 'Porsche',
            'modelo': '911',
            'anio': 2021,
            'precio': 120000.00,
            'color': 'Rojo',
            'kilometraje': 5000,
            'transmision': 'Manual',
            'combustible': 'Gasolina',
            'traccion': 'Trasera',
            'numero_puertas': 2,
            'descapotable': False,
            'descripcion': 'Deportivo de alto rendimiento para amantes de la velocidad.',
            'categorias': ['Deportivo', 'Coupé']
        },
        {
            'marca': 'Ford',
            'modelo': 'Fiesta',
            'anio': 2017,
            'precio': 18000.00,
            'color': 'Azul',
            'kilometraje': 25000,
            'transmision': 'Manual',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'Económico y práctico para la ciudad.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Toyota',
            'modelo': 'Prius',
            'anio': 2019,
            'precio': 28000.00,
            'color': 'Verde',
            'kilometraje': 30000,
            'transmision': 'Automática',
            'combustible': 'Híbrido',
            'traccion': 'Delantera',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'El clásico híbrido, perfecto para un consumo eficiente.',
            'categorias': ['Híbrido-Eléctrico']
        },
        {
            'marca': 'Seat',
            'modelo': 'Ibiza',
            'anio': 2015,
            'precio': 15000.00,
            'color': 'Rojo',
            'kilometraje': 35000,
            'transmision': 'Manual',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'Compacto y ágil, ideal para la ciudad.',
            'categorias': ['Familiar', 'Coupé']
        },
        {
            'marca': 'Volkswagen',
            'modelo': 'Golf',
            'anio': 2024,
            'precio': 32000.00,
            'color': 'Negro',
            'kilometraje': 0,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'Un compacto premium con tecnología avanzada.',
            'categorias': ['Sedan']
        },
        {
            'marca': 'Tesla',
            'modelo': 'Model 3',
            'anio': 2023,
            'precio': 45000.00,
            'color': 'Blanco',
            'kilometraje': 5000,
            'transmision': 'Automática',
            'combustible': 'Eléctrico',
            'traccion': 'Total',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'Eléctrico asequible y de alto rendimiento.',
            'categorias': ['Híbrido-Eléctrico', 'Sedan']
        },
        {
            'marca': 'Honda',
            'modelo': 'Civic',
            'anio': 2016,
            'precio': 22000.00,
            'color': 'Gris',
            'kilometraje': 28000,
            'transmision': 'Manual',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'Popular compacto con excelente rendimiento de combustible.',
            'categorias': ['Sedan', 'Deportivo']
        },
        {
            'marca': 'BMW',
            'modelo': 'X5',
            'anio': 2021,
            'precio': 70000.00,
            'color': 'Blanco',
            'kilometraje': 18000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El BMW X5 es un SUV de lujo que combina un diseño elegante con un rendimiento excepcional. '
                        'Con tracción total, ofrece una conducción segura en diversas condiciones climáticas. Su interior espacioso está equipado con tecnología avanzada, '
                        'incluyendo un sistema de infoentretenimiento intuitivo y asientos cómodos, lo que lo convierte en una excelente opción para familias que buscan confort y estilo.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Mercedes',
            'modelo': 'GLE',
            'anio': 2019,
            'precio': 80000.00,
            'color': 'Negro',
            'kilometraje': 22000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Mercedes GLE es un SUV elegante y robusto que ofrece un amplio espacio interior y un rendimiento dinámico. '
                        'Su sistema de tracción total y la suspensión adaptativa aseguran una conducción suave y segura, incluso en terrenos difíciles. '
                        'Con un enfoque en la comodidad y la tecnología avanzada, este vehículo es perfecto para aquellos que buscan un lujo práctico y funcional.',
            'categorias': ['Familiar', 'Sedan']
        },
        {
            'marca': 'Audi',
            'modelo': 'Q7',
            'anio': 2022,
            'precio': 90000.00,
            'color': 'Gris',
            'kilometraje': 5000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Audi Q7 es un SUV grande y espacioso, ideal para familias numerosas. Con un motor potente y tracción total, '
                        'ofrece un excelente rendimiento en carretera y fuera de ella. Su interior lujoso está diseñado con materiales de alta calidad y tecnología de vanguardia, '
                        'incluyendo un sistema de infoentretenimiento completo, lo que garantiza comodidad y diversión en cada viaje.',
            'categorias': ['Familiar', 'Deportivo']
        },
        {
            'marca': 'Porsche',
            'modelo': 'Cayenne',
            'anio': 2020,
            'precio': 95000.00,
            'color': 'Azul',
            'kilometraje': 15000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Porsche Cayenne es un SUV de lujo que ofrece un rendimiento excepcional y una experiencia de conducción inigualable. '
                        'Con su potente motor y tracción total, puede acelerar de 0 a 100 km/h en un tiempo impresionante. '
                        'El interior es un refugio de confort, con asientos de cuero de alta calidad y tecnología avanzada, ofreciendo tanto lujo como funcionalidad.',
            'categorias': ['Familiar', 'Deportivo']
        },
        {
            'marca': 'Ford',
            'modelo': 'Mustang',
            'anio': 2016,
            'precio': 50000.00,
            'color': 'Rojo',
            'kilometraje': 40000,
            'transmision': 'Manual',
            'combustible': 'Gasolina',
            'traccion': 'Trasera',
            'numero_puertas': 2,
            'descapotable': True,
            'descripcion': 'El Ford Mustang es un ícono deportivo estadounidense que combina potencia y estilo en un solo paquete. '
                        'Su motor V8 ofrece una aceleración emocionante y un sonido inconfundible. El diseño descapotable proporciona una experiencia de conducción al aire libre, '
                        'mientras que el interior moderno y las características tecnológicas avanzadas aseguran que cada viaje sea memorable y cómodo.',
            'categorias': ['Deportivo', 'Coupé']
        },
        {
            'marca': 'Toyota',
            'modelo': 'RAV4',
            'anio': 2018,
            'precio': 32000.00,
            'color': 'Gris',
            'kilometraje': 30000,
            'transmision': 'Automática',
            'combustible': 'Híbrido',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Toyota RAV4 es un SUV híbrido que combina eficiencia de combustible con un rendimiento confiable. '
                        'Su diseño robusto y espacioso es perfecto para aventuras familiares, y la tracción total proporciona seguridad en diversas condiciones. '
                        'Con un interior bien equipado y características de seguridad avanzadas, es una opción práctica y ecológica para los conductores modernos.',
            'categorias': ['Familiar', 'Híbrido-Eléctrico']
        },
        {
            'marca': 'Seat',
            'modelo': 'León',
            'anio': 2021,
            'precio': 29000.00,
            'color': 'Negro',
            'kilometraje': 10000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Seat León es un hatchback ágil y moderno que destaca por su diseño deportivo y tecnología avanzada. '
                        'Con una conducción dinámica y eficiente, es ideal para la vida urbana y los desplazamientos diarios. '
                        'Su interior ofrece comodidad y espacio, con un enfoque en la conectividad y la seguridad, lo que lo convierte en una excelente opción para jóvenes conductores.',
            'categorias': ['Sedan']
        },
        {
            'marca': 'Volkswagen',
            'modelo': 'Tiguan',
            'anio': 2020,
            'precio': 37000.00,
            'color': 'Blanco',
            'kilometraje': 20000,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Volkswagen Tiguan es un SUV diésel con tracción total que ofrece un gran espacio interior y una conducción cómoda. '
                        'Su diseño robusto y características de seguridad avanzadas lo convierten en una excelente opción para familias y aventureros. '
                        'Además, su eficiente motor diésel garantiza un consumo de combustible razonable, lo que lo hace perfecto para viajes largos.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Tesla',
            'modelo': 'Model X',
            'anio': 2023,
            'precio': 120000.00,
            'color': 'Negro',
            'kilometraje': 5000,
            'transmision': 'Automática',
            'combustible': 'Eléctrico',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Tesla Model X es un SUV eléctrico que destaca por su diseño innovador y sus características únicas, como las puertas de halcón. '
                        'Con una autonomía excepcional y un rendimiento ágil, ofrece una experiencia de conducción ecológica y emocionante. '
                        'El interior es espacioso y está lleno de tecnología avanzada, lo que garantiza un viaje cómodo y conectado para toda la familia.',
            'categorias': ['Híbrido-Eléctrico']
        },
        {
            'marca': 'Honda',
            'modelo': 'CR-V',
            'anio': 2017,
            'precio': 28000.00,
            'color': 'Azul',
            'kilometraje': 40000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Honda CR-V es un SUV compacto que combina confiabilidad y eficiencia. Su diseño práctico ofrece un amplio espacio interior, ideal para familias. '
                        'La tracción total proporciona seguridad en diferentes condiciones climáticas, y su reputación de bajo mantenimiento lo convierte en una opción inteligente a largo plazo.',
            'categorias': ['Familiar', 'Sedan']
        },
        {
            'marca': 'BMW',
            'modelo': 'X3',
            'anio': 2021,
            'precio': 70000.00,
            'color': 'Negro',
            'kilometraje': 12000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El BMW X3 es un SUV compacto de lujo con tracción total y un diseño moderno. Ofrece '
                           'un motor de gasolina potente y una experiencia de conducción equilibrada entre '
                           'confort y deportividad, perfecto tanto para la ciudad como para viajes largos.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Mercedes',
            'modelo': 'GLC',
            'anio': 2022,
            'precio': 82000.00,
            'color': 'Plata',
            'kilometraje': 10000,
            'transmision': 'Automática',
            'combustible': 'Híbrido',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Mercedes GLC es un SUV híbrido que combina lujo y eficiencia. Con tracción total y un '
                           'sistema híbrido avanzado, proporciona un excelente rendimiento tanto en carretera como fuera '
                           'de ella, ideal para conductores que buscan un vehículo versátil y elegante.',
            'categorias': ['Híbrido-Eléctrico', 'Familiar']
        },
        {
            'marca': 'Audi',
            'modelo': 'Q7',
            'anio': 2019,
            'precio': 90000.00,
            'color': 'Gris Metálico',
            'kilometraje': 25000,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Audi Q7 es un SUV grande y lujoso con tracción total y un motor diésel potente. '
                           'Destaca por su amplio espacio interior, ideal para familias, y su avanzada tecnología '
                           'de asistencia al conductor, lo que lo convierte en un vehículo cómodo y seguro en largas travesías.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Porsche',
            'modelo': 'Macan',
            'anio': 2021,
            'precio': 100000.00,
            'color': 'Blanco Perla',
            'kilometraje': 15000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Porsche Macan es un SUV deportivo que combina el rendimiento característico de Porsche con '
                           'la comodidad de un todoterreno. Ideal para quienes buscan un vehículo con espíritu deportivo '
                           'y capacidad para la familia, con tracción total y un motor de gasolina ágil.',
            'categorias': ['Deportivo', 'Familiar']
        },
        {
            'marca': 'Ford',
            'modelo': 'Kuga',
            'anio': 2020,
            'precio': 35000.00,
            'color': 'Rojo',
            'kilometraje': 20000,
            'transmision': 'Manual',
            'combustible': 'Híbrido',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Ford Kuga es un SUV híbrido compacto y eficiente, con tracción delantera. Diseñado para '
                           'ofrecer una gran economía de combustible sin sacrificar el rendimiento, es ideal para '
                           'conducir en ciudad o realizar viajes largos con comodidad.',
            'categorias': ['Híbrido-Eléctrico', 'Familiar']
        },
        {
            'marca': 'Toyota',
            'modelo': 'RAV4',
            'anio': 2023,
            'precio': 60000.00,
            'color': 'Verde Oscuro',
            'kilometraje': 5000,
            'transmision': 'Automática',
            'combustible': 'Híbrido',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Toyota RAV4 es un SUV híbrido compacto que ofrece un excelente equilibrio entre rendimiento, '
                           'economía de combustible y capacidad todoterreno. Con tracción total, es perfecto para familias '
                           'activas que buscan un vehículo versátil y fiable.',
            'categorias': ['Híbrido-Eléctrico', 'Familiar']
        },
        {
            'marca': 'Seat',
            'modelo': 'Arona',
            'anio': 2021,
            'precio': 25000.00,
            'color': 'Gris',
            'kilometraje': 30000,
            'transmision': 'Manual',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Seat Arona es un SUV compacto ágil y económico, ideal para la conducción urbana. Su '
                           'diseño juvenil y motor eficiente lo convierten en una opción excelente para quienes buscan '
                           'un vehículo compacto pero con espacio suficiente para la familia o amigos.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Volkswagen',
            'modelo': 'Passat',
            'anio': 2020,
            'precio': 40000.00,
            'color': 'Negro',
            'kilometraje': 20000,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Delantera',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'El Volkswagen Passat es un sedán de tamaño medio que destaca por su tecnología avanzada, su '
                           'confort y su eficiencia. Con un motor diésel, es ideal para quienes buscan un vehículo duradero '
                           'y con gran autonomía, perfecto tanto para viajes largos como para uso diario.',
            'categorias': ['Sedan', 'Familiar']
        },
        {
            'marca': 'Tesla',
            'modelo': 'Model S',
            'anio': 2024,
            'precio': 110000.00,
            'color': 'Plateado',
            'kilometraje': 1000,
            'transmision': 'Automática',
            'combustible': 'Eléctrico',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Tesla Model S es una berlina completamente eléctrica con una impresionante autonomía y '
                           'rendimiento. Ofrece tecnología de conducción autónoma, una aceleración increíble y un diseño '
                           'elegante, haciéndolo ideal para quienes buscan el futuro de la movilidad.',
            'categorias': ['Híbrido-Eléctrico', 'Sedan']
        },
        {
            'marca': 'Honda',
            'modelo': 'Jazz',
            'anio': 2022,
            'precio': 25000.00,
            'color': 'Blanco Perla',
            'kilometraje': 8000,
            'transmision': 'Automática',
            'combustible': 'Híbrido',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Honda Jazz es un compacto urbano que destaca por su gran eficiencia y espacio interior pese a su '
                        'tamaño reducido. Equipado con un motor híbrido, es ideal para quienes buscan un coche económico y '
                        'amigable con el medio ambiente, perfecto para la conducción en ciudad y con un diseño moderno.',
            'categorias': ['Híbrido-Eléctrico', 'Familiar']
        },
        {
            'marca': 'BMW',
            'modelo': 'Z4',
            'anio': 2023,
            'precio': 60000.00,
            'color': 'Rojo',
            'kilometraje': 5000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Trasera',
            'numero_puertas': 2,
            'descapotable': True,
            'descripcion': 'El BMW Z4 es un roadster deportivo que combina un diseño elegante con un rendimiento sobresaliente. '
                           'Con su motor potente y tracción trasera, ofrece una experiencia de conducción emocionante y abierta, '
                           'ideal para los amantes de la velocidad y la aventura en la carretera.',
            'categorias': ['Deportivo']
        },
        {
            'marca': 'Mercedes',
            'modelo': 'EQS',
            'anio': 2022,
            'precio': 130000.00,
            'color': 'Negro',
            'kilometraje': 3000,
            'transmision': 'Automática',
            'combustible': 'Eléctrico',
            'traccion': 'Total',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'El Mercedes EQS redefine el lujo en la era eléctrica. Con un diseño futurista, tecnología de vanguardia y '
                           'una autonomía excepcional, es la berlina eléctrica perfecta para quienes buscan confort y sostenibilidad, '
                           'sin sacrificar el rendimiento.',
            'categorias': ['Híbrido-Eléctrico', 'Sedan']
        },
        {
            'marca': 'Audi',
            'modelo': 'R8',
            'anio': 2023,
            'precio': 200000.00,
            'color': 'Gris Platino',
            'kilometraje': 2000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 2,
            'descapotable': False,
            'descripcion': 'El Audi R8 es un superdeportivo que combina un diseño impresionante con un motor V10 potente. '
                           'Con tracción total, acelera de 0 a 100 km/h en solo unos segundos, ofreciendo una experiencia de conducción '
                           'inigualable en circuito y en carretera.',
            'categorias': ['Deportivo']
        },
        {
            'marca': 'Porsche',
            'modelo': 'Cayenne',
            'anio': 2022,
            'precio': 80000.00,
            'color': 'Negro',
            'kilometraje': 4000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Porsche Cayenne es un SUV de lujo que combina un rendimiento excepcional con un diseño elegante. '
                           'Equipado con potentes motores y una tracción total que garantiza una conducción dinámica, es ideal para '
                           'aquellos que buscan estilo y versatilidad en un solo vehículo.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Ford',
            'modelo': 'Explorer',
            'anio': 2023,
            'precio': 50000.00,
            'color': 'Azul',
            'kilometraje': 5000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Ford Explorer es un SUV de tamaño mediano que ofrece una combinación perfecta de espacio, comodidad y rendimiento. '
                           'Con un interior versátil y tecnología avanzada, es ideal para familias que buscan aventuras y comodidad en sus viajes.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Seat',
            'modelo': 'Arona',
            'anio': 2021,
            'precio': 25000.00,
            'color': 'Gris',
            'kilometraje': 12000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Seat Arona es un SUV subcompacto que destaca por su diseño juvenil y su excelente relación calidad-precio. '
                           'Con un motor eficiente y un interior moderno, es perfecto para la conducción urbana y aventuras familiares.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Honda',
            'modelo': 'Pilot',
            'anio': 2023,
            'precio': 48000.00,
            'color': 'Negro',
            'kilometraje': 3000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Honda Pilot es un SUV de tamaño completo que ofrece un amplio espacio para hasta ocho pasajeros. '
                           'Con su tracción total y tecnología avanzada de seguridad, es perfecto para familias que buscan comodidad y '
                           'seguridad en todos sus viajes.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Tesla',
            'modelo': 'Model Y',
            'anio': 2023,
            'precio': 65000.00,
            'color': 'Blanco',
            'kilometraje': 2000,
            'transmision': 'Automática',
            'combustible': 'Eléctrico',
            'traccion': 'Total',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Tesla Model Y es un SUV totalmente eléctrico que ofrece un rendimiento impresionante, amplio espacio interior y tecnología de conducción autónoma. '
                           'Con una autonomía sobresaliente y un diseño moderno, es perfecto para quienes buscan un vehículo sostenible y práctico para la familia.',
            'categorias': ['Híbrido-Eléctrico']
        },
        {
            'marca': 'Toyota',
            'modelo': 'Supra',
            'anio': 2022,
            'precio': 55000.00,
            'color': 'Gris',
            'kilometraje': 15000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Trasera',
            'numero_puertas': 2,
            'descapotable': False,
            'descripcion': 'El Toyota Supra es un coupé deportivo que destaca por su diseño agresivo y su excepcional rendimiento. '
                           'Equipado con un motor turboalimentado, ofrece una experiencia de conducción ágil y emocionante, '
                           'perfecta para los entusiastas del automovilismo.',
            'categorias': ['Deportivo']
        },
        {
            'marca': 'BMW',
            'modelo': 'M4',
            'anio': 2023,
            'precio': 80000.00,
            'color': 'Gris',
            'kilometraje': 3000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Trasera',
            'numero_puertas': 2,
            'descapotable': False,
            'descripcion': 'El BMW M4 es un coupé deportivo que ofrece un rendimiento extraordinario y un manejo preciso. '
                           'Con su motor potente y su diseño agresivo, está diseñado para los entusiastas de la velocidad que buscan una experiencia de conducción emocionante.',
            'categorias': ['Deportivo']
        },
        {
            'marca': 'Mercedes',
            'modelo': 'Clase S',
            'anio': 2023,
            'precio': 150000.00,
            'color': 'Negro',
            'kilometraje': 500,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'La Mercedes Clase S es la máxima expresión de lujo y tecnología. Con un interior exquisito y un rendimiento sobresaliente, '
                           'es perfecta para quienes valoran la elegancia y el confort en cada viaje.',
            'categorias': ['Sedan']
        },
        {
            'marca': 'Audi',
            'modelo': 'A1',
            'anio': 2023,
            'precio': 30000.00,
            'color': 'Azul',
            'kilometraje': 2000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Audi A1 es un compacto que combina estilo y tecnología en un paquete atractivo. '
                           'Con su interior bien diseñado y su manejo ágil, es ideal para la ciudad y para quienes buscan un coche práctico y elegante.',
            'categorias': ['Sedan']
        },
        {
            'marca': 'Toyota',
            'modelo': 'C-HR',
            'anio': 2023,
            'precio': 28000.00,
            'color': 'Verde',
            'kilometraje': 1500,
            'transmision': 'Automática',
            'combustible': 'Híbrido',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Toyota C-HR es un SUV compacto que se destaca por su diseño futurista y su eficiencia energética. '
                           'Con un interior espacioso y tecnología avanzada, es perfecto para quienes buscan un vehículo moderno y ecológico.',
            'categorias': ['Híbrido-Eléctrico']
        },
        {
            'marca': 'Volkswagen',
            'modelo': 'GTI',
            'anio': 2023,
            'precio': 35000.00,
            'color': 'Rojo',
            'kilometraje': 1000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Volkswagen GTI es un hatchback deportivo que combina un diseño icónico con un rendimiento excepcional. '
                           'Con su motor potente y su chasis ágil, es ideal para quienes buscan una experiencia de conducción emocionante y divertida.',
            'categorias': ['Deportivo']
        },
        {
            'marca': 'Ford',
            'modelo': 'Focus',
            'anio': 2024,
            'precio': 28000.00,
            'color': 'Azul',
            'kilometraje': 5000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'El Ford Focus es un compacto versátil que combina un diseño elegante con tecnología avanzada. '
                           'Su conducción ágil y eficiente lo convierte en una excelente opción tanto para la ciudad como para viajes largos.',
            'categorias': ['Sedan']
        },
        {
            'marca': 'Tesla',
            'modelo': 'Roadster',
            'anio': 2024,
            'precio': 200000.00,
            'color': 'Plateado',
            'kilometraje': 0,
            'transmision': 'Automática',
            'combustible': 'Eléctrico',
            'traccion': 'Total',
            'numero_puertas': 2,
            'descapotable': True,
            'descripcion': 'El Tesla Roadster es un superdeportivo completamente eléctrico que redefine la velocidad y la eficiencia. '
                           'Con su aceleración impresionante y su diseño aerodinámico, es perfecto para quienes buscan lo último en tecnología y rendimiento.',
            'categorias': ['Deportivo', 'Híbrido-Eléctrico']
        },
        {
            'marca': 'Honda',
            'modelo': 'ZR-V',
            'anio': 2023,
            'precio': 35000.00,
            'color': 'Negro',
            'kilometraje': 2000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Honda ZR-V es un SUV compacto que combina un diseño moderno con una excelente eficiencia de combustible. '
                           'Con un interior espacioso y cómodo, es ideal para familias que buscan un vehículo práctico para la vida diaria.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Seat',
            'modelo': 'Ateca',
            'anio': 2023,
            'precio': 36000.00,
            'color': 'Blanco',
            'kilometraje': 1000,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Seat Ateca es un SUV que combina estilo y funcionalidad. Con un interior bien equipado y una conducción cómoda, '
                           'es perfecto para aventuras urbanas y escapadas familiares.',
            'categorias': ['Familiar']
        },
        {
            'marca': 'Porsche',
            'modelo': 'Panamera',
            'anio': 2023,
            'precio': 110000.00,
            'color': 'Rojo',
            'kilometraje': 1500,
            'transmision': 'Automática',
            'combustible': 'Gasolina',
            'traccion': 'Total',
            'numero_puertas': 4,
            'descapotable': False,
            'descripcion': 'El Porsche Panamera combina el rendimiento de un deportivo con la comodidad de un sedán de lujo. '
                           'Su motor potente y su diseño elegante lo convierten en un vehículo ideal para quienes buscan velocidad y confort en un solo paquete.',
            'categorias': ['Sedan']
        },
        {
            'marca': 'Mercedes',
            'modelo': 'Clase V',
            'anio': 2023,
            'precio': 60000.00,
            'color': 'Blanco',
            'kilometraje': 5000,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'La Mercedes Clase V es una furgoneta de lujo que ofrece un amplio espacio y confort. '
                           'Ideal para familias grandes o para transporte de pasajeros, combina un diseño elegante con tecnología avanzada.',
            'categorias': ['Furgoneta', 'Lujo']
        },
        {
            'marca': 'Volkswagen',
            'modelo': 'Transporter',
            'anio': 2023,
            'precio': 45000.00,
            'color': 'Gris',
            'kilometraje': 3000,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'La Volkswagen Transporter es una furgoneta versátil y robusta, perfecta para negocios y transporte. '
                           'Su espacio interior y capacidad de carga la convierten en una opción ideal para profesionales en movimiento.',
            'categorias': ['Furgoneta', 'Comercial']
        },
        {
            'marca': 'Ford',
            'modelo': 'Transit Custom',
            'anio': 2023,
            'precio': 35000.00,
            'color': 'Azul',
            'kilometraje': 2500,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'La Ford Transit Custom es una furgoneta diseñada para ofrecer flexibilidad y confort. '
                           'Con su amplia capacidad de carga y tecnología avanzada, es ideal para cualquier tipo de trabajo.',
            'categorias': ['Furgoneta', 'Comercial']
        },
        {
            'marca': 'Toyota',
            'modelo': 'Proace',
            'anio': 2023,
            'precio': 42000.00,
            'color': 'Negro',
            'kilometraje': 4000,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'El Toyota Proace es una furgoneta versátil y eficiente, ideal para el transporte de mercancías o personas. '
                           'Con un diseño práctico y una gran capacidad de carga, es perfecta para negocios en crecimiento.',
            'categorias': ['Furgoneta', 'Comercial']
        },
        {
            'marca': 'Mercedes',
            'modelo': 'Sprinter',
            'anio': 2023,
            'precio': 55000.00,
            'color': 'Blanco',
            'kilometraje': 3000,
            'transmision': 'Automática',
            'combustible': 'Diésel',
            'traccion': 'Delantera',
            'numero_puertas': 5,
            'descapotable': False,
            'descripcion': 'La Mercedes Sprinter es una furgoneta de gran capacidad y versatilidad. Con un interior espacioso y la opción de diferentes longitudes de chasis, '
                           'es ideal para transporte de mercancías, como vehículo de trabajo o incluso como camper. Su tecnología avanzada asegura una experiencia de conducción cómoda y segura.',
            'categorias': ['Furgoneta', 'Comercial']
        }
    ]

    for coche_data in coches:
        # Obtener o crear la marca
        marca, created = Marca.objects.get_or_create(nombre=coche_data['marca'])

        # Crear el coche
        coche = Coche.objects.create(
            marca=marca,
            modelo=coche_data['modelo'],
            anio=coche_data['anio'],
            precio=coche_data['precio'],
            color=coche_data['color'],
            kilometraje=coche_data['kilometraje'],
            transmision=coche_data['transmision'],
            combustible=coche_data['combustible'],
            traccion=coche_data['traccion'],
            numero_puertas=coche_data['numero_puertas'],
            descapotable=coche_data['descapotable'],
            descripcion=coche_data['descripcion']
        )

        # Obtener o crear las categorías y asignarlas al coche
        for categoria_nombre in coche_data['categorias']:
            categoria, created = Categoria.objects.get_or_create(nombre=categoria_nombre)
            coche.categoria.add(categoria)

        coche.save()

    print("Coches importados exitosamente.")

# Llamar a la función para importar coches
importar_coches()
