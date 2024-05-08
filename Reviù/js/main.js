(function ($) {
    "use strict";

    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit', function () {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) === false) {
                showValidate(input[i]);
                check = false;
            }
        }

       
        var username = $('.validate-form .input100[name="username"]').val().trim();
        var password = $('.validate-form .input100[name="pass"]').val().trim();

       
        if (username === 'admin' && password === 'admin') {
            window.location.href = 'admin/admin.html'; 
            return false; 
        } else if (username === 'utente' && password === 'utente') {
            window.location.href = 'utente/utente.html'; 
            return false; 
        }

        return check; 
    });


    $('.validate-form .input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('name') === 'username') {
            var username = $(input).val().trim();
            if (username !== 'admin' && username !== 'utente') {
                return false;
            }
        } else if ($(input).attr('name') === 'pass') {
            var username = $('.validate-form .input100[name="username"]').val().trim();
            var password = $(input).val().trim();
            if ((username === 'admin' && password !== 'admin') || (username === 'utente' && password !== 'utente')) {
                return false;
            }
        } else {
            if ($(input).val().trim() === '') {
                return false;
            }
        }
        return true;
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
    }

})(jQuery);
