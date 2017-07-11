/*
 * ----------------------------------------------------------------------------------------
 *  SEARCH BAR
 * ----------------------------------------------------------------------------------------
 */
$(document).on('click', '.search-button', function(event){
  event.preventDefault();
  $(".search-wrapper").addClass("search-active");
  $(".search-input").focus();
});
$(document).on('click', '.search-close', function(event){
  event.preventDefault();
  $(".search-wrapper").removeClass("search-active");
});
