var map_editor_app = angular.module('map_editor_app', ['ngRoute', 'mapEditorControllers']);

map_editor_app.config(['$routeProvider', 
    function($routeProvider){
		$routeProvider.when('/home', {
			templateUrl: 'partials/home.html',
			controller: 'homeController'
		}).when('/gallery', {
			templateUrl: 'partials/gallery.html',
			controller: 'galleryController'
		}).when('/about', {
			templateUrl: 'partials/about.html',
			controller: 'aboutController'
		}).when('/login', {
			templateUrl: 'partials/login.html',
			controller: 'loginController'
		}).when('/register', {
			templateUrl: 'partials/register.html',
			controller: 'registerController'
		}).when('/upload', {
			templateUrl: 'partials/upload.html'
		}).when('/list', {
			templateUrl: 'partials/list.html',
			controller: 'listMapController'
		}).when('/edit/:mapId', {
			templateUrl: 'partials/edit.html',
			controller: 'editPageController'
		}).otherwise({
			redirectTo: '/home'
		});
}]);