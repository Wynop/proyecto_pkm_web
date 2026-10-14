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
