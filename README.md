# Minerva
### Información
Minerva pretende ser un sistema anti-spam de eventos del tipo bot-following o "botting".
El sistema colecciona los ultimos seguidores y los deja en una cola de espera a que el streamer o un moderador los acepte, de esta manera se asegura que no sean falsos, ni sobrecargar la lista de eventos de alertas saturando con animaciones innecesarias, pudiendo así, agrupar en cantidades predefinidas a los usuarios para su bienvenida.

> Minerva aims to be an anti-spam system for bot-following or "botting" events.
> The system collects the latest followers and leaves them in a waiting queue for the streamer or a moderator to accept them, in this way it ensures that they are not false, nor overload the list of alert events saturating with unnecessary animations, thus being able to, group users in predefined numbers for your welcome.


Deben tener cuidado quienes utilicen esta herramienta de tener actualizada la lista de admisión para evitar dejar caer a un usuario junto con las cuentas falsas.
> Those who use this tool should be careful to keep the admission list updated to avoid dropping a user along with fake accounts.

### Instalación

Utiliza librerias nativas y "requests" para peticiones GET y POST, e importa un archivo donde se definen los datos de acceso a la api de Twitch.
> It uses native libraries and "requests" for GET and POST requests, and imports a file where the access data to the Twitch api are defined.


Instalación del requisito:
```
pip install requests
```

### Pending tasks
- [x] Use the twitch api to get a list of followers.
- [ ] Configure mysqli to only check new followers.
- [ ] Generate mass admission interface.
- [ ] Generate automatic detection script based on time.
- [ ] Be able to use it as a proxy for streamlabs alerts
(with streamlabs api, sending the corresponding event, previously accepted).
- [ ] ¿Render interface in OBS panel?.
