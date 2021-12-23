$(document).ready(function(){
    let fieldEmail = $('#id_email');
    let fieldName = $('#id_name');
    let button = $('#send');
    let pattern = /^[a-z0-9_.-]+@[a-z0-9-]+\.[a-z]{2,6}$/i;
    let namePattern = /^([a-zA-Z]{2,16})$/;

    button.prop('disabled', true);

    fieldEmail.on('keyup', function(event){
        if (fieldEmail.val() != '' && fieldName.val() != ''){
            button.prop('disabled', false);
        }else{
            button.prop('disabled', true);
        }
    })

    fieldName.on('keyup', function(event){
        if (fieldEmail.val() != '' && fieldName.val() != ''){
            button.prop('disabled', false);
        }else{
            button.prop('disabled', true);
        }
    })

    button.click(function(event){
        if (validateEmail() == false && validateName() == true){
            fieldEmail.css('box-shadow', '0 0 10px 4px red')
            fieldName.css('box-shadow', '');
            $("#errorName").css('display', 'none');
            $("#errorEmail").css('display', 'block');
            button.prop('disabled', true);
        }else if (validateName() == false && validateEmail() == true){
            fieldName.css('box-shadow', '0 0 10px 4px red');
            fieldEmail.css('box-shadow', '');
            $("#errorEmail").css('display', 'none');
            $("#errorName").css('display', 'block');
            button.prop('disabled', true);
        }else if(validateEmail() == false && validateName() == false){
            fieldEmail.css('box-shadow', '0 0 10px 4px red');
            fieldName.css('box-shadow', '0 0 10px 4px red');
            $("#errorEmail").css('display', 'block');
            $("#errorName").css('display', 'block');
            button.prop('disabled', true);
        }else if(validateEmail() == true && validateName() == true){
            fieldName.css('box-shadow', '');
            fieldEmail.css('box-shadow', '');
            $("#errorEmail").css('display', 'none');
            $("#errorName").css('display', 'none');
            $("#curtain").css('display', 'block');
            $(".spinner-border").css('display', 'block');
            showModal();
        }
    })

    function validateEmail(){
        if (fieldEmail.val().search(pattern) == 0){
            return true;
        }else{
            return false;
        }
    }

    function validateName(){
        if (fieldName.val().search(namePattern) == 0){
            return true;
        }else{
            return false;
        }
    }

    function check(id){
        if(id.is(':checked')){
            return true;
        }else{
            return false;
        }
    }

    function showModal(){
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: '/contacts/',
            type: 'POST',
            dataType: 'json',
            data:{
                'email': fieldEmail.val(),
                'name' : fieldName.val(),
                'interior': check($("#id_interior")),
                'logo': check($("#id_logo")),
                'graphic': check($("#id_graphic")),
            },
            success : function(result){
                for (let key in result){
                    $('#customer').html(result[key][0].toUpperCase() + result[key].substring(1));
                }
                $("#curtain").css('display', 'none');
                $(".spinner-border").css('display', 'none');
                $('#good').css('display', 'block');
                $('#modalWindow').click();
                $('#bad').css('display', 'none');
            },
            error :function(){
                $("#curtain").css('display', 'none');
                $(".spinner-border").css('display', 'none');
                $('#bad').css('display', 'block');
                $('#modalWindow').click();
                $('#good').css('display', 'none');
            }
        });
    }

});