from django.contrib import admin
from questions.models import Choice, TextQuestion
# from questions.models import QuestionList


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class TextQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ("Votes",            {"fields": ["votes"]}),
        ("ID",               {"fields": ["question_healthcenter_id"]}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'votes', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']




admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(Choice)
#admin.site.register(QuestionList, QuestionListAdmin)
