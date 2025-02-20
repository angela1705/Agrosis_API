import json 
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.Iot.sensores.models import Sensores
from asgiref.sync import sync_to_async

class SensoresConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Conexion WebSocket"""
        await self.channel_layer.group_add("sensores", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Desconexion WebSocket"""
        await self.channel_layer.group_discard("sensores", self.channel_name)

    async def receive(self, text_data):
        """Maneja los mensajes entrantes desde el cliente"""
        data = json.loads(text_data)

        if "fk_datos_metereologicos_id" in data:
            fk_datos_metereologicos_id = data["fk_datos_metereologicos_id"]

            # Obtener datos del sensor de la base de datos
            sensor_data = await self.get_sensor_data(fk_datos_metereologicos_id)

            if sensor_data:
                #Responder con los datos actuales del sensor 
                await self.send(text_data=json.dumps({"message": sensor_data}))

                #Tambien suscribimos al usuario a actualizaciones en tiempo real
                await self.channel_layer.group_send(
                    "sensores",
                    {
                        "type": "sensor_data",
                        "message": sensor_data
                    }
                )
            else:
                await self.send(text_data = json.dumps({"error": "Sensor no encontrado"}))
    
    async def sensor_data(self, event):
        """Envia los datos del sensor al cliente en tiempo real"""
        await self.send(text_data = json.dumps({"message": event["message"]}))

    @sync_to_async(thread_sensitive=True)
    def get_sensor_data(self, fk_datos_metereologicos_id):
        """Consulta la base de datos para obtener la información del sensor"""
        try:
            sensor = Sensores.objects.get(fk_datos_metereologicos_id=fk_datos_metereologicos_id)
            sensor_data = {
                "tipo_sensores": sensor.tipo_sensores,
                "fk_datos_metereologicos": sensor.fk_datos_metereologicos_id
            }
            print("Datos obtenidos:", sensor_data)  # Verifica si la consulta devuelve datos
            return sensor_data
        except Sensores.DoesNotExist:
            print("Error: Sensor no encontrado")
            return None
