class Pessoa:
   def __init__(self,Login,Nome,CPF,Genero,Data,Senha):
       self.Login = Login
       self.Nome = Nome
       self.CPF = CPF
       self.Genero = Genero
       self.Data = Data
       self.Senha = Senha


ListaPessoa = []


def CadastrarBD(Login,Nome,CPF,Genero,Data,Senha):
   Obj = Pessoa(Login,Nome,CPF,Genero,Data,Senha)
   ListaPessoa.append(Obj)


def AutenticarBD(Login,Senha):
   if not ListaPessoa:
       return "Vazia"
   else:
       for User in ListaPessoa:
           if User.Login == Login and User.Senha == Senha:
               return "Certo"
           else:
               return "Errado!"
