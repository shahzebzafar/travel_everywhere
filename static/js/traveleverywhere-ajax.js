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
    $('#airline').DataTable();
    $('#agency').DataTable();
    $('#website').DataTable();
});

function computeRating(likes, dislikes){
    rating = (likes/(likes+dislikes))*5;
    return rating;
}
    