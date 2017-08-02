
# redis schema

标签（空格分隔）： member 

---

文档规范
称Redis每个数据结构为集或者集合，不要称为表
使用//表名注释，前后要各空一格，TODO加在注释中
在key中一般只能一个动态字段，少量部分有二个，动态字段必须放在key的最后部分
所有字段的命名必须保持统一
统一文本的书写Style，具体看一便就知晓
所有格式都是通过Notepad++来整理的，其他编辑器可能会有格式变化
分界线=========和子分界线---------长度都是9
bool类型统一是用整数0和1表示。0-false 1-true

公共字段
---------
```
isDeleted - 0-否；1-是
isEnabled - 0-否；1-是
hashes - member:generator:id
    memberId            <memberId>          //用户编号
    logId               <logId>             //日志编号
```

用户
```
sorted sets - member:vip:list  <expireDate> <memberId>   VIP用户
sorted sets - member:all:list  <timestamp> <memberId>   用户列表
sorted sets - member:follow <memberId> <memberId>   用户关系  <上级用户> <下级用户>
sorted sets - member:myCode <memberId> myCode  我的邀请码
hashes - member:detail:<memberId>
            "memberId":1,
            "email":"edc@edc.com",
            "userName":"edc",
            "password":"111111",
            "score":100,
            "isDeleted":<isDeleted>,
            "isEnabled":<isEnabled>,
            "createTime":2323323232,
            "myCode":"sdssdswewekj",    //我的邀请码
```

升级记录
```
sorted sets - member:log:List <memberId> <logId>  
hashes - member:log:detail:<logId>
    "logId":<logId>,
    "createTime":323332,
    "desc":"我升级了...",
    "jsonDesc":"json str"
```

