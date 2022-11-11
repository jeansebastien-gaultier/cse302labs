	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $224, %rsp
	/*   %0 = const 0 [TAC] */
	movq $0, -8(%rbp)
	/*   %1 = const 0 [TAC] */
	movq $0, -16(%rbp)
	/*   %2 = const 0 [TAC] */
	movq $0, -24(%rbp)
	/*   %1 = const 1 [TAC] */
	movq $1, -16(%rbp)
	/*   %3 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -32(%rbp)
	/*   print %3 [TAC] */
	movq -32(%rbp), %rdi
	callq __bx_print_int
	/*   %4 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	/*   %5 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -48(%rbp)
	/*   %2 = add %4, %5 [TAC] */
	movq -40(%rbp), %r11
	addq -48(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %0 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %6 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   print %6 [TAC] */
	movq -56(%rbp), %rdi
	callq __bx_print_int
	/*   %7 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -64(%rbp)
	/*   %8 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -72(%rbp)
	/*   %2 = add %7, %8 [TAC] */
	movq -64(%rbp), %r11
	addq -72(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %0 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %9 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -80(%rbp)
	/*   print %9 [TAC] */
	movq -80(%rbp), %rdi
	callq __bx_print_int
	/*   %10 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -88(%rbp)
	/*   %11 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -96(%rbp)
	/*   %2 = add %10, %11 [TAC] */
	movq -88(%rbp), %r11
	addq -96(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %0 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %12 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -104(%rbp)
	/*   print %12 [TAC] */
	movq -104(%rbp), %rdi
	callq __bx_print_int
	/*   %13 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -112(%rbp)
	/*   %14 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -120(%rbp)
	/*   %2 = add %13, %14 [TAC] */
	movq -112(%rbp), %r11
	addq -120(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %0 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %15 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -128(%rbp)
	/*   print %15 [TAC] */
	movq -128(%rbp), %rdi
	callq __bx_print_int
	/*   %16 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -136(%rbp)
	/*   %17 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -144(%rbp)
	/*   %2 = add %16, %17 [TAC] */
	movq -136(%rbp), %r11
	addq -144(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %0 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %18 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -152(%rbp)
	/*   print %18 [TAC] */
	movq -152(%rbp), %rdi
	callq __bx_print_int
	/*   %19 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -160(%rbp)
	/*   %20 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -168(%rbp)
	/*   %2 = add %19, %20 [TAC] */
	movq -160(%rbp), %r11
	addq -168(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %0 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %21 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -176(%rbp)
	/*   print %21 [TAC] */
	movq -176(%rbp), %rdi
	callq __bx_print_int
	/*   %22 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -184(%rbp)
	/*   %23 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -192(%rbp)
	/*   %2 = add %22, %23 [TAC] */
	movq -184(%rbp), %r11
	addq -192(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %0 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %24 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -200(%rbp)
	/*   print %24 [TAC] */
	movq -200(%rbp), %rdi
	callq __bx_print_int
	/*   %25 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -208(%rbp)
	/*   %26 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -216(%rbp)
	/*   %2 = add %25, %26 [TAC] */
	movq -208(%rbp), %r11
	addq -216(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %0 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %27 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -224(%rbp)
	/*   print %27 [TAC] */
	movq -224(%rbp), %rdi
	callq __bx_print_int
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
