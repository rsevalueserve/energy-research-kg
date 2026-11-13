// Q5 Funding overview: per agency, funded projects, amounts and currencies,
// and the companies and utilities taking part in each project
MATCH (a:FundingAgency)-[f:FUNDS]->(p:Project)
OPTIONAL MATCH (o:Organization)-[:PARTICIPATES_IN]->(p)
  WHERE o:Company OR o:Utility
WITH a, f, p, collect(o.name + ' (' + o.type + ')') AS companies_and_utilities
RETURN a.name AS funding_agency,
       p.name AS project,
       f.amount AS amount,
       f.currency AS currency,
       toString(f.start_year) + '-' + toString(f.end_year) AS period,
       companies_and_utilities
ORDER BY funding_agency, project
