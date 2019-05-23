 // Initialize and add the map
 function initMap(data1, data2) {
    // The location of Uluru
    var uluru = {lat: data1, lng: data2};
    // The map, centered at Uluru
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 12, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
}

$(document).ready(function(){

    var delay = 8000;
    
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
                $('#inlineFormInput').val("");              
            },
            // on success, we push result from jsonify method form views.py on #answer div and show it
            success: function(data){
                $('#spinner').hide()                           
                if (data.error){
                    $('#answer').text(data.error).show();
                }
                else {
                    $('#answer').text(data.answer1).show()
                    // $('#map').html(data.map).show()
                    // initMap(data.map1, data.map2)
                    $('#map').show()
                    initMap(data.map1,data.map2);

                    setTimeout(function(){
                        $('#answer').text(data.answer2).show();
                    }, delay);
                }
            }
        })
        
    event.preventDefault();
    });

});