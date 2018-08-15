def city_country(city, country):
    return city + ", " + country

def make_album(artist_name, album_title, no_of_tracks = ''):
    artist_album = {'name' : artist_name, 'title' : album_title}
    if no_of_tracks:
        artist_album['no_tracks'] = no_of_tracks

    return artist_album

while True:
    print ("\nPlease enter album details")
    print ("Make sure to type 'q' to quit from the program")
    ar_name = input("Enter artist's name: ")
    al_title = input("Enter album's title: ")
    notracks = input("'OPTIONAL**' Enter no of tracks in the album")

    #Quit the program when q is pressed
    if ar_name == 'q':
        break
    if al_title == 'q':
        break
    if notracks == 'q':
        break

    
    new_album = make_album(ar_name, al_title, no_of_tracks = notracks)
    print(new_album)