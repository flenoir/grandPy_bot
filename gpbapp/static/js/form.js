$(document).ready(function(){

    var delay = 6000;
    
    $('form').on('submit', function(event) {
        // when clicked, we get value from form and send it as value in object data
        $.ajax({
            url : '/process',
            data : {
                // the key will be used as value in "request.form" in views.py
                answer : $('#inlineFormInput').val(),
            },
            type : 'POST',
            beforeSend: function(){
                $('#spinner').show();
                // $('#header').hide();
            },
            // on success, we push result from jsonify method form views.py on #answer div and show it
            success: function(data){
                $('#spinner').hide()                
                if (data.error){
                    $('#answer').text(data.error).show();
                }
                else {
                    $('#answer').text(data.answer1).show()
                    $('#map').html(data.map).show()
                    setTimeout(function(){
                        $('#answer').text(data.answer2).show();
                    }, delay);
                }
            }
        })
        
    event.preventDefault();
    });

});