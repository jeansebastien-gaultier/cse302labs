	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $128, %rsp
	/*   %0 = const 10 [TAC] */
	movq $10, -8(%rbp)
	/*   %1 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   print %1 [TAC] */
	movq -16(%rbp), %rdi
	callq __bx_print_int
	/*   %3 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %4 = const 20 [TAC] */
	movq $20, -32(%rbp)
	/*   %2 = add %3, %4 [TAC] */
	movq -24(%rbp), %r11
	addq -32(%rbp), %r11
	movq %r11, -40(%rbp)
	/*   %5 = copy %2 [TAC] */
	movq -40(%rbp), %r11
	movq %r11, -48(%rbp)
	/*   print %5 [TAC] */
	movq -48(%rbp), %rdi
	callq __bx_print_int
	/*   %7 = copy %2 [TAC] */
	movq -40(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   %8 = const 42 [TAC] */
	movq $42, -64(%rbp)
	/*   %6 = mul %7, %8 [TAC] */
	movq -56(%rbp), %rax
	imulq -64(%rbp)
	movq %rax, -72(%rbp)
	/*   %9 = copy %6 [TAC] */
	movq -72(%rbp), %r11
	movq %r11, -80(%rbp)
	/*   print %9 [TAC] */
	movq -80(%rbp), %rdi
	callq __bx_print_int
	/*   %12 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -88(%rbp)
	/*   %13 = copy %2 [TAC] */
	movq -40(%rbp), %r11
	movq %r11, -96(%rbp)
	/*   %11 = mul %12, %13 [TAC] */
	movq -88(%rbp), %rax
	imulq -96(%rbp)
	movq %rax, -104(%rbp)
	/*   %14 = copy %6 [TAC] */
	movq -72(%rbp), %r11
	movq %r11, -112(%rbp)
	/*   %10 = sub %11, %14 [TAC] */
	movq -104(%rbp), %r11
	subq -112(%rbp), %r11
	movq %r11, -120(%rbp)
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
