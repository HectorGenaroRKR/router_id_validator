# Router ID Validator 🌐

El programa procesa direcciones IP, aplica reglas de negocio estrictas y genera nomenclaturas dinámicas para dispositivos de red, sirviendo para flujos de automatización e IaC.

## 🚀 Características Principales

* **Validación de Topología:** Asegura que la dirección IP cumpla con el estándar IPv4 y pertenezca exclusivamente a la red privada 10.x.x.x.
* **Control Geográfico:** Valida que el segundo y tercer octeto correspondan a uno de los 32 estados de México, respetando el límite máximo de sucursales configurado por cada región geográfica.
* **Identificación de Hardware:** Clasifica el dispositivo (Router, Switch L3, Switch L2) basándose en los rangos de host reservados dentro del cuarto octeto.
* **Generación Dinámica de Hostnames:** Construye automáticamente nombres de equipo estandarizados (ej. `MEX-SUC06-SWC08`).

## 🛠️ Arquitectura del Sistema

El proyecto está diseñado siguiendo el Principio de Responsabilidad Única (SRP), separando la lógica en módulos independientes:

* **Fase de Procesamiento (`split_ip`):** Transformación de cadenas de texto a listas numéricas.
* **Orquestador Central (`octets_validator`):** Evalúa la IP contra las restricciones lógicas y de negocio de la corporación.
* **Capa de Metadatos:** Funciones aisladas (`state_identifier`, `branch_identifier`, `host_identifier`) encargadas de extraer y formatear la información específica.