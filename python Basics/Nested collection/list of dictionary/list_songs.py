songs = [
    {"id": 1, "title": "Mayajalam", "spotify_listen_count": 12000, "yt_music": 15000, "downloads": 5000},
    {"id": 2, "title": "vellaram tharam", "spotify_listen_count": 850000, "yt_music": 1200000, "downloads": 45000},
    {"id": 3, "title": "muthuchippi", "spotify_listen_count": 45000, "yt_music": 32000, "downloads": 1200},
    {"id": 4, "title": "Velvet Sky", "spotify_listen_count": 1200400, "yt_music": 980000, "downloads": 150000},
    {"id": 5, "title": "Echoes of You", "spotify_listen_count": 3100, "yt_music": 4500, "downloads": 200},
    {"id": 6, "title": "Rush Hour", "spotify_listen_count": 560000, "yt_music": 610000, "downloads": 88000},
    {"id": 7, "title": "kanmani anpode", "spotify_listen_count": 150000, "yt_music": 145000, "downloads": 12000}
]

# all tittles
all_titles={di.get("title")for di in songs}
print(all_titles)


# all downloads
all_downloads={di.get("downloads") for di in songs}
print(all_downloads)

# which song has most downloads

most_dwlnd_songs={di.get("downloads") for di in songs if di.get("downloads")==max(all_downloads)}
print(most_dwlnd_songs)
top_downloads=max(all_downloads)
top_dwnld_song={di.get("title") for di in songs if di.get("downloads")==top_downloads}
print(top_dwnld_song)


# top youtube  listen music
max_yt_music=max({di.get("yt_music")  for di in songs})
most_listen_yt_music={di.get("title") for di in songs if di.get("yt_music")==max_yt_music}
print(most_listen_yt_music)