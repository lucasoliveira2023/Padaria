from django.db import models


class Produtos(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do Produto")
    descricao = models.TextField(
        blank=True, null=True, verbose_name="Descrição do Produto"
    )
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço do Produto"
    )
    estoque = models.PositiveIntegerField(verbose_name="Estoque do Produto")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    criado_em = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Criado em"
    )
    atualizado_em = models.DateTimeField(
        auto_now=True, db_index=True, verbose_name="Atualizado em"
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["-criado_em"]
        indexes = [
            models.Index(fields=["nome"], name="idx_produto_nome"),
            models.Index(fields=["ativo"], name="idx_produto_ativo"),
            models.Index(fields=["criado_em"], name="idx_produto_criado_em"),
        ]

    def __str__(self):
        return self.nome
