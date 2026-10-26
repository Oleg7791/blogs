from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # задаёт поля модели, которые вы хотите
                                                    #показывать на странице списка объектов администрирования
    list_filter = ['status', 'created', 'publish', 'author'] # создаёт боковую панель, которая позволяет
                                                                # фильтровать результаты по полям
    search_fields = ['title', 'body'] # Строка поиска. Определяем список полей, по которым можно выполнять поиск
    prepopulated_fields = {'slug': ('title',)} # предзаполнять поле slug данными, вводимыми в поле title
    raw_id_fields = ['author'] # поле author отображается поисковым виджетом
    date_hierarchy = 'publish' #ниже строки поиска находятся навигационные ссылки для навигации по иерархии дат
    ordering = ['status', 'publish'] #критерии сортировки, которые будут использоваться по умолчанию.

