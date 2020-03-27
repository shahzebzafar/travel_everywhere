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
        $.post('/traveleverywhere/like_airline/',
            {'airline_id':airlineIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                console.log(airlineIdVar)
                $("#airline strong[data-airlineid='"+airlineIdVar+"'].like_count").html(data);
                $("#airline button[data-airlineid='"+airlineIdVar+"'].like").hide();
            })
    });
    $('#agency .like').click(function() {
        var agencyIdVar;
        agencyIdVar = $(this).attr('data-agencyid');
        $.post('/traveleverywhere/like_agency/',
            {'agency_id':agencyIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                $("#agency strong[data-agencyid='"+agencyIdVar+"'].like_count").html(data);
                $("#agency button[data-agencyid='"+agencyIdVar+"'].like").hide();
            })
    });
    $('#airline').DataTable();
    $('#agency').DataTable();
    $('#website').DataTable();

});
function computeRating(likes, dislikes){
    return (likes/(likes+dislikes))*5;
}


    