# PKM-BATTLE

Pequeña Pokédex web centrada en las diferentes evoluciones de **Eevee**, desarrollada como proyecto de aprendizaje con **Python, Flask, HTML, SCSS y Jinja**.

## 🛠️ Tecnologías

* 🐍 Python
* 🌶️ Flask
* 🧩 Jinja2
* 🌐 HTML5
* 🎨 SCSS
* 📦 JSON

## 📖 Funcionalidades

* Listado de las diferentes Eeveelutions.
* Página individual para cada Pokémon.
* Información sobre estadísticas y características.
* Listado de movimientos.
* Colores personalizados según el tipo de Pokémon.
* Diseño responsive.

## 📁 Estructura

```text
EeveeDex/
├── app.py
├── data/
│   └── pokemon.json
├── templates/
│   ├── base.html
│   ├── pkmList.html
│   └── pkmData.html
└── static/
    ├── css/
    ├── img/
    └── ...
```

## 🚀 Instalación

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd EeveeDex
```

Crea y activa un entorno virtual:

```bash
python -m venv venv
```

En Windows:

```bash
venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install flask
```

Ejecuta la aplicación:

```bash
flask --app app run
```

Después, abre:

```text
http://127.0.0.1:5000
```

## 📌 Objetivo

Proyecto realizado con fines educativos para practicar el desarrollo de aplicaciones web con **Flask**, el uso de **plantillas Jinja** y la gestión de datos mediante archivos **JSON**.
