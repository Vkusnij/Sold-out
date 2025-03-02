best_selling_albums = [
    {
        "artist": "Michael Jackson",
        "title": "Thriller",
        "year": 1982,
        "genres": ["pop", "post-disco", "funk", "rock"],
        "sale": 70000000,
    },
    {
        "artist": "AC/DC",
        "title": "Back in Black",
        "year": 1980,
        "genres": ["hard rock"],
        "sale": 50000000,
    },
    {
        "artist": "Whitney Houston",
        "title": "The Bodyguard",
        "year": 1992,
        "genres": ["r&b", "soul", "pop", "soundtrack"],
        "sale": 45000000,
    },
    {
        "artist": "Pink Floyd",
        "title": "The Dark Side of the Moon",
        "year": 1973,
        "genres": ["progressive rock"],
        "sale": 45000000,
    },
    {
        "artist": "Eagles",
        "title": "Their Greatest Hits (1971 - 1975)",
        "year": 1976,
        "genres": ["country rock", "soft rock", "folk rock"],
        "sale": 44000000,
    },
    {
        "artist": "Eagles",
        "title": "Hotel California",
        "year": 1976,
        "genres": ["soft rock"],
        "sale": 42000000,
    },
    {
        "artist": "Shania Twain",
        "title": "Come On Over",
        "year": 1997,
        "genres": ["country", "pop"],
        "sale": 40000000,
    },
    {
        "artist": "Fleetwood Mac",
        "title": "Rumours",
        "year": 1977,
        "genres": ["soft rock"],
        "sale": 40000000,
    },
]

# Average sales

total_sale = 0

for album in best_selling_albums:
    total_sale += album["sale"]
    average_sale  = total_sale / len(best_selling_albums)
print(average_sale)

# Average age

total_age = 0
current_year = 2024

for album in best_selling_albums:
    age = current_year - album["year"]
    total_age += age
    average_age = total_age / len(best_selling_albums)
print(average_age)

# Newest and oldest albums

newest_album = best_selling_albums[0]
oldest_album = best_selling_albums[0]

for album in best_selling_albums:
    if album["year"] > newest_album["year"]:
        newest_album = album
    if album["year"] < oldest_album["year"]:
        oldest_album = album
print(newest_album)
print(oldest_album)

# The albums of Eagles

eagles_sales = 0
is_both_soft_rock = True

for album in best_selling_albums:
    if album["artist"] == "Eagles":
        eagles_sales += album["sale"]
        if "soft rock" not in album["genres"]:
            is_both_soft_rock = False
albums_of_eagles = {"sales": eagles_sales, "is_both_soft_rock": is_both_soft_rock}
print(albums_of_eagles)

#Do you like it?

for album in best_selling_albums:
    if album["artist"] == "Michael Jackson" and album["title"] == "Thriller":
        album["i_like_it"] = True
    elif album["artist"] == "Pink Floyd" and album["title"] == "The Dark Side of the Moon":
        album["i_like_it"] = True
    else:
        album["i_like_it"] = False

for album in best_selling_albums:
    print(f"Artist: {album['artist']}")
    print(f"title: {album['title']}")
    print(f"year: {album['year']}")
    print(f"genres: {', '.join(album['genres'])}")
    print(f"sale: {album['sale']}")
    print(f"I like it: {album['i_like_it']}")
    print("-" * 40)