class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    
    songs = [
        ("99 Problems", "Jay Z", "Rap"),
        ("Halo", "Beyonce", "Pop"),
        ("Smells Like Teen Spirit", "Nirvana", "Rock")
    ]
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.count += 1
        
        self.genres.add(genre)
        self.artists.add(artist)
        
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
            
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
            
    