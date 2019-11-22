
import DataAccess

def getPercentageVotesWon(contestantId):
    totalVotes = DataAccess.getTotalVotes().get('TotalVotes')
    votesReceived = DataAccess.getVotes(contestantId).get('VotesCount')
    percentage = votesReceived * 100 / totalVotes
    return ("%.2f%%" % percentage)

def getListOfAllPercentageVotes():
    list = []
    for i in range(1,7):
        list.append(getPercentageVotesWon(i))
    return list

def getNamePartyPercentage():
    list = []
    nameParty = DataAccess.getContestantNameParty()
    percentages = getListOfAllPercentageVotes()
    for i in range(0,6):
        nameParty[i]['Percentage'] = percentages[i]
        list.append(nameParty[i])
    return list

def winnerUI():
    winner = DataAccess.getWinner()
    id = winner.get('ContestantId')
    index = id - 1
    winnerNamePartyPercentage = getNamePartyPercentage()[index]
    return winnerNamePartyPercentage
