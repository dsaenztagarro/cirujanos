from django import forms
import models


class ArticleForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = models.Article


class VideoForm(forms.ModelForm):
    class Meta:
        model = models.Video


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event


class SlideForm(forms.ModelForm):
    class Meta:
        model = models.Slide
