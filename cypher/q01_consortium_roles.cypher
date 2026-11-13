// Q1 Consortium roles: organizations in ALPINE, their role, and the funding agency
MATCH (o:Organization)-[r:PARTICIPATES_IN]->(p:Project {id: 'ALPINE'})<-[f:FUNDS]-(a:FundingAgency)
RETURN p.name AS project,
       o.name AS organization,
       r.role AS role,
       r.role_detail AS detail,
       a.name AS funding_agency,
       f.amount AS amount,
       f.currency AS currency
ORDER BY CASE r.role WHEN 'coordinator' THEN 0 ELSE 1 END, organization
