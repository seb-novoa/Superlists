$(document).ready function(){
  var loginlink = document.getElementById('login');
  if(loginlink){
    loginlink.onclick = function(){ navigator.id.request();};
  }

  var logoutlink = document.getElementById('logout');
  if(logoutlink){
    logoutlink.onclick = function(){ navigator.id.request();};
  }

  var currentUser = '{{ user.email }}' || null;
  var csrf_token = ' {{ csrf_token }}';
  console.log(currentUser);

  navigator.id.watch({
    loggedInUser : currentUser,
    onlogin: function(assertion){
      $.post('/accounts/login', {assertion:assertion, csrfmiddlewaretoken: csrf_token})
      .done(function() { window.location.reload(); })
      .fail(function() { navigator.id.logout(); });
    },
    onlogout: function(){
      $.post('/accounts/logout')
      .always(function() { window.location.reload(); });
    }
  });
}
