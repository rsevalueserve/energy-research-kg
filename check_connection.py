"""Step 1: verify the Aura instance is reachable and show what it currently contains."""
from kg.db import get_database, get_driver


def main():
    with get_driver() as driver:
        driver.verify_connectivity()
        db = get_database()
        records, _, _ = driver.execute_query(
            "CALL dbms.components() YIELD name, versions, edition "
            "RETURN name, versions[0] AS version, edition",
            database_=db,
        )
        for r in records:
            print(f"Connected: {r['name']} {r['version']} ({r['edition']}), database '{db}'")
        records, _, _ = driver.execute_query(
            "MATCH (n) RETURN count(n) AS nodes", database_=db
        )
        nodes = records[0]["nodes"]
        records, _, _ = driver.execute_query(
            "MATCH ()-[r]->() RETURN count(r) AS rels", database_=db
        )
        print(f"Current contents: {nodes} nodes, {records[0]['rels']} relationships")


if __name__ == "__main__":
    main()
