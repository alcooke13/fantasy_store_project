Fantasy Store Management

Flask application where the user is managing a store selling products usually found in a fantasy setting.

The technologies used:
- Python
- Flask
- HTML
- JINJA
- CSS

Brief
This was an individual project that the class had to do to combine all the things we've learned from the first four weeks at CodeClan. So I decided on creating an app managing a store in a fantasy setting. 

MVP
User is a merchant selling items

Products include a variety of weapons, potions, armors
    Which tracks: NAME | DESCRIPTION | COST | PRICE | PRODUCT TYPE | STOCK

Different manufacturers supplying each product type
    Which tracks : NAME | LOCATION

Have a visual indicator on how healthy stock is (good / low / out of stock)

NOTE
    Unfortunately I was not able to add the different manufacturers that I had originally planned. It was a lot more complicated to implement than I thought it would be at the beginning of my project. Instead of half baked everything I focused on have a more polished products section and leave out manufacturers for this project.
    However from finishing this project and taking in what I've learned I plan to continue developing this web app to include what I wasn't able to in this version. 
END NOTE

Extensions

Calculate markup and display for each product
Ability to filter inventory

Installation
- Python3
- PostgreSQL
- Flask
Will be required to run this

In the terminal:
```python
createdb store_inventory
psql -d store_inventory -f db/store_inventory.sql
python3 console.py
```

This will create the database and feed in starting values to the tables in the database.

To run the app
```python
flask run
```
To view the app visit:
http://127.0.0.1:4999
