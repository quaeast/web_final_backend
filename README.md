# web 期末大作业：北京林业大学夏令营报名系统

本系统后端使用 django rest framework 开发 REST 风格 API，使用 JWT 对 API 进行保护，以 sqlite3 作为数据库。前端以 Angular 9 作为基础框架，使用阿里开发的 Ant Design 组件库进行辅助开发。

项目代码同时步放在了 github 上：[前端](https://github.com/quaeast/web-final-ui)、[后端](https://github.com/quaeast/web_final_backend)

系统目前运行在我的阿里云服务器上 [阿里云](http://39.96.177.143/)

实现功能如下：

* 用户注册、登录
* 用户分级管理
* 信息公告和通知
* 学生报名功能
* 学生管理

## 依赖

### 后端

* sqlite3
* nginx
* python3.6
* django
* djangorestframework
* djangorestframework-jwt
* django-cors-headers
* usgi

### 前端

* node
* angular9
* Ant-Design: ng-zorro

## 启动测试 / 部署

### 后端

```shell script
# 安装环境
pip install -r requirements.txt

# 初始化项目
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser --email admin@example.com --username admin

# 管理数据
python manage.py shell 
```

```python3
from backend.models import Student 
s = Student.objects.all() 
```

### 前端

```shell script
# 安装 angular 客户端
npm install -g @angular/cli@9

# 安装依赖
npm install

# 开发环境测试
ng run serve

# 生产环境编译
ng build --prod
```

nginx 部署

```
location / {
    root /home/user/homepage;
    index index.html;
    try_files $uri $uri/ /index.html;
}
```

## 前端使用

### /login

正常登陆界面，面向广大用户

### 8000:/admin

系统管理员界面，面向招生办工作人员，在内网使用

管理员创建：

```shell script
python manage.py createsuperuser --username=username --email=user@example.com
```

## REST 接口

| 名称 | 动作 | 功能  | 测试   |
| ------ | ---- | ---- | ----- |
| api-token-auth   | POST | 登陆，获取 token     | api_test.user_test.get_token       |
| api-token-verify | POST | 验证 token           | api_test.user_test.verify_token    |
| logon            | POST | 创建用户             | api_test.user_test.create_user     |
| users            | GET  | 获取所有学生信息     | api_test.user_test.get_users       |
| student          | GET  | 当前登陆学生获取信息 | api_test.student_test.get_student  |
| student          | POST | 当前登陆学生提交信息 | api_test.student_test.post_student |

