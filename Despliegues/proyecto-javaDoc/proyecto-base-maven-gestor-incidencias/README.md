# Gestor de tareas — Proyecto de ejemplo

Aplicación Java sencilla utilizada para mostrar la relación entre **README.md** y **Javadoc**.

El README explica el proyecto de forma global. Los comentarios Javadoc incluidos en el código documentan las clases, constructores y métodos.

## Funcionalidades

- Mostrar todas las incidencias.
- Mostrar las incidencias abiertas.
- Buscar incidencias.
- Consultar una incidencia por su ID.

## Requisitos

- JDK 27 o compatible.

Comprueba la instalación:

```bash
java --version
javac --version
javadoc --version
```

## Estructura

```text
proyecto-base-maven-gestor-incidencias/
├── README.md
├── src/
│   └── com/
│       └── ejemplo/
│           └── tareas/
│               ├── Tarea.java
│               ├── GestorTareas.java
│               └── Main.java
└── docs/
```

## Compilación

Desde la raíz:

```bash
.\mvnw.cmd clean compile exec:java
```


## Generar Javadoc

```bash
javadoc -d docs/javadoc -sourcepath src -subpackages com.ejemplo.tareas -author -version
```

Abre después:

```text
docs/javadoc/index.html
```

## Qué debes observar

Busca en la documentación generada ejemplos de:

- `@author`;
- `@version`;
- `@param`;
- `@return`;
- `@throws`;
- `@since`;
- `@deprecated`;
- `@see`;
- `{@code}`;
- `{@link}`.

Comprueba también cómo Javadoc representa el método marcado con `@Deprecated`.
