
用户管理
---------
1. member.create
输入
```
{
    "memberId":1,
    "email":"edc@edc.com",
    "userName":"edc",
    "password":"111111",
    "score":100,
    "isDeleted":<isDeleted>,
    "isEnabled":<isEnabled>,
    "createTime":2323323232,
    "myCode":"sdssdswewekj",    //我的邀请码
}
```
输出
```
{
    "desc":"success",
    "result":0,
    "content":{
        "memberId":1
    }
}
```
2. member.delete
输入
```
{
    "memberId":1
}
```
输出
```
{
    "desc":"success",
    "result":0
}
```
3. member.update
输入
```
{
    "memberId":1,
    "email":"edc@edc.com",
    "userName":"edc",
    "password":"111111",
    "score":100,
    "isDeleted":<isDeleted>,
    "isEnabled":<isEnabled>,
    "createTime":2323323232,
    "myCode":"sdssdswewekj",    //我的邀请码
}
```
输出
```
{
    "desc":"success",
    "result":0,
    "content":{
        "memberId":1
    }
}
```
4. member.get
输入
```
{
    "memberId":1
}
```
输出
```
{
    "desc":"success",
    "result":0,
    "content":{
	    "memberId":1,
	    "email":"edc@edc.com",
	    "userName":"edc",
	    "score":100,
	    "isDeleted":<isDeleted>,
	    "isEnabled":<isEnabled>,
	    "createTime":2323323232,
	    "myCode":"sdssdswewekj",    //我的邀请码
    }
}
```
5. member.getList
输入
```
{
    "limit":10,
    "offset":0
}
```
输出
```
{
    "desc":"success",
    "result":0,
    "content": {
        "total":10,
	    "items": [
			{
			    "memberId":1,
			    "email":"edc@edc.com",
			    "userName":"edc",
			    "score":100,
			    "isDeleted":<isDeleted>,
			    "isEnabled":<isEnabled>,
			    "createTime":2323323232,
			    "myCode":"sdssdswewekj",    //我的邀请码
		    },
			{
			    "memberId":1,
			    "email":"edc@edc.com",
			    "userName":"edc",
			    "score":100,
			    "isDeleted":<isDeleted>,
			    "isEnabled":<isEnabled>,
			    "createTime":2323323232,
			    "myCode":"sdssdswewekj",    //我的邀请码
		    }
	    ]
    }
}
```
6. member.enabled
输入
```
{
    "memberId":1,
    "isEnabled":1,
}
```
输出
```
{
    "desc":"success",
    "result":0
}
```
7. member.myInvitation
```
{
    "memberId":1,
}
```
输出
```
{
    "desc":"success",
    "result":0,
    "content": [
		{
		    "memberId":1,
		    "email":"edc@edc.com",
		    "userName":"edc",
		    "score":100,
		    "isDeleted":<isDeleted>,
		    "isEnabled":<isEnabled>,
		    "createTime":2323323232,
		    "myCode":"sdssdswewekj",    //我的邀请码
	    },
		{
		    "memberId":1,
		    "email":"edc@edc.com",
		    "userName":"edc",
		    "score":100,
		    "isDeleted":<isDeleted>,
		    "isEnabled":<isEnabled>,
		    "createTime":2323323232,
		    "myCode":"sdssdswewekj",    //我的邀请码
	    }
    ]
}
```

VIP管理
---------
1. vip.extensionByMoney    延期VIP充值
输入
```
{
    "memberId":1,
}
```
输出
```
{
    "desc":"success",
    "result":0
}
```

2. vip.extensionByScore    延期VIP积分兑换
输入
```
{
    "memberId":1,
}
```
输出
```
{
    "desc":"success",
    "result":0
}
```


积分管理
--------
1. score.get  查看积分
输入
```
{
    "memberId":1,
}
```
输出
```
{
    "desc":"success",
    "result":0,
    "content":{
        "score":100
    }
}
```

