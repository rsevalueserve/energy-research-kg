"""
Facts I extracted from the 35 documents in energy_research_corpus/corpus.

I only keep what the 10 questions in queries.txt need. Every node has a
`source` property with the number(s) of the document(s) it comes from.
"""

# ---------------------------------------------------------------------------
# NODES
# ---------------------------------------------------------------------------

# `type` also becomes a second label (Q5 filters companies and utilities).
# `sector` gives the direction of a move in Q4, `country` is used in Q4 and Q6.
ORGANIZATIONS = [
    dict(id="HIT", name="Halvorsen Institute of Technology", short_name="HIT",
         type="University", sector="academia", city="Trondheim", country="Norway", source="01"),
    dict(id="RVU", name="Rhine Valley University", short_name="RVU",
         type="University", sector="academia", city="Karlsruhe", country="Germany", source="02"),
    dict(id="SPIS", name="Southern Peninsula Institute of Science", short_name="SPIS",
         type="ResearchInstitute", sector="academia", city="Chennai", country="India", source="03"),
    dict(id="MRU", name="Maple Ridge University", short_name="Maple Ridge",
         type="University", sector="academia", city="Vancouver", country="Canada", source="04"),
    dict(id="LSS", name="Lumen Storage Systems", short_name="Lumen",
         type="Company", sector="industry", city="Munich", country="Germany", source="05"),
    dict(id="FJG", name="Fjordgrid AS", short_name="Fjordgrid",
         type="Utility", sector="industry", city="Bergen", country="Norway", source="06"),
    dict(id="DPC", name="Deccan Power Corporation", short_name="Deccan Power",
         type="Utility", sector="industry", city="Hyderabad", country="India", source="07"),
    dict(id="PCT", name="Pacific Cell Technologies", short_name="Pacific Cell",
         type="Company", sector="industry", city="Vancouver", country="Canada", source="08"),
]

FUNDING_AGENCIES = [
    dict(id="ECEC", name="European Clean Energy Council", country="Belgium", source="09"),
    dict(id="NSEI", name="National Science Endowment of India", country="India", source="10"),
    dict(id="CIF", name="Canadian Innovation Fund", country="Canada", source="11"),
]

PERSONS = [
    dict(id="ingrid_solberg", name="Ingrid Solberg", source="16"),
    dict(id="markus_weber", name="Markus Weber", source="17"),
    dict(id="priya_raghunathan", name="Priya Raghunathan", source="18"),
    dict(id="daniel_okafor", name="Daniel Okafor", source="19"),
    dict(id="elena_voss", name="Elena Voss", source="20"),
    dict(id="tomas_berg", name="Tomas Berg", source="21"),
    dict(id="katarina_novak", name="Katarina Novak", source="02,32"),
    dict(id="sofia_lindqvist", name="Sofia Lindqvist", source="16,22"),
    dict(id="arjun_menon", name="Arjun Menon", source="03,13"),
    dict(id="li_wei", name="Li Wei", source="04,19"),
    dict(id="hannah_brooks", name="Hannah Brooks", source="04,08"),
]

PROJECTS = [
    dict(id="ALPINE", name="ALPINE", start_year=2021, end_year=2025, source="12"),
    dict(id="MONSOON", name="MONSOON", start_year=2022, end_year=2027, source="13"),
    dict(id="CASCADE", name="CASCADE", start_year=2022, end_year=2025, source="14"),
    dict(id="RECLAIM", name="RECLAIM", start_year=2022, end_year=2027, source="15"),
]

PUBLICATIONS = [
    dict(id="P-DEG-2023", title="Sodium-Ion Cell Degradation Under Variable Grid Loads",
         short_title="Na-ion degradation (2023)", year=2023, source="22"),
    dict(id="P-CATH-2022", title="Sodium-Ion Cathode Stability in Solid-State Electrolytes",
         short_title="Cathode stability (2022)", year=2022, source="23"),
    dict(id="P-THERM-2024", title="Thermal Management Strategies for Stationary Batteries in Hot Climates",
         short_title="Thermal management (2024)", year=2024, source="24"),
    dict(id="P-PLF-2023", title="Probabilistic Load Forecasting with Gradient-Boosted Models",
         short_title="Probabilistic load forecasting (2023)", year=2023, source="25"),
    dict(id="P-HYDRO-2024", title="Hydrometallurgical Recovery of Sodium-Ion Cathode Materials",
         short_title="Hydrometallurgical recovery (2024)", year=2024, source="26"),
    dict(id="P-FAD-2025", title="Forecast-Aware Dispatch of Grid Batteries",
         short_title="Forecast-aware dispatch (2025)", year=2025, source="27"),
]

PATENTS = [
    dict(id="LSS-PAT-2020-114", name="LSS-PAT-2020-114",
         title="Layered Sodium-Ion Cell with Composite Electrolyte Interface", source="32"),
]

SITES = [
    dict(id="VPS", name="Vestfjord Pilot Site", country="Norway", source="28"),
    dict(id="TTB", name="Tiruvallur Test Bed", country="India", source="29"),
    dict(id="FVDS", name="Fraser Valley Demonstration Site", country="Canada", source="30"),
]

TECHNOLOGIES = [
    dict(id="SIB", name="Sodium-Ion Battery", source="33"),
    dict(id="LFP", name="Lithium Iron Phosphate Battery", source="30,33"),
    dict(id="SSE", name="Solid-State Electrolyte", source="23"),
    dict(id="TM", name="Thermal Management", source="34"),
    dict(id="LF", name="Load Forecasting", source="35"),
    dict(id="DEG", name="Battery Degradation Modelling", source="22,27"),
    dict(id="DISP", name="Battery Dispatch", source="27"),
    dict(id="REC", name="Battery Recycling", source="26"),
]

NODES = {
    "Organization": ORGANIZATIONS,
    "FundingAgency": FUNDING_AGENCIES,
    "Person": PERSONS,
    "Project": PROJECTS,
    "Publication": PUBLICATIONS,
    "Patent": PATENTS,
    "Site": SITES,
    "Technology": TECHNOLOGIES,
}

# ---------------------------------------------------------------------------
# RELATIONSHIPS: (from_label, from_id, REL_TYPE, to_label, to_id, {props})
# ---------------------------------------------------------------------------
O, F, P, PR, PUB, PAT, S, T = (
    "Organization", "FundingAgency", "Person", "Project", "Publication",
    "Patent", "Site", "Technology",
)

RELATIONSHIPS = [
    # Q1, Q5, Q8: who takes part in each project and with what role
    (O, "HIT", "PARTICIPATES_IN", PR, "ALPINE", dict(role="coordinator", role_detail="Coordinates the consortium")),
    (O, "RVU", "PARTICIPATES_IN", PR, "ALPINE", dict(role="materials", role_detail="Develops solid-state electrolytes")),
    (O, "LSS", "PARTICIPATES_IN", PR, "ALPINE", dict(role="manufacturing", role_detail="Manufactures the sodium-ion cells")),
    (O, "FJG", "PARTICIPATES_IN", PR, "ALPINE", dict(role="pilot operation", role_detail="Operates the Vestfjord pilot")),
    (O, "SPIS", "PARTICIPATES_IN", PR, "MONSOON", dict(role="coordinator", role_detail="Leads the project")),
    (O, "DPC", "PARTICIPATES_IN", PR, "MONSOON", dict(role="pilot operation", role_detail="Co-operates the Tiruvallur Test Bed")),
    (O, "MRU", "PARTICIPATES_IN", PR, "MONSOON", dict(role="modelling", role_detail="Foreign partner contributing modelling expertise")),
    (O, "MRU", "PARTICIPATES_IN", PR, "CASCADE", dict(role="coordinator", role_detail="Leads the project")),
    (O, "PCT", "PARTICIPATES_IN", PR, "CASCADE", dict(role="software integration", role_detail="Integrates the algorithms into commercial software")),
    (O, "HIT", "PARTICIPATES_IN", PR, "CASCADE", dict(role="degradation modelling", role_detail="Provides battery degradation models")),
    (O, "RVU", "PARTICIPATES_IN", PR, "RECLAIM", dict(role="coordinator", role_detail="Leads the work")),
    (O, "LSS", "PARTICIPATES_IN", PR, "RECLAIM", dict(role="industrial partner", role_detail="Supplies production scrap and used cells")),

    # Q1, Q5: funding
    (F, "ECEC", "FUNDS", PR, "ALPINE", dict(amount=4200000, currency="EUR", start_year=2021, end_year=2025)),
    (F, "ECEC", "FUNDS", PR, "RECLAIM", dict(amount=3100000, currency="EUR", start_year=2022, end_year=2027)),
    (F, "NSEI", "FUNDS", PR, "MONSOON", dict(amount=380000000, currency="INR", start_year=2022, end_year=2027)),
    (F, "CIF", "FUNDS", PR, "CASCADE", dict(amount=2800000, currency="CAD", start_year=2022, end_year=2025)),

    # Q2, Q4, Q6: affiliations (employment / study / visiting)
    (P, "ingrid_solberg", "AFFILIATED_WITH", O, "RVU", dict(type="study", role="Doctoral student", end=2005, current=False)),
    (P, "ingrid_solberg", "AFFILIATED_WITH", O, "HIT", dict(type="employment", role="Professor", start=2008, current=True)),
    (P, "markus_weber", "AFFILIATED_WITH", O, "RVU", dict(type="employment", role="Professor", current=True)),
    (P, "priya_raghunathan", "AFFILIATED_WITH", O, "SPIS", dict(type="employment", role="Associate Professor", current=True)),
    (P, "priya_raghunathan", "AFFILIATED_WITH", O, "MRU", dict(type="visiting", role="Visiting scholar (sabbatical)", start=2019, end=2019, current=False)),
    (P, "daniel_okafor", "AFFILIATED_WITH", O, "MRU", dict(type="employment", role="Professor", current=True)),
    (P, "elena_voss", "AFFILIATED_WITH", O, "RVU", dict(type="employment", role="Postdoctoral researcher", start=2015, end=2019, current=False)),
    (P, "elena_voss", "AFFILIATED_WITH", O, "LSS", dict(type="employment", role="Senior engineer, CTO since 2022", start=2019, current=True)),
    (P, "tomas_berg", "AFFILIATED_WITH", O, "HIT", dict(type="study", role="Doctoral student", end=2016, current=False)),
    (P, "tomas_berg", "AFFILIATED_WITH", O, "FJG", dict(type="employment", role="Lead storage engineer", start=2016, current=True)),
    (P, "katarina_novak", "AFFILIATED_WITH", O, "RVU", dict(type="employment", role="Senior researcher", current=True)),
    (P, "sofia_lindqvist", "AFFILIATED_WITH", O, "HIT", dict(type="study", role="Doctoral student", current=True)),
    (P, "arjun_menon", "AFFILIATED_WITH", O, "SPIS", dict(type="study", role="Doctoral student", current=True)),
    (P, "li_wei", "AFFILIATED_WITH", O, "MRU", dict(type="employment", role="Research scientist", current=True)),
    (P, "hannah_brooks", "AFFILIATED_WITH", O, "MRU", dict(type="study", role="Doctoral student", end=2018, current=False)),
    (P, "hannah_brooks", "AFFILIATED_WITH", O, "PCT", dict(type="employment", role="Head of software division", start=2018, current=True)),

    # Q3: doctoral supervision
    (P, "markus_weber", "SUPERVISED", P, "ingrid_solberg", dict(year=2005, status="completed")),
    (P, "ingrid_solberg", "SUPERVISED", P, "tomas_berg", dict(year=2016, status="completed")),
    (P, "ingrid_solberg", "SUPERVISED", P, "sofia_lindqvist", dict(status="ongoing")),
    (P, "daniel_okafor", "SUPERVISED", P, "hannah_brooks", dict(year=2018, status="completed")),
    (P, "priya_raghunathan", "SUPERVISED", P, "arjun_menon", dict(status="ongoing")),

    # Q2, Q6, Q10: authorship (position = author order)
    (P, "ingrid_solberg", "AUTHORED", PUB, "P-DEG-2023", dict(position=1)),
    (P, "sofia_lindqvist", "AUTHORED", PUB, "P-DEG-2023", dict(position=2)),
    (P, "tomas_berg", "AUTHORED", PUB, "P-DEG-2023", dict(position=3)),
    (P, "katarina_novak", "AUTHORED", PUB, "P-CATH-2022", dict(position=1)),
    (P, "ingrid_solberg", "AUTHORED", PUB, "P-CATH-2022", dict(position=2)),
    (P, "elena_voss", "AUTHORED", PUB, "P-CATH-2022", dict(position=3)),
    (P, "priya_raghunathan", "AUTHORED", PUB, "P-THERM-2024", dict(position=1)),
    (P, "arjun_menon", "AUTHORED", PUB, "P-THERM-2024", dict(position=2)),
    (P, "daniel_okafor", "AUTHORED", PUB, "P-THERM-2024", dict(position=3)),
    (P, "daniel_okafor", "AUTHORED", PUB, "P-PLF-2023", dict(position=1)),
    (P, "li_wei", "AUTHORED", PUB, "P-PLF-2023", dict(position=2)),
    (P, "hannah_brooks", "AUTHORED", PUB, "P-PLF-2023", dict(position=3)),
    (P, "markus_weber", "AUTHORED", PUB, "P-HYDRO-2024", dict(position=1)),
    (P, "katarina_novak", "AUTHORED", PUB, "P-HYDRO-2024", dict(position=2)),
    (P, "hannah_brooks", "AUTHORED", PUB, "P-FAD-2025", dict(position=1)),
    (P, "sofia_lindqvist", "AUTHORED", PUB, "P-FAD-2025", dict(position=2)),
    (P, "daniel_okafor", "AUTHORED", PUB, "P-FAD-2025", dict(position=3)),

    # Q2: publication -> project
    (PUB, "P-DEG-2023", "PRODUCED_IN", PR, "ALPINE", {}),
    (PUB, "P-CATH-2022", "PRODUCED_IN", PR, "ALPINE", {}),
    (PUB, "P-THERM-2024", "PRODUCED_IN", PR, "MONSOON", {}),
    (PUB, "P-PLF-2023", "PRODUCED_IN", PR, "CASCADE", {}),
    (PUB, "P-FAD-2025", "PRODUCED_IN", PR, "CASCADE", {}),
    (PUB, "P-HYDRO-2024", "PRODUCED_IN", PR, "RECLAIM", {}),

    # Q7: citations
    (PUB, "P-DEG-2023", "CITES", PUB, "P-CATH-2022", {}),
    (PUB, "P-HYDRO-2024", "CITES", PUB, "P-CATH-2022", {}),
    (PUB, "P-THERM-2024", "CITES", PUB, "P-DEG-2023", {}),
    (PUB, "P-FAD-2025", "CITES", PUB, "P-PLF-2023", {}),
    (PUB, "P-FAD-2025", "CITES", PUB, "P-DEG-2023", {}),

    # Q10: technology areas of each publication
    (PUB, "P-DEG-2023", "ADDRESSES", T, "SIB", {}),
    (PUB, "P-DEG-2023", "ADDRESSES", T, "DEG", {}),
    (PUB, "P-CATH-2022", "ADDRESSES", T, "SIB", {}),
    (PUB, "P-CATH-2022", "ADDRESSES", T, "SSE", {}),
    (PUB, "P-THERM-2024", "ADDRESSES", T, "TM", {}),
    (PUB, "P-THERM-2024", "ADDRESSES", T, "SIB", {}),
    (PUB, "P-PLF-2023", "ADDRESSES", T, "LF", {}),
    (PUB, "P-HYDRO-2024", "ADDRESSES", T, "REC", {}),
    (PUB, "P-HYDRO-2024", "ADDRESSES", T, "SIB", {}),
    (PUB, "P-FAD-2025", "ADDRESSES", T, "LF", {}),
    (PUB, "P-FAD-2025", "ADDRESSES", T, "DEG", {}),
    (PUB, "P-FAD-2025", "ADDRESSES", T, "DISP", {}),

    # Q9: patent -> technology -> site, plus the site's projects, operators and inventors
    (O, "LSS", "HOLDS", PAT, "LSS-PAT-2020-114", {}),
    (P, "elena_voss", "INVENTED", PAT, "LSS-PAT-2020-114", {}),
    (P, "katarina_novak", "INVENTED", PAT, "LSS-PAT-2020-114", {}),
    (PAT, "LSS-PAT-2020-114", "COVERS", T, "SIB", {}),
    (PAT, "LSS-PAT-2020-114", "COVERS", T, "SSE", {}),
    (PAT, "LSS-PAT-2020-114", "LICENSED_WITHIN", PR, "ALPINE", {}),
    (S, "VPS", "USES_TECHNOLOGY", T, "SIB", {}),
    (S, "TTB", "USES_TECHNOLOGY", T, "SIB", {}),
    (S, "TTB", "USES_TECHNOLOGY", T, "TM", {}),
    (S, "FVDS", "USES_TECHNOLOGY", T, "LFP", {}),
    (S, "FVDS", "USES_TECHNOLOGY", T, "LF", {}),
    (O, "HIT", "OPERATES", S, "VPS", {}),
    (O, "FJG", "OPERATES", S, "VPS", {}),
    (O, "SPIS", "OPERATES", S, "TTB", {}),
    (O, "DPC", "OPERATES", S, "TTB", {}),
    (O, "MRU", "OPERATES", S, "FVDS", {}),
    (O, "PCT", "OPERATES", S, "FVDS", {}),
    (S, "VPS", "ESTABLISHED_UNDER", PR, "ALPINE", {}),
    (S, "TTB", "ESTABLISHED_UNDER", PR, "MONSOON", {}),
    (S, "FVDS", "ESTABLISHED_UNDER", PR, "CASCADE", {}),
]
