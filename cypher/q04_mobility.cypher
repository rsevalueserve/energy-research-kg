// Q4 Mobility: researchers affiliated (employment or study) with more than one
// organization, with each move in chronological order and its direction
MATCH (p:Person)-[a:AFFILIATED_WITH]->(o:Organization)
WHERE a.type IN ['employment', 'study']
WITH p, a, o
ORDER BY coalesce(a.end, 9999), coalesce(a.start, 0)
WITH p, collect({org: o.name, country: o.country, sector: o.sector, type: a.type,
                 start: a.start, end: a.end}) AS stints
WHERE size(stints) > 1
UNWIND range(0, size(stints) - 2) AS i
WITH p, stints[i] AS f, stints[i + 1] AS t
RETURN p.name AS researcher,
       f.org + ' (' + f.type + ') -> ' + t.org + ' (' + t.type + ')' AS move,
       coalesce(f.end, t.start) AS left_year,
       coalesce(t.start, f.end) AS joined_year,
       f.sector + ' -> ' + t.sector AS sector_direction,
       f.country + ' -> ' + t.country
         + CASE WHEN f.country = t.country THEN ' (domestic)' ELSE ' (international)' END
         AS geographic_direction
ORDER BY researcher, left_year
