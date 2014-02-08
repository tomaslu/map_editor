var mapEditorServices = angular.module('mapEditorServices', ['ngResource']);

mapEditorServices.factory('registerService', ['$resource', 
   function($resource){
		return $resource('/authentication/register/', {}, {
			save: {method: 'POST'},
			post: {method: 'POST'}
		});
}]);

mapEditorServices.factory('loginService', ['$resource', 
  function($resource){
	return $resource('/authentication/login/', {}, {
		save: {method: 'POST'},
		post: {method: 'POST'}
   		});
}]);

mapEditorServices.factory('Maps', ['$resource', 
   function($resource){
 	return $resource('/map/', {}, {
 		query: {method:'GET', isArray: true}
 	});
 }]);

mapEditorServices.factory('Map', ['$resource', 
   function($resource){
 	return $resource('/map/map/', {}, {
 		query: {method:'GET'}
 	});
 }]);

mapEditorServices.factory('UserMap', ['$resource', 
  function($resource){
	return $resource('/map/user_map/', {}, {
		query: {method:'GET'},
		post: {method: 'POST'}
	});
}]);