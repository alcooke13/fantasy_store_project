# Fantasy Store Project

Flask application where the user is managing a store selling products usually found in a fantasy setting.</br>

Technologies used: </br>
- Python
- Flask
- HTML
- JINJA
- CSS

Brief</br>
This was an individual project that the class had to do to combine all the things we've learned from the first four weeks at CodeClan. So I decided on creating an app managing a store in a fantasy setting.

MVP</br>
User is a merchant selling products

Products include a variety of weapons, potions, armors. </br>
- Each product will have a name, description, cost, price, product type
- Different manufacturers supplying each product type.
- Each manufacturer on a product type will have a name and location.
- Have a visual indicator on how healthy stock is (good / low / out of stock)

NOTE</br>
Unfortunately I was not able to add the different manufacturers that I had originally planned. It was more complicated to implement than I initially thought so with the limited time I had remaining I decided to leave manufacturer's
out from this version and instead focus on having a more polished products section and perhaps revisit this and finalise everyting at another time. </br>

I've decided not to update this exact version of the project, and instead build a new and complete version with different tools.
Fantasy Store V2: https://github.com/alcooke13/Fantasy_StoreV2

Extensions
- Calculate markup and display for each product
- Ability to filter inventory

Installation Guide</br>
Will be required to run this
- Python3
- PostgreSQL
- Flask

In the terminal:
```python
createdb store_inventory
psql -d store_inventory -f db/store_inventory.sql
python3 console.py
```
This will create the database and feed in starting values to the tables in the database.

```python
flask run
```
To run the app </br>

To view the app visit:
http://127.0.0.1:4999
