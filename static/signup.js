
function id_check() {
    let id = $("#id").val()
    if(id == ""){
        $("#alert-label").text("아이디를 입력해 주세요.").addClass("is-danger")
        $("#alert-label").css("color", "toamto")
        return;
    }
    if(!is_nickname(id)){
        $("#alert-label").text("아이디는 영문과 숫자, 일부 특수문자(._-)를 사용하여 2~10글자로 작성하세요").addClass("is-danger")
        $("#alert-label").css("color", "toamto")
        return;
    }

    $.ajax({
        type: "POST",
        url: "/check",
        data: {id_give: id},
        success: function (response) {
            if (response["msg"] == 0) {
                $("#alert-label").text("아이디가 존재 합니다.").addClass("is-danger")
                $("#alert-label").css("color", "toamto")
            } else if (response["msg"] == 1) {
                $("#alert-label").text("사용할 수 있는 아이디 입니다!").removeClass("is-danger")
                $("#alert-label").css("color", "cadetblue")
            }
        }
    })


}

function signup(){
    let id = $("#id").val()
    let pw = $("#pw").val()
    let repw = $("#pw-re").val()
    let name = $("#name").val()

    if($("#alert-label").hasClass("is-danger")){
        alert("아이디를 다시 확인해 주세요.")
        return;
    }
    if(pw == ""){
        $("#pw-label").text("비밀번호를 입력해 주세요.").addClass("is-danger")
        return;
    } else if(!is_password(pw)){
        $("#pw-label").text("비밀번호는 영문과 숫자를 필수 포함해 8~20글자 입니다.").addClass("is-danger")
        return;
    } else{
        $("#pw-label").text("").removeClass("is-danger")
    }

    if (repw == "") {
        $("#repw-label").text("비밀번호를 입력해 주세요.").addClass("is-danger")
        return;
    } else if (pw != repw) {
        $("#repw-label").text("비밀번호가 일치하지 않습니다.").addClass("is-danger")
        return;
    } else {
        $("#repw-label").text("").removeClass("is-danger")
    }

    if(name == ""){
        $("#name-label").text("이름을 입력해 주세요.").addClass("is-danger")
        return;
    }else{
        $("#name-label").text("").removeClass("is-danger")
    }
    if($("#pw-label").hasClass("is-danger") || $("#repw-label").hasClass("is-danger")){
        alert("패스워드를 다시 확인해 주세요.")
        return;
    }

    $.ajax({
        type: "POST",
        url: "/signup",
        data: {id_give: id, pw_give: pw, name_give: name},
        success: function (response) {
            window.location.href = "/"
        }
    })

}

function is_nickname(asValue) {
    var regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{2,10}$/;
    return regExp.test(asValue);
}

function is_password(asValue) {
    var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
    return regExp.test(asValue);
}