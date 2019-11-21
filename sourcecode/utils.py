from navigator import navigate

def goToLogin(source):
    from login import LoginUI
    source.destination = LoginUI()
    navigate(source)
    print("Login")

def goToMain(source,userId):
    from main import MainUI
    source.destination = MainUI(userId)
    navigate(source)
    print("Login")

def goToRegister(source):
    from register import RegisterUI
    source.destination = RegisterUI()
    navigate(source)
    print("Register")


def goToWinner(source,userId,name,party,percentage):
    from winner import WinnerUI
    source.destination = WinnerUI(userId,name,party,percentage)
    navigate(source)

def goToVote(source,userId):
    from vote import VoteUI
    source.destination = VoteUI(userId)
    navigate(source)

def goToAnnouncements(source,userId):
    from announcement import AnnouncementUI
    source.destination = AnnouncementUI(userId)
    navigate(source)

def goToContestant(source,userId,index):
    from contestant import ContestantUI
    source.destination = ContestantUI(userId,index)
    navigate(source)
    print("Clicked index: %d" % index)

def goToParty(source,userId,index):
    from party import PartyUI
    source.destination = PartyUI(userId,index)
    navigate(source)
    print("Clicked index: %d" % index)
