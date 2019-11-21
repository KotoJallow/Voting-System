CREATE TABLE IF NOT EXISTS "contestant" (
	"Id"	INTEGER UNIQUE,
	"Name"	TEXT,
	"Age"	INTEGER,
	"MaritalStatusId"	INTEGER,
	"PartyId"	INTEGER
);

CREATE TABLE IF NOT EXISTS "gender" (
	"id"	INTEGER,
	"type"	TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "maritalStatus" (
	"Id"	INTEGER,
	"type"	TEXT,
	PRIMARY KEY("Id")
);

CREATE TABLE IF NOT EXISTS "party" (
	"Id"	INTEGER,
	"Name"	TEXT,
	"Acronym"	TEXT,
	"Leader"	TEXT,
	"YearEstablished"	INTEGER,
	"Motto"	TEXT,
	"Address"	TEXT,
	"PhoneNumber"	TEXT,
	PRIMARY KEY("Id")
);

CREATE TABLE IF NOT EXISTS "user" (
	"Id"	INTEGER,
	"FirstName"	TEXT,
	"LastName"	TEXT,
	"IdNumber"	INTEGER UNIQUE,
	"GenderId"	INTEGER,
	"Password"	TEXT,
	PRIMARY KEY("Id")
);

CREATE TABLE IF NOT EXISTS "votes" (
	"Id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"UserId"	INTEGER,
	"ContestantId"	INTEGER
);

create view IF NOT EXISTS contestantView 
as select c.Id, c.Name, c.Age, m.Type, p.Acronym from contestant as c
join maritalStatus as m on c.MaritalStatusId = m.Id
join party as p on c.PartyId = p.Id

create view IF NOT EXISTS userView 
as select u.Id,u.FirstName,u.MiddleName,u.LastName,g.Type from user as u
join gender as g on u.GenderId = g.Id

create view IF NOT EXISTS loginView
as select Id, IdNumber as Username, Password from user

create view IF NOT EXISTS contestantNameParty
as select Name, Acronym as Party from contestantView