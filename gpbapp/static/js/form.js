$(document).ready(function(){
    
    $('form').on('submit', function(event) {

        $.ajax({
            url : '/process',
            data : {
                // the key will be used as value in "request.form" in views.py
                answer : $('#inlineFormInput').val(),
            },
            type : 'POST'
        })
        .done(function(data) {
            if (data.error){
                $('#answer').text(data.error).show()
            }
            else {
                $('#answer').text(data.answer).show()
            }
        });
    event.preventDefault();
    });

});