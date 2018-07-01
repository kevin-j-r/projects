import http.server
import socketserver



port = 8888 
resource_dir = "resources/" if os.exists("resources/") else "../core"




class mHandler(http.server.SimpleHTTPRequestHandler):

	def do_GET(self):
		
		print(str(self))
		self.wfile.write("hello world".encode("utf-8"))





server = socketserver.TCPServer(("127.0.01", port), mHandler)
server.serve_forever()


