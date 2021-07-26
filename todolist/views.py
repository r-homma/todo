



from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import MyToDoList
from .forms import todoAddForm, todoDeleteForm, todoEditForm

# Create your views here.
def index(request):
    all_todo = MyToDoList.objects.all()
    
    params = {# HTMLファイルで使いたい変数を辞書型でparamsに代入している。
        'todolist':all_todo,
    }
    return render(request, 'todolist/index.html', params)#辞書型データのparamsをindex.htmlに代入している

def todoAdd(request):
    if(request.method == 'POST'):#requeestオブジェクトがPOSTメソッドの時
        mtdl = MyToDoList()# インスタンス（オブジェクト）の作成
        mtdl.title = request.POST['title']# フォームtitleをmtdl.titleに代入。以下21行目まで同様
        mtdl.contents = request.POST['contents']
        mtdl.deadline = request.POST['deadline']
        mtdl.save()# 代入したデータをデータベースに保存している
        return redirect(to='/todolist/')
    form = todoAddForm
    params = {
        'form':form,
    }
    return render(request, 'todolist/todoAdd.html', params)

def todoDelete(request, del_id):
    mtdl_obj = MyToDoList.objects.filter(id=del_id).first()# 削除するToDoデータをMyDoListモデルから抽出している
    if(request.method == 'POST'):
        mtdl_obj.delete()
        return redirect(to='/todolist/')
    context = {
        'title':mtdl_obj.title,
        'contents':mtdl_obj.contents,
        'entryDate':mtdl_obj.entryDate,
        'deadline':mtdl_obj.deadline,
        'done':mtdl_obj.done,
    }
    form = todoDeleteForm(context)
    params = {
        'del_id':del_id,
        'form':form,
    }
    return render(request, 'todolist/todoDelete.html', params)

def todoEdit(request, edit_id):
    mtdl_obj = MyToDoList.objects.filter(id=edit_id).first()
    if(request.method == 'POST'):
        if('done' in request.POST):
            mtdl_obj.done = True
        else:
            mtdl_obj.done = False
        mtdl_obj.title = request.POST['title']
        mtdl_obj.contents = request.POST['contents']
        mtdl_obj.deadline = request.POST['deadline']
        mtdl_obj.save()
        return redirect(to='/todolist/')
    context = {
        'title':mtdl_obj.title,
        'contents':mtdl_obj.contents,
        'deadline':mtdl_obj.deadline,
        'done':mtdl_obj.done,
    }
    form = todoEditForm(context)
    params = {
        'edit_id':edit_id,
        'form':form,
    }
    return render(request, 'todolist/todoEdit.html', params)