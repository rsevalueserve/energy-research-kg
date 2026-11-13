// Q9 Intellectual property to field: sites using technology covered by a patent held by
// Lumen Storage Systems, with connected projects, operators and inventors
MATCH (:Organization {id: 'LSS'})-[:HOLDS]->(pat:Patent)-[:COVERS]->(t:Technology)
      <-[:USES_TECHNOLOGY]-(s:Site)
WITH pat, s, collect(DISTINCT t.name) AS technologies
RETURN pat.id AS patent,
       s.name AS site,
       technologies,
       [(s)-[:ESTABLISHED_UNDER]->(p:Project) | p.name]
         + [(pat)-[:LICENSED_WITHIN]->(p:Project) WHERE NOT (s)-[:ESTABLISHED_UNDER]->(p) | p.name]
         AS projects,
       [(o:Organization)-[:OPERATES]->(s) | o.name] AS operators,
       [(i:Person)-[:INVENTED]->(pat) | i.name] AS inventors
ORDER BY site
