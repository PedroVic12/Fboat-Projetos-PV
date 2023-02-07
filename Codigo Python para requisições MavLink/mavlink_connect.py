import pymavlink
from pymavlink import mavutil

# Criar uma instância de MAVLink
try:
    mav = pymavlink.mavutil.mavlink_connection('udp:localhost:14551')
except (OSError, serial.serialutil.SerialException) as e:
    print("Falha na conexão: ", e)
    mav = None

if mav is not None:
    # Enviar uma mensagem de heartbeat
    num_bytes = mav.mav.heartbeat_send(
        mavutil.mavlink.MAV_TYPE_GCS,
        mavutil.mavlink.MAV_AUTOPILOT_INVALID,
        0, 0, 0
    )

    if num_bytes == mav.mav.packet_size(mavutil.mavlink.MAVLINK_MSG_ID_HEARTBEAT):
        print("Mensagem de heartbeat enviada com êxito")
    else:
        print("Erro ao enviar mensagem de heartbeat")

    # Fechar a conexão
    mav.close()
