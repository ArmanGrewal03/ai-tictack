import random
import copy

class AI:

    def __init__(self,level=1,player=2):
        self.level=level
        self.player=player

    def rnd(self,board):
        empty_squares=board.get_empty_squares()
        idx=random.randrange(0,len(empty_squares))
        return empty_squares[idx]
    
    def minimax(self, board, maximizing, alpha, beta):
        case = board.final_state()
        if case == 1:
            return 1, None

        if case == 2:
            return -1, None

        elif board.is_full():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_squares()
            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval, _ = self.minimax(temp_board, False, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval, best_move

        else:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_squares()
            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval, _ = self.minimax(temp_board, True, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval, best_move

    def eval(self, main_board):
        if self.level == 0:
            eval = 'random'
            move = self.rnd(main_board)
        else:
            eval, move = self.minimax(main_board, False, -float('inf'), float('inf'))

        print(f'AI has chosen to mark the square in pos {move} with an eval of {eval}')
        return move