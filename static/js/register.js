function bindEmailCaptchaClick(){
  $("#captcha-btn").click(function (event){
    // $this：代表的是当前按钮的jquery对象
    var $this = $(this);
    // 阻止默认的事件
    event.preventDefault();

    var email = $("input[name='email']").val();
    $.ajax({
      url: "/user/captcha/email?email="+email,
      method: "GET",
      success: function (result){
        var code = result['code'];
        if(code == 200){
          var countdown = 60;
          $this.off("click");
          var timer = setInterval(function (){
            $this.text(countdown);
            countdown -= 1;
            if(countdown <= 0){
              clearInterval(timer);
              $this.text("获取验证码");
              bindEmailCaptchaClick();
            }
          }, 1000);
           alert("邮箱验证码发送成功！");
        }else{
          alert(result['message']);
        }
      },
      fail: function (error){
        console.log(error);
      }
    })
  });
}


$(function (){
  bindEmailCaptchaClick();
});