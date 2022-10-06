from django.db import models


class Category(models.Model):
    name = models.TextField('Категория', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Student(models.Model):
    name = models.CharField('Ученик', max_length=150)
    evaluations1 = models.IntegerField(verbose_name='Оценка по успеваемости', default=0)
    evaluations2 = models.IntegerField(verbose_name='Оценка по поведению', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class Teacher(models.Model):
    name = models.CharField('Учитель', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Schedule(models.Model):
    type2 = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    date_beginning = models.DateTimeField(verbose_name='Время начало',auto_now_add=False, auto_now=False)
    date_end = models.DateTimeField(verbose_name='Время окончания',auto_now_add=False, auto_now=False)
    teacher = models.ManyToManyField(Teacher, verbose_name='Учитель')
    student = models.ManyToManyField(Student, verbose_name='Ученик')
    tutor = models.BooleanField(verbose_name='Куратор')

    class Meta:
        ordering = ['date_beginning']
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class History(models.Model):
    text = models.TextField(verbose_name='текст(что делали на уроке или какие ни будь замечания')
    type2 = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    date_end = models.DateTimeField(verbose_name='Время окончания',auto_now_add=False, auto_now=False)
    evaluations1 = models.IntegerField(verbose_name='Оценка по успеваемости(от 1 до 10)')
    evaluations2 = models.IntegerField(verbose_name='Оценка по поведению(от 1 до 10)')
    teacher = models.ManyToManyField(Teacher, verbose_name='Учитель')
    student = models.ManyToManyField(Student, verbose_name='Ученик')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'




