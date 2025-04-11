from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ("id",)

    def __str__(self):
        return self.name
    

class Ad(models.Model):

    CONDITION = [
        ('new', 'Новый'),
        ('used', 'Б/у'),
    ]

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE  
)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="images", blank=True, null=True, default="images/default.png")  
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')
    condition = models.CharField(max_length=10, choices=CONDITION, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Карточку товара'
        verbose_name_plural = 'Карточки товаров'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})


class ExchangeProposal(models.Model):

    STATUS = [
        ('wait', 'В ожидании'),
        ('accept', 'Принято'),
        ('reject', 'Отклонено'),
    ]

    ad_sender = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='sent_proposals')
    ad_receiver = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='received_proposals')
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='wait')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Заявку на обмен'
        verbose_name_plural = 'Заявка на обмен'


    def __str__(self):
        return f"{self.ad_sender} → {self.ad_receiver} ({self.status})"