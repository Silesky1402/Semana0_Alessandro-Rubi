# Semana0_Alessandro-Rubi

## Tecnologías Utilizadas

### **1. FastAPI**
- Es un framework web en Python para construir APIs rápidas, modernas y escalables.
- Generación automática de documentación interactiva (Swagger UI).
  
### **2. Ollama**
- Plataforma de modelos de lenguaje grandes que permite consultas avanzadas utilizando IA.

### **3. dotenv**
- Utilizado para cargar variables de entorno desde un archivo `.env`.
- Ayuda a la configuración de modelos y claves sin incluirlas directamente en el código.

### **4. JSONResponse**
- Clase de FastAPI utilizada para retornar respuestas en formato JSON al cliente.


## Instalación y Configuración

### **Requisitos**
- Python 3.9 o superior.
- `pip` instalado para la gestión de dependencias.

### **Ejecución**
# Guía de Uso del Servidor y Postman

## Activación del Servidor
1. Ejecuta en la terminal el siguiente comando para activar el servidor:
   ```bash
   uvicorn main:app --reload
2. En postman ingresa la dirección:
    ```bash
    http://127.0.0.1:8000/resolver
3.En el Body, selecciona la opción raw y asegúrate de que el formato esté en JSON e ingresa el header:
    ```bash
        
    Content-Type: application/json

4.Realiza la pregunta en el formato correcto.

     

## Respuestas Clave

## ¿Qué es Ollama?
Ollama es una herramienta que permite usar modelos de inteligencia artificial avanzados directamente en tu computadora, sin depender de internet o servicios externos. Todo funciona localmente, lo que significa:
- **Privacidad**: No necesitas enviar datos a la nube.
- **Velocidad**: Mayor rapidez en el procesamiento de datos.
- **Personalización**: Ideal para desarrolladores o cualquier persona que quiera experimentar con IA adaptada a sus necesidades.

Es como tener un asistente virtual avanzado que trabaja exclusivamente para ti.

---

## ¿Qué es FastAPI?
FastAPI es una herramienta que facilita la creación de APIs (intermediarios entre diferentes sistemas). Por ejemplo:
- **Conexión**: Simplifica el vínculo entre clientes y servidores.
- **Eficiencia**: Manejo rápido y optimizado de solicitudes.

---

## ¿Qué es el modelo DeepSeek-R1?
DeepSeek-R1 es un modelo de inteligencia artificial diseñado para trabajar con tareas complejas como:
- Resolver problemas matemáticos.
- Generar código de programación.
- Analizar textos.

Es ideal para aquellos que necesitan precisión y razonamiento lógico en programación, investigación o proyectos técnicos.

---

## Uso de peticiones con stream=True
`stream=True` se utiliza en peticiones HTTP para manejar respuestas que llegan en fragmentos en lugar de recibir toda la información de golpe. Esto es útil para:
- **Datos grandes**: Procesarlos de forma controlada.
- **Respuestas en tiempo real**: Mayor eficiencia y flexibilidad.

---

## Cómo garantizar la escalabilidad de una API que consume modelos de IA pesados
Para que una API pueda manejar muchos usuarios sin fallar, se requieren estrategias de optimización. Por ejemplo:
- **Infraestructura en la nube**: Añadir más espacio para manejar la carga.
- **Balanceadores de carga**: Organizar solicitudes eficientemente.
- **Optimización**: Usar versiones más ligeras de los modelos o guardar resultados en caché.

---

## Parámetros que afectan rendimiento/calidad de respuestas en Ollama
1. **num_ctx**: Define la "memoria" del modelo. Valores altos permiten manejar conversaciones largas pero consumen más recursos.
2. **temperature**: Controla la creatividad en las respuestas. Valores bajos (ej. 0.2) son más precisos, valores altos (ej. 0.8) son más creativos.
3. **top_p** y **top_k**: Afectan la precisión y creatividad del modelo.
4. **repeat_penalty**: Evita repeticiones innecesarias para mejorar la fluidez.
5. **Ventana de contexto**: Influye en cómo el modelo maneja información extensa.

---

## Estrategias para Balancear Carga entre Múltiples Instancias de Ollama
1. **Distribución de solicitudes**: Usar un balanceador de carga para enviar solicitudes a la instancia correcta.
2. **Escalado horizontal**: Añadir más instancias según la demanda.
3. **Cacheo**: Guardar respuestas repetidas para evitar esfuerzos innecesarios.
4. **Tareas específicas**: Asignar tipos de solicitudes a distintas instancias.
5. **Streaming**: Procesar respuestas largas en fragmentos.
6. **Monitoreo**: Supervisar el volumen de trabajo en cada instancia.
7. **Límites de uso**: Establecer restricciones para evitar abusos del sistema.

---

## Patrones de Diseño Útiles para Integrar IA en Backend
1. **Singleton**: Garantiza una única instancia del modelo para optimizar recursos.
2. **CQRS**: Separa operaciones de lectura y escritura para mayor eficiencia.
3. **Factory**: Crea instancias según el tipo de tarea (por ejemplo, imágenes o texto).
4. **Decorator**: Añade funcionalidades extra como medición de tiempos o caché.
5. **Observer**: Notifica a otros sistemas tras procesar consultas.
6. **Strategy**: Permite usar diferentes formas de preprocesar datos según la tarea.

### Ejemplo Practico de Integración
Supongamos que tienes una API que usa un modelo de IA para responder preguntas y entrenar modelos:
- **Singleton**: El modelo se carga solo una vez al iniciar el servidor.
- **CQRS**: Se separan las rutas para consultas y entrenamiento.
- **Factory**: Escoge el modelo según el tipo de solicitud.
- **Decorator**: Mide tiempos y guarda estadísticas de ejecución.
- **Observer**: Registra el uso del modelo en sistemas externos.

---
