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
