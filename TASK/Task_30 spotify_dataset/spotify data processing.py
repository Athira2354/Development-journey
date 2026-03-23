from csv import DictReader


class Track:
    def __init__(self, track_name, artist, popularity):
        fr="TASK\\Task_30 spotify_dataset\\spotify-tracks-dataset.csv"
        self.track_name = track_name
        self.artist = artist
        self.popularity = popularity

    def display_info(self):
        print(self.track_name, "-", self.artist, "| Popularity:", self.popularity)


#
class TrackDuration:
    def __init__(self, track_name, duration_ms):
        self.track_name = track_name
        self.duration_ms = duration_ms

    def convert_to_minutes(self):
        minutes = self.duration_ms / 60000
        print(self.track_name, "Duration:", round(minutes, 2), "minutes")


# 3. Popularity Check
class TrackPopularity:
    def __init__(self, track_name, popularity):
        self.track_name = track_name
        self.popularity = popularity

    def check_popularity(self):
        if self.popularity > 80:
            print(self.track_name, ": High Popularity")
        elif 50 <= self.popularity <= 80:
            print(self.track_name, ": Medium Popularity")
        else:
            print(self.track_name, ": Low Popularity")



class Genre:
    def __init__(self, track_name, track_genre):
        self.track_name = track_name
        self.track_genre = track_genre

    def show_genre(self):
        print(self.track_name, "Genre:", self.track_genre)


class EnergyLevel:
    def __init__(self, track_name, energy):
        self.track_name = track_name
        self.energy = energy

    def check_energy(self):
        if self.energy > 0.7:
            print(self.track_name, ": High Energy Song")
        elif self.energy > 0.4:
            print(self.track_name, ": Medium Energy Song")
        else:
            print(self.track_name, ": Low Energy Song")



class DanceTrack:
    def __init__(self, track_name, danceability):
        self.track_name = track_name
        self.danceability = danceability

    def is_danceable(self):
        if self.danceability > 0.7:
            print(self.track_name, "is good for dancing")
        else:
            print(self.track_name, "is not good for dancing")



class TempoAnalyzer:
    def __init__(self, track_name, tempo):
        self.track_name = track_name
        self.tempo = tempo

    def classify_tempo(self):
        if self.tempo < 80:
            print(self.track_name, ": Slow")
        elif self.tempo <= 120:
            print(self.track_name, ": Medium")
        else:
            print(self.track_name, ": Fast")



class TrackSafety:
    def __init__(self, track_name, explicit):
        self.track_name = track_name
        self.explicit = explicit

    def check_content(self):
        if self.explicit:
            print(self.track_name, ": Explicit")
        else:
            print(self.track_name, ": Clean")



class Artist:
    def __init__(self, artist_name, track_name):
        self.artist_name = artist_name
        self.track_name = track_name

    def show_info(self):
        print("Artist:", self.artist_name, "| Track:", self.track_name)



class LoudnessCheck:
    def __init__(self, track_name, loudness):
        self.track_name = track_name
        self.loudness = loudness

    def classify_loudness(self):
        if self.loudness > -5:
            print(self.track_name, ": Loud")
        elif self.loudness > -15:
            print(self.track_name, ": Medium")
        else:
            print(self.track_name, ": Soft")


class AcousticTrack:
    def __init__(self, track_name, acousticness):
        self.track_name = track_name
        self.acousticness = acousticness

    def check_acoustic(self):
        if self.acousticness > 0.5:
            print(self.track_name, ": Acoustic")
        else:
            print(self.track_name, ": Non-Acoustic")


class InstrumentalTrack:
    def __init__(self, track_name, instrumentalness):
        self.track_name = track_name
        self.instrumentalness = instrumentalness

    def check_instrumental(self):
        if self.instrumentalness > 0.5:
            print(self.track_name, ": Instrumental")
        else:
            print(self.track_name, ": Has Vocals")


class MoodDetector:
    def __init__(self, track_name, valence):
        self.track_name = track_name
        self.valence = valence

    def detect_mood(self):
        if self.valence > 0.6:
            print(self.track_name, ": Happy")
        elif self.valence > 0.3:
            print(self.track_name, ": Neutral")
        else:
            print(self.track_name, ": Sad")


class TrackSummary:
    def __init__(self, track_name, artist, genre, popularity):
        self.track_name = track_name
        self.artist = artist
        self.genre = genre
        self.popularity = popularity

    def summary(self):
        print(f"{self.track_name} by {self.artist} | Genre: {self.genre} | Popularity: {self.popularity}")



class Playlist:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def display_tracks(self):
        for track in self.tracks:
            track.display_info()

    def count_tracks(self):
        print("Total Tracks:", len(self.tracks))


t1 = Track("Blinding Lights", "The Weeknd", 95)
t2 = Track("Shape of You", "Ed Sheeran", 92)

playlist = Playlist()
playlist.add_track(t1)
playlist.add_track(t2)

playlist.display_tracks()
playlist.count_tracks()