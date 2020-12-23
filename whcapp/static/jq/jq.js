$(document).ready(function(){
  // Add smooth scrolling to all links
    $("a").on('click', function(event) {
        console.log('400000000000000000000000000000000000');
        if (this.hash !== "") {
        event.preventDefault();

        // Store hash
        var hash = this.hash;
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 1000, function(){
    
            window.location.hash = hash;
        });
        } // End if
    });
});
$(document).ready(function(){
    $("button").click(function(){
        $("#section1").fadeIn();
        });

    // $("button").click(function(){
    //     $("#section1").show();
    //     });
    });

