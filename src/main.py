import brawlstats

API_KEY = 'tu_clave_de_api'  # Reemplaza esto con tu clave API
client = brawlstats.Client(API_KEY)

# Obtener información de un jugador
player_tag = 'YOUR_PLAYER_TAG'  # Reemplaza esto con el tag del jugador sin el #
player = client.get_player(player_tag)

print(player.name)
print(player.trophies)
print(player.club.name if player.club else "No Club")
