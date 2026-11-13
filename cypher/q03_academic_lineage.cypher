// Q3 Academic lineage: full doctoral supervision chain for every doctoral researcher,
// starting from the earliest known supervisor (root) down to the researcher
MATCH chain = (root:Person)-[:SUPERVISED*1..]->(researcher:Person)
WHERE NOT EXISTS { (:Person)-[:SUPERVISED]->(root) }
WITH researcher, chain, [n IN nodes(chain) | n.name] AS names
RETURN researcher.name AS doctoral_researcher,
       last(relationships(chain)).status AS doctorate_status,
       reduce(s = head(names), n IN tail(names) | s + ' -> ' + n) AS supervision_chain,
       names[-2] AS supervisor,
       CASE WHEN size(names) >= 3 THEN names[-3] ELSE null END AS academic_grandparent
ORDER BY length(chain) DESC, doctoral_researcher
