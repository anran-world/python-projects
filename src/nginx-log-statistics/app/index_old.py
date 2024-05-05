# 导入 http.server 模块
import http.server
import socketserver


# 定义请求处理程序
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 设置响应头
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # 返回响应内容
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")


def main():
    # 定义服务器地址和端口
    host = "localhost"
    port = 8000

    # 创建一个 HTTP 服务器对象，并指定请求处理程序
    with socketserver.TCPServer((host, port), MyHandler) as server:
        print("Server started at http://{}:{}".format(host, port))
        # 持续监听请求
        server.serve_forever()


if __name__ == '__main__':
    main()
