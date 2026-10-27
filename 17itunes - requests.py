# https://itunes.apple.com/search?entity=song&limit=1&term=weezer
import json # this comes manually with python
import requests
import sys

if len(sys.argv) != 2:
    sys.exit() # if i omit the () then i am telling python - show me the method called exit that belongs to the sys object
    # when adding the brackets i'm saying - execute the method and give me the result
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# we want to get track name
o = response.json()
for result in o["results"]:
    print(result["trackName"])
"""
# print(json.dumps(response.json(),indent = 2)) # python has converted it a python dictionary, which looks similar but not the same
{
  "resultCount": 1,
  "results": [ # this is a list
    { # a dictionary within a list
      "wrapperType": "track",
      "kind": "song",
      "artistId": 115234,
      "collectionId": 1440868131,
      "trackId": 1440868258,
      "artistName": "Weezer",
      "collectionName": "Weezer (Green Album)",
      "trackName": "Island In the Sun",
      "collectionCensoredName": "Weezer (Green Album)",
      "trackCensoredName": "Island In the Sun",
      "artistViewUrl": "https://music.apple.com/us/artist/weezer/115234?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/island-in-the-sun/1440868131?i=1440868258&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/island-in-the-sun/1440868131?i=1440868258&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/52/a6/03/52a6032e-39c0-fd3e-555d-ce683f3d9d31/mzaf_7707796819108024384.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/fc/ef/19/fcef196c-3f81-e9da-f02a-b55d900e7d69/16UMGIM53162.rgb.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/fc/ef/19/fcef196c-3f81-e9da-f02a-b55d900e7d69/16UMGIM53162.rgb.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/fc/ef/19/fcef196c-3f81-e9da-f02a-b55d900e7d69/16UMGIM53162.rgb.jpg/100x100bb.jpg",
      "collectionPrice": 9.99,
      "trackPrice": 1.29,
      "releaseDate": "2001-01-01T12:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 10,
      "trackNumber": 4,
      "trackTimeMillis": 200307,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Rock",
      "isStreamable": true
    }
  ]
}
"""
# within the results