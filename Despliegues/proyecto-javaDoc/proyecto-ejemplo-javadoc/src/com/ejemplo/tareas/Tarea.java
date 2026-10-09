package com.ejemplo.tareas;

/**
 * Representa una tarea que puede estar pendiente o completada.
 *
 * <p>Cada tarea tiene un identificador positivo, un título y un estado.
 * Una tarea recién creada comienza siempre como pendiente.</p>
 *
 * @author Profesor
 * @version 1.0
 * @since 1.0
 */
public class Tarea {

    private final int id;
    private String titulo;
    private boolean completada;

    /**
     * Crea una tarea pendiente.
     *
     * @param id identificador positivo y único de la tarea
     * @param titulo título descriptivo de la tarea
     * @throws IllegalArgumentException si {@code id <= 0}
     * @throws IllegalArgumentException si el título es {@code null} o está vacío
     */
    public Tarea(int id, String titulo) {
        if (id <= 0) {
            throw new IllegalArgumentException("El identificador debe ser positivo");
        }
        validarTitulo(titulo);
        this.id = id;
        this.titulo = titulo;
        this.completada = false;
    }

    /**
     * Devuelve el identificador de la tarea.
     *
     * @return identificador de la tarea
     */
    public int getId() {
        return id;
    }

    /**
     * Devuelve el título actual.
     *
     * @return título de la tarea
     */
    public String getTitulo() {
        return titulo;
    }

    /**
     * Modifica el título.
     *
     * @param titulo nuevo título
     * @throws IllegalArgumentException si el título es {@code null} o está vacío
     */
    public void setTitulo(String titulo) {
        validarTitulo(titulo);
        this.titulo = titulo;
    }

    /**
     * Indica si la tarea está completada.
     *
     * @return {@code true} si la tarea está completada; {@code false} en caso contrario
     */
    public boolean isCompletada() {
        return completada;
    }

    /**
     * Marca la tarea como completada.
     *
     * @see #reabrir()
     */
    public void completar() {
        completada = true;
    }

    /**
     * Vuelve a marcar la tarea como pendiente.
     *
     * @see #completar()
     * @since 1.1
     */
    public void reabrir() {
        completada = false;
    }

    /**
     * Cambia directamente el estado de la tarea.
     *
     * @param completada nuevo estado
     * @deprecated utilizar {@link #completar()} o {@link #reabrir()}.
     */
    @Deprecated
    public void setCompletada(boolean completada) {
        this.completada = completada;
    }

    private static void validarTitulo(String titulo) {
        if (titulo == null || titulo.isBlank()) {
            throw new IllegalArgumentException("El título no puede estar vacío");
        }
    }

    /**
     * Devuelve una representación textual de la tarea.
     *
     * @return texto con identificador, título y estado
     */
    @Override
    public String toString() {
        return id + " - " + titulo + (completada ? " [OK]" : " [PENDIENTE]");
    }
}
