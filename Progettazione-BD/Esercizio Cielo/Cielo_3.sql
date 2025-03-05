-- 1. Qual è la durata media, per ogni compagnia, dei voli che partono da un aeroporto
-- situato in Italia?
select c.nome as nome_compagnia, avg(v.durataMinuti) as Media_Durata
from Volo v
join ArrPart ap on v.codice = ap.codice and v.comp = ap.comp
join Aeroporto a on ap.partenza = a.codice
join LuogoAeroporto la on a.codice = la.aeroporto
join Compagnia c on v.comp = c.nome
where la.nazione = 'Italy'
group by c.nome
-- 2. Quali sono le compagnie che operano voli con durata media maggiore della durata
-- media di tutti i voli?
SELECT v.comp AS compagnia
FROM Volo v
GROUP BY v.comp
HAVING AVG(v.durataMinuti) > (
    SELECT AVG(durataMinuti) 
    FROM Volo
);
-- 3. Quali sono le città dove il numero totale di voli in arrivo è maggiore del numero
-- medio dei voli in arrivo per ogni città?
select la.citta
from LuogoAeroporto la
join ArrPart ap on ap.arrivo = la.aeroporto
group by la.citta
having count(a.arrivo) > (
    select avg(arrivo)
    from ArrPart
)
-- 4. Quali sono le compagnie aeree che hanno voli in partenza da aeroporti in Italia con
-- una durata media inferiore alla durata media di tutti i voli in partenza da aeroporti
-- in Italia?
-- 5. Quali sono le città i cui voli in arrivo hanno una durata media che differisce di più
-- di una deviazione standard dalla durata media di tutti i voli? Restituire città e
-- durate medie dei voli in arrivo.
-- 6. Quali sono le nazioni che hanno il maggior numero di città dalle quali partono voli
-- diretti in altre nazioni?