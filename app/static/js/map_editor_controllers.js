var mapEditorControllers = angular.module('mapEditorControllers', ['mapEditorServices']);

/**
 * Home page controller.
 * @param $scope
 */
mapEditorControllers.controller('homeController', ['$scope', 
   function homeController($scope){
		$scope.category = 'home';
}]);

/**
 * Gallery page controller.
 * @param $scope
 */
mapEditorControllers.controller('galleryController', ['$scope', 
   function galleryController($scope){
		$scope.category = 'gallery';
}]);

/**
 * Controller that is used when about page is loaded.
 * @param $scope
 */
mapEditorControllers.controller('aboutController', ['$scope', 
  function aboutController($scope){
	$scope.category = 'about';
}]);

/**
 * Controller that is used when registration page is loaded.
 * @param $scope
 */
mapEditorControllers.controller('registerController', ['$scope', 
  function registerController($scope){
	
}]);

/**
 * Controller that is used when login page is loaded.
 * @param $scope
 */
mapEditorControllers.controller('loginController', ['$scope',
   function loginController($scope){

}]);

/**
 * Controller that handles registration of new user.
 * @param $scope
 * @param registerService
 */
mapEditorControllers.controller('doRegisterController', ['$scope', 'registerService',
    function doRegisterController($scope, registerService){
		$scope.submit = function() {
			registerService.save({
								   "username": $scope.username,
								   "password": $scope.password,
								   "password_retype": $scope.password_retype,
								   "first_name": $scope.first_name,
								   "last_name": $scope.last_name
								 }, 
								function(data){
									alert('registration successfull');
								}, 
								function(data) {
									alert('error');
								});
		}
}]);

/**
 * Controller that handles login of a user.
 * @param $scope
 * @param loginService
 */
mapEditorControllers.controller('doLoginController', ['$scope', 'loginService', '$location',
    function doLoginController($scope, loginService, $location){
		$scope.submit = function() {
			loginService.save({
								   "username": $scope.username,
								   "password": $scope.password
								 }, 
								function(data){
									$location.path('/home');
								}, 
								function(data) {
									alert('error');
								});
		}
}]);

/**
 * Controller that handles editing of specified map.
 * 
 * @param $scope
 * @param $routeParams
 * @param Map
 */
mapEditorControllers.controller('editPageController', ['$scope', '$routeParams', 'Map', '$http',
 function editPageController($scope, $routeParams, Map, $http){
	$scope.map = Map.query({'mapId': $routeParams.mapId}, function(data){
		$scope.mapName = data.name;
		$scope.color = 'blue';
		// indicates should there be an attempt to do smart selection
		$scope.smartSelection = true;
		$http.get(data.url).success(function(data){
			$("#svgMap").html(data);
			
			$("path").click(function(event) {
				var selectedId = '#' + event.currentTarget.id;
				var selectedElement = $(selectedId)[0];
				var parentElement = selectedElement;
				if ( $scope.smartSelection ) {
					if ( selectedElement.tagName == 'path' && selectedElement.parentElement.tagName == "g"  ) {
						selectedElement = selectedElement.parentElement;
					}
				}
				// select label to show for selected element
				if ( selectedElement.children.length == 0 ) {
					$scope.currentElement = selectedElement.id;
				}
				else {
					$scope.currentElement = selectedElement.children[0].textContent;
				}
				$scope.$digest();
				
				if ( selectedElement.tagName == "g" ) {
					var currentElements = selectedElement.children;
					
					var currentElements = selectedElement.children; 
					for (var i=0; i<currentElements.length; i++) {
						if ( currentElements[i].tagName == 'path' ) {
							currentElements[i].style.fill = $scope.color;
						}
					}
				}
				else {
					selectedElement.style.fill = $scope.color;
				}
			});
			
			$scope.colorSelected = function(color) {
				$scope.color = color;
			}
		});
	});
 }]);

/**
 * Controller that handles saving of new maps.
 * @param $scope
 * @param UserMap - service for working with user maps
 */
mapEditorControllers.controller('saveMapController', ['$scope', 'UserMap',
  function saveMapController($scope, UserMap){
	$scope.submit = function() {
		var urlParts = location.hash.split("/");
		if ( urlParts.length == 3 ) {
			var svgContent = $("#svgMap").html();
			var mapId = urlParts[2];
			UserMap.save({'svgContent': svgContent, "name": $scope.name, "mapId": mapId}, 
					function(data){
				
			}
			, function(data){
				
			})
		};
	}
}]);

/**
 * Controller that handles list of maps.
 * 
 * @param $scope
 * @param Maps
 */
mapEditorControllers.controller('listMapController', ['$scope', 'Maps',
   function editPageController($scope, Maps){
	$scope.maps = Maps.query();
}]);