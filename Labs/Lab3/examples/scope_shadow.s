	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	/*   %0 = const 10 [TAC] */
	movq $10, -8(%rbp)
	/*   %1 = const 20 [TAC] */
	movq $20, -16(%rbp)
	/*   %2 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   print %2 [TAC] */
	movq -24(%rbp), %rdi
	callq __bx_print_int
	/*   %3 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -32(%rbp)
	/*   %4 = const 1 [TAC] */
	movq $1, -40(%rbp)
	/*   %1 = add %3, %4 [TAC] */
	movq -32(%rbp), %r11
	addq -40(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %5 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -48(%rbp)
	/*   print %5 [TAC] */
	movq -48(%rbp), %rdi
	callq __bx_print_int
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
