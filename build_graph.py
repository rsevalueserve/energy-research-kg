"""
Step 2: build the Knowledge Graph in Neo4j Aura from kg/data.py.

    python build_graph.py           # idempotent MERGE load
    python build_graph.py --reset   # wipe the database first, then load
"""
import argparse
from collections import defaultdict

from kg.data import NODES, ORGANIZATIONS, RELATIONSHIPS
from kg.db import get_database, get_driver

# Secondary labels for organizations (whitelisted: labels cannot be query parameters)
ORG_TYPE_LABELS = {"University", "ResearchInstitute", "Company", "Utility"}


def create_constraints(driver, db):
    for label in NODES:
        driver.execute_query(
            f"CREATE CONSTRAINT {label.lower()}_id IF NOT EXISTS "
            f"FOR (n:{label}) REQUIRE n.id IS UNIQUE",
            database_=db,
        )


def load_nodes(driver, db):
    for label, rows in NODES.items():
        driver.execute_query(
            f"UNWIND $rows AS row MERGE (n:{label} {{id: row.id}}) SET n += row",
            rows=rows, database_=db,
        )
        print(f"  {label:<14} {len(rows):>3} nodes")
    for org_type in ORG_TYPE_LABELS:
        ids = [o["id"] for o in ORGANIZATIONS if o["type"] == org_type]
        driver.execute_query(
            f"MATCH (o:Organization) WHERE o.id IN $ids SET o:{org_type}",
            ids=ids, database_=db,
        )


def load_relationships(driver, db):
    groups = defaultdict(list)
    for from_label, from_id, rel, to_label, to_id, props in RELATIONSHIPS:
        groups[(from_label, rel, to_label)].append(
            {"from": from_id, "to": to_id, "props": props}
        )
    for (from_label, rel, to_label), rows in groups.items():
        assert from_label in NODES and to_label in NODES and rel.replace("_", "").isalpha()
        summary = driver.execute_query(
            f"UNWIND $rows AS row "
            f"MATCH (a:{from_label} {{id: row.from}}) "
            f"MATCH (b:{to_label} {{id: row.to}}) "
            f"MERGE (a)-[r:{rel}]->(b) SET r += row.props "
            f"RETURN count(r) AS n",
            rows=rows, database_=db,
        )
        matched = summary.records[0]["n"]
        if matched != len(rows):
            raise RuntimeError(f"{rel}: expected {len(rows)} relationships, matched {matched} "
                               f"(check ids in kg/data.py)")
        print(f"  ({from_label})-[:{rel}]->({to_label}) x{len(rows)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="delete all nodes first")
    args = parser.parse_args()

    db = get_database()
    with get_driver() as driver:
        driver.verify_connectivity()
        if args.reset:
            driver.execute_query("MATCH (n) DETACH DELETE n", database_=db)
            print("Database cleared.")
        create_constraints(driver, db)
        print("Loading nodes...")
        load_nodes(driver, db)
        print("Loading relationships...")
        load_relationships(driver, db)
        records, _, _ = driver.execute_query(
            "MATCH (n) WITH count(n) AS nodes "
            "MATCH ()-[r]->() RETURN nodes, count(r) AS rels",
            database_=db,
        )
        print(f"Done: {records[0]['nodes']} nodes, {records[0]['rels']} relationships in graph.")


if __name__ == "__main__":
    main()
