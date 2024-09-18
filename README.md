# PRAC2---Arreglos-e-Infograf-a
### **Conclusiones del código**

1. **Eficiencia en el Acceso a Datos:**
   - **Forma 1 (Alumnos en Filas, Materias en Columnas):** Esta organización resultó ser más eficiente en las búsquedas cuando se incrementó el número de alumnos. Esto debido a que los datos de un mismo alumno se almacenan contiguamente en memoria, lo que facilita un acceso rápido y eficiente. Las búsquedas por alumno en esta estructura demostraron ser más rápidas y consistentes, especialmente en matrices grandes.
   - **Forma 2 (Materias en Filas, Alumnos en Columnas):** Esta forma fue menos eficiente en comparación con la forma 1. La búsqueda de datos en esta estructura implicó un mayor número de accesos dispersos a través de la memoria, lo que incrementó el tiempo de búsqueda. Esto debido a que los datos de un mismo alumno están distribuidos a lo largo de varias filas, lo que no aprovecha la localidad de referencia de la memoria tan eficazmente.

2. **Impacto del Tamaño de Datos:**
   - El rendimiento de las búsquedas en ambas estructuras se vio afectado por el aumento en el tamaño de los datos (número de alumnos y materias). El tiempo de búsqueda aumentó con el tamaño de las matrices, pero la forma 1 mostró un incremento menos pronunciado en el tiempo de búsqueda comparado con la forma 2.

3. **Localidad de Memoria:**
   - La localidad de referencia en la forma 1, donde los datos relacionados se almacenan en ubicaciones contiguas en memoria, resulta en un acceso más rápido. La forma 2, al dispersar los datos de un alumno a través de diferentes filas, no aprovecha tan bien esta característica de la memoria, lo que ralentiza el acceso a los datos.

4. **Recomendaciones para Estructuración de Datos:**
   - Si el principal objetivo es realizar búsquedas rápidas basadas en los alumnos, la forma 1 (alumnos en filas, materias en columnas) es preferible. Esta estructura resulta más eficiente para operaciones que se centran en consultar las calificaciones de un alumno específico en múltiples materias.
   - Si el enfoque fuera diferente, como realizar búsquedas frecuentes sobre materias, podría ser útil considerar la forma 2. Sin embargo, para el caso específico de la actividad, la forma 1 demostró ser más efectiva.

5. **Relevancia en Diferentes Escenarios:**
   - La elección de la estructura de datos adecuada debe basarse en el tipo de consultas que se realizarán con mayor frecuencia. Para consultas centradas en un alumno o un conjunto de alumnos, la forma 1 es más adecuada. Para consultas centradas en materias o un conjunto de materias, la forma 2 podría tener ventajas en algunos contextos, aunque no se evidenció en las pruebas realizadas.
