from django.db import models

# 예제 4-26을 위한 모델 (혼자 만들어 봄) ==========================
class Book(models.Model):
    book_name = models.CharField(max_length=300)
    pub_date = models.DateTimeField('publication_date')

    def __str__(self):
        return self.book_name

# =============================================================