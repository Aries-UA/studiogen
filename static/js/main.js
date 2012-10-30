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

$(document).ready(function(){
	if ($("#content div.fengshui_bg").length >0) {
  		$('.fengshui_bg').bgStretcher({
			images:["/images/fengshui-bg.jpg"],
			slideShow:false
		}); 
	}

	if ($("#content div.contacts-page").length >0) {
        $('#content div.contacts-page').bgStretcher({
            images:["/images/contacts-bg.jpg"],
            slideShow:false
        }); 
    }

    $('.tp').my_tooltip();

    if ($('#id_news_image').length > 0) {
        slide.init();
    }

});

function show_img_big(item) {
	//console.log(item);
    ///
}

