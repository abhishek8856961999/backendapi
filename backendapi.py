def handle_connect(sid, environ):
    logger.info(f"Socket connected with sid {sid}")

class SocketManager:
    def __init__(self, origins: List[str]):
        self.server = socketio.AsyncServer(
            cors_allowed_origins=origins,
            async_mode="asgi",
            logger=True,
            engineio_logger=True,
        )
        self.app = socketio.ASGIApp(self.server)

    @property
    def on(self):
        return self.server.on

    @property
    def send(self):
        return self.server.send

    def mount_to(self, path: str, app: ASGIApp):
        app.mount(path, self.app)


socket_manager = SocketManager(settings.origins)
socket_manager.on("connect", handler=handle_connect)


import { io } from "socket.io-client"; const socket = io("ws://localhost:8000", {{ path: "/ws/socket.io/", transports: ['websocket', 'polling'] }}); socket.on("connect", () => { console.log("Connected", socket.id) }); socket.on("response", () => { console.log("Response", socket.id) }); socket.on("message", data => { console.log(data) });

