'''
In chess, the Elo rating system is used to calculate player strengths based on game results.

A simplified description of the Elo system is as follows. Every player begins at the same score. For each 
subsequent game, the loser transfers some points to the winner, where the amount of points transferred 
depends on how unlikely the win is. For example, a 1200-ranked player should gain much more points for beating 
a 2000-ranked player than for beating a 1300-ranked player.
'''
import numpy as np

def win_probability(elo1, elo2):
    elo_gap = (elo1 - elo2)/500
    sigma_squared = (np.sqrt(2/np.pi))**2
    mu = 0
    if elo1 < elo2:
        result = (1/np.sqrt(sigma_squared*2*np.pi))*np.exp(-0.5*((elo_gap-mu)**2)/sigma_squared)
    else: 
        result = 1-(1/np.sqrt(sigma_squared*2*np.pi))*np.exp(-0.5*((elo_gap-mu)**2)/sigma_squared)
    return result

def gain_elo(win_proba):
    if  10/(win_proba) < 100:
        gain = 10/(win_proba)
    else:
        gain = 100
    return gain

print('elo of the winner')
elo_player1 = int(input())
print('elo of the looser')
elo_player2 = int(input())

print('the probability of winning was {}, the winner gain {}'
      .format(win_probability(elo_player1, elo_player2), gain_elo(win_probability(elo_player1, elo_player2))))
