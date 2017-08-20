from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .forms import FormAddNewWord
from .models import Word

@csrf_exempt
def add_new_word(request):
    if request.method == "POST":

        form = FormAddNewWord(request.POST or None)

        if form.is_valid():

            word = Word()

            if Word.objects.filter(word=form.cleaned_data['word']).exists():
                word = Word.objects.get(word=form.cleaned_data['word'])

            # 파싱
            word.word = form.cleaned_data['word']

            word.rage = form.cleaned_data['rage']
            word.loathing = form.cleaned_data['loathing']
            word.grief = form.cleaned_data['grief']
            word.amazement = form.cleaned_data['amazement']
            word.terror = form.cleaned_data['terror']
            word.admiration = form.cleaned_data['admiration']
            word.ecstasy = form.cleaned_data['ecstasy']
            word.vigilance = form.cleaned_data['vigilance']
            word.save()

            isSaved = True

            return JsonResponse({"saved": isSaved, "word": word.word})

        else:
            return render(request, 'word_add_new.html', {"form": form})

    else:
        form = FormAddNewWord()
        return render(request, 'word_add_new.html', {"form": form})

@csrf_exempt
def get_word_emotions(request, word):
    wordData = get_object_or_404(Word, pk=word)

    return JsonResponse({
        "rage": wordData.rage,
        "loathing": wordData.loathing,
        "grief": wordData.grief,
        "amazement": wordData.amazement,
        "terror": wordData.terror,
        "admiration": wordData.admiration,
        "ecstasy": wordData.ecstasy,
        "vigilance": wordData.vigilance,
    })