
getContestant = "select * from contestantView where Id = ?"
getParty = "select * from party where Id = ?"
getUser = "select * from userView where Id = ?"
getLogin = "select Id from loginView where Username = ? and Password = ?"
getVotes = "select count(*) as VotesCount from votes where ContestantId = ?"
getTotalVotes = "select count(*) as TotalVotes from votes"
getWinner = '''SELECT ContestantId,COUNT(ContestantId) AS VotesCount FROM votes 
               GROUP BY ContestantId
               ORDER BY max(ContestantId) DESC
               LIMIT 1;'''

insertUser = '''insert into user(FirstName,MiddleName,LastName,IdNumber,GenderId,Password) values(?,?,?,?,?,?)'''
insertVote = '''insert into votes(UserId,ContestantId) values(?,?)'''
