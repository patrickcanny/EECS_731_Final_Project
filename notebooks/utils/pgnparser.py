import pandas as pd
import chess
import chess.pgn

class PGNParser:
    def __init__(self, pgnPath):
        self.pgnPath = pgnPath

    def parse(self, numGames):
        pgn = open(self.pgnPath)
        df = []
        cols = ['Event', 'Site', 'Date', 'Round', 'White', 'Black', 'Result', 'BlackElo', 'BlackRatingDiff', 'ECO', 'Opening', 'Termination', 'TimeControl', 'UTCDate', 'UTCTime', 'WhiteElo', 'WhiteRatingDiff']
        for i in range(0, numGames):
            game = chess.pgn.read_game(pgn)
            g_headers = []
            for header in game.headers:
                g_headers.append(game.headers[header])
            df.append(g_headers)
        return pd.DataFrame(df, columns=cols)
