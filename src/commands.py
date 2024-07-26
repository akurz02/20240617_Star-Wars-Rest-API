
import click
import json
from models import db, Person, Planet

file_sample_characters = open('src/sample_characters')
file_sample_planets = open('src/sample_planets')
sample_characters = json.load(file_sample_characters)
sample_planets = json.load(file_sample_planets)

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with you database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """

    @app.cli.command("insert-test-planets")
    def renders_test_planets():
        max_count = 2
        print("Creating Star Wars planets) in database...")
        for x in range(0, max_count):
            planet = Planet()
            planet.name = sample_planets[x]["name"],
            planet.terrain = sample_planets[x]["terrain"],
            db.session.add(planet)
            db.session.commit()
            print("Planet: ", planet.name, " created.")

        print("All test planets created")
    

    @app.cli.command("insert-test-characters") 
    @click.argument("count") 
    def renders_test_characters(count):
        print("Creating Star Wars character(s) in database...")
        for x in range(0, int(count)):
            # print(sample_users[x])
            person = Person()
            person.name = sample_characters[x]["name"],
            person.homeworld = Planet.query
            db.session.add(person)
            db.session.commit()
            print("Person: ", person.name, " created.")

        print("All test users created")