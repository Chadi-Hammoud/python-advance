import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import mysql.connector

# Replace these values with your MySQL database credentials
db_host = 'localhost'
db_user = 'root'
db_password = 'root'
db_name = 'UBILITY_DB'

# Sample data for the API
# data = [
#     {"id": 1, "name": "John Doe", "age": 30},
#     {"id": 2, "name": "Jane Smith", "age": 25},
#     {"id": 3, "name": "Michael Johnson", "age": 40}
# ]
data=[
{"id":1, "name":'chadi'   ,"salary": 25000,"Dept_id": 201, "last_name":'alex'},
{"id":2, "name": 'Hammoud',"salary":2500 , "Dept_id": 201, "last_name":'lastname'},
{"id":3, "name": 'Hammoud',"salary": 2500 ,"Dept_id": 201, "last_name":'lastname'},
{"id":4, "name": 'Hammoud',"salary": 2500 ,"Dept_id": 201, "last_name": 'lastname'},
{"id":5, "name": 'John'   ,"salary": 25000,"Dept_id": 201, "last_name":'Newyork'}
]

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# Define the API handler
class MyAPIHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/data':
            self._get_all_data()
        else:
            self._set_response(404, 'text/plain')
            self.wfile.write(b'Not Found')

    def _get_all_data(self):
        # Fetch data from MySQL database
        cursor = connection.cursor()
        query = "SELECT * FROM employee"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        # Convert the result to a list of dictionaries
        data_from_db = [{"id": row[0], "name": row[1], "salary": row[2], "Dept_id":row[3], "last_name":row[4]} for row in result]

        # Merge the database data with the sample data
        merged_data = data + data_from_db

        self._set_response()
        self.wfile.write(json.dumps(merged_data).encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyAPIHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
