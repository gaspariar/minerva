# Minerva
Minerva pretende ser un sistema anti-spam de eventos del tipo bot-following o "botting".
El sistema colecciona los ultimos seguidores y los deja en una cola de espera a que el streamer o un moderador los acepte, de esta manera se asegura que no sean falsos, ni sobrecargar la lista de eventos de alertas saturando con animaciones innecesarias, pudiendo así, agrupar en cantidades predefinidas a los usuarios para su bienvenida.

Deben tener cuidado quienes utilicen esta herramienta de tener actualizada la lista de admisión para evitar dejar caer a un usuario junto con las cuentas falsas.

### Instalacion

Utiliza librerias nativas y "requests" para peticiones GET y POST, e importa un archivo donde se definen los datos de acceso a la api de Twitch.

Instalación del requisito:
```
pip install requests
```

### Tareas pendientes
- [x] Utilizar la api de twitch para obtener listado de followers.
- [ ] Configurar mysqli para solo revisar a los nuevos seguidores.
- [ ] Generar interfaz de admisión en masa.
- [ ] Generar script de detección automatica en base del tiempo.
- [ ] Lograr utilizarlo como proxy de alertas de streamlabs 
(con api de streamlabs, enviando el evento correspondiente, previamente aceptado).
- [ ] ¿Renderizar interfaz en panel de OBS?.
