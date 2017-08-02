# learnDjango

#三步来实现模型的变更：

1. 修改你的模型（在models.py中）。
2. 运行python manage.py makemigrations 来为这些修改创建迁移文件
3. 运行python manage.py migrate 以运用这些改变到数据库中。


#安装及启动app
1. 安装django
```
 pip install django
```
2. 创建project
```
 django-admin startproject memberSystem
```
3. 创建app
```
 cd memberSystem
 python manage.py startapp app
```
4. 创建model
 ```
class Member(models.Model):
    class Meta:
        verbose_name = '用户' #提供了一个更容易让人阅读的名称
        verbose_name_plural = '用户' #复数形式
    memberId = models.AutoField(primary_key=True) #models.IntegerField(auto_created=True)
    email = models.CharField(max_length=50, null=True)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True)
    score = models.IntegerField(null=True)
    isDeleted = models.BooleanField()
    isEnabled = models.BooleanField()
    createTime = models.DateTimeField()
    myCode = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.userName
 ```
5. 安装app
```
   INSTALLED_APPS = (
       ...
       'app',
   )
```
6. 注册到admin.py
```
from django.contrib import admin
from models import Member

# Register your models here.
admin.site.register(Member)

```

7. 使用mysql
创建数据库，支持中文中文
```
CREATE DATABASE memberSystem DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
```
配置数据库
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'memberSystem',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'sino@123.com',
    }
}
```
7. 创建管理员
```
python manage.py createsuperuser
```

8. 应用到数据库
```
python manage.py makemigrations
python manage.py migrate
```

9. 启动project
```
python manage.py runserver
```

#引入bootstrap
1. 安装bootstrap
```
pip install django-admin-bootstrapped
```

2. 修改setting.py
 ```
INSTALLED_APPS = (
    'django_admin_bootstrapped', #必须在django.contrib.admin之前
    'django.contrib.admin',
    ...
)
 ```

#引入markdown
1. 安装markdown
```
 pip install markdown
```

2. view修改
```
from markdown import markdown
def detail(request, id):
    article = models.Article.objects.get(id__exact=id)
    article.content = markdown(article.content)
    return render(request, 'template/detail.html', {'article': article})
```
3. 模板修改
```
{{ article.content|safe }}
```

#model导出为json
```
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr),datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr),datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                d[attr] = getattr(self, attr)

        import json
        return json.dumps(d)

```

10. json response
```
def api_members(request):
    members = Member.objects.all()
    jsonStrx = serializers.serialize('json', members)

    j = json.loads(jsonStrx)
    jsonStrx = json.dumps(j, indent=4)

    return HttpResponse(jsonStrx, content_type="application/json")

```

model配置技巧
---------
1. Meta,表名/对象名
2. 自增列,AutoField
3. 是否可以为空, null=True/False
4. 表单可以为空, black=True/False
5. 字段长度, max_length=50


总结
---------
1. 通过model，把展示APP与数据库关联起来
2. 通过view，把展示页面与数据库关联起来

