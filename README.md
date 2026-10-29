# PKM-BATTLE

Pequeña Pokédex web centrada en las diferentes evoluciones de **Eevee**, desarrollada como proyecto de aprendizaje con **Python, Flask, HTML, CSS y Jinja**.

## Tecnologías

* Python
* Flask
* Jinja2
* HTML5
* CSS
* JSON

## Funcionalidades

* Listado de las diferentes Eeveelutions.
* Página individual para cada Pokémon.
* Información sobre estadísticas y características.
* Listado de movimientos.
* Colores personalizados según el tipo de Pokémon.

## Flujo de interacción y vistas

La aplicación organiza la navegación mediante diferentes rutas y plantillas HTML renderizadas en el servidor con Flask y Jinja2.

1. **Listado de Pokémon (`pkmList.html`):** muestra las diferentes evoluciones de Eevee y permite al usuario acceder a la información individual de cada Pokémon.

2. **Detalle del Pokémon (`pkmData.html`):** presenta la información del Pokémon seleccionado, incluyendo sus estadísticas, características y movimientos disponibles. Desde esta vista se puede iniciar el flujo de preparación de una batalla.

3. **Registro del entrenador:** la aplicación solicita un nombre al usuario y lo guarda en la sesión para mantenerlo disponible durante la navegación, evitando tener que introducirlo de nuevo en cada petición.

4. **Preparación de la batalla:** se establece el Pokémon atacante seleccionado (`pkmSel`), se genera un Pokémon defensor aleatorio (`pkmRand`) y se seleccionan cuatro movimientos para el atacante (`pkmAtqMoves`).

5. **Vista de batalla (`battle.html`):** muestra los datos de los Pokémon seleccionados y los movimientos preparados para el combate. La aplicación utiliza una redirección a la ruta `/battle` para centralizar la carga de esta vista y recuperar los datos necesarios.

6. **Plantilla base (`base.html`):** proporciona la estructura común de las páginas, permitiendo reutilizar elementos compartidos y mantener una presentación coherente en toda la aplicación.

## Uso de la sesión de Flask

La aplicación utiliza `session` para conservar información entre diferentes peticiones HTTP. Esto es necesario porque, por defecto, cada petición es independiente y Flask no mantiene automáticamente las variables de una petición anterior.

Se guarda la siguiente información:

- **Nombre del entrenador:** permite conservar la identidad elegida por el usuario durante la navegación y mostrarla en las vistas que lo necesiten.
- **Pokémon atacante (`pkmAtq`):** almacena la información del Pokémon seleccionado para combatir.
- **Pokémon defensor (`pkmDef`):** conserva el Pokémon generado aleatoriamente para enfrentarse al atacante.
- **Movimientos del atacante (`pkmAtqMoves`):** mantiene los cuatro movimientos seleccionados para utilizarlos en la vista de batalla.

Estos datos permiten redirigir al usuario a `/battle` sin tener que pasar toda la información mediante parámetros en la URL ni perder los datos preparados durante la petición anterior.

## Estructura

```text
proyecto_pkm_web/
├── app/
│   ├── ...
│   ├── templates/
│   │   ├── base.html
│   │   ├── pkmList.html
│   │   └── pkmData.html
│   └── static/
│       ├── css/
│       ├── scss/
│       └── ...
├── data/
│   └── ...
├── .gitignore
└── README.md
```

## Instalación

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto_pkm_web
```

Crea y activa un entorno virtual:

```bash
python -m venv venv
```

Activar:

```bash
venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta la aplicación:

```bash
py app/main.py
```

Después, abre:

```text
http://127.0.0.1:5000
```
