begin transaction;

create domain PosInteger as integer
    default 0
    CHECK (value>=0);
create domain StringaM as varchar(100);
create domain CodiATA as char(3);

create table Volo(
    codice PosInteger not null,
    comp StringaM not null,
    durataMinuti PosInteger not null,
    PRIMARY KEY (codice),
    FOREIGN KEY comp references Compagnia(nome),
    FOREIGN KEY (codice, comp)references ArrPart(codice, comp)
);
create table ArrPart(
    codice PosInteger not null,
    comp StringaM not null,
    arrivo CodiATA not null,
    partenza CodiATA not null,
    PRIMARY KEY (codice),
    FOREIGN KEY (codice, comp)references Volo(codice, comp),
    FOREIGN KEY (arrivo) references Aeroporto(codice),
    FOREIGN KEY (partenza) references Aeroporto(codice)
);
create table Aeroporto(
    codice CodiATA not null,
    nome StringaM not null,
    PRIMARY KEY (codice),
    FOREIGN KEY (codice) references LuogoAeroporto(Aeroporto)
);
create table LuogoAeroporto(
    Aeroporto CodiATA not null,
    citta StringaM not null,
    nazione StringaM not null,
    PRIMARY KEY (Aeroporto),
    FOREIGN KEY (Aeroporto) references Aeroporto(codice)
);
create table Compagnia(
    nome StringaM not null,
    annoFondazione PosInteger null,
    PRIMARY KEY(nome)
);


commit
