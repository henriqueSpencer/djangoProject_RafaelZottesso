from django.db import models

# Create your models here.
#TODO: por padrao, todos os atributos de uma classe sao obrigatorios

class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')#verbose_name vai mostrar o nome armazenado nele

    def __str__(self): #é tipo um toString, se nao ele ia imprimir tipo o enderço de memoria
        return "{} ({})".format(self.nome, self.descricao) # o nome vai para a primeira chave e a descricao para a segunda

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT) #ele nao vai deixar deletar o campo se houver alguma atv cadastrada com ele

    def __str__(self):
        return "{} - {} ({})".format(self.numero, self.descricao, self.campo.nome)# vai mostrar o nome da atv e o nome do campo

class Status(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    def __str__(self):
        return "{} - {} ".format(self.nome, self.descricao)

class Classe(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.DecimalField(decimal_places=1, max_digits=5)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    def __str__(self):
        return "{} - {} -{}".format(self.nome, self.nivel, self.descricao)

class Campus(models.Model):
    cidade = models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    telefone = models.IntegerField(verbose_name="Número")
    def __str__(self):
        return "{} - {} -{}".format(self.cidade, self.endereço, self.telefone)


