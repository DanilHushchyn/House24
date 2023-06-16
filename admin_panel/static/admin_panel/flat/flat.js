if ($('.form-house-select option:selected').text()==='Выберите...'){
    clearSelects()
}else{

    $.ajax({
            url: `/admin/get_house-info/${$('.form-house-select option:selected').val()}`,         /* Куда отправить запрос */
            method: 'get',             /* Метод запроса (post или get) */
            dataType: 'html',
            context: 'html',
            success: function (data) {   /* функция которая будет выполнена после успешного запроса.  */
                if ($('.form-section-select option:selected').text()!=='Выберите...'){
                   var selectedSection = $('.form-section-select option:selected').val()
                }
                if ($('.form-floor-select option:selected').text()!=='Выберите...'){
                   var selectedFloor = $('.form-floor-select option:selected').val()
                }
                clearSelects()
                data = JSON.parse(data)
                for(let section of JSON.parse(data['sections'])){
                    if (section['pk']==selectedSection){
                        $('.form-section-select').append($(`
                            <option value="${section['pk']}" selected>${section['fields']['title']}</option>
                        `))
                    }else{
                         $('.form-section-select').append($(`
                            <option value="${section['pk']}" >${section['fields']['title']}</option>
                        `))
                    }
                }
                for(let floor of JSON.parse(data['floors'])){
                    if (floor['pk']==selectedFloor){
                        $('.form-floor-select').append($(`
                            <option value="${floor['pk']}" selected>${floor['fields']['title']}</option>
                        `))
                    }else{
                         $('.form-floor-select').append($(`
                            <option value="${floor['pk']}">${floor['fields']['title']}</option>
                        `))
                    }
                }
            }
    });
}
$('.form-house-select').on('change',function () {
    if($('.form-house-select option:selected').text()==='Выберите...'){
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
     $('.form-section-select').append(`
       <option>Выберите...</option>
     `)
     $('.form-floor-select').append(`
       <option>Выберите...</option>
     `)
}