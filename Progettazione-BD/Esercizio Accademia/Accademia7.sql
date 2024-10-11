--ACCADEMIA 7 -----------------------------------------------------------------------------------------------------------------------------------------------------
-- 1. Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati?
select p.posizione, avg(stipendio) as media, STDDEV_POP(stipendio) as dev_standard
from Persona p
group by p.posizione
-- 2. Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media
-- della loro categoria?
with Media_Ricercatori as (
	select avg(stipendio) as media
	from Persona p
	where p.posizione = 'Ricercatore'
)
Select *
from Persona p
where p.posizione = 'Ricercatore'
	and p.stipendio > (select media from Media_Ricercatori)
-- 3. Per ogni categoria di strutturati quante sono le persone con uno stipendio che
-- differisce di al massimo una deviazione standard dalla media della loro categoria?
with Statistiche(
  select avg(stipendio) as media, STDDEV_POP(stipendio) as dev_standard
  from Persona p
  group by p.posizione
)
select p.posizione, count(*)
from Persona p
where 

----Da Completare----

-- 4. Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività
-- progettuali? Restituire tutti i loro dati e il numero di ore lavorate.

select p.id, p.nome, p.cognome, p.posizione, p.stipendio, sum(ap.oreDurata) as Somma_ore
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
group by p.id, p.nome, p.cognome, p.posizione, p.stipendio
HAVING sum(ap.oreDurata) >=20

-- 5. Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i
-- progetti? Restituire nome dei progetti e loro durata in giorni.

with Media_Durata(
  select avg()
)

----Da Completare----


-- 6. Quali sono i progetti terminati in data odierna che hanno avuto attività di tipo
-- “Dimostrazione”? Restituire nome di ogni progetto e il numero complessivo delle
-- ore dedicate a tali attività nel progetto.
select pr.id, pr.nome, sum(ap.oreDurata) as somma_ore
from progetto pr
join AttivitaProgetto ap on pr.id = ap.progetto
where pr.fine < Current_date
  and ap.tipo = 'Dimostrazione'
group by pr.id, pr.nome
-- 7. Quali sono i professori ordinari che hanno fatto più assenze per malattia del nu-
-- mero di assenze medio per malattia dei professori associati? Restituire id, nome e
-- cognome del professore e il numero di giorni di assenza per malattia

----Da Completare----
