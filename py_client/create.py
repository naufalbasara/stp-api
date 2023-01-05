import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    'name': 'e-mobile',
    'product_class': 'Bus',
    'style': 'Vectors',
    'layout': 'Vectors',
    'frame': 'SUV Bus',
    'length': '300.00',
    'width': '130.00',
    'height': '120.00',
    'wheelbase': '90.12',
    'weight': '50.12',
    'battery_capacity': '100V',
    'charge_port': 'bottom',
    'port_location': 'rear',
    'voltage': '79',
    'charging_time': '15-16',
    'top_speed': 99,
    'electric_range': 70,
    'power': '90',
    'torque': '90',
    'drivetrain': '80',
    'category': 'Motorcycle',
    'rim': 'wheel',
    'front_tire': 'wheel',
    'rear_tire': 'wheel',
    'front_suspension': 'wheel',
    'rear_suspension': 'wheel',
    'front_brake': 'pop',
    'rear_brake': 'pop',
    'production_year': '2020-01-01',
    'price': 129
}
get_req = requests.post(endpoint, json=data)
print(get_req.json())