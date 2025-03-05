-- 1. Quanti sono gli strutturati di ogni fascia?
select count(p.posizione)
from Persona p
group by p.posizione
-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?
select count(p.posizione)
from Persona p
where p.stipendio >= 40000
-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?
select count(pr.nome)
from Progetto pr
where pr.fine <= CurrentDate and budget >= 50000
-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto
-- ‘Pegasus’ ?
select avg(ap.OreDurata) as Media_Ore, max(ap.OreDurata) as Massimo_Ore, min(ap.OreDurata) as Minimo_Ore
from AttivitaProgetto ap 
    join Progetto pr on pr.nome= ap.progetto
where pr.nome = 'Pegasus'
-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?
select p.nome, p.cognome, avg(ap.OreDurata) as Media_Ore, max(ap.OreDurata) as Massimo_Ore, min(ap.OreDurata) as Minimo_Ore
from Persona p
    join Progetto pr on pr.nome= ap.progetto
    join AttivitaProgetto ap on p.id = ap.persona
where pr.nome = 'Pegasus' and p.posizione = 'Professore Associato' or p.posizione = 'Professore Ordinario'
group by p.nome, p.cognome
-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?
select p.nome as Nome, p.cognome as Cognome, count(anp.oreDurata) as numero_totale
from AttivitaNonProgettuale anp join Persona p on p.id = anp.persona
where anp.tipo = 'Didattica'
-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?
select avg(p.stipendio), max(p.stipendio), min(p.stipendio)
from Persona p
where p.posizione = 'Ricercatore'
-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
-- associati e dei professori ordinari?
select avg(p.stipendio), max(p.stipendio), min(p.stipendio)
from Persona p
where p.posizione = 'Ricercatore' or p.posizione = 'Professore Associato', p.posizione = 'Professore Ordinario' 
group by p.posizione
-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?
-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?