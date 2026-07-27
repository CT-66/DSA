class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        i = 0  # player pointer
        j = 0  # trainer pointer
        matches = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                # trainer can handle player
                matches += 1
                i += 1
                j += 1
            else:
                # trainer is too weak, skip it
                j += 1

        return matches