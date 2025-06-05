from django.conf import settings
from django.db import models

from produtos.models import Produtos


class Vendas(models.Model):
    STATUS_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("PAGO", "Pago"),
        ("CANCELADO", "Cancelado"),
    ]

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="vendas",
        verbose_name="Cliente",
    )
    data = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Data da Venda"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDENTE",
        db_index=True,
        verbose_name="Status",
    )
    valor_total = models.DecimalField(
        max_digits=10,
        choices=STATUS_CHOICES,
        default="PENDENTE",
        db_index=True,
        verbose_name="Status",
    )
    valor_total = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00, verbose_name="Valor Total"
    )
    ativo = models.BooleanField(default=True, db_index=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ["-data"]
        indexes = [
            models.Index(fields=["data"], name="idx_venda_data"),
            models.Index(fields=["status"], name="idx_venda_status"),
            models.Index(fields=["ativo"], name="idx_venda_ativo"),
        ]

    def __str__(self):
        return f"Venda #{self.id} - Client: {self.client}"


class ItemVenda(models.Model):
    venda = models.ForeignKey(
        Vendas, on_delete=models.CASCADE, related_name="itens", verbose_name="Venda"
    )
    produto = models.ForeignKey(
        Produtos,
        on_delete=models.PROTECT,
        related_name="itens_venda",
        verbose_name="Produto",
    )
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade")
    preco_unitario = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Preço Unitário"
    )
    subtotal = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Subtotal"
    )

    class Meta:
        verbose_name = "Item da Venda"
        verbose_name_plural = "Itens da Venda"
        indexes = [
            models.Index(fields=["venda"], name="idx_item_venda"),
            models.Index(fields=["produto"], name="idx_item_produto"),
        ]

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)
