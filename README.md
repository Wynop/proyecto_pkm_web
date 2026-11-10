# PKM-BATTLE

Pequeña Pokédex web centrada en las diferentes evoluciones de **Eevee**, desarrollada como proyecto de aprendizaje utilizando **Python, Flask, HTML, CSS y Jinja2**.

## Tecnologías

- Python
- Flask
- Flask-WTF
- WTForms
- Jinja2
- HTML5
- CSS / SCSS
- JavaScript
- JSON

## Funcionalidades

- Listado de las diferentes Eeveelutions.
- Página individual para cada Pokémon.
- Información sobre estadísticas y características.
- Listado de movimientos.
- Colores personalizados según el tipo de Pokémon.
- Registro e identificación del entrenador mediante sesiones.
- Filtrado de Pokémon por nombre y tipo.
- Sistema de preparación de batallas entre Pokémon.
- Selección aleatoria de movimientos para el combate.

## Arquitectura y organización

La aplicación está organizada siguiendo una arquitectura por capas, separando las responsabilidades de las diferentes partes del proyecto.

- **Routes:** gestiona las rutas y las peticiones HTTP mediante Blueprints.
- **Services:** contiene la lógica de negocio de la aplicación, como la gestión de Pokémon, entrenadores y batallas.
- **Repositories:** se encarga del acceso y recuperación de los datos.
- **Models:** define las estructuras y clases utilizadas para representar los datos, como los Pokémon y sus movimientos.
- **Forms:** contiene las clases de formularios desarrolladas con Flask-WTF.
- **Templates:** almacena las plantillas HTML renderizadas mediante Jinja2.
- **Static:** contiene los recursos estáticos, como hojas de estilos, scripts e imágenes.
- **Config:** centraliza constantes y configuraciones utilizadas en la aplicación.

### Organización mediante Blueprints

Las rutas se han dividido en tres Blueprints para separar las funcionalidades principales:

- **auth:** gestiona el inicio y cierre de sesión de los entrenadores.
- **pokemon:** contiene las rutas del listado, filtrado y consulta individual de los Pokémon.
- **battle:** gestiona la vista correspondiente al sistema de combate.

Esta separación permite organizar mejor las rutas, reducir el acoplamiento entre funcionalidades y facilitar el mantenimiento y la ampliación del proyecto.

### Formularios Flask-WTF

Se ha incorporado Flask-WTF para gestionar los formularios desde clases Python, centralizando la definición de campos y sus validaciones.

Actualmente se utilizan los siguientes formularios:

- **LoginForm:** gestiona el registro del entrenador, validando que el nombre introducido tenga una longitud adecuada.
- **BattleForm:** permite seleccionar un Pokémon para iniciar una batalla y valida que se haya introducido un nombre.
- **PokemonFilterForm:** permite filtrar el listado por nombre y tipo, admitiendo que los campos estén vacíos.

Los formularios utilizan validadores de WTForms y protección CSRF mediante tokens generados por Flask-WTF.

## Flujo de interacción y vistas

La aplicación organiza la navegación mediante diferentes rutas y plantillas HTML renderizadas en el servidor con Flask y Jinja2.

1. **Registro del entrenador (`index.html`):** la aplicación solicita un nombre al usuario mediante un formulario Flask-WTF. Una vez validado, se guarda en la sesión para mantenerlo disponible durante la navegación.

2. **Listado de Pokémon (`pkmList.html`):** muestra las diferentes evoluciones de Eevee y permite acceder a la información individual de cada Pokémon. También incorpora formularios para filtrar el listado por nombre y tipo, e iniciar una batalla.

3. **Detalle del Pokémon (`pkmData.html`):** presenta la información del Pokémon seleccionado, incluyendo sus estadísticas, características y movimientos disponibles.

4. **Preparación de la batalla:** el usuario selecciona un Pokémon atacante y el sistema genera un Pokémon defensor aleatorio. También se seleccionan cuatro movimientos aleatorios para el atacante.

5. **Vista de batalla (`battle.html`):** muestra los datos de los Pokémon seleccionados y los movimientos preparados para el combate. La aplicación utiliza una redirección a la ruta `/battle` para recuperar los datos almacenados en la sesión y renderizar esta vista.

6. **Plantilla base (`_base.html`):** proporciona la estructura común de las páginas, permitiendo reutilizar elementos compartidos y mantener una presentación coherente en toda la aplicación.

## Uso de la sesión de Flask

La aplicación utiliza `session` para conservar información entre diferentes peticiones HTTP. Esto es necesario porque, por defecto, cada petición es independiente y Flask no mantiene automáticamente las variables de una petición anterior.

Se guarda la siguiente información:

- **Nombre del entrenador (`name`):** permite conservar el nombre elegido por el usuario durante la navegación y mostrarlo en las vistas que lo necesiten.
- **Datos de la batalla (`battle`):** conserva los Pokémon participantes y la información preparada para el combate.

Estos datos permiten redirigir al usuario a `/battle` sin tener que pasar toda la información mediante parámetros en la URL ni perder los datos preparados durante la petición anterior.

Además, se utiliza un decorador de autenticación (`login_requerido`) para restringir el acceso a determinadas rutas cuando el entrenador no ha iniciado sesión.

## Estructura del proyecto

```text
proyecto_pkm_web/
├── app/
│   ├── forms/
│   │   ├── auth_form.py
│   │   └── pokemon_form.py
│   ├── models/
│   │   ├── move_model.py
│   │   └── pokemon_model.py
│   ├── repositories/
│   │   └── pokemon_repository.py
│   ├── services/
│   │   ├── pokemon_service.py
│   │   └── battle_service.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── pokemon_routes.py
│   │   └── battle_routes.py
│   ├── config/
│   │   ├── config.py
│   │   ├── constants.py
│   │   └── deps.py
│   ├── templates/
│   │   ├── _base.html
│   │   ├── index.html
│   │   ├── pkmList.html
│   │   ├── pkmData.html
│   │   └── battle.html
│   ├── static/
│   │   ├── css/
│   │   ├── scss/
│   │   ├── js/
│   │   └── ...
│   └── main.py
├── data/
│   └── pokemons-eeveelutions.json
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto_pkm_web
```

Crea un entorno virtual:

```bash
python -m venv venv
```

Activa el entorno virtual:

```bash
venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecuta la aplicación desde la raíz del proyecto:

```bash
python app/main.py
```

Después, abre la siguiente dirección en el navegador:

```text
http://127.0.0.1:8080
```