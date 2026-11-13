// Q8 Collaboration horizon: organizations reachable from HIT within two
// project-collaboration hops (Org -> Project <- Org = 1 hop), and through which projects
MATCH (hit:Organization {id: 'HIT'})
MATCH path = (hit)-[:PARTICIPATES_IN*2..4]-(o:Organization)
WHERE o <> hit
  AND all(i IN range(0, size(nodes(path)) - 2)
          WHERE NOT nodes(path)[i] IN nodes(path)[i + 1..])
WITH o, path, length(path) / 2 AS hops
ORDER BY hops
WITH o, collect({hops: hops, path: path}) AS paths
WITH o, paths[0].hops AS hops, [x IN paths WHERE x.hops = paths[0].hops | x.path] AS shortest
RETURN o.name AS organization,
       hops,
       [p IN shortest |
          reduce(s = 'HIT', i IN range(1, size(nodes(p)) - 1) |
                 s + CASE WHEN i % 2 = 1 THEN ' -[' + nodes(p)[i].name + ']- '
                          ELSE nodes(p)[i].short_name END)] AS via_projects
ORDER BY hops, organization
