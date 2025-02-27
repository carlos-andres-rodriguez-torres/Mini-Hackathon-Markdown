jQuery(document).ready(function ($) {
  $('.dexp-container').find('.block-big-title').wrap('<div class="container">');
  $('.search-icon').click(function (e) {
    e.preventDefault();
    $(this).parent().find('.search-wrapper').show(0, function () {
      $(this).parent().find('.search-wrapper').find('input[type=text]').focus();
    });
  });
  $('.search-close').click(function () {
    $(this).closest('.search-wrapper').hide(0);
  });
  // Auto clear default value field NO MOLA!
  //$('.form-text,.form-textarea').cleardefault();
  // Tooltips
  $('.bs-example-tooltips').tooltip({
    selector: "[data-toggle=tooltip]",
    container: "body"
  });
  $('.dtooltip').tooltip({
    container: 'body'
  });
  $("#bs-example a").popover();

  $(".stat-count").each(function () {
    //alert('ok');
    $(this).data('count', parseInt($(this).html(), 10));
    $(this).html('0');
    count($(this));
  });

  /* links externs target _blank */

  $('a').filter(function() {
    return this.hostname && this.hostname !== location.hostname;
  }).addClass("external");

  $('a.external').attr('target' ,'_blank');

  /* per evitar el simbol external links a les imatges i icones*/
  $('a img').parent().addClass('linked-img');
  $('a i').parent().addClass('linked-img');

  /* per evitar el zoom sobre el mapa */

  $('#osm_map').hover(function(){
        stopScroll();}, function () {
        $('#osm_map iframe').css("pointer-events", "none");
      }
  );

  function stopScroll(){
    $('#osm_map').click(function () {
      $('#osm_map iframe').css("pointer-events", "auto");
    });
  }

  //Go to top
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('#go-to-top').css({
        bottom: "25px"
      });
    } else {
      $('#go-to-top').css({
        bottom: "-100px"
      });
    }
  });
  $('#go-to-top').click(function () {
    $('html, body').animate({
      scrollTop: '0px'
    }, 800);
    return false;
  });

  function scrollToAnchor(aid){
    var aTag = $('#'+aid+',a[name='+aid+']');
    $('html,body').animate({scrollTop: aTag.offset().top-120},'slow');
  }

  /* Salvar espai capcalera als anchors */
  $("a[href*='#']:not([href*='#dexp'])").click(function(){
    var href = $(this).attr('href');
    var arr = href.split('#');
    scrollToAnchor(arr[1]);
    return false;
  });

  if (window.location.hash) {
    desti = window.location.hash.split('#');
    scrollToAnchor(desti[1]);
  }


  //Masonry hover on ipad
  $('.dexp-masonry-item').hover(function () {
    $(this).find('.portfolio-item-inner').trigger('hover');
  });

  $('.scroll-down').click(function () {
    $('html, body').animate({
      scrollTop: $(window).height(),
    }, 800);
    return false;
  });
  //scroll collapsed
  $('a.collapsed').click(function(){
    var href = $(this).attr("data-parent");
    if($(href).offset() != null) {
        var scroll = $(href).offset().top;
        var offsetheader = 90;
        if (scroll < jQuery(document).scrollTop()) {
            jQuery("html, body").animate({scrollTop: scroll - offsetheader}, 250);
        }
    }
  });
});


function count($this) {
  var current = parseInt($this.html(), 10);
  current = current + 1; /* Where 50 is increment */

  $this.html(++current);
  if (current > $this.data('count')) {
    $this.html($this.data('count'));
  } else {
    setTimeout(function () {
      count($this)
    }, 50);
  }
}
jQuery.fn.cleardefault = function () {
  return this.focus(function () {
    if (this.value == this.defaultValue) {
      this.value = "";
    }
  }).blur(function () {
    if (!this.value.length) {
      this.value = this.defaultValue;
    }
  });
};
;
