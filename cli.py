import click
from database import session
from models import Vehicle

@click.group()
def cli():
    """Vehicle VIN Lookup System"""
    pass

@cli.command()
@click.option('--vin', prompt='Vehicle VIN', help='The VIN of the vehicle')
@click.option('--make', prompt='Vehicle Make', help='The make of the vehicle')
@click.option('--model', prompt='Vehicle Model', help='The model of the vehicle')
@click.option('--year', prompt='Vehicle Year', type=int, help='The year of the vehicle')
def add_vehicle(vin, make, model, year):
    """Add a new vehicle"""
    vehicle = Vehicle(vin=vin, make=make, model=model, year=year)
    session.add(vehicle)
    session.commit()
    click.echo(f'Added {vehicle}')

@cli.command()
@click.argument('vin')
def find_vehicle(vin):
    """Find a vehicle by VIN"""
    vehicle = session.query(Vehicle).filter_by(vin=vin).first()
    click.echo(vehicle if vehicle else 'Vehicle not found.')

@cli.command()
def list_vehicles():
    """List all vehicles"""
    vehicles = session.query(Vehicle).all()
    for vehicle in vehicles:
        click.echo(vehicle)

@cli.command()
@click.argument('vin')
def delete_vehicle(vin):
    """Delete a vehicle by VIN"""
    vehicle = session.query(Vehicle).filter_by(vin=vin).first()
    if vehicle:
        session.delete(vehicle)
        session.commit()
        click.echo(f'Deleted vehicle {vin}')
    else:
        click.echo('Vehicle not found.')

if __name__ == '__main__':
    cli()
