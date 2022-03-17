# Generated by Django 4.0 on 2022-03-17 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('F', 'Fêmea'), ('M', 'Masculino'), ('N', 'Outro')], max_length=1)),
                ('raca', models.CharField(max_length=20)),
                ('porte', models.CharField(choices=[('p', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande'), ('N', 'Outro')], max_length=1)),
                ('idade', models.IntegerField()),
                ('tipo', models.CharField(choices=[('Gato', 'Gato'), ('Cachorro', 'Cachorro'), ('Outro', 'Outro')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('formaPag', models.CharField(choices=[('Dinheiro', 'Dinheiro'), ('Cartao', 'Cartao'), ('PIX', 'PIX'), ('Deposito', 'Deposito'), ('Outro', 'Outro')], max_length=8)),
                ('TipoServico', models.CharField(choices=[('Banho', 'Banho'), ('Tosa', 'Tosa'), ('Transporte', 'Transporte'), ('Outro', 'Outro')], max_length=10)),
                ('Animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Servico', to='appPetShop.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('fone', models.CharField(max_length=14)),
                ('CPF', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='appPetShop.endereco')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal', to='appPetShop.cliente'),
        ),
    ]
