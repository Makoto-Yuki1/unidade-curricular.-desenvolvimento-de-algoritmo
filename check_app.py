from app import load_data

try:
    data = load_data()
    print('OK: menu=', len(data.get('menu', [])), 'orders=', len(data.get('orders', [])))
except Exception as e:
    print('ERROR:', type(e).__name__, e)
