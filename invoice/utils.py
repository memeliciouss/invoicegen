from django.db.models import Sum, F, DecimalField
from invoice.models import Items
from django.db.models.functions import Cast


# from invoice.utils import calculate_invoice_total

def calculate_invoice_total(invoice_id):

    # Calculates the total amount for an invoice, including GST.

    # Args:
    #     invoice_id (int): The ID of the invoice.

    # Returns:
    #     Decimal: The total amount for the invoice, or 0 if no items are found.

    total_amount = Items.objects.filter(invID=invoice_id).annotate(
        base_amount=F('rate') * F('qty'),
        gst_amount=Cast(F('gst') * F('base_amount') / 100.0, output_field=DecimalField()),
        total_item_amount=F('base_amount') + F('gst_amount')
    ).aggregate(total=Sum('total_item_amount'))['total'] or 0
    return total_amount

    # F --> Field Reference
    # Annotate --> Adds temporary columns / calculate fields
    # Aggregate --> summarizes query result into a single value
    
    return total_amount