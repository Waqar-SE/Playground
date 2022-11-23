

var csrfcookie = function() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

function load_ingredients() {
    var ingredients = $("#ingredients").data('url');
    const COLORS = ['warning', 'info', 'primary']
    iziToast.info({
        title: 'Loading Ingredients',
    })
    $.get(
        ingredients, function (data, status) {
            data.forEach(element => {
                $('#ingredients').append(
                    `<span class="btn btn-warning mx-1">${element.name}</span>`
                )
            });

            iziToast.success({
                title: status.toUpperCase(),
                messsage: 'We are done bro !!'
            })
        }
    )
}

function create_ingredients() {
    $.post(
        $('#ingredients-add').data('url'), 
        {
            'name': 'New one',
            'origin': 'Plants',
            'e_number': 1,
            'is_halal': 'H'
        },
        function(){
            iziToast.success({
                title:'Posted'
            })
        }
    )
}

$(document).ready(
    load_ingredients(),
    $.ajaxSetup({
        headers:{"X-CSRFToken":csrfcookie()}
    })
)

$('#ingredients-add').on('click', create_ingredients)

