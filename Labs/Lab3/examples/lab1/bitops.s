	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $208, %rsp
	/*   %0 = const 0 [TAC] */
	movq $0, -8(%rbp)
	/*   %1 = const 0 [TAC] */
	movq $0, -16(%rbp)
	/*   %2 = const 0 [TAC] */
	movq $0, -24(%rbp)
	/*   %0 = const 10 [TAC] */
	movq $10, -8(%rbp)
	/*   %1 = const 42 [TAC] */
	movq $42, -16(%rbp)
	/*   %2 = const -100 [TAC] */
	movq $-100, -24(%rbp)
	/*   %4 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -32(%rbp)
	/*   %5 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -40(%rbp)
	/*   %3 = and %4, %5 [TAC] */
	movq -32(%rbp), %r11
	andq -40(%rbp), %r11
	movq %r11, -48(%rbp)
	/*   print %3 [TAC] */
	movq -48(%rbp), %rdi
	callq __bx_print_int
	/*   %7 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   %8 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -64(%rbp)
	/*   %6 = and %7, %8 [TAC] */
	movq -56(%rbp), %r11
	andq -64(%rbp), %r11
	movq %r11, -72(%rbp)
	/*   print %6 [TAC] */
	movq -72(%rbp), %rdi
	callq __bx_print_int
	/*   %10 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -80(%rbp)
	/*   %11 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -88(%rbp)
	/*   %9 = or %10, %11 [TAC] */
	movq -80(%rbp), %r11
	orq -88(%rbp), %r11
	movq %r11, -96(%rbp)
	/*   print %9 [TAC] */
	movq -96(%rbp), %rdi
	callq __bx_print_int
	/*   %13 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -104(%rbp)
	/*   %14 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -112(%rbp)
	/*   %12 = or %13, %14 [TAC] */
	movq -104(%rbp), %r11
	orq -112(%rbp), %r11
	movq %r11, -120(%rbp)
	/*   print %12 [TAC] */
	movq -120(%rbp), %rdi
	callq __bx_print_int
	/*   %16 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -128(%rbp)
	/*   %17 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -136(%rbp)
	/*   %15 = xor %16, %17 [TAC] */
	movq -128(%rbp), %r11
	xorq -136(%rbp), %r11
	movq %r11, -144(%rbp)
	/*   print %15 [TAC] */
	movq -144(%rbp), %rdi
	callq __bx_print_int
	/*   %19 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -152(%rbp)
	/*   %20 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -160(%rbp)
	/*   %18 = xor %19, %20 [TAC] */
	movq -152(%rbp), %r11
	xorq -160(%rbp), %r11
	movq %r11, -168(%rbp)
	/*   print %18 [TAC] */
	movq -168(%rbp), %rdi
	callq __bx_print_int
	/*   %22 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -176(%rbp)
	/*   %21 = not %22 [TAC] */
	movq -176(%rbp), %r11
	notq %r11
	movq %r11, -184(%rbp)
	/*   print %21 [TAC] */
	movq -184(%rbp), %rdi
	callq __bx_print_int
	/*   %24 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -192(%rbp)
	/*   %23 = not %24 [TAC] */
	movq -192(%rbp), %r11
	notq %r11
	movq %r11, -200(%rbp)
	/*   print %23 [TAC] */
	movq -200(%rbp), %rdi
	callq __bx_print_int
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
