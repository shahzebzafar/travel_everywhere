$(document).ready(function() {
    $('#like_btn').click(function() {
        var blogIdVar;
        blogIdVar = $(this).attr('data-blogid');
        $.get('/traveleverywhere/like_blog/', 
            {'blog_id': blogIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
    $('#airline .like').click(function() {
        var airlineIdVar;
        airlineIdVar = $(this).attr('data-airlineid');
        airlineNameVar = $(this).attr('data-airlinename');
        $.post('/traveleverywhere/like/',
            {'airline_id':airlineIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                console.log(airlineIdVar)
                $("#airline strong[data-airlineid='"+airlineIdVar+"'].like_count").html(data);
                $("#airline button[data-airlineid='"+airlineIdVar+"'].like").hide();
            })
    });
    $('#airline').DataTable();
    $('#agency').DataTable();
    $('#website').DataTable();

});
function computeRating(likes, dislikes){
    return (likes/(likes+dislikes))*5;
}


    