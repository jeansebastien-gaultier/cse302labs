	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	/*   %1 = const 1 [TAC] */
	movq $1, -8(%rbp)
	/*   %2 = const 2 [TAC] */
	movq $2, -16(%rbp)
	/*   %0 = add %1, %2 [TAC] */
	movq -8(%rbp), %r11
	addq -16(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %3 = copy %0 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -32(%rbp)
	/*   print %3 [TAC] */
	movq -32(%rbp), %rdi
	callq __bx_print_int
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
