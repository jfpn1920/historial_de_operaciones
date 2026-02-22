## 👋 ¡Bienvenidos usuarios a mi proyecto! historial de operaciones

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en el desarrollo de una calculadora en Python que registra un historial de todas las operaciones matemáticas realizadas por el usuario. Cada operación ejecutada se almacena en un diccionario, permitiendo llevar un control organizado y numerado de los cálculos efectuados durante la sesión.

El sistema permite realizar operaciones básicas como suma, resta, multiplicación y división. Cada resultado se guarda junto con la expresión completa de la operación (por ejemplo: `5 + 3 = 8`), lo que facilita la consulta posterior del historial.

El programa funciona mediante un menú interactivo en consola que permite realizar múltiples operaciones sin reiniciar el sistema, mostrando el historial acumulado en cualquier momento. Esta estructura facilita una experiencia continua y dinámica para el usuario, ya que puede alternar entre realizar nuevos cálculos y consultar registros anteriores de manera sencilla.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar diccionarios para almacenar el historial de operaciones.
- Aplicar funciones para organizar cada operación matemática.
- Utilizar bucles para crear un menú interactivo continuo.
- Validar datos ingresados por el usuario.
- Manejar errores como la división por cero.
- Simular el funcionamiento de una calculadora con registro histórico.

#
### 🧠 Temas que se a aplicado
- Diccionarios
- Funciones
- Listas conceptuales de registro
- Condicionales (`if`, `elif`, `else`)
- Bucles `while`
- Bucles `for`
- Manejo de excepciones (`try` / `except`)
- Operaciones matemáticas
- Uso de variables globales

#
### ⚙️ Funcionamiento
1. El usuario selecciona una operación desde el menú principal:
   - Sumar
   - Restar
   - Multiplicar
   - Dividir
   - Mostrar historial
   - Salir

2. El sistema solicita dos números y realiza el cálculo correspondiente.

3. Cada operación se almacena en un diccionario:
   - La clave representa el número consecutivo de la operación.
   - El valor almacena la descripción completa del cálculo realizado.

4. Si ocurre un error (por ejemplo, división por cero o ingreso de datos no numéricos), el sistema muestra un mensaje de advertencia.

5. El programa se ejecuta de forma continua hasta que el usuario decide salir.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```