# -*- coding: utf-8 -*-
from car_sales import app, db
from car_sales.model import  UsedStock, Users, CarSale
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand
import car_makes as makes
import car_models as models

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def insert_data():
    user = Users(first_name="James", last_name="Horan", email="horan5034@gmail.com", password="P@ssw0rd", is_active=True)

    db.session.add(user)

    # for make in makes.makes:
    #     db.session.add(make)
    for model in models.models:
        db.session.add(model)
    # for car in cars:
    #     db.session.add(car)
    db.session.commit()


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print 'Dropped the database'

if __name__ == '__main__':
    manager.run()
