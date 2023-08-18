
import json

with open('importedGames.json', 'r') as f:
  importedGames = json.load(f)

resultGames = []
for importedGame in importedGames:
    resultGame = {
        'name': importedGame['name'],
        'url': importedGame['url'],
        'thumb3': importedGame['thumb3'],
    }
    resultGames.append(resultGame)
with open('games.json', 'w') as json_file:
  json.dump(resultGames, json_file)