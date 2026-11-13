// Q10 Collaborator recommendation: researcher pairs who never co-authored, share at least
// one common co-author, and whose publications address the same technology area
MATCH (a:Person)-[:AUTHORED]->(:Publication)<-[:AUTHORED]-(common:Person)
      -[:AUTHORED]->(:Publication)<-[:AUTHORED]-(b:Person)
WHERE a.name < b.name
  AND NOT EXISTS { (a)-[:AUTHORED]->(:Publication)<-[:AUTHORED]-(b) }
WITH a, b, collect(DISTINCT common.name) AS common_coauthors
MATCH (a)-[:AUTHORED]->(:Publication)-[:ADDRESSES]->(t:Technology)
      <-[:ADDRESSES]-(:Publication)<-[:AUTHORED]-(b)
WITH a, b, common_coauthors, collect(DISTINCT t.name) AS shared_technology_areas
RETURN a.name AS researcher_1,
       b.name AS researcher_2,
       common_coauthors,
       shared_technology_areas
ORDER BY size(common_coauthors) + size(shared_technology_areas) DESC, researcher_1, researcher_2
