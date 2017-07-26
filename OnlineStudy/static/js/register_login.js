/**
 * Created by gogo on 17-7-23.
 */
// 注册页面的js 验证信息=================================
$(function () {
    var submit_email = true;
    var submit_password = true;
    // 邮箱验证信息
    var $email = $('#id_email');
    $email.focus(function () {
        $('.email_err').html('');
    });
    $email.blur(function () {
        var email = $(this).val();
        var email_re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i;
        if (email_re.test(email)) {
            $.get('/users/register', {'email': email}, function (data) {
                if (data.code === '0') {
                    $('.email_err').html('**邮箱已经存在...');
                    submit_email = false
                } else {
                    submit_email = true
                }
            })
        } else {
            $('.email_err').html('**邮箱格式不正确...');
            submit_email = false
        }
    });
    //密码验证
    var $password = $('#id_password');
    $password.focus(function () {
        $('.password_err').html('');
    });
    $password.blur(function () {
        var rePass = /^[\w!@#$%^&*]{6,20}$/;
        if (rePass.test($(this).val())) {
            submit_password = true
        } else {
            $('.password_err').html('**密码格式不正确...');
            submit_password = false
        }
    });

    // 阻止表单的默认行为 验证不通过的时候 禁止提交
    $('#jsEmailRegBtn').click(function () {
        $email.trigger('blur');
        $password.trigger('blur');
        if (submit_email === false || submit_password === false) {
            return false
        }
    });

    $('.captcha').click(function () {
        // 注册邮箱验证码刷新功能
        var $captcha = $(this);
        $.get("/captcha/refresh/?" + Math.random(), function (result) {
            $('#id_captcha_0').val(result.key);
            $captcha.attr("src", result.image_url);
        });
        return false;
    });
});

// 登录页面的js 验证信息=================================
$(function () {
    var $username = $('#account_l');
    var $password = $('#password_l');
    $username.focus(function () {
        $('#jsLoginTips').html('')
    });
    $password.focus(function () {
        $('#jsLoginTips').html('')
    });
    $('#jsLoginBtn').click(function () {
        if ($username.val() === '' || $password.val() === '') {
            $('#jsLoginTips').html('用户名或者密码不能为空...');
            return false
        }
    });
});