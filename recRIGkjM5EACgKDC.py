Task #1
START
READ number n
IF n == 1 THEN return
FOR i = 1, i <= n, i + 1
	FOR j = 1; j <= n, j + 1
		print "*"
		BREAK
END

Task #2
START
READ number n
numbers i = 0, j = 0, a = 0
FOR i = n/2, i <= n; i + 1
	FOR j = 2, j <= n, j * 2
		a = a + n / 2
END

Task #3
START
READ number n
number a = 0
FOR i = 0, i < n, i + 1
	FOR j = n, j > i, j - 1
		a = a + i + j
END

Task #4
START
READ number n
numbers a = 0, i = n
WHILE i > 0
	a = a + i
	i = i / 2
END
