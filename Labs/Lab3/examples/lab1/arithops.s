	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $256, %rsp
	/*   %0 = const 0 [TAC] */
	movq $0, -8(%rbp)
	/*   %1 = const 0 [TAC] */
	movq $0, -16(%rbp)
	/*   %2 = const 0 [TAC] */
	movq $0, -24(%rbp)
	/*   %0 = const 42 [TAC] */
	movq $42, -8(%rbp)
	/*   %1 = const 21 [TAC] */
	movq $21, -16(%rbp)
	/*   %2 = const 5 [TAC] */
	movq $5, -24(%rbp)
	/*   %4 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -32(%rbp)
	/*   %5 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -40(%rbp)
	/*   %3 = add %4, %5 [TAC] */
	movq -32(%rbp), %r11
	addq -40(%rbp), %r11
	movq %r11, -48(%rbp)
	/*   print %3 [TAC] */
	movq -48(%rbp), %rdi
	callq __bx_print_int
	/*   %7 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   %8 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -64(%rbp)
	/*   %6 = sub %7, %8 [TAC] */
	movq -56(%rbp), %r11
	subq -64(%rbp), %r11
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
	/*   %9 = mul %10, %11 [TAC] */
	movq -80(%rbp), %rax
	imulq -88(%rbp)
	movq %rax, -96(%rbp)
	/*   print %9 [TAC] */
	movq -96(%rbp), %rdi
	callq __bx_print_int
	/*   %13 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -104(%rbp)
	/*   %14 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -112(%rbp)
	/*   %12 = div %13, %14 [TAC] */
	movq -104(%rbp), %rax
	cqto
	idivq -112(%rbp)
	movq %rax, -120(%rbp)
	/*   print %12 [TAC] */
	movq -120(%rbp), %rdi
	callq __bx_print_int
	/*   %16 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -128(%rbp)
	/*   %17 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -136(%rbp)
	/*   %15 = div %16, %17 [TAC] */
	movq -128(%rbp), %rax
	cqto
	idivq -136(%rbp)
	movq %rax, -144(%rbp)
	/*   print %15 [TAC] */
	movq -144(%rbp), %rdi
	callq __bx_print_int
	/*   %19 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -152(%rbp)
	/*   %20 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -160(%rbp)
	/*   %18 = mod %19, %20 [TAC] */
	movq -152(%rbp), %rax
	cqto
	idivq -160(%rbp)
	movq %rdx, -168(%rbp)
	/*   print %18 [TAC] */
	movq -168(%rbp), %rdi
	callq __bx_print_int
	/*   %22 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -176(%rbp)
	/*   %21 = neg %22 [TAC] */
	movq -176(%rbp), %r11
	negq %r11
	movq %r11, -184(%rbp)
	/*   print %21 [TAC] */
	movq -184(%rbp), %rdi
	callq __bx_print_int
	/*   %25 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -192(%rbp)
	/*   %24 = neg %25 [TAC] */
	movq -192(%rbp), %r11
	negq %r11
	movq %r11, -200(%rbp)
	/*   %26 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -208(%rbp)
	/*   %23 = div %24, %26 [TAC] */
	movq -200(%rbp), %rax
	cqto
	idivq -208(%rbp)
	movq %rax, -216(%rbp)
	/*   print %23 [TAC] */
	movq -216(%rbp), %rdi
	callq __bx_print_int
	/*   %29 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -224(%rbp)
	/*   %28 = neg %29 [TAC] */
	movq -224(%rbp), %r11
	negq %r11
	movq %r11, -232(%rbp)
	/*   %30 = copy %2 [TAC] */
	movq -24(%rbp), %r11
	movq %r11, -240(%rbp)
	/*   %27 = mod %28, %30 [TAC] */
	movq -232(%rbp), %rax
	cqto
	idivq -240(%rbp)
	movq %rdx, -248(%rbp)
	/*   print %27 [TAC] */
	movq -248(%rbp), %rdi
	callq __bx_print_int
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
