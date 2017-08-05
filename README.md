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


数据库处理
---------
```
增
models.Member.objects.create(userName='edc')

删
models.Member.objects.filter(userName='edc').delete()

改
models.Member.objects.filter(userName='edc').update(password='520')

查
models.Member.objects.get(userName='edc')
```




显示列表样式
---------
[参考](http://blog.csdn.net/wendysun0504/article/details/43758973)
```
from django.contrib import admin
from models import Member, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'userName', 'createTime', 'isReceiveOrder')
    search_fields = ('mobile', 'userName')

# Register your models here.
admin.site.register(Member)
admin.site.register(Order, OrderAdmin)

```

配置项
---------
```

LANGUAGE_CODE = 'zh_CN'  //管理后台配置成中文

TIME_ZONE = 'Asia/Shanghai'  //修改时区位上海

```


使用bootstrap样式
---------
1. 下载bootstrap文件到 app/static/目录
```
wget https://github.com/twbs/bootstrap/releases/download/v3.3.1/bootstrap-3.3.1-dist.zip
unzip bootstrap-3.3.1-dist.zip
```
2. 配置setting, 
```
STATIC_URL = '/static/'
```
3. 设置一个静态页面 bootstrap.html
```
<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="http://getbootstrap.com/favicon.ico">

    <title>Starter Template for Bootstrap</title>
    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
  
<div class="container-fluid">
  <div class="row-fluid">
    <div class="span12">
      <form>
        <fieldset>
          <legend>MY ORDER</legend> 
          <label>userName</label><input type="text" name="userName" /> <span class="help-block"> </span> 
          <label>mobile</label><input type="text" name="mobile" /> <span class="help-block"> </span> 
          <label>url</label><input type="text" name="url" /> <span class="help-block"> </span> 
          <label>desc</label><input type="text" name="desc" /> <span class="help-block"> </span> 
          <button class="btn" type="submit">提交</button>
        </fieldset>
      </form>
    </div>
  </div>
</div>

    <!-- jquery JavaScript -->
    <script src="/static/js/jquery.min.js"></script>
    <!-- Bootstrap core JavaScript -->
    <script src="/static/js/bootstrap.min.js"></script> 
  

</body></html>

```

Tips
---------
1. Django Admin 时间格式化
```
DATETIME_FORMAT = 'Y-m-d H:i:s'
```

