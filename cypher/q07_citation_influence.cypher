// Q7 Citation influence: publications citing the 2022 cathode stability paper,
// directly or indirectly (transitive CITES chain)
MATCH (target:Publication {id: 'P-CATH-2022'})
MATCH path = (citing:Publication)-[:CITES*1..]->(target)
WITH citing, path
ORDER BY length(path)
WITH citing, collect(path)[0] AS shortest
RETURN citing.title AS citing_publication,
       citing.year AS year,
       length(shortest) AS citation_distance,
       CASE length(shortest) WHEN 1 THEN 'direct' ELSE 'indirect' END AS citation_type,
       reduce(s = '', n IN nodes(shortest) |
              s + CASE s WHEN '' THEN '' ELSE ' -> ' END + n.short_title) AS citation_chain
ORDER BY citation_distance, year
