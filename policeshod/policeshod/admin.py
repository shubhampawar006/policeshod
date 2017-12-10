from django.contrib import admin

# from policeshod.models import (news_details, news_editorial, breaking_news, main_news, khandesh_news, dhule_special_news, mix_news)
from policeshod.models import *
admin.site.register(news_details)
admin.site.register(news_editorial)
admin.site.register(breaking_news)
admin.site.register(main_news)
admin.site.register(khandesh_news)
admin.site.register(dhule_special_news)
admin.site.register(mix_news)