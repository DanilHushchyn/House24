clearSelects()
$('.form-house-select').on('change',function () {
    if($('.form-house-select option:selected').text()==='Всем...'){
             clearSelects()
    }else {
        let id = $(this).val()
        $.ajax({
            url: `/admin/get_house-info/${id}`,         /* Куда отправить запрос */
            method: 'get',             /* Метод запроса (post или get) */
            dataType: 'html',
            context: 'html',
            success: function (data) {   /* функция которая будет выполнена после успешного запроса.  */
                clearSelects()
                data = JSON.parse(data)
                for(let section of JSON.parse(data['sections'])){
                    $('.form-section-select').append($(`
                        <option value="${section['pk']}">${section['fields']['title']}</option>
                    `))
                }
                for(let flat of JSON.parse(data['flats'])){
                    $('.form-flat-select').append($(`
                        <option value="${flat['pk']}">${flat['fields']['number']}</option>
                    `))
                }
                for(let floor of JSON.parse(data['floors'])){
                    $('.form-floor-select').append($(`
                        <option value="${floor['pk']}">${floor['fields']['title']}</option>
                    `))
                }
            }
        });
    }
})
function clearSelects() {
     $('.form-section-select').children().remove()
     $('.form-floor-select').children().remove()
     $('.form-flat-select').children().remove()
     $('.form-section-select').append(`
       <option value="">Выберите...</option>
     `)
     $('.form-floor-select').append(`
       <option value="">Выберите...</option>
     `)
    $('.form-flat-select').append(`
       <option value="">Выберите...</option>
     `)
}

