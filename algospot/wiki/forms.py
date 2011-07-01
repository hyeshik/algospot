# -*- coding: utf-8 -*-
from django import forms
from models import Page, PageRevision

class EditForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "large",
        "rows": "20"}))
    summary = forms.CharField(max_length=100,
            widget=forms.TextInput(attrs={"class": "large"}))

    def save(self, page, user):
        revision = PageRevision(text=self.cleaned_data["text"],
                edit_summary=self.cleaned_data["summary"],
                user=user,
                revision_for=page)
        revision.save()
        page.current_revision = revision
        page.save()

