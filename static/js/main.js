jQuery.fn.my_tooltip = function(options) {
    var options = jQuery.extend({
        'fadeIn': 300,
        'fadeOut': 300,
        'left': 20,
        'top': 40
    }, options);
    return this.each(function() {
        var $elem = this;
        var div_id = $($elem).attr('data-id');
        var position = $($elem).position();
        $(div_id).css({
            'left': position.left + options.left + 'px',
            'top': position.top + options.top + 'px'
        });
        $($elem).mouseover(function() {
            $(div_id).fadeIn(options.fadeIn);
        });
        $($elem).mouseout(function() {
            $(div_id).fadeOut(options.fadeOut);
        });
    });
};

var cf = {
    names: [],
    set: function(obj) {
        var found = false;
        var name = $(obj).attr('name');
        var val = $(obj).val();
        for (var k in this.names) {
            if (k == name) {
                found = true;
                break;
            }
        }
        if (found) {
            if (this.names[name] == val) {
                $(obj).val('');
            }
        }
        else {
            this.names[name] = val;
            $(obj).val('');
        }
    },
    get: function(obj) {
        var name = $(obj).attr('name');
        if ($(obj).val() == '') {
            $(obj).val(this.names[name]);
        }
    }
};

var slide = {
    timer: null,
    current: -1,
    data: new Array(),
    fade: 100,
    interval: 5000,
    rand: function() {
        return '?' + Math.floor(Math.random()*10000000);
    },
    image: function(img) {
        this.data.push(img);
    },
    set: function() {
        $this = slide;
        if ($this.current >= ($this.data.length - 1)) {
            $this.current = -1;
        }
        $this.current = $this.current + 1;
        $('#id_news_image').fadeOut($this.fade);
        $('#id_news_image').hide();
        $('#id_news_image').attr('src', $this.data[$this.current]);
        $('#id_news_image').fadeIn($this.fade);
    },
    init: function() {
        this.set();
        this.timer = window.setInterval(this.set, this.interval);
    }
};

var gallery = {
    set: function(img) {
        $('#big_picture').attr('src', img);
    }
};

var LANG = {
    set: function (ln) {
        jQuery.ajax({
            type: 'get',
            url: '/language/set/?ln='+ln,
            data: '',
            dataType: 'json',
            success: function(data, status) {
                if (data.error == 0) {
                    document.location = document.location;
                }
            },
            error: function(data, status, e) {
                alert(e);
            }
        });
    }
};

var Imgs = {
    images: {},
    add: function(id) {
        this.images[id] = 2;
    },
    view: function(id) {
        var f = 1000;
        $('#img1_'+id).hide();
        $('#img2_'+id).hide();
        $('#img3_'+id).hide();
        $('#img'+Imgs.images[id]+'_'+id).fadeIn(f);
        if (Imgs.images[id] < 3) {
            Imgs.images[id]++;
        }
        else {
            Imgs.images[id] = 1;
        }
    },
    go: function(id) {
        setInterval('Imgs.view("'+id+'")', 3000);
    }
};

var ONLY_HOME = false;

var bgSlide = {
    current: 4,
    lock: false,
    images: [
        '/static/images/bg/bg1.jpg',
        '/static/images/bg/bg2.jpg',
        '/static/images/bg/bg3.jpg',
        '/static/images/bg/bg4.jpg',
        '/static/images/bg/bg5.jpg'
    ],
    slideId: 'slidebox',
    contentId: 'content_body',
    sleep: 2000,
    hide: function(box) {
        var self = this;
        box.fadeOut(self.sleep);
    },
    set_bg: function(box) {
        var self = this;
        var img_old = this.images[this.current];
        this.current = this.current + 1;
        if (this.current >= (this.images.length - 1)) {
            this.current = 0;
        }
        var img_new = this.images[this.current];
        box.css({'background': 'url(' + img_old + ') top center no-repeat'});
        $('#' + self.contentId).css({'background': 'url(' + img_new + ') top center no-repeat'});
        return box
    },
    create_box: function() {
        var self = this;
        var cb = $('#' + self.contentId);
        var w = cb.width();
        var h = cb.height();
        var box = $('<div></div>');
        $('#' + self.slideId).remove();
        box.attr('class', self.slideId)
           .attr('id', self.slideId)
           .width(w)
           .height(h)
           .css({'top': '0px', 'left': '0px'});
        return box;
    },
    remove_box: function() {
        var self = this;
        $('#' + self.slideId).remove();
    },
    slide: function() {
        var self = this;
        if (!self.lock && ONLY_HOME) {
            self.lock = true;
            var box = this.create_box();
            box = self.set_bg(box);
            $('#' + self.contentId).append(box);
            self.hide(box);
            self.lock = false;
        }
    }
};

$(document).ready(function(){
	if ($("#content div.fengshui_bg").length > 0) {
  		$('.fengshui_bg').bgStretcher({
			images:["/images/fengshui-bg.jpg"],
			slideShow:false
		}); 
	}

	if ($("#content div.contacts-page").length > 0) {
        $('#content div.contacts-page').bgStretcher({
            images:["/images/contacts-bg.jpg"],
            slideShow:false
        }); 
    }

    $('.tp').my_tooltip();

    if ($('#id_news_image').length > 0) {
        slide.init();
    }

    setTimeout(
        function() {
            console.log(111);
            setInterval(
                function() {
                    bgSlide.slide();
                }, 
                5000);
        },
        50
    );

});

function show_img_big(item) {
	//console.log(item);
    ///
}

