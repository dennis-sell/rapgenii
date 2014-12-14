
var rapView = {
  'config' : {
    'upvote_button' : $('.up'),
    'downvote_button' : $('.down'),
  },
  'init' : function(config) {
    if (config && typeof(config) == 'object') {
          $.extend(rapView.config, config);
    }
    rapView.$upvote = rapView.config.upvote_button;
    rapView.$downvote = rapView.config.downvote_button;

    var upvote = rapView.upvote(rapView.$upvote);
    var downvote = rapView.downvote(rapView.$downvote);

    rapView.initialized = true;
  },
  'upvote' : function($upvote) {
    $upvote.click(function(){
      var line_id = $(this).parent().attr("id");
      console.log(line_id);
      rapView.sendRequest(line_id, "upvote", this); 
    });
  },
  'downvote' : function($downvote) { 
    $downvote.click(function(){
      var line_id = $(this).parent().attr("id");
      rapView.sendRequest(line_id, "downvote", this); 
    });
  },
  'sendRequest' : function(line_id, vote_type, vote_ele) {
    $.post( "/line/_" + vote_type, { 'lineID' : line_id } )
      .success(function( data ) {
        $vote = $(vote_ele);
        $vote.css({"color" : "red" });
    });
  }
}

