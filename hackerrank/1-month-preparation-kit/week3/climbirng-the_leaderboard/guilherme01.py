from bisect import insort, bisect


from bisect import insort,bisect
def climbingLeaderboard(ranked=[], player=[]):  # Falhou em 3/12 por time limit exceeded
    ranked = list(set(ranked))
    ranked.sort()
    # print(ranked)
    rank = []
    for i, p in enumerate(player):
        position = bisect(ranked, p)
        len_ranked = len(ranked)
        rank.append(len_ranked - position + 1)

        # print(i,p,rank, ranked)
        # print(rank)
    return rank
