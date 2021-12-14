//(function($){})(jQuery)参数为$的匿名函数，实参为jQuery
(function($){
    //$.fn.xx 扩展jQuery元素得到新的snow方法
    $.fn.snow = function (options) {
        //var $x = $('<div id = "xxx"/>').css({...,...}).html('')新建一个div元素并设计样式，不过为什么没有appendTo()?
        var  $flake = $('<div id = "snowbox"/>').css({'position':'absolute','top':'-50px','z-index':'9999'}).html('&#10052'),
            documentHeight = $(document).height(),
            documentWidth = $(document).width(),
            defaults = {
             // 雪花最小、最大尺寸、出现频率、雪花颜色
                minSize : 10,
                maxSize : 15,
                newOn : 800,
                flakeColor: "#AFDAEF"
            },
            // 将一个新的空对象（{}）做为$.extend的第一个参数，defaults和用户传递的参数对象紧随其后，这样做的好处是所有值被合并到这个空对象上，保护了插件里面的默认值。
            options = $.extend({}, defaults, options);
        //setInterval() 方法可按照指定的周期（以毫秒计）来调用函数或计算表达式。
        var interval = setInterval(function () {
                var  startPositionLeft = Math.random() * documentWidth -100 ,
                     startOpacity = 0.5 + Math.random(),
                     sizeFlake = options.minSize + Math.random() * options.maxSize,
                     endPositionTop = documentHeight -100,
                     endPositionLeft = startPositionLeft - 500 + Math.random() * 500,
                     //自由下落持续时间
                     durationFall = documentHeight * 10 + Math.random() * 5000;
                //appendTo():在body内部结尾处插入flake的克隆，并设置css样式，opacity:透明度，0——100；
                $flake.clone().appendTo('body').css({left:startPositionLeft,opacity:startOpacity,'font-size':sizeFlake,
                    color:options.flakeColor}).animate({top : endPositionTop, left : endPositionLeft, opacity: 0.2},

                    durationFall,'linear',function () {
                    $(this).remove()

                    }
                );


        },options.newOn);



    };
})(jQuery);
//$(function(){})页面载入后执行其中的代码，完整形式为$(document).ready(function(){})
//$.fn.snow({})
$(function(){
    $.fn.snow({
        minSize:10,
        maxSize:20,
        newOn:400
    });
});


