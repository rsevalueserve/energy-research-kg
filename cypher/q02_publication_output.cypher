// Q2 Publication output: per project, its publications with authors and their
// affiliation at the time of publication (employment or study valid in that year)
MATCH (proj:Project)<-[:PRODUCED_IN]-(pub:Publication)<-[au:AUTHORED]-(per:Person)
OPTIONAL MATCH (per)-[aff:AFFILIATED_WITH]->(org:Organization)
  WHERE aff.type IN ['employment', 'study']
    AND coalesce(aff.start, 0) <= pub.year
    AND coalesce(aff.end, 9999) >= pub.year
WITH proj, pub, au, per, collect(org.name) AS orgs
ORDER BY au.position
WITH proj, pub, collect(per.name + ' (' + coalesce(head(orgs), 'unknown') + ')') AS authors
RETURN proj.name AS project,
       pub.year AS year,
       pub.title AS publication,
       authors
ORDER BY project, year
