// 声明一个新的模块，并依赖ng-admin
var app = angular.module('myApp', ['ng-admin']);

// 在模块启动过程中（config过程）声明一个函数运行
app.config(['NgAdminConfigurationProvider', function (nga) {
    // 创建一个admin应用对象
    var admin = nga.application('我的应用')
                   .baseApiUrl('http://localhost:3000/');

    //创建一个仓库实体
    var warehouse = nga.entity('warehouses');
    warehouse.label('仓库');

    //设置仓库实体的列表页面显示的字段信息
    warehouse.listView()
        .fields([
            nga.field('name')
               .isDetailLink(true)
               .label('名称'),
            nga.field('address').label('地址'),
            nga.field('contact').label('联系人')
        ])
        .filters([
            nga.field('q')
                .label('搜索')
                .pinned(true)
                .template('<div class="input-group"><input type="text" ng-model="value" placeholder="通过名称进行搜索" class="form-control"></input><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span></div>')
        ])
        .title('仓库信息');

    warehouse.showView()
        .fields([
            nga.field('name').label('名称'),
            nga.field('address').label('地址'),
            nga.field('contact') .label('联系人')       
        ])
        .title('显示仓库信息');

	warehouse.creationView()
        .fields([
    	    nga.field('name').label('名称'),
    	    nga.field('address').label('地址'),
    	    nga.field('contact').label('联系人')
	    ])
        .title('创建仓库');

    warehouse.editionView()
        .fields(warehouse.creationView().fields())
        .title('编辑仓库');

    // 将仓库实体加到admin应用
    admin.addEntity(warehouse);


    var user = nga.entity('user');

    user.listView()
        .fields([
            nga.field('name')
               .isDetailLink(true)
               .label('名称'),
            nga.field('tel').label('电话'),
            nga.field('sex').label('性别')
        ])
        .filters([
            nga.field('q')
                .label('搜索')
                .pinned(true)
                .template('<div class="input-group"><input type="text" ng-model="value" placeholder="通过名称进行搜索" class="form-control"></input><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span></div>')
        ])
        .title('用户信息');

    user.creationView()
         .fields(user.listView().fields())
        .title('创建用户');

    user.editionView()
         .fields(user.listView().fields())
        .title('编辑用户');

    // 将仓库实体加到admin应用
    admin.addEntity(user);

    // 将管理应用连接到DOM中，然后运行它
    nga.configure(admin);

}]);

// API映射
app.config(['RestangularProvider', function (RestangularProvider) {
    // use the custom query parameters function to format the API request correctly
    RestangularProvider.addFullRequestInterceptor(function(element, operation, what, url, headers, params) {
        if (operation === 'getList') {
            // 自定义分页参数
            // if (params._page) {
            //     var start = (params._page - 1) * params._perPage;
            //     var end = params._page * params._perPage - 1;
            //     params.range = "[" + start + "," + end + "]";
            //     delete params._page;
            //     delete params._perPage;
            // }

            // // 自定义排序参数
            // if (params._sortField) {
            //     params.sort = '["' + params._sortField + '","' + params._sortDir + '"]';
            //     delete params._sortField;
            //     delete params._sortDir;
            // }

            // 自定义过滤项 = {'q': '...'}
            if (params._filters) {
                // params.filter = params._filters;
                params.name = params._filters.q;
                delete params._filters;
            }
        }
        return { params: params };
    });

    RestangularProvider.addResponseInterceptor(function(data, operation, what, url, response) {
        if (operation === "getList") {
            var headers = response.headers();
            if (headers['content-range']) {
                response.totalCount = headers['content-range'].split('/').pop();
            }
        }

        return data;
    });
}]);
