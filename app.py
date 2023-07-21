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
            
    def do_POST(self):
        if self.path == '/api/Postdata':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                # Convert the received JSON data to a Python dictionary
                data_dict = json.loads(post_data)

                # Insert the data into the MySQL database
                cursor = connection.cursor()
                query = "INSERT INTO employee (name, salary,Dept_id,last_name) VALUES (%s,%s,%s,%s)"
                values = (data_dict['name'], data_dict['salary'], data_dict['Dept_id'], data_dict['last_name'])
                cursor.execute(query, values)
                connection.commit()
                cursor.close()

                self._set_response(201, 'application/json')
                self.wfile.write(json.dumps({"message": "Data inserted successfully"}).encode('utf-8'))

            except json.JSONDecodeError:
                self._set_response(400, 'application/json')
                self.wfile.write(json.dumps({"error": "Invalid JSON data"}).encode('utf-8'))

        else:
            self._set_response(404, 'text/plain')
            self.wfile.write(b'Not Found')
            
        def do_Update(self):
            if self.path == '/api/udatedata':
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)

                try:
                    # Convert the received JSON data to a Python dictionary
                    data_dict = json.loads(post_data)

                    # Check if the "id" field exists in the received data
                    if 'id' not in data_dict:
                        self._set_response(400, 'application/json')
                        self.wfile.write(json.dumps({"error": "Missing 'name' field in the request data"}).encode('utf-8'))
                        return

                    # Check if the record with the given "id" exists in the database
                    cursor = connection.cursor()
                    query = "SELECT * FROM employee WHERE name = %s"
                    cursor.execute(query, (data_dict['name'],))
                    existing_record = cursor.fetchone()
                    cursor.close()

                    if not existing_record:
                        self._set_response(404, 'application/json')
                        self.wfile.write(json.dumps({"error": "Record with the given 'id' not found"}).encode('utf-8'))
                        return

                    # Update the existing record in the MySQL database
                    cursor = connection.cursor()
                    query = "UPDATE employee SET name = %s,  salary= %s,  Dept_id=%s ,last_name = %s WHERE  = %s"
                    values = (data_dict['name'], data_dict['salary'], data_dict['Dept_id'], data_dict['last_name'])
                    cursor.execute(query, values)
                    connection.commit()
                    cursor.close()

                    self._set_response(200, 'application/json')
                    self.wfile.write(json.dumps({"message": "Record updated successfully"}).encode('utf-8'))

                except json.JSONDecodeError:
                    self._set_response(400, 'application/json')
                    self.wfile.write(json.dumps({"error": "Invalid JSON data"}).encode('utf-8'))

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
