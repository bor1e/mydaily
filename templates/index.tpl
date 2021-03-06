<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="description" content="Personal Learning Compendium - Daily Learning. Learn in your own paste. Optimized for smartphone use.">
        <meta name="keywords" content="Chumasch, Rashi, Dailylearning, Chabad, Chabad.org, Rmabam, Tanach, HaYomYom">
        <meta name="author" content="Elyahu De">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Let's learn</title>
        <link rel="stylesheet" href="./css/bulma.min.css">
        <link rel="stylesheet" href="./css/fontawesome-all.min.css">
    </head>
    <body>
        {{!content}}
        <!-- progress bar -->
    </body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <!--script src="js/jquery-3.3.1.min.js"></script-->
  
    <script type="text/javascript">
     $(document).ready(function() {
        if (localStorage.getItem("scroll") != null) {
            $(window).scrollTop(localStorage.getItem("scroll"));
        }

        $(window).on("scroll", function() {
            localStorage.setItem("scroll", $(window).scrollTop());
        });
    });

    /*$('input[type="checkbox"]').on('click', function(){
		
	var data = {};
        data.name = $(this).attr('name');
        console.log(data.name);

        $.ajax({
            type: "POST",
            url: data.name,
            data: data,
        }).done(function(data) {
                console.log(data);
        });
    });*/


     function confirm() {
        alert('Thank you, your suggestions was received!')
     }
    </script>
</html>
