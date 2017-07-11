$(function(){

	/*
   * ----------------------------------------------------------------------------------------
   *  TYPEWRITER JS
   * ----------------------------------------------------------------------------------------
   */
	$("#typed").typed({
		strings: ["a Data Scientist.^500", "a Machine Learning Engineer.^1000", "Greg."],
		typeSpeed: 0,
    callback: function() {
      $(".sub-tagline").css("opacity", "1");
      $(".sub-tagline").css("margin", "0");
      $(".tagline").css("margin", "0");
    }
	});

	/*
   * ----------------------------------------------------------------------------------------
   *  PARTICLES JS
   * ----------------------------------------------------------------------------------------
   */
  // particlesJS.load(@dom-id, @path-json, @callback (optional));
  particlesJS.load('particles-js', "theme/particlesjs-config.json");

	/*
   * ----------------------------------------------------------------------------------------
   *  SMOOTH SCROLL JS
   * ----------------------------------------------------------------------------------------
   */
  $(document).on('click', '.smooth-scroll', function(event){
    event.preventDefault();
    $('html, body').animate({
      scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 1000);
  });

	/*
   * ----------------------------------------------------------------------------------------
   *  WORK JS
   * ----------------------------------------------------------------------------------------
   */
	var mixer = mixitup('.work-inner');

});
