from django.db import models

# Create your models here.
class MyToDoList(models.Model):
    id = models.AutoField(primary_key=True)# 通し番号フィールド
    title = models.CharField(max_length=200)# todolistの見出しフィールド
    contents = models.TextField()# 文字列（todoの内容）を入力するフィールド
    entryDate = models.DateField(auto_now_add=True)# 記入日の取得。auto_now_addはデータを格納した日にちを自動取得するフィールド
    deadline = models.DateField()# 締め切り日を入力するフィールド
    done = models.BooleanField(default=False)# チェックボックスフィールド
   