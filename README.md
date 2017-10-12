# 周报系统 #

[![python3.x](https://img.shields.io/badge/python-3.X-brightgreen.svg)](https://www.python.org/)
[![django](https://img.shields.io/badge/django-1.11.4-brightgreen.svg)](https://www.djangoproject.com/)
[![django-rest-framework](https://img.shields.io/badge/djangorestframework-3.6.3-brightgreen.svg)](http://www.django-rest-framework.org/)
[![django-rest-framework-jwt](https://img.shields.io/badge/djangorestframeworkjwt-1.11.0-brightgreen.svg)](https://github.com/GetBlimp/django-rest-framework-jwt)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/itimor/report-frontend/blob/master/LICENSE)

**周报系统是采用的前后端分离开发，本项目是周报系统的后端** [点我到前端](https://github.com/itimor/report-frontend.git)

**注意：该项目支持python2.7X和python3.X**

**注意：周报系统使用 `django rest framework` 提供的restful API功能进行开发，后端主要提供api数据支持，前端负责路由和页面渲染，访问正常页面请配和使用前端项目** 

## 功能
- 登录/注销
- 权限验证
- 用户管理
- 角色管理
- 权限管理
- 周报管理

## 开发
```bash
    # 克隆项目
    git clone https://github.com/itimor/weekReport.git

    # 安装依赖
    cd weekReport
   pip install -r requirements.txt
 
    #初始化数据库
    python manage.py migrate
    
    #创建admin用户
    python manage.py createsuperuser 
    
    #启动
    python manage.py runserver 0.0.0.0:8000

```
浏览器访问API `http://localhost:8000/api/`， 若前端项目已经部署好，可以直接访问前端

## 效果图

### api界面


### 前端界面


## 目录结构
```shell
├── LICENSE
├── manage.py
├── README.md
├── requirements.txt
├── statics
├── upload
└── utils

```

## 待开发功能
- [ ] 
