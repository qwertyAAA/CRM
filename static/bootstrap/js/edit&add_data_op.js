//添加与修改数据时判断用户是否把必填项全部填写完整

$('#dataform').submit(function () {
        var fileInput = $('#datafile').get(0).files[0];
        var nameinput = $('#dataname').val();
        var catinput=$('#datacategory').val();
        var userinput=$('#datauser').val();
        if (fileInput && nameinput && catinput != '请选择资料分类' && userinput)
        {
            return true
            // console.log(fileInput,nameinput,catinput,userinput);
        }
        else
        {
            alert('请填写所有选项');
            return false;
        }
     });