'use strict';

angular.module('frontendApp')
  .controller('WishesCtrl', ['$scope', '$rootScope', '$timeout', 'Restangular', function ($scope, $rootScope, $timeout, Restangular) {
    var account = Restangular.one('accounts', $rootScope.account.slug);

    account.getList('wishes').then(function(response) {
      $scope.wishes = response;
    }, function(reason) {
      console.log(reason);
    });

    $scope.edit = function() {
      console.log('editing');
    };

    $scope.remove = function(index, wish) {
      wish.remove().then(function() {
        $scope.wishes.splice(index, 1);
      });
    };

  }]);