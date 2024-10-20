begin transaction;

create type Strutturato as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');
create type LavoroProgetto as enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management, Altro');
create type LavoroNonProgettuale as enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');
create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita, Malattia');
create domain PosInteger as integer
    default 0
    CHECK (value>=0);
create domain StringaM as varchar(100);
create domain NumeroOre as integer
    default 0
    CHECK (value >= 0 and value <= 8);
create domain Denaro as real
    default 0
    CHECK (value >= 0);


create table Persona (
  id PosInteger not null,
  nome StringaM not null,
  cognome StringaM not null,
  posizione strutturato not null,
  stipendio Denaro not null,
  PRIMARY KEY (id)
);

create table Progetto (
  id PosInteger not null,
  nome StringaM not null,
  inizio date not null,
  fine date not null,
  budget Denaro not null,
  PRIMARY KEY (id),
  UNIQUE (nome),
  CHECK (inizio < fine)
);

create table WP (
  progetto PosInteger not null,
  id PosInteger not null,  
  nome StringaM not null,
  inizio date not null,
  fine date not null,
  PRIMARY KEY (progetto, id),
  UNIQUE (progetto, nome),
  CHECK (inizio < fine),  
  FOREIGN KEY (progetto) references Progetto(id) 
);

create table AttivitaProgetto (
  id PosInteger not null,
  persona PosInteger not null,
  progetto PosInteger not null,
  wp PosInteger not null,
  giorno date not null,
  tipo LavoroProgetto not null,
  oreDurata NumeroOre not null,
  PRIMARY KEY (id),
  FOREIGN KEY (persona) references Persona(id)  ,
  FOREIGN KEY (progetto, wp) references WP(progetto, id)  
);

create table AttivitaNonProgettuale (
  id PosInteger not null,
  persona PosInteger not null,
  tipo LavoroNonProgettuale not null,
  giorno date not null,
  oreDurata NumeroOre not null,
  PRIMARY KEY (id),
  FOREIGN KEY (persona) references Persona(id)  
);

create table Assenza (
  id PosInteger not null,
  persona PosInteger not null,
  tipo CausaAssenza not null,
  giorno date not null,
  PRIMARY KEY (id),
  UNIQUE (persona, giorno),
  FOREIGN KEY (persona) references Persona(id)  
);