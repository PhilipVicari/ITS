-- ACCADEMIA 5
--   Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:
--   1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome
--   ‘Pegasus’ ?
SELECT  WP.nome, WP.inizio, WP.fine
from WP, Progetto
where WP.progetto = Progetto.id and Progetto.nome = 'Pegasus'
--   2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
--   una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
SELECT distinct s.nome, s.cognome, s.posizione
from AttivitaProgetto a, Persona s, Progetto p
where a.persona = s.id 
    and a.progetto = p.id 
    and p.nome = 'Pegasus'
ORDER by s.cognome desc

--   3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
--   una attività nel progetto ‘Pegasus’ ?
SELECT *
from AttivitaProgetto a1, AttivitaProgetto a2, progetto p,
where a1.id
--   4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
--   fatto almeno una assenza per malattia?
select distinct pe.id, pe.nome, pe.cognome
from Persona pe
join Assenza a ON pe.id = a.persona
where pe.posizione= 'Professore Ordinario'
    and a.tipo = 'Malattia'

--   5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
--   fatto più di una assenza per malattia?
SELECT p.nome, p.cognome, p.posizione
FROM Persona p
JOIN Assenza a ON p.id = a.persona
WHERE p.posizione = 'Professore Ordinario' AND a.tipo = 'Malattia'
GROUP BY p.id, p.nome, p.cognome, p.posizione
HAVING COUNT(*) > 1;
--   6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
--   un impegno per didattica?
select distinct pe.id, pe.nome, pe.cognome
from Persona pe
join AttivitaNonProgettuale atn ON pe.id = atn.persona
where pe.posizione= 'Ricercatore'
    and atn.tipo = 'Didattica'
--   7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
--   impegno per didattica?
SELECT p.nome, p.cognome, p.posizione
FROM Persona p
JOIN AttivitaNonProgettuale atn ON p.id = atn.persona
WHERE p.posizione = 'Ricercatore' AND atn.tipo = 'Didattica'
GROUP BY p.id, p.nome, p.cognome, p.posizione
HAVING COUNT(*) > 1;
--   8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
--   attività progettuali che attività non progettuali?
SELECT DISTINCT pe id, pe.nome, pe.cognome
FROM Persona pe
JOIN AttivitaProgetto atp ON pe.id = ap.persona
JOIN AttivitaNonProgettuale atn ON pe.id = atn.persona AND atp.giorno = atn.giorno;

--   9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
--   attività progettuali che attività non progettuali? Si richiede anche di proiettare il
--   giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
--   entrambe le attività.

SELECT p.nome, p.cognome, ap.giorno, pr.nome, anp.tipo, ap.oreDurata, anp.oreDurata
FROM Persona p
JOIN AttivitaProgetto ap ON p.id = ap.persona
JOIN AttivitaNonProgettuale anp ON p.id = anp.persona AND ap.giorno = anp.giorno
JOIN Progetto pr ON ap.progetto = pr.id

-- 10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali?
SELECT DISTINCT pe.id, pe.nome, pe.cognome
FROM Persona pe
JOIN AttivitaProgetto atp ON pe.id = atp.persona
join Assenza a on pe.id = a.persona and atp.giorno = a.giorno

--  11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
--  assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
--  nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
SELECT pe.nome, pe.cognome, atp.giorno, pr.nome, a.tipo, atp.oreDurata
FROM Persona pe
JOIN AttivitaProgetto atp ON pe.id = atp.persona
JOIN Progetto pr ON atp.progetto = pr.id
join Assenza a on pe.id = a.persona and atp.giorno = a.giorno
-- 12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
select WP.nome
from WP
join Progetto pr on pr.id = WP.progetto
where WP.nome =