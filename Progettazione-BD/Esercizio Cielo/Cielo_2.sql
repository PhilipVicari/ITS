-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?
select a.codice, a.nome, count(distinct ar.comp) 
from arrpart ar, aeroporto a
where a.codice = ar.partenza or a.codice = ar.arrivo
group by a.codice
-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno 100 minuti?
SELECT COUNT(DISTINCT ar.partenza) as num_voli
FROM ArrPart ar
JOIN Volo v on v.codice = ar.codice
WHERE ar.partenza = 'HTR' and v.durataMinuti >= 100
-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione nella quale opera?
SELECT la.nazione, COUNT(DISTINCT a.codice) AS numero_aeroporti
FROM Compagnia c
JOIN ArrPart ap ON c.nome = ap.comp
JOIN Aeroporto a ON a.codice = ap.arrivo OR a.codice = ap.partenza
JOIN LuogoAeroporto la ON a.codice = la.aeroporto
WHERE c.nome = 'Apitalia'
GROUP BY la.nazione;
-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla compagnia ‘MagicFly’ ?
select avg(durataMinuti), max(durataMinuti), min(durataMinuti)
from Volo v
where v.comp = 'MagicFly'
-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli aeroporti?
select a.codice as Codice, a.nome as Nome_Aeroporto, min(c.annofondaz) as anno
from ArrPart ap
join Volo v on v.codice = ap.codice and v.comp = ap.comp
join compagnia c on c.nome = v.comp
join Aeroporto a ON a.codice = ap.arrivo OR a.codice = ap.partenza
group by a.codice;
-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più voli?

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

select a.codice as Codice, a.nome as Nome_Aeroporto, avg(v.durataMinuti) as Media_durata
from Volo v
join ArrPart ap on ap.codice = v.codice
join Aeroporto a ON a.codice = ap.partenza
group by a.codice;

-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate a partire dal 1950?

select c.nome as Nome_Compagnia, sum(v.durataMinuti) as durata_complessiva
from Volo v
join compagnia c on v.comp = c.nome
where c.annofondaz >= '1950'
group by c.nome

-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?

select a.nome as Nome_Aeroporto, COUNT(distinct ap.comp) as numero_compagnie
from ArrPart ap
join Aeroporto a on a.codice = ar.arrivo OR a.codice = ar.partenza
group by a.nome
Having COUNT(numero_compagnie) = 2

-- 10. Quali sono le città con almeno due aeroporti?

select la.citta as nome
from LuogoAeroporto la
join Aeroporto a on a.codice = la.aeroporto
group by la.citta
having COUNT(la.citta) >= 2

-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6 ore?

select c.nome
from Compagnia c
join Volo v on v.comp = c.nome
group by c.nome
having avg(v.durataMinuti) >= '360'

-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?
select distinct v.comp
from Volo v
group by v.comp
having min(v.durataMinuti) > 100