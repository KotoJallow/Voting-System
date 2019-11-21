
getContestant = "select * from contestantView where Id = %d"
getNamesOfAllContestants = "select Name from contestant"
getParty = "select * from party where Id = %d"
getUser = "select * from userView where Id = %d"
getLogin = "select Id from loginView where Username = ? and Password = ?"
getVotes = "select count(*) as VotesCount from votes where ContestantId = %d"
getTotalVotes = "select count(*) as TotalVotes from votes"
getWinner = '''SELECT ContestantId,COUNT(ContestantId) AS VotesCount FROM votes 
               GROUP BY ContestantId
               ORDER BY VotesCount DESC
               LIMIT 1;'''

insertUser = '''insert into user(FirstName,MiddleName,LastName,IdNumber,GenderId,Password) values(?,?,?,?,?,?)'''
insertVote = '''insert into votes(UserId,ContestantId) values(?,?)'''
