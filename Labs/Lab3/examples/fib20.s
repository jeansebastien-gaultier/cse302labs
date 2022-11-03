	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $96, %rsp
	/*   %0 = const 20 [TAC] */
	movq $20, -8(%rbp)
	/*   %1 = const 0 [TAC] */
	movq $0, -16(%rbp)
	/*   %2 = const 1 [TAC] */
	movq $1, -24(%rbp)
	/*   %3 = const 0 [TAC] */
	movq $0, -32(%rbp)
	/*  %.L4: [TAC] */
.main.L4:
	/*   %7 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	/*   %8 = const 0 [TAC] */
	movq $0, -48(%rbp)
	/*   %9 = sub %7, %8 [TAC] */
	movq -40(%rbp), %r11
	subq -48(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   jnle %9, %.L5 [TAC] */
	jnle .main.L5
	/*   jmp %.L6 [TAC] */
	jmp .main.L6
	/*  %.L5: [TAC] */
.main.L5:
	/*   %10 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -64(%rbp)
	/*   %11 = const 1 [TAC] */
	movq $1, -72(%rbp)
	/*   %0 = sub %10, %11 [TAC] */
	movq -64(%rbp), %r11
	subq -72(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   %12 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -80(%rbp)
	/*   print %12 [TAC] */
	movq -80(%rbp), %rdi
	callq __bx_print_int
	/*   %13 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -88(%rbp)
	/*   %14 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -96(%rbp)
	/*   %3 = add %13, %14 [TAC] */
	movq -88(%rbp), %r11
	addq -96(%rbp), %r11
	movq %r11, -32(%rbp)
	/*   %1 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %2 = copy %3 [TAC] */
	movq -32(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   jmp %.L4 [TAC] */
	jmp .main.L4
	/*  %.L6: [TAC] */
.main.L6:
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
