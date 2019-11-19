from navigator import navigate

def goToLogin(source):
    from login import LoginUI
    source.destination = LoginUI()
    navigate(source)
    print("Login")

def goToMain(source):
    from main import MainUI
    source.destination = MainUI()
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

def goToVote(source):
    from vote import VoteUI
    source.destination = VoteUI()
    navigate(source)

def goToAnnouncements(source):
    from announcement import AnnouncementUI
    source.destination = AnnouncementUI()
    navigate(source)

def goToContestant(source):
    from contestant import ContestantUI
    source.destination = ContestantUI()
    navigate(source)

def goToParty(source):
    from party import PartyUI
    source.destination = PartyUI()
    navigate(source)
