# rounding
rounding（数字修约）

A named value which indicates the algorithm to be used when rounding is necessary. Rounding is applied when a result coefficient has more significant digits than the value of precision; in this case the result coefficient is shortened to precision digits and may then be incremented by one (which may require a further shortening), depending on the rounding algorithm selected and the remaining digits of the original coefficient. The exponent is adjusted to compensate for any shortening.

当进行数字修约时，这些值用来表明将会使用哪种算法。数字修约应用于结果有效数字的位数大于其精度时；在这种情况下，结果会从精度开始被截断并可能增1，这依赖于选择哪种数字修约规则和要保留的数。调整指数来弥补结果的截断。

round-down:(Round toward 0; truncate.) The discarded digits are ignored; the result is unchanged.

round-down：（趋近于0）直接截断，结果不变

round-half-up:If the discarded digits represent greater than or equal to half (0.5) of the value of a one in the next left position then the result coefficient should be incremented by 1 (rounded up). Otherwise the discarded digits are ignored.

round-half-up：四舍五入

round-half-even:If the discarded digits represent greater than half (0.5) the value of a one in the next left position then the result coefficient should be incremented by 1 (rounded up). If they represent less than half, then the result coefficient is not adjusted (that is, the discarded digits are ignored).Otherwise (they represent exactly half) the result coefficient is unaltered if its rightmost digit is even, or incremented by 1 (rounded up) if its rightmost digit is odd (to make an even digit).

round-half-even：四舍六入五留双

round-ceiling:(Round toward Emax) If all of the discarded digits are zero or if the sign is 1 the result is unchanged. Otherwise, the result coefficient should be incremented by 1 (rounded up).

round-ceiling：（趋近于正无穷）引入正负的概念
 

round-floor:(Round toward Emin) If all of the discarded digits are zero or if the sign is 0 the result is unchanged. Otherwise, the sign is 1 and the result coefficient should be incremented by 1.

round-floor：（趋近于负无穷） 引入正负的概念

round-half-down:If the discarded digits represent greater than half (0.5) of the value of a one in the next left position then the result coefficient should be incremented by 1 (rounded up). Otherwise (the discarded digits are 0.5 or less) the discarded digits are ignored.

round-half-down：小于等于5舍去，大于5进1

round-up:(Round away from 0.) If all of the discarded digits are zero the result is unchanged. Otherwise, the result coefficient should be incremented by 1 (rounded up).

round-up：和round-down相对应

round-05up:(Round zero or five away from 0.) The same as round-up, except that rounding up only occurs if the digit to be rounded up is 0 or 5, and after overflow the result is the same as for round-down.When a result is rounded, the coefficient may become longer than the current precision. In this case the least significant digit of the coefficient (it will be a zero) is removed (reducing the precision by one), and the exponent is incremented by one. This in turn may give rise to an overflow condition, which determines the result after overflow.

round-05up：0和5时进1，其他情况截断
