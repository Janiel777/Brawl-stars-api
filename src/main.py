import brawlstats

API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNhYzYxMmI1LTRkYWItNGRkYy05NGRmLTViMTQ4MWMzNzJjOCIsImlhdCI6MTcxNzI3NTA2NCwic3ViIjoiZGV2ZWxvcGVyLzU3MjQzNmQ3LWVjZmEtNjE1My03ZTA2LWRkMzg0YzFlOGZhMyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzIuNTAuMS4xMTAiXSwidHlwZSI6ImNsaWVudCJ9XX0.QNf5D08YCqXomLWrnxSvfs7-REmPZcLTO_I7yRXfnelYYn_ubvQ5SbkhghjRW-tczXqakX3VUNRyJNjhyq7ggg'  # Reemplaza esto con tu clave API
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
