// 用户名
$(function(){
    $("#username").focus(function(){
       document.getElementById("userinfo").style.display = 'block';
       document.getElementById("username").style.border = '1px solid #ddd';
       document.getElementById("userinfo1").style.display = 'none';
       document.getElementById("userinfo2").style.display = 'none';
       document.getElementById("userinfo3").style.display = 'none';
    });
    // 获取焦点

    $("#username").blur(function(){
        document.getElementById("userinfo").style.display = 'none';

        //空字符
        if(this.value.length == 0){
            this.html("");
        }

        // 判断长度
        var len = 0; // 用户名长度
        for (var i = 0; i < this.value.length; i++ ) {
            
            // 中文+2,其它+1
            if (/[\u4e00-\u9fa5]/.test(this.value[i])) {
                len += 2;
            } else {
                len += 1;
            }
            if (len > 14) {
                document.getElementById("userinfo1").style.display = 'block';
                document.getElementById("userinfo3").style.display = 'none';
                document.getElementById("username").style.border = 'border: 1px solid #fc4343;';
                break;
            }
                    
            // 判断非法字符和纯数字
            if(/[@#\$%\^&\*]+/g.test(this.value)) {
                document.getElementById("userinfo2").style.display = 'block';
                document.getElementById("userinfo3").style.display = 'none';
                document.getElementById("username").style.border = '1px solid #fc4343';
                break;
            }
            if(/^[0-9]+$/.test(this.value)) {
                document.getElementById("userinfo2").style.display = 'block';
                document.getElementById("userinfo3").style.display = 'none';
                document.getElementById("username").style.border = '1px solid #fc4343';
                break;
            }
                    
            // 成功
            if (len <= 14){
                document.getElementById("userinfo3").style.display = 'block';
            }
        }
    });
    // 失去焦点
});

// 手机号      
$(function(){
    $("#phno").focus(function(){
        document.getElementById("number").style.display = 'block';
        document.getElementById("phno").style.border = '1px solid #ddd';
        document.getElementById("number1").style.display = 'none';
        document.getElementById("number2").style.display = 'none';
    });
    // 获取焦点

    $("#phno").blur(function(){
        document.getElementById("number").style.display = 'none';

        // 为空
        if(this.value.length == 0){
            this.html("");
        }

        // 验证成功
        if(/(13|14|15|18)[0-9]{9}/.test(this.value) && this.value.length == 11){
            document.getElementById("number2").style.display = 'block';
        }

        // 验证失败
        else {
            document.getElementById("number1").style.display = 'block';
            document.getElementById("phno").style.border = '1px solid #fc4343';
        }
    });
    // 失去焦点
});

// 密码
$(function(){
    $("#password").focus(function(){
        document.getElementById("pwd3").style.display = 'block';
    });
    // 获取焦点

    $("#password").blur(function(){

        // 为空
        if(this.value.length == 0){
            this.html("");
        }

        // 判断长度
        if(/\s/.test(this.value) && this.value.length >= 8 && this.value.length <= 14){
            document.getElementById("img1").src = './imgs/ok.png';
            document.getElementById("img2").src = './imgs/ok.png';
            document.getElementById("img3").src = './imgs/err.png';
        }
        else if(/\s/.test(this.value) && (this.value.length < 8 || this.value.length > 14)){
            document.getElementById("img1").src = './imgs/err.png';
            document.getElementById("img2").src = './imgs/ok.png';
            document.getElementById("img3").src = './imgs/err.png';
        }
        else if(/[^\s]/.test(this.value) && (this.value.length < 8 || this.value.length > 14)){
            document.getElementById("img1").src = './imgs/err.png';
            document.getElementById("img2").src = './imgs/ok.png';
            document.getElementById("img3").src = './imgs/ok.png';
        }
        else{
            document.getElementById("img1").src = './imgs/ok.png';
            document.getElementById("img2").src = './imgs/ok.png';
            document.getElementById("img3").src = './imgs/ok.png';
            document.getElementById("ok").style.display = 'block';
            document.getElementById("pwd3").style.display = 'none';
        }
    });
    // 失去焦点
});