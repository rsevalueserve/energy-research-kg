// Q6 International reach: rank researchers by the number of distinct countries among
// their co-authors, excluding their own country (country = current affiliation's country)
MATCH (r:Person)-[ra:AFFILIATED_WITH {current: true}]->(ro:Organization)
WHERE EXISTS { (r)-[:AUTHORED]->(:Publication) }
OPTIONAL MATCH (r)-[:AUTHORED]->(:Publication)<-[:AUTHORED]-(c:Person)
               -[:AFFILIATED_WITH {current: true}]->(co:Organization)
  WHERE co.country <> ro.country
WITH r, ro.country AS own_country, collect(DISTINCT co.country) AS foreign_coauthor_countries
RETURN r.name AS researcher,
       own_country,
       size(foreign_coauthor_countries) AS distinct_foreign_countries,
       foreign_coauthor_countries
ORDER BY distinct_foreign_countries DESC, researcher
