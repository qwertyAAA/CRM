$('#dataform').submit(function () {
        var fileInput = $('#datafile').get(0).files[0];
        var nameinput = $('#dataname').val();
        var catinput=$('#datacategory').val();
        var userinput=$('#datauser').val();
        if (fileInput && nameinput && catinput != '请选择资料分类' && userinput)
        {
            console.log(fileInput,nameinput,catinput,userinput);
        }
        else
        {
            alert('请填写所有选项');
            return false;
        }
     })