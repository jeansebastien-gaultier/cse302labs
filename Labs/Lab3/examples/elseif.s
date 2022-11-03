	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $256, %rsp
	/*   %0 = const 833779 [TAC] */
	movq $833779, -8(%rbp)
	/*   %5 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -16(%rbp)
	/*   %6 = const 2 [TAC] */
	movq $2, -24(%rbp)
	/*   %4 = mod %5, %6 [TAC] */
	movq -16(%rbp), %rax
	cqto
	idivq -24(%rbp)
	movq %rdx, -32(%rbp)
	/*   %7 = const 0 [TAC] */
	movq $0, -40(%rbp)
	/*   %8 = sub %4, %7 [TAC] */
	movq -32(%rbp), %r11
	subq -40(%rbp), %r11
	movq %r11, -48(%rbp)
	/*   jz %8, %.L1 [TAC] */
	jz .main.L1
	/*   jmp %.L2 [TAC] */
	/* --jmp .main.L2-- */
	/*  %.L2: [TAC] */
.main.L2:
	/*   %13 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   %14 = const 3 [TAC] */
	movq $3, -64(%rbp)
	/*   %12 = mod %13, %14 [TAC] */
	movq -56(%rbp), %rax
	cqto
	idivq -64(%rbp)
	movq %rdx, -72(%rbp)
	/*   %15 = const 0 [TAC] */
	movq $0, -80(%rbp)
	/*   %16 = sub %12, %15 [TAC] */
	movq -72(%rbp), %r11
	subq -80(%rbp), %r11
	movq %r11, -88(%rbp)
	/*   jz %16, %.L9 [TAC] */
	jz .main.L9
	/*   jmp %.L10 [TAC] */
	/* --jmp .main.L10-- */
	/*  %.L10: [TAC] */
.main.L10:
	/*   %21 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -96(%rbp)
	/*   %22 = const 5 [TAC] */
	movq $5, -104(%rbp)
	/*   %20 = mod %21, %22 [TAC] */
	movq -96(%rbp), %rax
	cqto
	idivq -104(%rbp)
	movq %rdx, -112(%rbp)
	/*   %23 = const 0 [TAC] */
	movq $0, -120(%rbp)
	/*   %24 = sub %20, %23 [TAC] */
	movq -112(%rbp), %r11
	subq -120(%rbp), %r11
	movq %r11, -128(%rbp)
	/*   jz %24, %.L17 [TAC] */
	jz .main.L17
	/*   jmp %.L18 [TAC] */
	/* --jmp .main.L18-- */
	/*  %.L18: [TAC] */
.main.L18:
	/*   %29 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -136(%rbp)
	/*   %30 = const 7 [TAC] */
	movq $7, -144(%rbp)
	/*   %28 = mod %29, %30 [TAC] */
	movq -136(%rbp), %rax
	cqto
	idivq -144(%rbp)
	movq %rdx, -152(%rbp)
	/*   %31 = const 0 [TAC] */
	movq $0, -160(%rbp)
	/*   %32 = sub %28, %31 [TAC] */
	movq -152(%rbp), %r11
	subq -160(%rbp), %r11
	movq %r11, -168(%rbp)
	/*   jz %32, %.L25 [TAC] */
	jz .main.L25
	/*   jmp %.L26 [TAC] */
	/* --jmp .main.L26-- */
	/*  %.L26: [TAC] */
.main.L26:
	/*   %37 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -176(%rbp)
	/*   %38 = const 11 [TAC] */
	movq $11, -184(%rbp)
	/*   %36 = mod %37, %38 [TAC] */
	movq -176(%rbp), %rax
	cqto
	idivq -184(%rbp)
	movq %rdx, -192(%rbp)
	/*   %39 = const 0 [TAC] */
	movq $0, -200(%rbp)
	/*   %40 = sub %36, %39 [TAC] */
	movq -192(%rbp), %r11
	subq -200(%rbp), %r11
	movq %r11, -208(%rbp)
	/*   jz %40, %.L33 [TAC] */
	jz .main.L33
	/*   jmp %.L34 [TAC] */
	/* --jmp .main.L34-- */
	/*  %.L34: [TAC] */
.main.L34:
	/*   jmp %.L35 [TAC] */
	jmp .main.L35
	/*  %.L33: [TAC] */
.main.L33:
	/*   %41 = const 11 [TAC] */
	movq $11, -216(%rbp)
	/*   print %41 [TAC] */
	movq -216(%rbp), %rdi
	callq __bx_print_int
	/*  %.L35: [TAC] */
.main.L35:
	/*   jmp %.L27 [TAC] */
	jmp .main.L27
	/*  %.L25: [TAC] */
.main.L25:
	/*   %42 = const 7 [TAC] */
	movq $7, -224(%rbp)
	/*   print %42 [TAC] */
	movq -224(%rbp), %rdi
	callq __bx_print_int
	/*  %.L27: [TAC] */
.main.L27:
	/*   jmp %.L19 [TAC] */
	jmp .main.L19
	/*  %.L17: [TAC] */
.main.L17:
	/*   %43 = const 5 [TAC] */
	movq $5, -232(%rbp)
	/*   print %43 [TAC] */
	movq -232(%rbp), %rdi
	callq __bx_print_int
	/*  %.L19: [TAC] */
.main.L19:
	/*   jmp %.L11 [TAC] */
	jmp .main.L11
	/*  %.L9: [TAC] */
.main.L9:
	/*   %44 = const 3 [TAC] */
	movq $3, -240(%rbp)
	/*   print %44 [TAC] */
	movq -240(%rbp), %rdi
	callq __bx_print_int
	/*  %.L11: [TAC] */
.main.L11:
	/*   jmp %.L3 [TAC] */
	jmp .main.L3
	/*  %.L1: [TAC] */
.main.L1:
	/*   %45 = const 2 [TAC] */
	movq $2, -248(%rbp)
	/*   print %45 [TAC] */
	movq -248(%rbp), %rdi
	callq __bx_print_int
	/*  %.L3: [TAC] */
.main.L3:
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
