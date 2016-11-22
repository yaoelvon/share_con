# 使用ng-admin管理REST API

[ng-admin](https://github.com/marmelab/ng-admin)是一个基于Angularjs的用于管理RESTFul API的GUI工具。

使用ng-admin配合RESTFul风格的后端API可以马上得到一个完整的管理界面，功能包括：数据表格（datagrid）、过滤器（filters）、复杂的表单控件（complex form widgets）、多模型关系（multi-model relationships）和仪表盘/概览（dashboard）。它不仅仅拥有简单的增删该查（CRUD）功能，在不影响其他开发进度的情况下，ng-admin能够很快帮助你构建一个复杂的图形用户界面。

1. 安装
2. 配置结构
3. 测试后端框架
4. 关联
5. 定制API映射

## 1.安装
当前的ng-admin版本（master分支）基于Angular.js 1.4。如果你需要兼容Angular 1.3，请使用ng-admin 0.9。

使用包管理工具npm或bower获取ng-admin：

```sh
npm install ng-admin —save
# 或
bower install ng-admin —save
```

将库文件ng-admin.min.css和ng-admin.min.js添加到HTML中，然后在`<body></body>中`增加`<div ui-view>`，最后对admin进行配置：

```html
<!doctype html>
<html lang=“en”>
  <head>
    <title>My First Admin</title>
    <link rel=“stylesheet” href=“node_modules/ng-admin/build/ng-admin.min.css”>
  </head>
  <body ng-app=“myApp”>
    <div ui-view></div>
    <script src=“node_modules/ng-admin/build/ng-admin.min.js”></script>
    <script type=“text/javascript”>
    var myApp = angular.module(‘myApp’, [‘ng-admin’]);
    myApp.config([‘NgAdminConfigurationProvider’, function(NgAdminConfigurationProvider) {
        var nga = NgAdminConfigurationProvider;
        // 创建一个管理应用
        var admin = nga.application(‘My First Admin’);
        // 之后的更多配置
        // ...
        // 将管理应用连接到DOM中，然后运行它
        nga.configure(admin);
    }]);
    </script>
  </body>
</html>
```

## 2.配置参考

在ng-admin中，admin是由包含多个*实体（entities)*的*应用*组成。每个实体（entity)拥有5种*视图*，每个视图拥有很多*字段（fields）*。

```
application
 |-header
 |-menu
 |-dashboard
 |-entity[]
    |-creationView
    |-editionView
    |-deletionView
    |-showView
    |-listView
        |-field[]
           |-name
           |-type
```

## 3.测试后端

我们会使用[json-server](https://github.com/typicode/json-server)构建一些RESTFul API，然后使用ng-admin将这些API管理起来。

## 4.支持关联

Ng-admin的读写视图实体之间支持‘关联’。它提供了特定的字段类型来实现这些‘关联’：`reference`, `referenced_list`, `reference_many`, 和 `embedded_list`。


## 5.定制API映射

ng-admin对REST API所做的所有HTTP请求都是由[Restangular](https://github.com/mgonto/restangular)执行的。

REST规范没有提供足够的详细信息来涵盖管理GUI的所有需求。 ng-admin对如何设计您的API进行了一些假设。 所有这些假设都可以通过[Restangular的请求和响应拦截器](https://github.com/mgonto/restangular#addresponseinterceptor)来覆盖。

这意味着你不需要为了ng-admin而调整你的API; ng-admin可以适应任何REST API，这要归功于Restangular的灵活性。
