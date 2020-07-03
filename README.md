### 创建用户

```shell script
python manage.py createsuperuser --email admin@example.com --username admin
```

### 管理数据

```shell script
python manage.py shell 
```

```python3
from backend.models import Student 
s = Student.objects.all() 
```