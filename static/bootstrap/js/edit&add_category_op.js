//添加与修改类别时候判断是否填写了所有的必填项
$('#dataform').submit(function () {
        if ($('#dataname').val())
        {
            return true
        }
        else {
            alert('请填写类别名称');
            return false
        }
    })