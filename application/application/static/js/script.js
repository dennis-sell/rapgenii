var homeView = {
  'config' : {
    'signin_button' : $('#signin-button'),
    'signin_field' : $('#email-add')
  },
  //init function
  'init' :  function(config) {
    if (config && typeof(config) == 'object') {
          $.extend(myFeature.config, config);
      }

      // create and/or cache some DOM elements
      // we'll want to use throughout the code
      homeView.$signin = homeView.config.signin_button;
      homeView.$email = homeView.config.signin_field;
     
      //initialize event listeners
      var login = homeView.signin(homeView.$signin, homeView.$email);

      // not useful, but just for testing
      homeView.initialized = true;
  },
  //event listener for typing
  'signin' : function($signin, $email) {
    // set event listener for button
    $signin.click(function(){
      homeView.sendRequest($email);
    });
  },
  'sendRequest' : function($email) {
    $.post( "/signin", { 'email' : $email.val() } )
      .done(function( data ) {
        location.reload();
    });
  }
}

var mainView = {
  'config' : {
    'add_button' : $('#stress-button'),
    'add_field' : $('#stress-add'),
    'stress_container' : $('#singleFrustration'),
    'response_field': $('#response-add'),
    'response_button' : $('#response-button')
  },
  //init function
  'init' :  function(config) {
    if (config && typeof(config) == 'object') {
          $.extend(myFeature.config, config);
      }

      // create and/or cache some DOM elements
      // we'll want to use throughout the code
      mainView.$add = mainView.config.add_button;
      mainView.$stress = mainView.config.add_field;
      mainView.$single = mainView.config.stress_container;
      mainView.$response_field = mainView.config.response_field;
      mainView.$response_btn = mainView.config.response_button;

      //initialize event listeners
      var add_weight = mainView.addStress(mainView.$add, mainView.$stress);
      var add_response = mainView.addResponse(mainView.$response_btn, mainView.$response_field);
      var initialize_single = mainView.initSingle(mainView.$single);
      // not useful, but just for testing
      mainView.initialized = true;
  },

  'initSingle' : function($single) {
    $single.empty();
    $.get( "/get_stress", function( data ) {
      if (Object.getOwnPropertyNames(data).length === 0) {
        $single.append('<p>Luckily, there are no more weights to carry.</p>');
      } else {
        $single.append('<p class="q" id="' + data.id + '">' + data.question + '</p>');
      }
    });
  },

  'addResponse' : function($add, $response) {
    $add.click(function(){
      mainView.sendResponseRequest($response);
      return false;
    });
  },
  //event listener for typing
  'addStress' : function($add, $stress) {
    // set event listener for button
    $add.click(function(){
      mainView.sendPostRequest($stress);
      return false;
    });
  },
  'sendResponseRequest' : function($response) {
    $.post( "/add_response", { 'response' : $response.val(), 'id':$('.q').attr('id') } )
      .success(function( data ) {
        mainView.initSingle(mainView.$single);
    });
  },
  'sendPostRequest' : function($stress) {
    $.post( "/add_post", { 'question' : $stress.val() } )
      .success(function( data ) {
        $('#addFrustration').modal('hide')
    });
  }
}

