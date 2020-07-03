## 启动应用

### 依赖

后端

* sqlite3
* python3.6
* django
* djangorestframework
* djangorestframework-jwt
* django-cors-headers

后端

* node
* angular9

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

## 后端接口

