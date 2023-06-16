if ($('.form-house-select option:selected').text()==='Выберите...'){
    clearSelects()
}else{
    // $.ajax({
    //         url: `/admin/get_house-info/${$('.form-house-select option:selected').val()}`,         /* Куда отправить запрос */
    //         method: 'get',             /* Метод запроса (post или get) */
    //         dataType: 'html',
    //         context: 'html',
    //         success: function (data) {   /* функция которая будет выполнена после успешного запроса.  */
    //             if ($('.form-section-select option:selected').text()!=='Выберите...'){
    //                var selectedSection = $('.form-section-select option:selected').val()
    //             }
    //             clearSelects()
    //             data = JSON.parse(data)
    //             for(let section of JSON.parse(data['sections'])){
    //                 if (section['pk']==selectedSection){
    //                     $('.form-section-select').append($(`
    //                         <option value="${section['pk']}" selected>${section['fields']['title']}</option>
    //                     `))
    //                 }else{
    //                      $('.form-section-select').append($(`
    //                         <option value="${section['pk']}" >${section['fields']['title']}</option>
    //                     `))
    //                 }
    //             }
    //
    //         }
    // });
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
                for(let flat of JSON.parse(data['flats'])){
                    $('.form-flat-select').append($(`
                        <option value="${flat['pk']}">${flat['fields']['number']}</option>
                    `))
                }

            }
        });
    }
})
$('.form-section-select').on('change',function () {
    if($('.form-section-select option:selected').text()==='Выберите...'){
         $('.form-flat-select').children().remove()
         $('.form-flat-select').append(`
           <option>Выберите...</option>
         `)
        $('#user-fullname').text('не выбран')
        $('#user-phone').text('не выбран')
    }else {
        $('#user-fullname').text('не выбран')
        $('#user-phone').text('не выбран')
        let id = $(this).val()
        $.ajax({
            url: `/admin/get_section-info/${id}`,         /* Куда отправить запрос */
            method: 'get',             /* Метод запроса (post или get) */
            dataType: 'html',
            context: 'html',
            success: function (data) {   /* функция которая будет выполнена после успешного запроса.  */
                 $('.form-flat-select').children().remove()
                 $('.form-flat-select').append(`
                   <option>Выберите...</option>
                 `)
                data = JSON.parse(data)
                for(let flat of JSON.parse(data['flats'])){
                    $('.form-flat-select').append($(`
                        <option value="${flat['pk']}">${flat['fields']['number']}</option>
                    `))
                }

            }
        });

    }
})
$('.form-flat-select').on('change',function () {
    if($('.form-flat-select option:selected').text()==='Выберите...'){
        $('#user-fullname').text('не выбран')
        $('#user-phone').text('не выбран')
    }else {

        let id = $(this).val()
        $.ajax({
            url: `/admin/get_flat-info/${id}`,         /* Куда отправить запрос */
            method: 'get',             /* Метод запроса (post или get) */
            dataType: 'html',
            context: 'html',
            success: function (data) {   /* функция которая будет выполнена после успешного запроса.  */
                data = JSON.parse(data)
                let flat_owner_obj = JSON.parse(data['flat_owner'])[0]['fields']
                let user_obj = JSON.parse(data['user'])[0]['fields']
                $('#user-fullname').text(`${user_obj['last_name']} ${user_obj['first_name']} ${flat_owner_obj['patronymic']}`)
                $('#user-phone').text(`${user_obj['phone']}`)


            }
        });

    }
})
function clearSelects() {
     $('.form-section-select').children().remove()
     $('.form-section-select').append(`
       <option>Выберите...</option>
     `)
     $('.form-flat-select').children().remove()
     $('.form-flat-select').append(`
       <option>Выберите...</option>
     `)
}