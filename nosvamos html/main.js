function go_login(){
    $(location).attr('href', 'index.html')
}


$('.js-send').on('click', function () {
    let that = $('.js-contact-form');
    $.ajax({
        url: that.data('url'),
        type: that.attr('method'),
        data: that.serialize(),
        success(data) {
            if(data.errors) {
                $.each(data.errors, function(name, errors) {
                    $(`<label class="lines js-field-error error"></label>`).text(errors.join('\n')).insertAfter($(`.js-${name}`));
                });
            } else {
                console.log('ok');
                var text_data = '';

                $.each( data.response , function( k, v ) {
                    text_data += (
                        '<b>Fecha de viaje</b>: ' + v.travel_date + '<br>' +
                        '<b>Ciudad de salida</b>: ' + v.city_from + '<br>' +
                        '<b>Ciudad de llegada</b>: ' + v.city_to + '<br>' +
                        '<b>Cupos disponibles</b>: ' + v.quotas + '<br><hr>'
                    );

                });
                $('.js-trip-list').html(text_data);
            }
        },
    });
});


$('.js-login').on('click', function () {
    let that = $('.js-login-form');
    if ($('.js-username').val() == '' ||$('.js-password').val() == '' ) {
        $('.js-login-message').html('<div class="lines error">Debe ingresar los datos solicitados</div>')
        return false
    }
    $.ajax({
        url: that.data('url'),
        type: that.attr('method'),
        data: that.serialize(),
        success(data) {
            if(!data.ok) {
                $('.js-login-message').html('<div class="lines error">' + data.response + '</div>');
            } else {
                $('.js-login-message').html('<div class="message">' + data.response + '</div>');
                setTimeout(go_login, 4000);
            }
        },
    });
});


$('.js-create-user').on('click', function () {
    let that = $('.js-login-form');
    if ($('.js-username').val() == '' || $('.js-password1').val() == '' || $('.js-password2').val() == '') {
        $('.js-message').html('<div class="lines error">Debe ingresar los datos solicitados</div>')
        return false
    }

    if ($('.js-password1').val() != $('.js-password2').val()) {
        $('.js-message').html('<div class="lines error">Las contraseñas no coinciden</div>')
        return false
    }

    $.ajax({
        url: that.data('url'),
        type: that.attr('method'),
        data: that.serialize(),
        success(data) {
            if(!data.ok) {
                $('.js-message').html('<div class="lines error">' + data.response + '</div>');
            } else {
                $('.js-message').html('<div class="message">' + data.response + '</div>');
                setTimeout(go_login, 4000);
            }
        },
    });
});


$('.js-post').on('click', function () {
    let that = $('.js-trip-form');
    if (
        $('.js-date').val() == '' ||
        $('.js-from').val() == '' ||
        $('.js-to').val() == '' ||
        $('.js-places').val() == ''
    ) {
        $('.js-message').html('<div class="lines error">Debe ingresar los datos solicitados</div>')
        return false
    }

    $.ajax({
        url: that.data('url'),
        type: that.attr('method'),
        data: that.serialize(),
        success(data) {
            if(!data.ok) {
                $('.js-message').html('<div class="lines error">' + data.response + '</div>');
            } else {
                $('.js-message').html('<div class="message">' + data.response + '</div>');
                setTimeout(go_login, 4000);
            }
        },
    });
});
