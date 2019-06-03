function create_post(){
    console.log("create post is working")
    $.ajax({
        url : "create_post",
        type : "POST",
        data : {the_post : $('#post-content').val()},
        success : function(json){
            $('#post-content').val('');
            console.log(json);
            console.log("success");
        },

        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }

    });
    console.log($('#post-text').val())
};