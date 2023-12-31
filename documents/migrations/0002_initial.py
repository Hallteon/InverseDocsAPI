# Generated by Django 3.2.18 on 2023-09-13 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentstatus',
            name='roles',
            field=models.ManyToManyField(related_name='statuses_role', to='users.Role', verbose_name='Доступ'),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='reciever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories_user', to=settings.AUTH_USER_MODEL, verbose_name='Получатель'),
        ),
        migrations.AddField(
            model_name='documenthistory',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories_status', to='documents.documentstatus', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents_category', to='documents.documentcategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='document',
            name='contractors',
            field=models.ManyToManyField(related_name='documents_contractor', to='documents.Contractor', verbose_name='Контрагенты'),
        ),
        migrations.AddField(
            model_name='document',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents_creator', to=settings.AUTH_USER_MODEL, verbose_name='Созатель'),
        ),
        migrations.AddField(
            model_name='document',
            name='history',
            field=models.ManyToManyField(related_name='documents_history', to='documents.DocumentHistory', verbose_name='История'),
        ),
        migrations.AddField(
            model_name='document',
            name='products',
            field=models.ManyToManyField(related_name='documents_product', to='documents.Product', verbose_name='Товары'),
        ),
        migrations.AddField(
            model_name='document',
            name='recievers',
            field=models.ManyToManyField(related_name='documents_reciever', to=settings.AUTH_USER_MODEL, verbose_name='Получатели'),
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='documents_status', to='documents.documentstatus', verbose_name='Статус'),
        ),
    ]
