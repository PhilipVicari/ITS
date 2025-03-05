-- 1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome
-- ‘Pegasus’ ?
select wp.nome as Nome, wp.inizio as Inizio_Progetto, wp.fine as Fine_Progetto
from WP wp, progetto pr
where pr.id = wp.progetto and pr.nome = 'Pegasus'
-- 2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
-- una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
select distinct p.nome as Nome, p.cognome as cognome, p.posizione as posizione
from Persona p, AttivitaProgetto ap, progetto pr
where p.id = ap.persona and pr.id = ap.progetto and pr.nome = 'Pegasus'
order by cognome DESC
-- 3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
-- una attività nel progetto ‘Pegasus’ ?
select distinct p.nome as Nome, p.cognome as cognome, p.posizione as posizione
from Persona p, AttivitaProgetto ap, AttivitaProgetto ap2
where p.id = ap.persona and pr.id = ap.progetto and pr.nome = 'Pegasus'
having COUNT(ap.id) > 1
-- 4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto almeno una assenza per malattia?
select p.nome as Nome, p.cognome as cognome, p.posizione as posizione
from Persona p, Assenza ass
where p.id = ass.persona
    and p.posizione= 'Professore Ordinario'
    and ass.tipo = 'Malattia'
-- 5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto più di una assenza per malattia?
select p.nome as Nome, p.cognome as cognome, p.posizione as posizione
from Persona p, Assenza ass
where p.id = ass.persona
    and p.posizione= 'Professore Ordinario'
    and ass.tipo = 'Malattia'
group by p.nome, p.cognome, p.posizione
having COUNT(ass.tipo) > 1
-- 6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
-- un impegno per didattica?
select p.nome as Nome, p.cognome as cognome, p.posizione as posizione
from Persona p, AttivitaProgetto ap
where p.id=ap.persona and ap.tipo = 'Didattica'
-- 7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
-- impegno per didattica?
select p.nome as Nome, p.cognome as cognome, p.posizione as posizione
from Persona p, AttivitaNonProgettuale anp
where p.id=anp.persona 
    and anp.tipo = 'Didattica'
group by p.nome, p.cognome, p.posizione
having count(ap.tipo) > 1

-- 8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali?
select p.nome as Nome, p.cognome as cognome, p.posizione as posizione
from Persona p 
    join AttivitaProgetto ap on p.id = ap.persona
    join AttivitaNonProgettuale anp on p.id = anp.persona
where ap.giorno = anp.giorno
-- 9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali? Si richiede anche di proiettare il
-- giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
-- entrambe le attività.
select p.nome as Nome, 
    p.cognome as cognome, 
    p.posizione as posizione, 
    ap.giorno as Giorno, 
    pr.nome as Nome_Progetto,
    anp.tipo as Tipo_Lavoro,
    ap.oreDurata as Ore_Prog
    anp.oreDurata as Ore_N_Prog 
from Persona p 
    join AttivitaProgetto ap on p.id = ap.persona
    join AttivitaNonProgettuale anp on p.id = anp.persona
    JOIN Progetto pr ON ap.progetto = pr.id
where ap.giorno = anp.giorno
-- 10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali?
select p.nome as Nome, p.cognome as cognome, p.posizione as posizione
from Persona p 
    join AttivitaProgetto ap on p.id = ap.persona
    join Assenza ass on p.id = ass.persona
where ap.giorno = anp.giorno
-- 11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
-- nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
select p.nome as Nome, 
    p.cognome as cognome, 
    p.posizione as posizione, 
    ap.giorno as Giorno, 
    pr.nome as Nome_Progetto,
    ass.tipo as Causa_Assenza
    ap.oreDurata as Ore_Prog
from Persona p 
    join AttivitaProgetto ap on p.id = ap.persona
    join Assenza ass on p.id = ass.persona
    join Progetto pr ON ap.progetto = pr.id
where ap.giorno = anp.giorno
-- 12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
select wp.nome
from WP wp, Progetto pr
where pr.nome=wp.progetto and wp.nome = pr.nome