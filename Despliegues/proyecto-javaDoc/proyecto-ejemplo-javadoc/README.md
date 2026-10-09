# Gestor de tareas — Proyecto de ejemplo

Aplicación Java sencilla utilizada para mostrar la relación entre **README.md** y **Javadoc**.

El README explica el proyecto de forma global. Los comentarios Javadoc incluidos en el código documentan las clases, constructores y métodos.

## Funcionalidades

- Crear tareas.
- Modificar su título.
- Marcar tareas como completadas.
- Reabrir tareas.
- Buscar una tarea por identificador.
- Listar todas las tareas.
- Listar únicamente las pendientes.

## Requisitos

- JDK 21 o compatible.

Comprueba la instalación:

```bash
java --version
javac --version
javadoc --version
```

## Estructura

```text
proyecto-ejemplo-javadoc/
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
javac -d out src/com/ejemplo/tareas/*.java
```

## Ejecución

```bash
java -cp out com.ejemplo.tareas.Main
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

## Idea principal

El README responde a preguntas sobre **el proyecto**.

Javadoc responde a preguntas sobre **cómo utilizar sus componentes Java**.
