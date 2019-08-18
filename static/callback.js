// Main JavaScript file for button callback
// Test button
$(function() {
    $('button#kanji').bind('click', function() {
      $.getJSON('/load_kanji',
          function(data) {
        //do nothing
      });
      return false;
    });
});

$(function() {
    $('button#hiragana').bind('click', function() {
      $.getJSON('/load_hiragana',
          function(data) {
        //do nothing
      });
      return false;
    });
});

$(function() {
    $('button#english').bind('click', function() {
      $.getJSON('/load_english',
          function(data) {
        //do nothing
      });
      return false;
    });
});

$(function() {
    $('button#random').bind('click', function() {
      $.getJSON('/load_random',
          function(data) {
        //do nothing
      });
      return false;
    });
});

$(function() {
    $('button#print').bind('click', function() {
      $.getJSON('/print_df',
          function(data) {
        //do nothing
      });
      return false;
    });
});
