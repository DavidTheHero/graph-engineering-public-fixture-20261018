# Invoice discounts fixture

Run `python -m unittest discover -s tests -v`.

The percentage discount applies to the integer-cent subtotal, rounding the discount down. A 10% discount on 20000 cents must return 18000. Zero discount preserves the subtotal.
