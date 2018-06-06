var hide_error = function () {
  $('input').on("keypress", function() {
    $( ".has-error" ).hide();
  });
}

$(document).ready(function(){
  $('input').on('keypress', function(){
    $('.has-error').hide();
  });
});
