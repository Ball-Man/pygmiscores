import enum
import hashlib
import base64
import requests


class SubmitMode(enum.Enum):
    """Submit modes for gmiscores.

    ALL - insert all the scores in the leaderboard
    HIGHER - update score when a user beats their record
    LOWER - update score when a user beats their record(less is better)
    """
    ALL = 'all'
    HIGHER = 'higher'
    LOWER = 'lower'


class Scores:
    """Class encapsulating ajax requests to a leaderboard service.

    The service documentation can be found at
    https://gmiscores.altervista.org/documentation.php.

    For this class to correctly send requests, a the game secret
    is required(can be obtained from the site above).

    NOTE: private key security is not supported.
    """
    upstream = 'https://gmiscores.altervista.org/api/v1'

    def __init__(self, game_id=-1, secret=''):
        self.secret = secret
        self.game_id = game_id

    def submit_score(self, username, score, mode=SubmitMode.ALL,
                     game_id=None, secret=None):
        """Submit a score online.
        Note that this request is synchronous, run it in a separate
        thread when used in real time applications.

        username - The username of the player
        score - The score of the player
        mode - The submit mode (see SubmitMode)
        game_id - The game_id (from https://gmiscores.altervista.org)
        secret - The game secret (from https://gmiscores.altervista.org)

        A request.model.Response instance.
        """
        if game_id is None:
            game_id = self.game_id

        if secret is None:
            secret = self.secret

        # Assemble body
        player = base64.b64encode(username.encode()).decode()
        data = {
            'game': int(game_id),
            'player': player,
            'score': score,
            'insertMode': mode.value,
            'hash': hashlib.sha1(('game={}&score={}&player={}{}')
                .format(int(game_id), score, player, secret).encode())
                .hexdigest()
        }

        return requests.post('{}/add.php'.format(self.upstream),
                             data=data)
