from flask import Flask

def create_app():
    app = Flask(__name__)

    # 加载配置
    app.config.from_pyfile('../config.py')

    # 注册蓝图
    from .routes import bp
    app.register_blueprint(bp)

    return app
