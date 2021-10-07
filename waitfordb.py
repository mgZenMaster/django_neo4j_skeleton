from neo4j import GraphDatabase
from neo4j.exceptions import ClientError, AuthError, ServiceUnavailable
from time import sleep

db_there = False
wait_seconds = 3

while not db_there:
    driver = GraphDatabase.driver("neo4j://db:7687", auth=("neo4j", "pass"))
    try:
        driver.verify_connectivity()
        db_there = True
    except AuthError:
        driver = GraphDatabase.driver("neo4j://db:7687", auth=("neo4j", "neo4j"))
        with driver.session(database="system") as session:
            try:
                session.run("CALL dbms.showCurrentUser();")
                db_there = True
            except ClientError as ex:
                print("Changing initial password.")
                if ex.code == 'Neo.ClientError.Security.CredentialsExpired':
                    session.run("ALTER CURRENT USER SET PASSWORD FROM 'neo4j' TO 'pass';")
        continue
    except ServiceUnavailable:
        print("Database is not there yet.")
        sleep(wait_seconds)
        continue
    except ValueError as ex:
        if ex.args[0].startswith("Cannot resolve address"):
            print("Database container db is not there yet.")
            sleep(wait_seconds)
            continue


