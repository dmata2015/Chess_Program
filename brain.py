
def minimax(position,depth,alpha,beta,maximizing_player):
    if depth == 0 or game_over in position:
        return static evaluation of position
    if maximizing_player:
        max_eval =- infinity
        for child in position:
            eval = minimax(child, depth-1,alpha,beta,False)
            max_eval = max(max_eval,eval)
            alpha = max(alpha,eval)
            if beta<= alpha:
                break
        return max_eval
    else :
        min_eval=+infinity
        for child in position:
            eval = minimax(child,depth=1,alpha,beta,True)
            min_eval = min(min_eval,eval)
            beta = min(beta,eval)
            if beta <=  alpha:
                break
        return min_eval