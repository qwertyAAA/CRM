//添加与修改类别时候判断是否填写了所有的必填项
$('#dataform').submit(function () {
    var newname=$('#dataname').val();
    var flag=false;
    var titlelist= {{ titlelist|safe }};
    alert(titlelist);
    if (newname)
    {
        if (flag){
            return false
        }
        else {
            alert('nihao');
            return true
        }
    }
    else {
        alert('请填写类别名称');
        return false
    }
});