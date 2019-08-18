// Main JavaScript file for button callback
// Test button
$(function() {
    $('button#start').bind('click', function() {
      $.getJSON('/start_stream',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

$(function() {
    $('#kanji').bind('click', function() {
      $.getJSON('/load_kanji',
          function(data) {
        //do nothing
      });
      return false;
    });
});

$(function() {
    $('#hiragana').bind('click', function() {
      $.getJSON('/load_hiragana',
          function(data) {
        //do nothing
      });
      return false;
    });
});

$(function() {
    $('#english').bind('click', function() {
      $.getJSON('/load_english',
          function(data) {
        //do nothing
      });
      return false;
    });
});

$(function() {
    $('#random').bind('click', function() {
      $.getJSON('/load_random',
          function(data) {
        //do nothing
      });
      return false;
    });
});

$(function() {
    $('#print').bind('click', function() {
      $.getJSON('/print_df',
          function(data) {
        //do nothing
      });
      return false;
    });
});
