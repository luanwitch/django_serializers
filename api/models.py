from django.db import models

class Curso(models.Model):
    codigo_curso = models.CharField(max_length=10, unique=True)
    nome_curso = models.CharField(max_length=100)
    descricao = models.TextField(max_length=300)

    def __str__(self):
        return self.nome_curso

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=100)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_aluno
