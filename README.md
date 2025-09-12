# pymenth

Practice mental arithmatic in decimal, hex, binary or octal.

Features:
+ Variable number of operands, with different operators
+ Highly customizable test format
+ Operands and answers in different bases

*Normal order of operations is ignored, all calculations should be done left to right, top to bottom.

### Examples

Add two single digit decimal numbers, answer in decimal
```
> menth "1;10,+1;10"
5 + 3
> 8
```

Convert double digit hex to decimal
```
> menth "10;ff#16"
0xf0
> 240
```

Convert binary to octal
```
> menth -b 8 "0;111#2"
0b10
> 0b2
```

Multiply a binary number by a hexadecimal and answer in octal
```
> menth -b 8 "0:11#2,*0:ff#16"
0b1 * 0xf0
> 0o360
```

Limit test length to 20
```
> menth -l 20 "0:10,+0:10,-0:10"
5 + 2 - 0
> 7
```

Practice powers of two, with 3 tries per question
```
> menth -t 3 "2,^0:10"
2 ^ 9
> 256
incorrect
2 ^ 9
> 512
correct
```
