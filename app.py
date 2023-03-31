from flask import Flask, render_template
from datetime import datetime
# render_template :渲染模板
app = Flask(__name__)


def datetime_format(value, format='%Y年-%m月-%d日 %H:%M'):
    return value.strftime(format)


app.add_template_filter(datetime_format, 'dformat')


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route('/')
def hello_world():
    user = User('lqw', '123@126.com ')  # 对象形式
    person = {                          # 字典形式 访问可以person['username'],也可以person.username
        'username': '张三',
        'email': 'zhangsan@qq.com'
    }

    return render_template('index.html', user=user, person=person)


@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template('blog_detail.html', blog_id=blog_id)


@app.route('/filter')
def filter_demo():
    user = User(username='lqw', email='123@qq.com')
    mytime = datetime.now()
    return render_template('filter.html', user=user, mytime=mytime)  # 过滤器，使用管道符，jinja2内置过滤器不够时可以自定义过滤器


@app.route('/control')
def control_statement():
    age = 18
    books = [
        {'name': '三国演义',
            'author': '罗贯中'},
        {'name': '水浒传',
            'author': '施耐庵'},
        {'name': '西游记',
            'author': '吴承恩'}
    ]
    return render_template('control.html', age=age, books=books)


@app.route('/child1')
def child1():
    return render_template('child1.html')


@app.route('/child2')
def child2():
    return render_template('child2.html')


@app.route('/static')  # 加载静态文件，包括图片、css文件、js文件
def static_demo():
    return render_template('static.html')


if __name__ == '__main__':
    app.run(debug=True)
