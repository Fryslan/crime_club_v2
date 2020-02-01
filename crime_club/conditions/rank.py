from crime_club.values import Values


class Rank:

    def get_rank_id(rank):
        if Values.rank == 'Scum':
            return 0
        elif Values.rank == 'Pee Wee':
            return 1
        elif Values.rank == 'Thug':
            return 2
        elif Values.rank == 'Gangster':
            return 3
        elif Values.rank == 'Hitman':
            return 4
        elif Values.rank == 'Assassin':
            return 5
        elif Values.rank == 'Boss':
            return 6
        elif Values.rank == 'Godfather':
            return 7
        elif Values.rank == 'Legendary Godfather':
            return 8
        elif Values.rank == 'Don':
            return 9
        elif Values.rank == 'Respectable Don':
            return 10
        elif Values.rank == 'Legendary Don':
            return 11
        else:
            return -1