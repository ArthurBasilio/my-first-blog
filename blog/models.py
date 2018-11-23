from django.db import models
from django.utils import timezone
#from ou import são linhas que adicionam alguns pedaços de outros arquivos.Então ao invés de copiar e colar as mesmas coisas em cada arquivo, podemos incluir algumas partes com from...import... .


class Post(models.Model):#Esta linha define o nosso modelo
#class é uma palavra-chave especial que indica que estamos definindo um objeto
#Post é o nome do nosso modelo(sempre iniciado com letra maiúscula).
#models.Model significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados.
#Definimos as propriedades:
#Obs: as observações abaixo vão paraq os termos em azul (Ex:ForeignKey)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#Este é um link para outro modelo
    title = models.CharField(max_length=200)#É assim que definimos um texto com um número limitado de caracteres
    text = models.TextField()#Este campo é para textos sem um limite fixo.
    created_date = models.DateTimeField(#Este é uma data hora
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):#Este é o método publish
    #def signifca que é uma função/método e que publish é seu nome
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        #Neste caso, quando chamarmos __str__() obteremos um texto(string) como retorno que será o título do Post
        return self.title
