
// 操作全选与多选删除

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
    });

    $('#deletebt').click(function () {
            var idlist=[];
            if ($('#all').is(':checked'))
            {
                var checklist=$('.dataid');
                for (i = 0; i <= checklist.length; i++)
                {
                    idlist.push($(checklist[i]).text())
                }
            }
            else
            {
                var checklist=$('input:checked');
                for (i = 0; i <= checklist.length; i++)
                {
                    idlist.push($(checklist[i]).attr('dataid'))
                }
            }
            $.ajax({
                type:'post',
                url:'/data_manage/delete_category/',
                dataType:'json',
                traditional:true,
                data:{
                    'idlist':idlist,
                    "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()
                },
                success:function (data) {
                    location.href='/data_manage/check_category/'
                }
            })
        });