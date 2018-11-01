    $('#all').click(function () {
        if($('#all').is(':checked'))
        {
            console.log(true);
            $('.one').attr('checked','checked')
        }
        else
        {
            console.log(false);
            $('.one').attr('checked',null)
        }
    })