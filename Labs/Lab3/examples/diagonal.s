	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $144, %rsp
	/*   %0 = const 20 [TAC] */
	movq $20, -8(%rbp)
	/*   %1 = const 0 [TAC] */
	movq $0, -16(%rbp)
	/*   %2 = const 0 [TAC] */
	movq $0, -24(%rbp)
	/*  %.L3: [TAC] */
.main.L3:
	/*   jmp %.L4 [TAC] */
	/* --jmp .main.L4-- */
	/*  %.L4: [TAC] */
.main.L4:
	/*   %9 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -32(%rbp)
	/*   %10 = const 0 [TAC] */
	movq $0, -40(%rbp)
	/*   %11 = sub %9, %10 [TAC] */
	movq -32(%rbp), %r11
	subq -40(%rbp), %r11
	movq %r11, -48(%rbp)
	/*   jz %11, %.L6 [TAC] */
	jz .main.L6
	/*   jmp %.L7 [TAC] */
	/* --jmp .main.L7-- */
	/*  %.L7: [TAC] */
.main.L7:
	/*   jmp %.L8 [TAC] */
	jmp .main.L8
	/*  %.L6: [TAC] */
.main.L6:
	/*   jmp %.L5 [TAC] */
	jmp .main.L5
	/*  %.L8: [TAC] */
.main.L8:
	/*   %12 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   print %12 [TAC] */
	movq -56(%rbp), %rdi
	callq __bx_print_int
	/*   %1 = const 1 [TAC] */
	movq $1, -16(%rbp)
	/*   %2 = const 0 [TAC] */
	movq $0, -24(%rbp)
	/*  %.L13: [TAC] */
.main.L13:
	/*   jmp %.L14 [TAC] */
	/* --jmp .main.L14-- */
	/*  %.L14: [TAC] */
.main.L14:
	/*   %19 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -64(%rbp)
	/*   %20 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -72(%rbp)
	/*   %21 = sub %19, %20 [TAC] */
	movq -64(%rbp), %r11
	subq -72(%rbp), %r11
	movq %r11, -80(%rbp)
	/*   jnle %21, %.L16 [TAC] */
	jnle .main.L16
	/*   jmp %.L17 [TAC] */
	/* --jmp .main.L17-- */
	/*  %.L17: [TAC] */
.main.L17:
	/*   jmp %.L18 [TAC] */
	jmp .main.L18
	/*  %.L16: [TAC] */
.main.L16:
	/*   jmp %.L15 [TAC] */
	jmp .main.L15
	/*  %.L18: [TAC] */
.main.L18:
	/*   %22 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -88(%rbp)
	/*   %23 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -96(%rbp)
	/*   %2 = add %22, %23 [TAC] */
	movq -88(%rbp), %r11
	addq -96(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %24 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -104(%rbp)
	/*   %25 = const 1 [TAC] */
	movq $1, -112(%rbp)
	/*   %1 = add %24, %25 [TAC] */
	movq -104(%rbp), %r11
	addq -112(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   jmp %.L13 [TAC] */
	jmp .main.L13
	/*  %.L15: [TAC] */
.main.L15:
	/*   %26 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -120(%rbp)
	/*   print %26 [TAC] */
	movq -120(%rbp), %rdi
	callq __bx_print_int
	/*   %27 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -128(%rbp)
	/*   %28 = const 1 [TAC] */
	movq $1, -136(%rbp)
	/*   %0 = sub %27, %28 [TAC] */
	movq -128(%rbp), %r11
	subq -136(%rbp), %r11
	movq %r11, -8(%rbp)
	/*   jmp %.L3 [TAC] */
	jmp .main.L3
	/*  %.L5: [TAC] */
.main.L5:
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
