package com.ejemplo.tareas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Gestiona una colección en memoria de objetos {@link Tarea}.
 *
 * <p>Permite añadir tareas, buscarlas por identificador y consultar
 * cuáles siguen pendientes.</p>
 *
 * @author Profesor
 * @version 1.0
 * @since 1.0
 */
public class GestorTareas {

    private final List<Tarea> tareas = new ArrayList<>();

    /**
     * Añade una tarea al gestor.
     *
     * @param tarea tarea que se desea añadir
     * @throws IllegalArgumentException si {@code tarea} es {@code null}
     * @throws IllegalArgumentException si ya existe otra tarea con el mismo identificador
     */
    public void agregar(Tarea tarea) {
        if (tarea == null) {
            throw new IllegalArgumentException("La tarea no puede ser null");
        }
        if (buscarPorId(tarea.getId()) != null) {
            throw new IllegalArgumentException("Ya existe una tarea con ese id");
        }
        tareas.add(tarea);
    }

    /**
     * Busca una tarea por su identificador.
     *
     * @param id identificador buscado
     * @return tarea encontrada o {@code null} si no existe
     * @see Tarea#getId()
     */
    public Tarea buscarPorId(int id) {
        for (Tarea tarea : tareas) {
            if (tarea.getId() == id) {
                return tarea;
            }
        }
        return null;
    }

    /**
     * Devuelve una vista de todas las tareas.
     *
     * @return lista no modificable con todas las tareas
     */
    public List<Tarea> listar() {
        return Collections.unmodifiableList(tareas);
    }

    /**
     * Obtiene las tareas que todavía no están completadas.
     *
     * @return nueva lista que contiene únicamente tareas pendientes
     */
    public List<Tarea> listarPendientes() {
        List<Tarea> pendientes = new ArrayList<>();
        for (Tarea tarea : tareas) {
            if (!tarea.isCompletada()) {
                pendientes.add(tarea);
            }
        }
        return pendientes;
    }

    /**
     * Devuelve el número total de tareas almacenadas.
     *
     * @return número de tareas
     */
    public int total() {
        return tareas.size();
    }
}
