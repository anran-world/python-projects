from flask import Blueprint
from .utils import read_file

bp = Blueprint('main', __name__)

# 首页
@bp.route('/')
def index():
    return 'Hello, World!'


@bp.route('/getData')
def getData():
    # 读取文件
    return read_file()