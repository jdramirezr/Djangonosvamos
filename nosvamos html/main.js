function go_login(){
    $(location).attr('href', 'index.html')
}

function ajax_func(that) {
    $.ajax({
        url: that.data('url'),
        type: that.attr('method'),
        data: that.serialize(),
        success(data) {
            if(!data.ok) {
                $('.js-message').html('<div class="lines error">' + data.response + '</div>');
            } else {
                $('.js-message').html('<div class="message">' + data.response + '</div>');
                $('.loader').fadeIn('slow');
                setTimeout(go_login, 4000);
            }
        },
    });
}

$('.js-send').on('click', function () {
    var that = $('.js-contact-form');
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
                var text_data = '';

                $.each( data.response , function( k, v ) {
                    text_data += (
                        '<div class="city-list city-text"><b>Fecha de viaje</b>: ' + v.travel_date + '<br>' +
                        '<b>Ciudad de salida</b>: ' + v.city_from + '<br>' +
                        '<b>Ciudad de llegada</b>: ' + v.city_to + '<br>' +
                        '<b>Cupos disponibles</b>: ' + v.quotas + '<br>' +
                        '<b>Precio</b>: ' + v.price + '<br></div>' +
                        '<div class="city-list"><b>Foto</b>: ' + '<img src=' + v.image + '><br></div><hr>'
                    );

                });
                $('.js-trip-list').hide().html(text_data).fadeIn('slow');
            }
        },
    });
});


$('.js-login').on('click', function () {
    var that = $('.js-login-form');
    if ($('.js-username').val() == '' ||$('.js-password').val() == '' ) {
        $('.js-message').html('<div class="lines error">Debes ingresar los datos solicitados</div>')
        return false
    }
    ajax_func(that);
});

$('.js-create-user').on('click', function () {
    var that = $('.js-login-form');
    if ($('.js-username').val() == '' || $('.js-password1').val() == '' || $('.js-password2').val() == '') {
        $('.js-message').html('<div class="lines error">Debes ingresar los datos solicitados</div>')
        return false
    }

    if ($('.js-password1').val() != $('.js-password2').val()) {
        $('.js-message').html('<div class="lines error">Las contraseñas no coinciden</div>')
        return false
    }

    ajax_func(that);
});


$('.js-post').on('click', function () {
    var that = $('.js-trip-form');
    if (
        $('.js-date').val() == '' ||
        $('.js-from').val() == '' ||
        $('.js-to').val() == '' ||
        $('.js-trip-price').val() == '' ||
        $('.js-places').val() == ''
    ) {
        $('.js-message').html('<div class="lines error">Debes ingresar los datos solicitados</div>')
        return false
    }

    ajax_func(that);
});
