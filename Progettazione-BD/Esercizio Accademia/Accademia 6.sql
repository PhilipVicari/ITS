-- ACCADEMIA 6                                                                           -

-- 1. Quanti sono gli strutturati di ogni fascia?
SELECT posizione, count(*)
FROM persona
GROUP by posizione
-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?
SELECT count(*) as numero
from persona p
where p.stipendio >= 40000
-- 3. Quanti sono i progetti già finiti che superano il budget di 50000? ****
select count(*)
from progetto pr
where pr.budget >= 50000
and pr.fine < Current_date
-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto
-- ‘Pegasus’ ?
select avg(oreDurata), max(oreDurata), min(oreDurata)
from progetto p, AttivitaProgetto ap
where ap.progetto = p.id
and p.nome = 'Pegasus'
-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?
select p.id, p.nome, p.cognome, atp.persona, avg(oreDurata), max(oreDurata), min(oreDurata)
from AttivitaProgetto atp
join Persona p on atp.persona = p.id
where atp.progetto = '1'
GROUP by p.id, p.nome, p.cognome, atp.persona
-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?
select p.id, p.nome, p.cognome, SUM(anp.oreDurata) AS ore_didattica_totali
from AttivitaNonProgettuale anp
join Persona p on anp.persona = p.id
where anp.tipo = 'Didattica'
GROUP by p.id, p.nome, p.cognome, anp.oreDurata
-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?
select avg(stipendio), max(stipendio), min(stipendio)
from Persona p
where p.posizione = 'Ricercatore'
--associati e dei professori ordinari?
select avg(stipendio), max(stipendio), min(stipendio)
from Persona p
group by posizione
-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?
SELECT ap.progetto, pr.nome, sum(ap.oreDurata)
FROM Persona p
JOIN AttivitaProgetto ap on ap.persona = p.id
JOIN Progetto pr ON ap.progetto = pr.id
WHERE p.nome = 'Ginevra' and p.cognome = 'Riva'
GROUP by ap.id, pr.nome
-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?
SELECT pr.nome, COUNT(DISTINCT ap.persona)
FROM Progetto pr
JOIN AttivitaProgetto ap on ap.progetto = pr.id
JOIN Persona p on p.id = ap.persona 
WHERE p.posizione IN ('Professore Associato', 'Professore Ordinario')
GROUP by pr.nome
HAVING COUNT (DISTINCT ap.persona) > 1
-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?
SELECT p.id, p.nome, p.cognome
FROM Persona p
JOIN AttivitaProgetto ap on ap.persona = p.id
where p.posizione = 'Professore Associato'
GROUP by p.nome, p.cognome, p.id
