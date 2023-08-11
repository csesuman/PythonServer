from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, headers=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        if headers:
            for key, value in headers.items():
                self.send_header(key, value)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            parsed_data = json.loads(post_data.decode('utf-8'))
            self._set_response()

            response_data = {
                'message': 'Request data received successfully',
                'data': parsed_data
            }

            response_json = json.dumps(response_data)
            self.wfile.write(response_json.encode('utf-8'))

            # Print the JSON body of the request
            print(json.dumps(response_data, indent=4))
            # print("Received JSON body:", json.dumps(parsed_data, indent=4))

        except Exception as e:
            self._set_response(status_code=400)
            error_response = {
                'error': 'Invalid JSON data',
                'details': str(e)
            }
            self.wfile.write(json.dumps(error_response, indent=4).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
