from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

IP = '127.0.0.1'
PORT = 7000

# UDPのクライアントを作る
client = udp_client.UDPClient(IP, PORT)

# TouchDesignerにOSCでテキストを送信
msg = OscMessageBuilder(address='/mytext')
msg.add_arg("テストです")
m = msg.build()

client.send(m)