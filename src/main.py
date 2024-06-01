import brawlstats

API_KEY = 'tu_clave_de_api'  # Reemplaza esto con tu clave API
client = brawlstats.Client(API_KEY)

def get_player_info(player_tag):
    try:
        player = client.get_player(player_tag)
        return {
            'name': player.name,
            'trophies': player.trophies,
            'club': player.club.name if player.club else "No Club"
        }
    except brawlstats.errors.NotFoundError:
        return None
