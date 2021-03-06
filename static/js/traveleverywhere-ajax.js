$(document).ready(function() {
    $('#like_btn').click(function() {
        var blogIdVar;
        blogIdVar = $(this).attr('data-blogid');
        $.post('/traveleverywhere/like_blog/', 
            {'blog_id': blogIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').addClass("disabled");
            })
    });
    $('#airline .like').click(function() {
        var airlineIdVar;
        airlineIdVar = $(this).attr('data-airlineid');
        $.post('/traveleverywhere/like_airline/',
            {'airline_id':airlineIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                $("#airline strong[data-airlineid='"+airlineIdVar+"'].rating_airline").html(data);
                $("#airline button[data-airlineid='"+airlineIdVar+"'].like").addClass("disabled");
                $("#airline button[data-airlineid='"+airlineIdVar+"'].dislike").removeClass("disabled");
            })
    });
    $('#airline .dislike').click(function() {
        var airlineIdVar;
        airlineIdVar = $(this).attr('data-airlineid');
        $.post('/traveleverywhere/dislike_airline/',
            {'airline_id':airlineIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                $("#airline strong[data-airlineid='"+airlineIdVar+"'].rating_airline").html(data);
                $("#airline button[data-airlineid='"+airlineIdVar+"'].dislike").addClass("disabled");
                $("#airline button[data-airlineid='"+airlineIdVar+"'].like").removeClass("disabled");
            })
    });
    $('#agency .like').click(function() {
        var agencyIdVar;
        agencyIdVar = $(this).attr('data-agencyid');
        $.post('/traveleverywhere/like_agency/',
            {'agency_id':agencyIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                $("#agency strong[data-agencyid='"+agencyIdVar+"'].rating_agency").html(data);
                $("#agency button[data-agencyid='"+agencyIdVar+"'].like").addClass("disabled");
                $("#agency button[data-agencyid='"+agencyIdVar+"'].dislike").removeClass("disabled");

            })
    });
    $('#agency .dislike').click(function() {
        var agencyIdVar;
        agencyIdVar = $(this).attr('data-agencyid');
        $.post('/traveleverywhere/dislike_agency/',
            {'agency_id':agencyIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                $("#agency strong[data-agencyid='"+agencyIdVar+"'].rating_agency").html(data);
                $("#agency button[data-agencyid='"+agencyIdVar+"'].dislike").addClass("disabled");
                $("#agency button[data-agencyid='"+agencyIdVar+"'].like").removeClass("disabled");
            })
    });
    $('#website .like').click(function() {
        var websiteIdVar;
        websiteIdVar = $(this).attr('data-websiteid');
        $.post('/traveleverywhere/like_website/',
            {'website_id':websiteIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                $("#website strong[data-websiteid='"+websiteIdVar+"'].rating_website").html(data);
                $("#website button[data-websiteid='"+websiteIdVar+"'].like").addClass("disabled");
                $("#website button[data-websiteid='"+websiteIdVar+"'].dislike").removeClass("disabled");
            })
    });
    $('#website .dislike').click(function() {
        var websiteIdVar;
        websiteIdVar = $(this).attr('data-websiteid');
        $.post('/traveleverywhere/dislike_website/',
            {'website_id':websiteIdVar,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            function(data) {
                $("#website strong[data-websiteid='"+websiteIdVar+"'].rating_website").html(data);
                $("#website button[data-websiteid='"+websiteIdVar+"'].dislike").addClass("disabled");
                $("#website button[data-websiteid='"+websiteIdVar+"'].like").removeClass("disabled");
            })
    });
    $('.quest-item').hover(function(){
        $(this).addClass("white-text");
        $(this).addClass("active");
        }, function(){
        $(this).removeClass("white-text");
        $(this).removeClass("active");
    });
    $('#airline').DataTable();
    $('#agency').DataTable();
    $('#website').DataTable();

});


    