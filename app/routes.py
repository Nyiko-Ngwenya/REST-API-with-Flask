from app import app
from app.models import Character
from flask import request
from app import db
# https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/api/v1.0/characters',methods=['GET','POST'] )
def characters_list():
    if request.method == 'GET':
        Characters = Character.query.all()
        results = [
                {
                    "name": character.name,
                    "trait": character.trait,
                    "cost": character.cost
                } for character in Characters]
        return {"Characters":results}
    else:
        if request.is_json:
            data = request.get_json()
            new_character = Character(name=data['name'], trait=data['trait'], cost=data['cost'])
            db.session.add(new_character)
            db.session.commit()
            return {"message": f"Character {new_character.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    

@app.route('/api/v1.0/characters/<character_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_specific_characters(character_id):
    character = Character.query.get_or_404(character_id)

    if request.method == 'GET':
        response = {
            
                    "name": character.name,
                    "trait": character.trait,
                    "cost": character.cost
        }
        return {"message": "success", "character": response}

    elif request.method == 'PUT':
        data = request.get_json()
        character.name = data['name']
        character.trait = data['trait']
        character.cost = data['cost']
        db.session.add(character)
        db.session.commit()
        return {"message": f"car {car.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(character)
        db.session.commit()
        return {"message": f"Car {character.name} successfully deleted."}