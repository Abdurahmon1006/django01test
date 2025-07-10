from django.db import models

# Create your models here.


# Django Model Maydonlari - O'zbek tilida

# Matnli maydonlar

# - CharField Matn (string) saqlash uchun. `max_length` majburiy.
# - TextField Uzoq matnlar uchun. `max_length` talab qilinmaydi.
# - SlugField URL uchun qulay formatdagi matnlar (`my-title`).

# Raqamli maydonlar

# - IntegerField Butun son.
# - BigIntegerField Juda katta butun sonlar.
# - SmallIntegerField Kichik butun sonlar.
# - PositiveSmallIntegerField kichik musbat sonlar uchun
# - PositiveIntegerField Faqat musbat butun sonlar.
# - FloatField Kasr sonlar (masalan: 3.14).
# - DecimalField Pul qiymatlar uchun aniq kasr sonlar. `max_digits` va `decimal_places` kerak.

# Boolean maydon

# - BooleanField True/False qiymatlar (ha/yoq).

# Sana va vaqt

# - DateField Faqat sana (`auto_now`, `auto_now_add` mavjud).
# - DateTimeField Sana va vaqt.
# - TimeField Faqat vaqt.

# Maxsus maydonlar

# - EmailField Email manzil uchun, email validatsiyasi bilan.
# - URLField URL manzillar uchun.
# - UUIDField UUID (unikal identifikator) uchun.
# - JSONField JSON formatdagi ma'lumotlar (Django 3.1+).
# - FileField Fayl yuklash uchun.
# - ImageField Rasm fayllari uchun (Pillow kerak).

# Aloqador model maydonlar

# - ForeignKey Boshqa modelga boglanish (`on_delete` kerak).
# - OneToOneField Birga bir boglanish.
# - ManyToManyField Kopga kop boglanish.


# Create your models here.


class Xizmat(models.Model):
    xizmatnomi = models.CharField(max_length=20)
    xizmatturi = models.CharField(max_length=50)
    narxi = models.BigIntegerField()
    ishsoati = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.xizmatnomi


class Maxsulot(models.Model):
    nomi = models.CharField(max_length=20)
    narxi = models.BigIntegerField()
    tavsifi = models.TextField()
    tasviri = models.ImageField()
    def __str__(self):
        return self.nomi






