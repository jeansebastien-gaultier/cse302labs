	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $144, %rsp
	/*   %0 = const 42 [TAC] */
	movq $42, -8(%rbp)
	/*   %2 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %3 = const 1 [TAC] */
	movq $1, -24(%rbp)
	/*   %1 = shr %2, %3 [TAC] */
	movq -16(%rbp), %r11
	movq -24(%rbp), %rcx
	sarq %cl, %r11
	movq %r11, -32(%rbp)
	/*   %5 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	/*   %6 = copy %1 [TAC] */
	movq -32(%rbp), %r11
	movq %r11, -48(%rbp)
	/*   %4 = add %5, %6 [TAC] */
	movq -40(%rbp), %r11
	addq -48(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   print %4 [TAC] */
	movq -56(%rbp), %rdi
	callq __bx_print_int
	/*   %8 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -64(%rbp)
	/*   %9 = copy %1 [TAC] */
	movq -32(%rbp), %r11
	movq %r11, -72(%rbp)
	/*   %7 = sub %8, %9 [TAC] */
	movq -64(%rbp), %r11
	subq -72(%rbp), %r11
	movq %r11, -80(%rbp)
	/*   print %7 [TAC] */
	movq -80(%rbp), %rdi
	callq __bx_print_int
	/*   %12 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -88(%rbp)
	/*   %13 = const 3 [TAC] */
	movq $3, -96(%rbp)
	/*   %11 = mul %12, %13 [TAC] */
	movq -88(%rbp), %rax
	imulq -96(%rbp)
	movq %rax, -104(%rbp)
	/*   %14 = copy %1 [TAC] */
	movq -32(%rbp), %r11
	movq %r11, -112(%rbp)
	/*   %10 = add %11, %14 [TAC] */
	movq -104(%rbp), %r11
	addq -112(%rbp), %r11
	movq %r11, -120(%rbp)
	/*   %16 = copy %10 [TAC] */
	movq -120(%rbp), %r11
	movq %r11, -128(%rbp)
	/*   %17 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -136(%rbp)
	/*   %15 = mod %16, %17 [TAC] */
	movq -128(%rbp), %rax
	cqto
	idivq -136(%rbp)
	movq %rdx, -144(%rbp)
	/*   print %15 [TAC] */
	movq -144(%rbp), %rdi
	callq __bx_print_int
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
