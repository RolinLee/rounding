#/usr/bin/env python

'''rounding algorithm
A named value which indicates the algorithm to be used 
when rounding is necessary. Rounding is applied when a 
result coefficient has more significant digits than the 
value of precision; in this case the result coefficient 
is shortened to precision digits and may then be 
incremented by one (which may require a further shortening), 
depending on the rounding algorithm selected and the 
remaining digits of the original coefficient. The exponent 
is adjusted to compensate for any shortening.

'''

from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, \
ROUND_HALF_EVEN, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_DOWN, \
ROUND_UP, ROUND_05UP


def round_test(num, rd):
    "test rounding algorithm"

    print Decimal(num).quantize(Decimal('0.0000'), 
        rounding=rd)


if __name__ == "__main__":
    print 'round-down'
    round_test('0.12330', ROUND_DOWN)
    round_test('0.1233333', ROUND_DOWN)

    print 'round-half-up'
    round_test('0.12330', ROUND_HALF_UP)
    round_test('0.12331', ROUND_HALF_UP)
    round_test('0.12335', ROUND_HALF_UP)
    round_test('0.12338', ROUND_HALF_UP)

    print 'round-half-even'
    round_test('0.123350', ROUND_HALF_EVEN)
    round_test('0.123450', ROUND_HALF_EVEN)
    round_test('0.123351', ROUND_HALF_EVEN)
    round_test('0.123451', ROUND_HALF_EVEN)

    print 'round-half-down'
    round_test('0.12330', ROUND_HALF_DOWN)
    round_test('0.12331', ROUND_HALF_DOWN)
    round_test('0.12335', ROUND_HALF_DOWN)
    round_test('0.12338', ROUND_HALF_DOWN)

    print 'round-up'
    round_test('0.12330', ROUND_UP)
    round_test('0.1233333', ROUND_UP)

    print 'round-05up'
    round_test('0.12350', ROUND_05UP)
    round_test('0.12306', ROUND_05UP)
    round_test('0.12316', ROUND_05UP)
    round_test('0.12356', ROUND_05UP)


    print 'round-ceiling'
    round_test('0.12330', ROUND_CEILING)
    round_test('-0.12330', ROUND_CEILING)
    round_test('0.12331', ROUND_CEILING)
    round_test('-0.12331', ROUND_CEILING)

    print 'round-floor'
    round_test('0.12330', ROUND_FLOOR)
    round_test('-0.12330', ROUND_FLOOR)
    round_test('0.12331', ROUND_FLOOR)
    round_test('-0.12331', ROUND_FLOOR)





 
