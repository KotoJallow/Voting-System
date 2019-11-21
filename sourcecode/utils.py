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


def goToWinner(source):
    from winner import WinnerUI
    source.destination = WinnerUI()
    navigate(source)

def goToVote(source,userId):
    from vote import VoteUI
    source.destination = VoteUI(userId)
    navigate(source)

def goToAnnouncements(source):
    from announcement import AnnouncementUI
    source.destination = AnnouncementUI()
    navigate(source)

def goToContestant(source,index):
    from contestant import ContestantUI
    source.destination = ContestantUI(index)
    navigate(source)
    print("Clicked index: %d" % index)

def goToParty(source,index):
    from party import PartyUI
    source.destination = PartyUI(index)
    navigate(source)
    print("Clicked index: %d" % index)
