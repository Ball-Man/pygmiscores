# PyGMIScores
An API implementation for [gmiscores](https://gmiscores.altervista.org/), an online leaderboard service for games.

## Requirements
- Python >= 3.5
- requests (python package)

## Installation
To use the lib, simply copy the `pygmiscores` directory in your project root. You can easily import it with `import pygmiscores`.

## Usage
The library can be used by manually instantiating the `Scores` class. When a single client is required there is a simpler approach at module level. Here's a complete example:

```py
import pygmiscores as scores

# Get your game ID and secret from the gmiscores website(e.g. 16)
# and insert them here.
scores.game(game_id=..., secret=...)
# The secret isn't required if you're not submitting new scores, only reading

scores.add('Vegeta', 9001)    # Add a record for Vegeta, with a score of 9001

print(scores.list_parsed())   # Get the top 10
```

The printed result (assuming Vegeta is our first ever player) would be:
```
{'status': 200, 'scores': [{'player_id': 82, 'username': 'Vegeta', 'score': 9001, 'created_at': '2020-11-07 00:11:35', 'updated_at': '2020-11-07 00:11:35', 'sign': None}], 'playerScore': None}
```
