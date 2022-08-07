from django import forms
from board.models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'contents']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contents']