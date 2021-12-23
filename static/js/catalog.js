let catalogLeaveTop = $(".blog-catalog").offset().top;
        let catalogHeight = document.getElementsByClassName("blog-catalog")[0].clientHeight;
        let sum_height = catalogHeight;
        let all_Height = document.body.clientHeight;
        let maxHeight = document.body.getElementsByClassName("about_box")[0].clientHeight;
        let standard_height = 239;
        $(window).scroll( function(){
		//滚动条离页面最上方的距离
		let scoll_pos = $(document).scrollTop();
        if (scoll_pos === 0)
        {
            $('#catalog').css({
                "width": 150,
                "position": "absolute",
                "right": 70,
                "top": standard_height,
                /*text-align: center;*/
                "float": "right",

            });
        }
        if(scoll_pos > catalogHeight+400 && scoll_pos <=maxHeight-800)
        {
            $('#catalog').css({
                "width": 150,
                "position": "absolute",
                "right": 70,
                "top": catalogHeight,
                /*text-align: center;*/
                "float": "right",

            });
            catalogHeight += sum_height*0.6;
        }
       else {
            if (scoll_pos < catalogHeight && scoll_pos >= standard_height)
        {
            $('#catalog').css({
                "width": 150,
                "position": "absolute",
                "right": 70,
                "top": scoll_pos,
                /*text-align: center;*/
                "float": "right",

            });
        }
        }
	});