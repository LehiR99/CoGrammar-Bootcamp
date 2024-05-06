# Create Album with 3 class variables
class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist


    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# Create albums1 list
albums1 = [
    Album("Hats", 7, "The Blue Nile"),
    Album("Silent Alarm", 13, "Bloc Party"),
    Album("Saves The World", 12, "MUNA"),
    Album("Brent ii", 5, "Jeremy Zucker"),
    Album("Malibu Nights", 9, "LANY")
]

# Print albums1 list
print("Albums1:")
for album in albums1:
    print(album)

# Sort albums1 by the number_of_songs
albums1.sort(key=lambda x: x.number_of_songs)

print("\nSorted albums1 list by number of songs")
for album in albums1:
    print(album)

# Swapped position of albums 1 and 2
albums1[1], albums1[2] = albums1[2], albums1[1]

# Print albums1 after swapping
print("\nAlbums1 after swapping elements at positions 1 and 2:")
for album in albums1:
    print(album)

# Create albums2 list
albums2 = []

# Add 5 albums to album2 list
albums2.extend([
    Album("Nurture", 14, "Porter Robinson"),
    Album("Room For Squares", 13, "John Mayer"),
    Album("A Brief Inquiry Into Online Relationships", 15, "The 1975"),
    Album("Kids", 9, "The Midnight"),
    Album("Take the Sadness Out of Saturday Night", 10, "Bleachers")
])

print("\nAlbums2:")
for album in albums2:
    print(album)

# Copy all albums from albums1 to albums2
albums2.extend(albums1)

# Add new albums to albums2
albums2.extend([
    Album("Dark Side of the Moon", 9, "Pink Floyd"),
    Album("Oops!... I Did It Again", 16, "Britney Spears")
])

# Sort albums2 alphabetically by album name
albums2.sort(key=lambda x: x.album_name)

# Print sorted albums2
print("\nSorted albums2 alphabetically by album name:")
for album in albums2:
    print(album)

# Search for "Dark Side of the Moon" in albums2
for i, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(f"\nIndex of 'Dark Side of the Moon' in albums2: {i}")
        break