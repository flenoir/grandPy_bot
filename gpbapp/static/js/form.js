$(document).ready(function(){
    
    $('form').on('submit', function(event) {
        
        $.ajax({
            url : '/process',
            data : {
                // the key will be used as value in "request.form" in views.py
                answer : $('#inlineFormInput').val(),
            },
            type : 'POST',
            beforeSend: function(){
                $('#spinner').show();
            },
            success: function(data){
                $('#spinner').hide()
                if (data.error){
                    $('#answer').text(data.error).show()
                }
                else {
                    $('#answer').text(data.answer).show()
                }
            }
        })
        
    event.preventDefault();
    });

});