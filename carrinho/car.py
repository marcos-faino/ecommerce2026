
from django.conf import settings
from catalogo.models import Produto


class Carrinho(object):

    def __init__(self, request):
        """
        Inicializa o carrinho de compras
        :param request: a requisição https
        """
        self.session = request.session
        carrinho = self.session.get(settings.CAR_SESSION_ID)
        if not carrinho:
            carrinho = self.session[settings.CAR_SESSION_ID] = {}
        self.carrinho = carrinho

    def addProduto(self, produto, quant=1, alterarquant=False):
        """
        Adiciona um produto ao carrinho ou atualiza a quantidade
        :param produto: O item a ser adicionado
        :param quant: a quantidade do produto
        :param alterarquant: quando necessário alterar a quantidade de produtos
        :return: sem retorno
        """
        idprod = str(produto.id)
        if idprod not in self.carrinho:
            self.carrinho[idprod] = {"quantidade": 0, "preco":str(produto.preco)}
        if alterarquant:
            self.carrinho[idprod]["quantidade"] = quant
        else:
            self.carrinho[idprod]["quantidade"] += quant
        self._salvar()

    def _salvar(self):
        self.session.modified = True