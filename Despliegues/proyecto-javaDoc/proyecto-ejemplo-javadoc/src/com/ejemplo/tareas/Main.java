package com.ejemplo.tareas;

/**
 * Punto de entrada de la aplicación de ejemplo.
 *
 * @author Profesor
 * @version 1.0
 */
public class Main {

    /**
     * Crea varias tareas y muestra un ejemplo de uso del gestor.
     *
     * @param args argumentos de línea de comandos; no se utilizan
     */
    public static void main(String[] args) {
        GestorTareas gestor = new GestorTareas();

        Tarea estudiar = new Tarea(1, "Repasar Markdown");
        Tarea documentar = new Tarea(2, "Generar Javadoc");

        gestor.agregar(estudiar);
        gestor.agregar(documentar);

        estudiar.completar();

        System.out.println("Todas las tareas:");
        gestor.listar().forEach(System.out::println);

        System.out.println("\nPendientes:");
        gestor.listarPendientes().forEach(System.out::println);
    }
}
